"""
open3d-unofficial-arm: Universal Open3D installer

This package provides a universal way to install Open3D that works on all platforms:
- ARM64 (aarch64): Installs from bundled wheels (0.19.0)
- Other platforms (x86_64, etc.): Installs official open3d package from PyPI

Usage in your code:
    import open3d_unofficial_arm as o3d  # Auto-installs and imports open3d
    # OR
    import open3d_unofficial_arm  # Just install
    import open3d as o3d          # Then use normally

Post-install setup (one-time):
    open3d-arm-setup    # Ensures open3d is installed
"""

__version__ = "0.19.0.post2"

# Auto-trigger installation on first import
from .install_hook import auto_install_open3d
auto_install_open3d()

# Re-export everything from open3d for convenience
from open3d import *  # noqa: F401, F403


if __name__ == "__main__":
    auto_install_open3d()
