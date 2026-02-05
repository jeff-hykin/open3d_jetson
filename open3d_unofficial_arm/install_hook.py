"""
Auto-install hook for open3d-unofficial-arm.
This runs automatically when the package is installed.
"""
import sys
import platform
import subprocess
from pathlib import Path


def auto_install_open3d():
    """Check if open3d is installed, and install it if not."""
    try:
        import open3d
        # Already installed, nothing to do
        return
    except ImportError:
        pass

    # open3d not found, install it
    is_arm = platform.machine() == "aarch64"

    if is_arm:
        # Install from bundled wheels
        wheels_dir = Path(__file__).parent / "wheels"
        py_version = f"cp{sys.version_info.major}{sys.version_info.minor}"
        wheel_files = list(wheels_dir.glob(f"open3d-*-{py_version}-*.whl"))

        if wheel_files:
            print(f"open3d-unofficial-arm: Installing Open3D from bundled ARM wheel...", file=sys.stderr)
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", str(wheel_files[0])],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
    else:
        # Install official package from PyPI
        print(f"open3d-unofficial-arm: Installing official Open3D from PyPI...", file=sys.stderr)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet", "open3d"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


# Run the auto-install when this module is imported
auto_install_open3d()
