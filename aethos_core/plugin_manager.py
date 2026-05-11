"""Load optional ``aethos_pro.*`` extensions when enabled (commercial wheel)."""

from __future__ import annotations

import importlib
import os
from typing import Any


class PluginManager:
    """Load proprietary AethOS Pro modules when ``AETHOS_PRO_ENABLED`` is true."""

    @staticmethod
    def load_proprietary(module_name: str, fallback: Any | None = None) -> Any | None:
        if not module_name or "." in module_name:
            return fallback
        flag = (os.getenv("AETHOS_PRO_ENABLED") or "").strip().lower()
        if flag not in ("1", "true", "yes"):
            return fallback
        try:
            return importlib.import_module(f"aethos_pro.{module_name}")
        except ImportError:
            return fallback

    @staticmethod
    def is_pro_available() -> bool:
        """True when ``aethos_pro`` is installed and a license env var is set."""
        try:
            import importlib

            importlib.import_module("aethos_pro")
        except ImportError:
            return False
        key = (os.getenv("AETHOS_LICENSE_KEY") or os.getenv("NEXA_LICENSE_KEY") or "").strip()
        return bool(key)


__all__ = ["PluginManager"]
