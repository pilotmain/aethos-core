"""Tests for optional ``aethos_pro`` plugin loader."""

from __future__ import annotations

import os

from aethos_core.plugin_manager import PluginManager


def test_is_pro_available_false_without_wheel(monkeypatch) -> None:
    monkeypatch.delenv("AETHOS_LICENSE_KEY", raising=False)
    monkeypatch.delenv("NEXA_LICENSE_KEY", raising=False)
    assert PluginManager.is_pro_available() is False


def test_load_proprietary_returns_fallback_when_disabled(monkeypatch) -> None:
    monkeypatch.delenv("AETHOS_PRO_ENABLED", raising=False)
    sentinel = object()
    assert PluginManager.load_proprietary("anything", fallback=sentinel) is sentinel


def test_load_proprietary_invalid_name_returns_fallback() -> None:
    assert PluginManager.load_proprietary("bad.name", fallback=1) == 1
