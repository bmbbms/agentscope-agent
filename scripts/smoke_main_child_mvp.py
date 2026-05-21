from __future__ import annotations

import json
import os
import sys
import urllib.request


def main() -> int:
    url = os.getenv("MAIN_AGENT_API_URL", "http://127.0.0.1:8090/main/query")
    token = os.getenv("MAIN_AGENT_API_TOKEN", "")
    payload = {
        "query": "analyze yesterday core merchant gmv drop",
        "user_id": "demo.analyst",
        "tenant_id": "merchant-data",
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"request_failed: {exc}")
        return 1

    print("reply:", body.get("reply"))
    session = body.get("session", {})
    task = body.get("task", {})
    decision = body.get("lifecycle_decision", {})
    print("session_id:", session.get("session_id"))
    print("session_status:", session.get("status"))
    print("task_id:", task.get("task_id"))
    print("task_status:", task.get("status"))
    print("decision:", decision.get("note"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
