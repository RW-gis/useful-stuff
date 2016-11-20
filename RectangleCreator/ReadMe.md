This is a simple script for use with QGIS to create a rectangle polygon.

The rectangle is added it to a temporary layer. It can then be copied, and duplicated. 

The intention is to provide an easy way to define a rectangle which can be used in QGIS Atlas generation. 

When creating an atlas you need a 'coverage layer' - where each object in the layer is used to define the coverage of one page in the atlas. Often when using the atlas function you wish to see on the map what area will be shown on the atlas page (defined in the print composer). On print composer define the box in which the map is to be shown - and note its dimensions (in millimetres). This script will provide you with a rectangle at the appropriate number of metres which for a given scale matches this. 

It is assumed that the user is working with a project using the Ordnance Survey grid CRS (EPSG:27700), and the temporary rectangle is placed at the coordinates 331176,677509 (which is northeast of Edinburgh, Scotland). The script will work for any projected CRS with units in metres, in that it simply defines a rectangle with the appropriate number of metres dimension.

To install copy the two files into the folder on your machine where user processing scripts are stored (on Windows this is likely to be something like: C:\Users\[username]\.qgis2\processing\scripts (where [username] is replaced by a user name). Re-start QGIS. 

To run the script on QGIS:
Menu item: Processing | Toolbox 
(the processing toolbox panel becomes visible)
Select item from panel: Scripts | User scripts | RectangleCreator
(A processing window becomes visible)

x_millimeters_on_paper: write the number of millimetres for the x dimension (left-right) for the print composer map
y_millimeters_on_paper: write the number of millimetres for the y dimension (up-down) for the print composer map
scale_to_print_at: write the scale at which you are going to print the paper map (e.g. '25000' for a 1:25000 scale). 

Click the 'run' button. Click the 'close' button.
