"""Minimal file helpers for standalone ``aethos-core`` (OSS)."""

from __future__ import annotations

from pathlib import Path


def read_text(path: str | Path, *, encoding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encoding)


def write_text(path: str | Path, content: str, *, encoding: str = "utf-8") -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding=encoding)


__all__ = ["read_text", "write_text"]
