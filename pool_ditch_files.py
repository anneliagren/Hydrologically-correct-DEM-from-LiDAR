import os
import glob
import shutil

original_dir = '/data/original/'
out_dir = '/data/pooled_ditch_files/'
list_ditch_files = glob.glob('/data/original/**/**/*.tif', recursive = True)

non_border = []
for i in list_ditch_files:
    if 'border' not in i:
        filename = os.path.basename(i)
        out = out_dir + filename
        shutil.copy(i, out)
        print('copied ', i)
