# open3d-unofficial-arm

Universal Open3D installer that works on all platforms.

## What is this?

This package provides a universal way to install Open3D that automatically does the right thing for your platform:

- **ARM64 (aarch64)**: Installs pre-built ARM wheels (Open3D 0.19.0) - a stop-gap while waiting for official ARM support
- **Other platforms** (x86_64, etc.): Installs the official `open3d` package from PyPI

No more platform-specific installation logic in your code!

## Installation

```bash
pip install open3d-unofficial-arm
```

## Usage

### Option 1: Direct Import (Recommended)
```python
import open3d_unofficial_arm as o3d

# Use it like normal open3d
pcd = o3d.geometry.PointCloud()
```

On first import, this automatically installs the appropriate Open3D package for your platform.

### Option 2: Traditional Import
```bash
# One-time setup after installation:
open3d-arm-setup
```

Then in your code:
```python
import open3d as o3d
```

### Option 3: In Your Project
Add to your `requirements.txt`:
```
open3d-unofficial-arm
```

Then in your code:
```python
import open3d_unofficial_arm  # Triggers auto-install
import open3d as o3d          # Now works everywhere
```

## Supported Platforms

**ARM64:**
- **OS**: Linux (manylinux_2_35)
- **Architecture**: ARM64 (aarch64)
- **Python versions**: 3.10, 3.11, 3.12, 3.13

**Other platforms:**
- Automatically installs official `open3d` package with full platform support

## How It Works

1. When you import `open3d_unofficial_arm`, it checks if `open3d` is installed
2. If not, it automatically installs:
   - ARM64: Bundled wheel for your Python version
   - Other platforms: Official `open3d` from PyPI
3. Re-exports all `open3d` functionality for direct use

## Notes

- This is an **unofficial** package and is not affiliated with the Open3D project
- On ARM64: Uses bundled wheels as a temporary solution until official ARM support is available
- On other platforms: Installs the official open3d package
- The package automatically detects your platform and installs the correct version

## License

MIT License - See LICENSE file for details

The bundled Open3D wheels are subject to their own license terms.
