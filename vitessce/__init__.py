import sys

from ._version import __version__

from .widget import VitessceWidget
from .config import VitessceConfig, hconcat, vconcat
from .constants import CoordinationType, Component, DataType, FileType
from .wrappers import (
    AbstractWrapper,
    OmeTiffWrapper,
    MultiImageWrapper,
    AnnDataWrapper,
    SnapWrapper,
)
from .entities import (
    CellSets,
    Cells,
    Molecules,
)
from .export import (
    export_to_s3,
    export_to_files,
)

try:
    if "google.colab" in sys.modules:
        from google.colab import output

        output.enable_custom_widget_manager()
except ImportError:
    pass

def _jupyter_labextension_paths():
    """Called by Jupyter Lab Server to detect if it is a valid labextension and
    to install the widget

    Returns
    =======
    src: Source directory name to copy files from. Webpack outputs generated files
        into this directory and Jupyter Lab copies from this directory during
        widget installation
    dest: Destination directory name to install widget files to. Jupyter Lab copies
        from `src` directory into <jupyter path>/labextensions/<dest> directory
        during widget installation
    """
    return [{
        'src': 'labextension',
        'dest': 'vitessce-jupyter',
    }]


def _jupyter_nbextension_paths():
    """Called by Jupyter Notebook Server to detect if it is a valid nbextension and
    to install the widget

    Returns
    =======
    section: The section of the Jupyter Notebook Server to change.
        Must be 'notebook' for widget extensions
    src: Source directory name to copy files from. Webpack outputs generated files
        into this directory and Jupyter Notebook copies from this directory during
        widget installation
    dest: Destination directory name to install widget files to. Jupyter Notebook copies
        from `src` directory into <jupyter path>/nbextensions/<dest> directory
        during widget installation
    require: Path to importable AMD Javascript module inside the
        <jupyter path>/nbextensions/<dest> directory
    """
    return [{
        'section': 'notebook',
        'src': 'nbextension',
        'dest': 'vitessce-jupyter',
        'require': 'vitessce-jupyter/extension'
    }]
