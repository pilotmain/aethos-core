"""AethOS Core — open-source utilities and optional Pro plugin loading."""

from __future__ import annotations

from .command_executor import execute_command
from .file_ops import read_text, write_text
from .plugin_manager import PluginManager
from .response_formatter import (
    LIST_FORMATTING_LLM_GUIDANCE,
    clean_response_formatting,
    finalize_user_facing_text,
)

__version__ = "1.0.0"

__all__ = [
    "PluginManager",
    "LIST_FORMATTING_LLM_GUIDANCE",
    "clean_response_formatting",
    "finalize_user_facing_text",
    "execute_command",
    "read_text",
    "write_text",
    "__version__",
]
