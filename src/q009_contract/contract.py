from __future__ import annotations

from datetime import datetime
from typing import Any, Mapping


REQUIRED = ("event_id", "event_type", "subject_id", "occurred_at", "version", "source")


def validate_event(value: Mapping[str, Any]) -> list[str]:
    errors = [f"缺少字段：{name}" for name in REQUIRED if name not in value]
    if errors:
        return errors
    if not isinstance(value["version"], int) or isinstance(value["version"], bool) or value["version"] < 1:
        errors.append("version 必须是正整数")
    try:
        timestamp = datetime.fromisoformat(str(value["occurred_at"]).replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            errors.append("occurred_at 必须带时区")
    except ValueError:
        errors.append("occurred_at 格式无效")
    return errors
