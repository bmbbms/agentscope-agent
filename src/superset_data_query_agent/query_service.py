from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
SUPERSET_DATA_QUERY_DIR = REPO_ROOT / "superset_data_query"

if str(SUPERSET_DATA_QUERY_DIR) not in sys.path:
    sys.path.insert(0, str(SUPERSET_DATA_QUERY_DIR))

from superset_query import SupersetClient  # type: ignore  # noqa: E402


@dataclass(slots=True)
class SupersetQueryRequestSpec:
    query: str
    action: str = "schema_search"
    sql: str | None = None
    database_name: str | None = None
    preview_rows: int = 20
    enable_mask: bool = True
    export_excel: bool = False
    export_name: str | None = None
    schema_keyword: str | None = None
    search_limit: int = 10
    output_dir: str | None = None
    timeout_seconds: int = 120


class SupersetDataQueryService:
    def __init__(self, *, output_dir: str | None = None) -> None:
        resolved_output_dir = output_dir or str(SUPERSET_DATA_QUERY_DIR / "output")
        self.output_dir = Path(resolved_output_dir)
        self.schema_dir = self._resolve_schema_dir()

    def handle(self, spec: SupersetQueryRequestSpec) -> dict[str, Any]:
        action = spec.action.lower()
        if action == "list_databases":
            return self.list_databases()
        if action == "sql_query":
            return self.execute_sql(spec)
        return self.search_schema(spec)

    def list_databases(self) -> dict[str, Any]:
        client = SupersetClient()
        if not client.login():
            raise RuntimeError("Failed to login to Superset.")
        items = [
            {"database_id": database_id, "database_name": database_name}
            for database_id, database_name in client.list_databases()
        ]
        return {
            "action": "list_databases",
            "count": len(items),
            "items": items,
        }

    def search_schema(self, spec: SupersetQueryRequestSpec) -> dict[str, Any]:
        keyword = (spec.schema_keyword or spec.query).strip()
        if not keyword:
            raise ValueError("schema keyword is required for schema search")

        normalized = keyword.lower()
        results: list[dict[str, Any]] = []
        for path in sorted(self.schema_dir.rglob("*.md")):
            file_key = path.stem.lower()
            if normalized not in file_key:
                try:
                    content = path.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                if normalized not in content.lower():
                    continue
            results.append(
                {
                    "table_file": path.name,
                    "table_name": path.stem.split("+", 1)[0],
                    "description": path.stem.split("+", 1)[1] if "+" in path.stem else path.stem,
                    "path": str(path),
                }
            )
            if len(results) >= spec.search_limit:
                break

        return {
            "action": "schema_search",
            "keyword": keyword,
            "count": len(results),
            "items": results,
        }

    def execute_sql(self, spec: SupersetQueryRequestSpec) -> dict[str, Any]:
        if not spec.sql or not spec.sql.strip():
            raise ValueError("sql is required for sql_query action")

        client = SupersetClient()
        if not client.login():
            raise RuntimeError("Failed to login to Superset.")

        df = client.execute_sql(
            spec.sql,
            database_name=spec.database_name,
            timeout=spec.timeout_seconds,
            enable_mask=spec.enable_mask,
            enable_chinese_columns=True,
        )
        if df is None:
            raise RuntimeError("Superset query returned no result object.")

        row_count = len(df.index)
        column_count = len(df.columns)
        preview_rows = max(1, min(spec.preview_rows, 100))
        preview = self._records(df.head(preview_rows))

        export_path = None
        if spec.export_excel:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            export_name = spec.export_name or self._default_export_name()
            export_path = str(self.output_dir / export_name)
            if not client.export_to_excel(df, export_path, enable_mask=False):
                raise RuntimeError("Failed to export query result to Excel.")

        return {
            "action": "sql_query",
            "database_name": spec.database_name,
            "row_count": row_count,
            "column_count": column_count,
            "columns": [str(column) for column in df.columns.tolist()],
            "preview": preview,
            "export_path": export_path,
            "mask_enabled": spec.enable_mask,
        }

    def _resolve_schema_dir(self) -> Path:
        env_path = os.environ.get("SUPERSET_SCHEMA_DIR", "").strip()
        if env_path:
            return Path(env_path)

        exact_match = SUPERSET_DATA_QUERY_DIR / "BI数据表结构全量"
        if exact_match.exists():
            return exact_match

        for candidate in SUPERSET_DATA_QUERY_DIR.iterdir():
            if not candidate.is_dir():
                continue
            lowered_name = candidate.name.lower()
            if "bi" in lowered_name or "表结构" in candidate.name:
                return candidate
        raise FileNotFoundError("Unable to locate schema directory in superset_data_query.")

    @staticmethod
    def _default_export_name() -> str:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"superset_query_result_{timestamp}.xlsx"

    @staticmethod
    def _records(df: pd.DataFrame) -> list[dict[str, Any]]:
        safe_df = df.astype(object).where(pd.notna(df), None)
        records = safe_df.to_dict(orient="records")
        return [SupersetDataQueryService._normalize_record(record) for record in records]

    @staticmethod
    def _normalize_record(record: dict[str, Any]) -> dict[str, Any]:
        normalized: dict[str, Any] = {}
        for key, value in record.items():
            if hasattr(value, "isoformat"):
                try:
                    normalized[str(key)] = value.isoformat()
                    continue
                except TypeError:
                    pass
            if hasattr(value, "item"):
                try:
                    normalized[str(key)] = value.item()
                    continue
                except Exception:
                    pass
            normalized[str(key)] = value
        return normalized
