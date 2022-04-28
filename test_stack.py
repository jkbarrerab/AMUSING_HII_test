import edge_pydb.util as edgeutil
import numpy as np
from astropy.io import fits, ascii
import os, fnmatch
from collections import Counter
import re

from astropy.table import QTable, Column, join, Table, vstack, hstack
from matplotlib import pyplot as plt

#path of files
path_files = '/Users/jorgebarrera/Dropbox/Public/AMUSING/2022/HIIblob/cat_HII_pyHIIexplorer.220125/HII/HII_fe/'
names = os.listdir(path_files)
print(len(names))
data =[]

for i in range(len(names)):
    converters = {'HIIREGID': [ascii.convert_numpy(str)]}
    aux = Table.read(path_files+names[i], converters=converters)
    data.append(aux)
    print(i,'of', len(names))
print('stacking individual files ...')    
flux_cat = vstack(data)
print('done...')
# Adding Galaxy name column

name_gal=[]
print('adding name column ...')
for i in flux_cat['HIIREGID']:
        val_now = i.rstrip('1234567890')
        name_gal.append(val_now.rstrip('-'))
        
flux_cat.add_column(name_gal, name='Name', index=1)        

print('done...')

print('writing the ecsv catalogue ...')

flux_cat.write('cat_flux_elines.table.ecsv', overwrite=True)

print('done!')
