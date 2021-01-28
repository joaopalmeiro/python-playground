# Source: https://youtu.be/fclLpp9U8aw.

import warnings

try:
    from IPython.display import HTML, Javascript, display
except ImportError:
    msg = "It must be used in Jupyter Notebook."
    warnings.warn(msg)
