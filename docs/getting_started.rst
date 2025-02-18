Getting Started
################

The ``vitessce`` Python package includes:

* **Vitessce as a Jupyter Widget**

  * Use Vitessce directly within Jupyter Notebook or Jupyter Lab as an interactive widget

* **View config API**

  * Create and edit Vitessce configurations using Python object-oriented syntax

* **Data preparation**

  * Use our data conversion wrapper classes to process data stored in common single-cell file types including AnnData and SnapATAC.


Installation
-------------

Installation requires Python 3.8 or greater.

.. code-block:: bash

    pip install vitessce

To use the widget in `Jupyer Notebook <https://jupyter.readthedocs.io/en/latest/install.html#jupyter-notebook-interface>`_ also run the following:

.. code-block:: bash
    
    jupyter nbextension install --py --sys-prefix vitessce
    jupyter nbextension enable --py --sys-prefix vitessce

To use the widget in `JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_ also run the following:

.. code-block:: bash

    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install vitessce-jupyter


Widget Compatibility
--------------------

The Vitessce widget is compatible with the following interactive Python platforms:

* JupyterLab ``>=3.0.0``
* Jupyter Notebook (classic) ``>=1.0.0``


Optional dependencies
---------------------

The following dependencies are optional, and only required when using certain features.

* ``jupyter-server-proxy>=1.5.2`` - Required for using the widget through a proxy (e.g. a cloud notebook service like Binder). See widget parameter ``proxy``.

