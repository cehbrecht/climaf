"""
This module declares locations for searching data for CORDEX outputs.

Example for a CORDEX dataset declaration ::

 >>> tas1pc=ds(project='CORDEX', model='CNRM-CM6-1', experiment='1pctCO2', variable='tas', table='Amon',
               realization='r3i1p1f2', period='1860-1861')
"""

import os
from climaf.dataloc import dataloc
from climaf.classes import cproject, calias, cfreqs, cdef


root = '/opt/data'


# Declare a 'CMIP6 CliMAF project
cproject('CMIP6', 'root',
         'product',
         'domain',
         'institute',
         'experiment',
         'realization',
         'model',
         'frequency',
         'variable',
         'version',
         )
# Set default values
cdef('root', root, project='CORDEX')
cdef('procuct', '*', project='CORDEX')
cdef('institute', '*', project='CORDEX')
cdef('realization', 'r1i1p1', project='CORDEX')
cdef('experiment', 'historical', project='CORDEX')
cdef('version', '*', project='CORDEX')


# Define the patterns
# "/opt/data/cordex/output/AFR-44i/MOHC/ECMWF-ERAINT/evaluation/r1i1p1/MOHC-HadRM3P/v1/mon/tasmin/v20131211/
#    tasmin_AFR-44i_ECMWF-ERAINT_evaluation_r1i1p1_MOHC-HadRM3P_v1_mon_199001-199012.nc"
base_pattern = "${root}/cordex/"
base_pattern += "${product}/"
base_pattern += "${domain}/"
base_pattern += "${institute}/*/"
base_pattern += "${experiment}/"
base_pattern += "${realization}/"
base_pattern += "${model}/*/"
base_pattern += "${frequency}/"
base_pattern += "${variable}/"
base_pattern += "${version}/"
base_pattern += "${variable}_${domain}_*_${experiment}_${realization}_${model}_*_${frequency}_"
patterns = []
for date_format in ["YYYY-YYYY", "YYYYMM-YYYYMM", "YYYYMMDD-YYYYMMDD", "YYYYMMDDHHMM-YYYYMMDDHHMM"]:
    patterns.append(base_pattern + date_format + ".nc")

# call the dataloc CliMAF function
dataloc(project='CORDEX', organization='generic', url=patterns)

# calias('CMIP6', 'tos', offset=273.15)
# calias('CMIP6', 'thetao', offset=273.15)
# calias('CMIP6', 'sivolu', 'sivol')
# calias('CMIP6', 'sic', 'siconc')
# calias('CMIP6', 'sit', 'sithick')
# calias('CMIP6', 'NO3', 'no3')
# calias('CMIP6', 'PO4', 'po4')
# calias('CMIP6', 'Si', 'si')
# calias('CMIP6', 'O2', 'o2')
