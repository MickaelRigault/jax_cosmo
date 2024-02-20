# Cosmology in JAX
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


from . import angular_cl as cl
from . import background as background
from . import bias as bias
from . import likelihood as likelihood
from . import power as power
from . import probes as probes
from . import redshift as redshift
from . import transfer as transfer
from .core import *
from .parameters import *
from . import sparse as sparse
