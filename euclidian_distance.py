import os
import geopandas as gpd
import pandas as pd
import shutil
from geopandas.tools import sjoin
import sys
try:
    sys.path.insert(1, 'F:/Diken/WhiteBT') #
    from whitebox_tools import WhiteboxTools
    wbt = WhiteboxTools()
except: 
    print('failed to import local whitebox, using pip instead')
else:
    import whitebox as wbt
# read lidar tile index to geopnadas dataframe (change to ditch tiles)

lidar_tiles_index = gpd.read_file('E:/William/Indexrutor/Indexrutor_2_5km_Sverige.shp')
path_to_block_metadata = 'E:/William/laserdataskog/20D001/metadata/'
json_list = []
for tile in os.listdir(path_to_block_metadata):
    if tile.endswith('.json'):
        name = path_to_block_metadata + tile
        tile_json = gpd.read_file(name)
        json_list.append(tile_json)
# merge all json polygons to a geopandas dataframe        
block_extent = gpd.GeoDataFrame(pd.concat(json_list, ignore_index=True), crs=json_list[0].crs)
# intersecct lidar tiles with block extent with one tile overlap
intersect = gpd.sjoin(lidar_tiles_index, block_extent, how='inner', op='intersects')
# get uniqe names
uniqe_names = intersect['Indexruta'].unique()


path_to_downloaded_data = 'E:/William/laserdataskog/pooled/'
path_to_working_dir = 'E:/William/laserdataskog/workdir/'
names_relevant_tiles = []
for name in os.listdir(path_to_downloaded_data):
    if name.endswith('.laz') and os.path.basename(name[7:20]) in uniqe_names:
        downladed_tile = path_to_downloaded_data + name
        copied_tile = path_to_working_dir + name
        shutil.copy(downladed_tile, copied_tile)
        
        
# Function to gather the file names of TIF files and puts them in a list
def find_tif_files(input_directory): # finds TIF files in an input directory
    files = os.listdir(input_directory)
    file_names = []
    for f in files:
        if f.endswith(".tif"): #change accordingly for appropriate raster type 
            file_names.append(f)
    return file_names


def main():
    ########################
    # Set up WhiteboxTools #
    ########################
    wbt = WhiteboxTools()
    wbt.set_verbose_mode(False) # Sets verbose mode. If verbose mode is False, tools will not print output messages
    #wbt.set_compress_rasters(True) # Compressed TIF file format based on the DEFALTE algorithm
    in_directory = 'E:/William/laserdataskog/workdir/' # Input file directory; change to match your environment
    
    #reclassify ditches to 0 and non-ditches to 1
    wbt.set_working_dir(in_directory)
    wbt.reclass(
    i, 
    output, 
    reclass_vals, 
    assign_mode=False, 
    callback=default_callback
    )
    
    # Calculate Eucledian (horizontal) Distance to Ditch
    wbt.euclidean_distance(
    i, 
    output, 
    callback=default_callback
    )
    
   
    print("Completed Eucledian Distance \n")

    
main()
