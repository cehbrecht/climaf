# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = __import__('climaf').version
description = 'CliMAF: a Climate Model Assessment Framework.'
long_description = (
    open('README.rst').read()
)

requires = [line.strip() for line in open('requirements.txt')]

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    # 'License :: CeCILL-C Free Software License Agreement (CECILL-C)'
]

setup(name='climaf',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      keywords='python climate model',
      author='',
      author_email="",
      url='https://github.com/senesis/climaf',
      license="CeCILL-C license",
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      scripts=[
          'bin/climaf',
          'bin/exiv2',
          'bin/pdfcrop',
          'climaf/scripts/cdfsectionsm.sh',
          'climaf/scripts/cdfsections.sh',
          'climaf/scripts/cdftransport.sh',
          'climaf/scripts/cdftransp.sh',
          'climaf/scripts/clean_pdf.sh',
          'climaf/scripts/curl_tau_atm.jnl',
          'climaf/scripts/curves.ncl',
          'climaf/scripts/ensemble_time_series_plot.py',
          'climaf/scripts/gplot.ncl',
          'climaf/scripts/hovmoller.ncl',
          'climaf/scripts/ks.sh',
          'climaf/scripts/LinearRegression_UVCDAT.py',
          'climaf/scripts/mcdo_remote.py',
          'climaf/scripts/mcdo.sh',
          'climaf/scripts/mcdo_aux.sh',
          'climaf/scripts/mean_and_std.sh',
          'climaf/scripts/ml2pl.sh',
          'climaf/scripts/ml2pl',
          'climaf/scripts/mtimavg.sh',
          'climaf/scripts/plot_cross_section.ncl',
          'climaf/scripts/plotmap.ncl',
          'climaf/scripts/read_ncks.sh',
          'climaf/scripts/regridll.sh',
          'climaf/scripts/regrid.sh',
          'climaf/scripts/time_average_basics.sh',
          'climaf/scripts/wcdo.sh',
      ],)
