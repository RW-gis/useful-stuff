This folder contains some useful resources related to Ordnance Survey data or mapping and QGIS.

terrain50_example.vrt is a vrt file for using with QGIS and the Ordnance Survey Terrain 50 DEM raster data available from here:
https://www.ordnancesurvey.co.uk/opendatadownload/products.html

A vrt file effectively means you can load up a whole set of raster files all in one go - properly georeferenced so that they make a single layer. Without this you'd have to load them up one by one.

Download the terrain50 data - it comes in a zip file terr50_gagg_gb.zip
Unzip this file to make a folder terr50_gagg_gb, which contains a folder 'data' and a file licence.txt
Don't unzip the data files (within the data folder).

This file should be downloaded and edited with a text editor. 

This file is formatted for use on Microsoft Windows. I have not tested it on other operating systems - however based on some information I'm guessing that the '\' backslashes need to be '/' forward slashes, and '/vsizip/ may need to be '/vsizip//'. If you're just using Windows read on...

Use find and replace. The lines with content like the one below need to be changed:

<SourceFilename relativeToVRT="0">/vsizip/C:\Users\****PUT_THE_PATH_TO_FILES_HERE****\terr50_gagg_gb\data\hp\hp40_OST50GRID_20160726.zip\HP40.asc</SourceFilename>

As is obvious ****PUT_THE_PATH_TO_FILES_HERE**** needs to be updated with the path to the data on your computer/system. You may need to change the section which reads 'C:\Users\' too of course.

You also need to update the part of the address of each zip file (in the case above 'hp40_OST50GRID_20160726.zip') which reads 'OST50GRID_20160726'. Ordnance Survey change this when they update the data - you can see that 20160726 is a date. Check within the zip files in the 'data' folder (and any sub-folder) to see what date is used in the file/folder names for the data you have downloaded. Update the vrt file to match this.

Load the vrt file into QGIS using the button for loading a raster file. It may take considerable time to load and display. If you're having problems copy and unzip one single .asc file from those in the 'data' folder and load this into QGIS on its own so you can see what to expect (you may need to pan the map to the appropriate place of course). 
