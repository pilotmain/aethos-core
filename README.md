# AethOS Core

Open-source building blocks from the AethOS stack: user-facing **response cleanup**, minimal **file** and **command** helpers, and a **plugin loader** for optional commercial extensions (`aethos-pro`).

## License

Apache-2.0 — see `LICENSE`.

## Installation

```bash
pip install "aethos-core @ git+https://github.com/pilotmain/aethos-core.git"
# or from a checkout:
pip install .
```

## Usage

```python
from aethos_core import (
    PluginManager,
    clean_response_formatting,
    execute_command,
    read_text,
    write_text,
)

text = clean_response_formatting("**1.** First item")
code, out, err = execute_command(["python", "-c", "print(1)"])
```

Standalone installs use a **reduced** `finalize_user_facing_text` pipeline unless the full AethOS `app` package is available.

## AethOS Pro (commercial)

Advanced goal planning, self-healing, negotiation, and enterprise features ship in the private **`aethos-pro`** package. Set `AETHOS_PRO_ENABLED=true` and install `aethos-pro` to load `aethos_pro.*` modules via `PluginManager`.

Contact: **license@aethos.ai**

## Development

```bash
pip install -e ".[dev]"
pytest
```
