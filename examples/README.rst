.. sidebar:: Ipython notebooks

   An Ipython notebook is a way to mix Python commands, their results, comments and notes; results can be graphics; you can also edit and replay the commands, and edit the comments at length; 

   You can save the resulting notebook and restore it with or without re-executing the Python code; some people see it as the ultimate form of a laboratory notebook, allowing for recording a research/analysis interactive session after some house-cleaning for false tries

   This is documented at length at `Ipython notebooks <http://ipython.org/notebook.html>`_. 

   **For running the example Ipython notebook**, first launch Firefox
   (on the same machine as the one used hereafter - you muse use ``ssh
   -x`` if necessary ) and then execute ::

     
     $ cd <climaf_dir>
     $ export PYTHONPATH=$PYTHONPATH:$(pwd)
     $ cd examples
     $ ipython notebook 

     # Once the notebook server tab shows in your favorite Web Browser, 
     # just click on "ATourOfClimaf"


:download:`A Tour Of Climaf <../examples/ATourOfCliMAF.html>` is **a progressive and but quite comprehensive tour**, which is :download:`here presented as an html page <../examples/ATourOfCliMAF.html>` , but which can also be run as an IPython notebook (see sidenote); the nootebook content is currently behind the status of CliMAF

For **running CliMAF**, or running one of the Python scripts example described below, you will use a Python shell, after telling Python where the CliMAF code is:: 

    $ export PYTHONPATH=$PYTHONPATH:<climaf_dir>
    $ python

::

    >>> from climaf.api import *
    >>> .... 


A number of examples show in directory ``<climaf_dir>/examples`` and are also dowloadable using the links below; you will copy and paste the code lines to the Python shell using your favorite method. Each code line is documented by a comment which tries to bring all necessary information for letting your CliMAF expertise grow steadily. 

.. |indx| image:: html_index.png 
  :scale: 13%



Some of the examples can be run anywhere, as they use the data sample installed with CliMAF :

  - :download:`plotmap.py <../examples/plotmap.py>`      : basic and advanced map plotting (using ncview and ncl)
  - :download:`plot_xsection.py <../examples/plot_xsection.py>`:
    plotting a pressure-lat or pressure-lon cross section
  - :download:`basic_oce.py <../examples/basic_oce.py>`   : acces ocean data on ORCA grid in CMIP5_DRS data, and perfome some basic operations (works at CNRM and on Ciclad)
  - :download:`export.py <../examples/export.py>`        : various ways to 'export' results out of CliMAF
  - :download:`derived.py <../examples/derived.py>`      : how to define a new geophysical variable and use it in CliMAF
  - :download:`increm.py <../examples/increm.py>`        : compute any derived variable incrementally (i.e. using new inputs as they become available)
  - :download:`latlonbox.py <../examples/latlonbox.py>`  : define a dataset on a lat-lon box; also extract a box out of a dataset
  - :download:`regrid.py <../examples/regrid.py>`        : regrid some data or object to a named grid or to the grid of another object/data
  - :download:`ann_cycle.py <../examples/ann_cycle.py>`  : compute an annual cycle, using CDO
  - :download:`macro.py <../examples/macro.py>`          : define a macro in-a-while, use it, save it, ....
  - :download:`ensemble.py <../examples/ensemble.py>`    : how to create ensembles and compute with it
  - :download:`index_html.py <../examples/index_html.py>`: create an
    :download:`html index <html_index.png>` including multiple tables of links to figures, possibly
    with thumbnails. 


.. _examples_data:

Others show how to acces some known data sets on CNRM or IPSL file system :
 
  - :download:`data_cmip6drs.py  <../examples/data_cmip6drs.py>`    : access data which are organized using the CMIP5 Data Reference Syntax 
  - :download:`data_cmip5drs.py  <../examples/data_cmip5drs.py>`    : access data which are organized using the CMIP5 Data Reference Syntax 
  - :download:`data_generic.py <../examples/data_generic.py>`     : using the 'generic' type of organization on various examples : 
     - OCMIP5 data on Ciclad
     - Obs4MIPS data at CNRM
     - CAMI Obs data at CNRM
     - example data as included in CliMAF package
  - :download:`data_em.py <../examples/data_em.py>`     : access CNRM-CM data organized 'a la EM'
  - :download:`seaice.py <../examples/seaice.py>`       : access and
    plot ORCA1-grid sea-ice data, with control on levels and projection  
  - :download:`data_obs <../examples/data_obs.py>`      : access
    observation data sets as handled at CNRM by VDR

.. _examples_operators:

If you have Cdftools 3.0 installed (in a flavor with some bugfixes,
and with CMIP variable names in modcdfnames.F90 when applicable) , you may use it through CliMAF :

  - :download:`cdftools.py  <../examples/cdftools.py>`   : easy access to basic Cdftools operators
  - :download:`cdftransport.py  <../examples/cdftransport.py>`   : computing transport is a little more tricky
    



