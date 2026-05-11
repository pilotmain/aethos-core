"""Lightweight command execution helper for standalone ``aethos-core``."""

from __future__ import annotations

import subprocess
from typing import Sequence


def execute_command(
    argv: str | Sequence[str],
    *,
    cwd: str | None = None,
    timeout: float | None = 120.0,
    env: dict[str, str] | None = None,
) -> tuple[int, str, str]:
    """
    Run a subprocess; return ``(returncode, stdout, stderr)``.

    ``argv`` may be a shell string (POSIX) or argument list (preferred).
    """
    if isinstance(argv, str):
        proc = subprocess.run(
            argv,
            shell=True,
            cwd=cwd,
            timeout=timeout,
            env=env,
            capture_output=True,
            text=True,
        )
    else:
        proc = subprocess.run(
            list(argv),
            shell=False,
            cwd=cwd,
            timeout=timeout,
            env=env,
            capture_output=True,
            text=True,
        )
    return proc.returncode, proc.stdout or "", proc.stderr or ""


__all__ = ["execute_command"]
