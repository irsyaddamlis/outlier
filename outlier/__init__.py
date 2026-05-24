from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("outlier")    # auto-reads from pyproject.toml
except PackageNotFoundError:
    __version__ = "unknown"             # fallback if not installed yet

__author__ = "Your Name"
__email__ = "your@email.com"
__license__ = "MIT"
__status__ = "Development"

from .detector import OutlierDetector

__all__ = ["OutlierDetector"]