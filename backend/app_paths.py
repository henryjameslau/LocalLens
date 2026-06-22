import os
import sys
from pathlib import Path


def get_app_data_dir() -> Path:
    """
    Resolve the LocalLens data directory and ensure it exists.

    Priority:
    1) LOCALLENS_DATA_DIR override (useful to force index storage to a local disk)
    2) Platform default:
       - Windows: %APPDATA%/LocalLens
       - macOS:   ~/Library/Application Support/LocalLens
       - Linux:   $XDG_CONFIG_HOME/LocalLens or ~/.config/LocalLens
    """
    override = os.getenv("LOCALLENS_DATA_DIR")
    if override:
        app_data_path = Path(override).expanduser()
    elif sys.platform == "win32":
        appdata_env = os.getenv("APPDATA")
        if not appdata_env:
            raise RuntimeError("APPDATA environment variable is not set on Windows.")
        app_data_path = Path(appdata_env) / "LocalLens"
    elif sys.platform == "darwin":
        app_data_path = Path.home() / "Library" / "Application Support" / "LocalLens"
    else:
        xdg_config_home = os.getenv("XDG_CONFIG_HOME")
        base = Path(xdg_config_home).expanduser() if xdg_config_home else (Path.home() / ".config")
        app_data_path = base / "LocalLens"

    app_data_path.mkdir(parents=True, exist_ok=True)
    return app_data_path
