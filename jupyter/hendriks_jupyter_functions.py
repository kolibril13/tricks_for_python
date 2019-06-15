from IPython.display import display_html
from ipyleaflet import *
from ipyleaflet import *


def restartkernel() :
    display_html("<script>Jupyter.notebook.kernel.restart()</script>",raw=True)


