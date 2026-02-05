# open3d-unofficial-arm

Unofficial ARM (aarch64) wheel distribution for Open3D.

## What is this?

This is a stop-gap package providing pre-built ARM wheels for Open3D while waiting for official ARM support. It contains Open3D 0.19.0 wheels built for Linux ARM64 (aarch64) architecture.

## Installation

```bash
pip install open3d-unofficial-arm
```

This will automatically install the appropriate Open3D wheel for your Python version (3.10 or 3.12).

## Supported Platforms

- **OS**: Linux (manylinux_2_35)
- **Architecture**: ARM64 (aarch64)
- **Python versions**: 3.10, 3.12

## Usage

After installation, simply import open3d as usual:

```python
import open3d as o3d
```

## Notes

- This is an **unofficial** package and is not affiliated with the Open3D project
- This is a temporary solution until official ARM support is available
- The package automatically installs the correct wheel for your Python version

## License

MIT License - See LICENSE file for details

The bundled Open3D wheels are subject to their own license terms.
