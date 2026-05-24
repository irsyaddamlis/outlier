from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("outlier")    # auto-reads from pyproject.toml
except PackageNotFoundError:
    __version__ = "unknown"             # fallback if not installed yet

__author__ = "Irsyad Damlis"
__email__ = "irsyad.damlis@gmail.com"
__license__ = "arch-notions"

from .detector import OutlierDetector

__all__ = ["OutlierDetector"]