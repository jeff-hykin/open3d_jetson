"""
open3d-unofficial-arm: Unofficial ARM builds of Open3D

This package provides ARM (aarch64) wheel files for Open3D 0.19.0 as a stop-gap
solution while waiting for official ARM support to be merged and published.

Usage:
    pip install open3d-unofficial-arm

The package will automatically install the correct Open3D wheel for your
Python version on first import.
"""

__version__ = "0.19.0"

import sys
import platform
import subprocess
from pathlib import Path


def get_wheel_path():
    """Get the path to the appropriate wheel file for this system."""
    if platform.machine() != "aarch64":
        # Silently skip on non-ARM platforms (for development/testing)
        return None

    wheels_dir = Path(__file__).parent / "wheels"
    py_version = f"cp{sys.version_info.major}{sys.version_info.minor}"

    wheel_files = list(wheels_dir.glob(f"open3d-*-{py_version}-*.whl"))

    if not wheel_files:
        available = [w.name for w in wheels_dir.glob("*.whl")]
        raise RuntimeError(
            f"No wheel found for Python {sys.version_info.major}.{sys.version_info.minor} on aarch64. "
            f"Available wheels: {available}"
        )

    return wheel_files[0]


def install_open3d():
    """Install the Open3D wheel for this system."""
    wheel_path = get_wheel_path()

    if wheel_path is None:
        # Not on ARM platform, skip installation
        return

    print(f"Installing Open3D from: {wheel_path}")

    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--quiet", str(wheel_path)
    ])

    print("Open3D installed successfully!")


# Auto-install on first import if open3d is not already available
try:
    import open3d
except ImportError:
    if platform.machine() == "aarch64":
        print("open3d-unofficial-arm: Installing Open3D for ARM64...")
        install_open3d()


if __name__ == "__main__":
    install_open3d()
