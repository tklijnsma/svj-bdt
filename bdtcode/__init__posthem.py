import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

UL = False
def do_ultra_legacy(flag=True):
    global UL
    UL = flag

from . import crosssections
from . import dataset
from . import histogramming_PostHEM
from . import utils
from . import sample_posthem