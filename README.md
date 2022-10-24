# Calulating distance to ditch across Sweden
How to make a rasterlayer for Sweden with latteral (eucledian) distance to ditch.  

The ditcehs are defined as the AI detected ditcehs in DOI: 10.1061/JIDEDH/IRENG-9796.


# With docker container:
docker build -t dem .

**Start container**

docker run -it  --mount type=bind,source=/mnt/Extension_100TB/national_datasets/ditches/1m/classified,target=/data --mount type=bind,source=/mnt/Extension_100TB/Anneli/DistanceToDitch/,target=/code dem:latest

**Select and copy relevant ditchtiles to new directory**
python3 /code/pool_laz_files.py 

once all data is pooled the script loop_process_new_block.py can be used to create tiles without edgeeffects. This script uses the json files in the metadata directory of each block and intersect the block extent with a lidar tile index file. All raster files that intersect that extent gets copied to a new directory. This includes neighbouring tiles. Raster tiles are then created from the copied raster tiles but only tiles that are inside the block gets copied to the final output directory. This enables looping over lidar blocks and creating a seamless distanace to ditch raster.  


# Process all existing blocks SFA
python E:/William/laserdataskog/loop_process_new_block.py E:/William/Indexrutor/Indexrutor_2_5km_Sverige.shp E:/LAZ/original/ E:/William/laserdataskog/pooled/ E:/William/laserdataskog/workdir/ E:/William/laserdataskog/dem_dir/



# Process all existing blocks docker - SLU
python3 /code/loop_process_new_block.py /code/data/Indexrutor_2_5km_Sverige.shp /data/original/ /data/pooled_laz_files/ /data/workdir/ /data/dem05m/




# Process all existing blocks SLU anaconda
python Y:/William/GitHub/Hydrologically-correct-DEM-from-LiDAR/loop_process_new_block.py Y:/William/GitHub/Hydrologically-correct-DEM-from-LiDAR/data/Indexrutor_2_5km_Sverige.shp Y:/national_datasets/laserdataskog/original/ Y:/national_datasets/laserdataskog/pooled_laz_files/ Y:/national_datasets/laserdataskog/workdir/ /Y:/national_datasets/laserdataskog/dem05m/

# process new block
python E:/William/laserdataskog/loop_process_new_block.py E:/William/Indexrutor/Indexrutor_2_5km_Sverige.shp E:/William/newblock/20C045/ E:/William/laserdataskog/pooled/ E:/William/laserdataskog/workdir/ E:/William/laserdataskog/dem_dir/


python E:/William/laserdataskog/process_new_block.py E:/William/Indexrutor/Indexrutor_2_5km_Sverige.shp E:/William/newblock/20C045/ E:/William/laserdataskog/pooled/ E:/William/laserdataskog/workdir/ E:/William/newblockoutput/

# process remaining files from 2018, 2021 and new files from 2022
# new blocks are stored in E:/LAZ/2018/2022/ the script will loop over each block in this directory
python E:/William/laserdataskog/loop_process_new_block.py E:/William/Indexrutor/Indexrutor_2_5km_Sverige.shp E:/William/newblock/20C045/ E:/William/laserdataskog/pooled/ E:/William/laserdataskog/workdir/ E:/William/laserdataskog/dem_dir/


