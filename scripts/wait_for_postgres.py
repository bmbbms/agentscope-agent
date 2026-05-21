from __future__ import annotations

import os
import urllib.parse

try:
    import asyncpg
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("asyncpg is required") from exc

import asyncio


def _dsn() -> str:
    dsn = os.getenv("AGENT_AUDIT_PG_DSN", "").strip()
    if not dsn:
        raise RuntimeError("AGENT_AUDIT_PG_DSN is required")
    return dsn


def _sql_path() -> str:
    return os.getenv("AUDIT_SCHEMA_SQL_PATH", "/app/sql/audit_schema.sql")


async def _wait_for_db(dsn: str, retries: int = 60, sleep_seconds: float = 1.0) -> None:
    last_error: Exception | None = None
    for _ in range(retries):
        try:
            conn = await asyncpg.connect(dsn)
            await conn.close()
            return
        except Exception as exc:  # pragma: no cover
            last_error = exc
            await asyncio.sleep(sleep_seconds)
    raise RuntimeError(f"Postgres did not become ready in time: {last_error}")


async def _apply_schema(dsn: str, sql_path: str) -> None:
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()
    conn = await asyncpg.connect(dsn)
    try:
        await conn.execute(sql)
    finally:
        await conn.close()


async def main() -> None:
    dsn = _dsn()
    sql_path = _sql_path()
    await _wait_for_db(dsn)
    await _apply_schema(dsn, sql_path)


if __name__ == "__main__":
    asyncio.run(main())
