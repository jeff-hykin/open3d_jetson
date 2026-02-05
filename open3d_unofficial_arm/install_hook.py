"""
Auto-install hook for open3d-unofficial-arm.
This runs automatically when the package is installed.
"""
import sys
import platform
import subprocess
import tempfile
import urllib.request
from pathlib import Path


# GitHub repository info
GITHUB_REPO = "jeff-hykin/open3d_jetson"
GITHUB_BRANCH = "master"
WHEELS_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/open3d_unofficial_arm/wheels"

# Available wheel files
AVAILABLE_WHEELS = {
    "cp310": "open3d-0.19.0-cp310-cp310-manylinux_2_35_aarch64.whl",
    "cp311": "open3d-0.19.0+db32df3a-cp311-cp311-manylinux_2_35_aarch64.whl",
    "cp312": "open3d-0.19.0-cp312-cp312-manylinux_2_35_aarch64.whl",
    "cp313": "open3d-0.19.0+db32df3a-cp313-cp313-manylinux_2_35_aarch64.whl",
}


def download_wheel(url, dest_path):
    """Download a wheel file from URL."""
    try:
        print(f"open3d-unofficial-arm: Downloading from {url}...", file=sys.stderr)
        urllib.request.urlretrieve(url, dest_path)
        print(f"open3d-unofficial-arm: Download complete ({dest_path.stat().st_size // (1024*1024)} MB)", file=sys.stderr)
    except Exception as e:
        print(f"open3d-unofficial-arm: ERROR downloading wheel: {e}", file=sys.stderr)
        raise


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

    try:
        if is_arm:
            # Install from GitHub-hosted wheels
            py_version = f"cp{sys.version_info.major}{sys.version_info.minor}"

            if py_version not in AVAILABLE_WHEELS:
                available = list(AVAILABLE_WHEELS.keys())
                raise RuntimeError(
                    f"No wheel available for Python {sys.version_info.major}.{sys.version_info.minor} on aarch64. "
                    f"Available Python versions: {', '.join(available)}"
                )

            wheel_filename = AVAILABLE_WHEELS[py_version]
            wheel_url = f"{WHEELS_BASE_URL}/{wheel_filename}"

            print(f"open3d-unofficial-arm: Installing Open3D for ARM64...", file=sys.stderr)

            # Download to temporary directory
            with tempfile.TemporaryDirectory() as tmpdir:
                wheel_path = Path(tmpdir) / wheel_filename
                download_wheel(wheel_url, wheel_path)

                # Install the downloaded wheel (show output for debugging)
                print(f"open3d-unofficial-arm: Installing wheel...", file=sys.stderr)
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", str(wheel_path)],
                    capture_output=True,
                    text=True
                )

                if result.returncode != 0:
                    print(f"open3d-unofficial-arm: pip install failed!", file=sys.stderr)
                    print(f"STDOUT: {result.stdout}", file=sys.stderr)
                    print(f"STDERR: {result.stderr}", file=sys.stderr)
                    raise RuntimeError(f"Failed to install wheel: {result.stderr}")

            print("open3d-unofficial-arm: Installation complete!", file=sys.stderr)

            # Verify installation
            try:
                import open3d
                print(f"open3d-unofficial-arm: ✓ Open3D {open3d.__version__} is now available", file=sys.stderr)
            except ImportError as e:
                print(f"open3d-unofficial-arm: WARNING - Installation completed but open3d still not importable: {e}", file=sys.stderr)
                raise

        else:
            # Install official package from PyPI
            print(f"open3d-unofficial-arm: Installing official Open3D from PyPI...", file=sys.stderr)
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "open3d"],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"open3d-unofficial-arm: pip install failed!", file=sys.stderr)
                print(f"STDERR: {result.stderr}", file=sys.stderr)
                raise RuntimeError(f"Failed to install open3d: {result.stderr}")

            print("open3d-unofficial-arm: Installation complete!", file=sys.stderr)

    except Exception as e:
        print(f"open3d-unofficial-arm: FATAL ERROR during installation: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        # Don't raise - allow import to succeed even if open3d installation failed
        # User will get error when they try to use it


# Run the auto-install when this module is imported
auto_install_open3d()
