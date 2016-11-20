##x_millimetres_on_paper=number
##y_millimetres_on_paper=number
##scale_to_print_at=number

from qgis.core import *
from PyQt4.QtCore import *
#define x and y coordinates based on a fixed starting point, the scale of the box
#and the defined box size to be printed
southwestx = 331176
southwesty = 677509
northwesty = southwesty + (y_millimetres_on_paper * scale_to_print_at / 1000)
southeastx  = southwestx + (x_millimetres_on_paper * scale_to_print_at / 1000)
#define all four points
southwestpoint = QgsPoint(southwestx,southwesty)
northwestpoint = QgsPoint(southwestx,northwesty)
northeastpoint = QgsPoint(southeastx,northwesty)
southeastpoint = QgsPoint(southeastx,southwesty)
#define a list with all four points in it
prototypepoly = [southwestpoint, northwestpoint, northeastpoint, southeastpoint]
#create a memory layer with
#polygon content, called TemporaryRectangleLayer
v_layer = QgsVectorLayer("Polygon", "TemporaryRectangleLayer", "memory")
pr = v_layer.dataProvider()
#create feature
seg = QgsFeature()
# add geometry to feature, 
seg.setGeometry(QgsGeometry.fromPolygon([prototypepoly]))
# add geometry to the layer
pr.addFeatures( [ seg ] )
#update extent of the layer (not necessary)
v_layer.updateExtents()
# show the polygon 
QgsMapLayerRegistry.instance().addMapLayers([v_layer])

