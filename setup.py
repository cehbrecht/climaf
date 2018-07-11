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
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='climaf',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      keywords='python climate model',
      author='Stéphane Sénési',
      author_email="",
      url='https://github.com/senesis/climaf',
      license="CeCILL-C license",
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      entry_points={
          'console_scripts': []},
      )
