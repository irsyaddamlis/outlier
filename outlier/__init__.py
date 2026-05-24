from importlib.metadata import version, PackageNotFoundError
from .detector import OutlierDetector
import sys

# --- Metadata ---
try:
    __version__ = version("outlier")
except PackageNotFoundError:
    __version__ = "unknown"

__author__ = "Irsyad Damlis"
__email__ = "irsyad.damlis@gmail.com"
__license__ = "MIT"

__all__ = ["OutlierDetector"]

# --- Make module callable: outlier(data) ---
class _CallableModule(sys.modules[__name__].__class__):
    def __call__(self, *args, **kwargs):
        return OutlierDetector(*args, **kwargs)

sys.modules[__name__].__class__ = _CallableModule