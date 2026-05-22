from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_DASHBOARD_DIR = REPO_ROOT / "report_dashboard"
REPORT_DASHBOARD_SRC_DIR = REPORT_DASHBOARD_DIR / "src"

for path in (str(REPORT_DASHBOARD_DIR), str(REPORT_DASHBOARD_SRC_DIR)):
    if path not in sys.path:
        sys.path.insert(0, path)

from config import OUTPUT_DIR, SUPERSET_CONFIG  # type: ignore  # noqa: E402
from api_client import create_data_fetcher  # type: ignore  # noqa: E402
from html_generator import (  # type: ignore  # noqa: E402
    generate_large_pos_dashboard_html,
    generate_small_pos_dashboard_html,
)
from pdf_generator import get_playwright_status, html_to_pdf  # type: ignore  # noqa: E402


@dataclass(slots=True)
class ReportRequestSpec:
    query: str
    stat_month: str | None = None
    generate_pdf: bool = True
    generate_html: bool = True
    dashboard_type: str = "both"
    output_dir: str | None = None


class ReportDashboardGenerator:
    def __init__(self, *, output_dir: str | None = None) -> None:
        resolved_output_dir = output_dir or str(REPORT_DASHBOARD_DIR / OUTPUT_DIR)
        self.output_dir = Path(resolved_output_dir)

    def generate(self, spec: ReportRequestSpec) -> dict[str, Any]:
        output_dir = Path(spec.output_dir) if spec.output_dir else self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        normalized_type = (spec.dashboard_type or "both").lower()
        selected_types = self._resolve_dashboard_types(normalized_type)

        fetcher = create_data_fetcher(
            {
                "mode": "api",
                "base_url": SUPERSET_CONFIG.get("base_url"),
                "username": SUPERSET_CONFIG.get("username"),
                "password": SUPERSET_CONFIG.get("password"),
            }
        )
        try:
            dashboard_data_map: dict[str, dict[str, Any]] = {}
            if "large_pos" in selected_types:
                dashboard_data_map["large_pos"] = fetcher.fetch_large_pos_dashboard(spec.stat_month)
            if "small_pos" in selected_types:
                dashboard_data_map["small_pos"] = fetcher.fetch_small_pos_dashboard(spec.stat_month)
        finally:
            if hasattr(fetcher, "close"):
                fetcher.close()

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        artifacts: list[dict[str, Any]] = []
        for dashboard_key in selected_types:
            dashboard_data = dashboard_data_map[dashboard_key]
            html_content = self._generate_html(dashboard_key, dashboard_data)
            latest_month = dashboard_data.get("latest_month") or spec.stat_month or "unknown"
            label = self._dashboard_label(dashboard_key)
            html_path = output_dir / f"{label}_{latest_month}_{timestamp}.html"
            pdf_path = output_dir / f"{label}_{latest_month}_{timestamp}.pdf"

            html_written = False
            pdf_written = False
            pdf_error = None

            with html_path.open("w", encoding="utf-8") as handle:
                handle.write(html_content)
            html_written = True

            if spec.generate_pdf:
                try:
                    pdf_written = html_to_pdf(str(html_path), str(pdf_path), auto_setup=True)
                    if not pdf_written:
                        pdf_error = "pdf_generation_unavailable"
                except Exception as exc:  # pragma: no cover - defensive around external renderer
                    pdf_error = str(exc)
                    pdf_written = False

            if not spec.generate_html and html_written and pdf_written:
                html_path.unlink(missing_ok=True)
                html_written = False

            artifacts.append(
                {
                    "dashboard_type": dashboard_key,
                    "title": dashboard_data.get("title", label),
                    "latest_month": latest_month,
                    "update_time": dashboard_data.get("update_time"),
                    "summary": dashboard_data.get("summary", {}),
                    "html_path": str(html_path) if html_written else None,
                    "pdf_path": str(pdf_path) if pdf_written else None,
                    "pdf_error": pdf_error,
                }
            )

        return {
            "query": spec.query,
            "stat_month": spec.stat_month or self._infer_stat_month(artifacts),
            "dashboard_type": normalized_type,
            "artifacts": artifacts,
            "playwright_status": get_playwright_status() if spec.generate_pdf else None,
        }

    @staticmethod
    def _resolve_dashboard_types(dashboard_type: str) -> list[str]:
        mapping = {
            "large_pos": ["large_pos"],
            "small_pos": ["small_pos"],
            "both": ["large_pos", "small_pos"],
        }
        try:
            return mapping[dashboard_type]
        except KeyError as exc:
            raise ValueError(f"Unsupported dashboard_type: {dashboard_type}") from exc

    @staticmethod
    def _dashboard_label(dashboard_type: str) -> str:
        return {
            "large_pos": "merchant_collection_dashboard",
            "small_pos": "small_pos_product_dashboard",
        }[dashboard_type]

    @staticmethod
    def _generate_html(dashboard_type: str, data: dict[str, Any]) -> str:
        if dashboard_type == "large_pos":
            return generate_large_pos_dashboard_html(data)
        return generate_small_pos_dashboard_html(data)

    @staticmethod
    def _infer_stat_month(artifacts: list[dict[str, Any]]) -> str | None:
        for artifact in artifacts:
            latest_month = artifact.get("latest_month")
            if latest_month:
                return str(latest_month)
        return None
