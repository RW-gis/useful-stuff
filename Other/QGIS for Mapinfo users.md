# QGIS for Mapinfo users

## Key differences and some key ideas
QGIS opens ’layers’ rather than ‘tables’ (this is the same thing with a different name).
QGIS layers always show up on the list of layers in the ‘Layers panel’ – although they can be hidden of course (unlike the way that Mapinfo can have open tables which aren’t shown anywhere). 
There’s no need (or ability) to have multiple map canvases open. There are easier ways to manage what you’d do with multiple map windows in Mapinfo. If you really need to have two maps showing at the same time you can easily open a second instance of QGIS.
QGIS has a ‘print composer’ rather than a ‘layout window’. Print composers are easy to set up and aren’t tied to the map canvas view in the way that Mapinfo does this – so if you want you can have many different composers focused on different areas. 
QGIS doesn’t use ‘queries’ in the way that Mapinfo does, but there are several ways to achieve the same thing. The closest to a Mapinfo query is to create a ‘virtual layer’ – for which you use an SQL select statement (effectively a query). If you choose to save data in a Spatialite file you can also set up an SQL driven ‘view’ within the Spatialite database (and add this separately to QGIS).
QGIS working set-ups are stored as a ‘project’ rather than a ‘workspace’
QGIS symbology is data-driven – or at least is assigned on a project by project basis. Features loaded into QGIS will be assigned a random simple symbology/colour. 
It’s expected that you will save your QGIS project regularly – in the same way that you would save your document regularly if working on any other normal application like Word (whereas Mapinfo is based on the assumption that a ‘workspace’ is only changed irregularly). We have template QGIS projects saved in a special location (to be copied for the set up of a new project). 
You may need to keep an eye on the settings for projections. QGIS deals with these easily – and they are easy to change (and so mess up). QGIS talks about a ‘coordinate reference system’ or CRS. It’s helpful to know the EPSG numbers for the common projections: 27700 (OS grid), 3857 (web mapping) and 4326 (GPS data). ‘On the fly’ CRS transformation should be on. There’s a box at the bottom right of the QGIS window where you can change the current project CRS.
Dealing with different data formats is much simpler than in Mapinfo. Generally you should assume that QGIS will be able to cope with any data format (it uses GDAL ogr2ogr for this). The biggest inconvenience is that it treats some formats as something to be imported/exported (“save as…”) – which means that you need to save to a new layer (or temporary ‘scratch’ layer) to make edits, before saving back over the original file.
There’s no such thing as a ‘thematic map’ on QGIS – the assumption is that all mapping is ‘themaic’ in that you will always be choosing to colour/style the mapped data in one way or another. Data normally has no inherent symbology (in the way that Mapinfo works like a drawing program). There are some formats you can use (like TAB or KML) where you can save symbology with the data – and styling is saved with the QGIS project (or you can save a style as a separate style file). Typically you will style data according to the data values rather than simply assigning a single style to a layer. The styling possibilities for data are extremely powerful.
Setting up dynamic database relationships between associated data layers (which you can then use in a number of ways) is simple, and powerful.
Setting up joins between data layers is simple and powerful. 
Shifting different QGIS panels (i.e. windows) around, docking them, undocking them – even moving onto other screens – is simple. These changes are remembered reliably from project to project.

## Getting started
Start with a working QGIS project, with some key plugins installed. Load data by drag and drop into the map canvas window. There are buttons for choosing data formats which are sometimes necessary, but drag and drop almost always works for most simple formats (e.g. Shapefile).
Save data as a Shapefile to begin with. QGIS recently gained the capability of editing TAB files (rather than just importing/exporting them), but I’ve not tested this.
Get used to these key actions:
..* Double click on the layer in the layers panel to open the layer properties (or right click and select properties)
..* Right click on the layer in the layers panel and choose ‘open attribute table’ (or select the attribute table button on the toolbar) – equivalent of opening a browser window in Mapinfo. Note the buttons at the bottom right of the attribute table – these change the table to a form and back again.
..* Create a new layer (rather than loading an existing one) using the specific button for new layers – which lets you choose between creating a Spatialite layer, a Shapefile layer, or a ‘scratch’ layer (for short term use – not saved - all data will be lost when the project is closed).
..* Create a new ‘virtual layer’ using an SQL query (click the virtual layer button). Use this same button to edit an existing virtual layer.
..* Edit a layer – first you need to click the button with the pencil icon – this toggles the editing mode. There’s a save button for the data too (separate from the project save button).
..* To see the data for an individual feature use the ‘identify features’ button. This brings up data on an ‘Identify Results’ panel. In the ‘Actions’ section of this is an option to open a data form – but easier is to check the ‘Auto open form’ box in the ‘Identify Results’ panel so that this form opens automatically most of the time. Note that on the ‘identify results’ panel you can also set what layers the identify tool will get data from (top down, menu, active layer). You can also turn on/off what layers this tool ignores in project properties.
..* Change the symbology of a layer. Set up some interesting symbology. Try something with multiple symbols, driven by the data values, which varies at different zoom levels. Try changing the size settings to be based on map units rather than pixels.
..* Find the plugin management tool. Plugins are likely to be a fundamental part of your work. Notice that you can turn off/on and install/uninstall.
..* Look up the properties (settings) for the QGIS project under the menu item… Project | Project properties
..* Look up the settings for QGIS generally under the menu item… Settings
..* Find snapping options… (Settings | Snapping options)
..* Try using the ‘Select by expression’ button (and its options). 
..* Try the ‘field calculator’ button – use it to add a new calculated field to a layer.
..* Find the ‘show statistical summary’ button. Try it.
..* Find the Measure tool. Try it. CHECK your answers – odd things have been known to happen with different CRS set ups (not normally an issue though).
..* Try setting up a join between layers (in a layer’s properties).
..* Try setting up a relationship between layers (in project properties). See what this does to the data form.
..* Try telling QGIS about how to display the boxes for data that it shows on the data form (e.g. using the identify tool). You can do nice things like providing drop down boxes, hiding some fields, or providing a calendar tool for date entry. Find the settings in a layer’s properties under ‘Fields’.

## More advanced
Some things you might want to find out about really soon:
..* You can change the appearance of a data form (using QT designer for complex set-up) or a drag and drop editor for simpler changes.  
..* You can change the title that QGIS uses to show identified data and linked-through-relationship records. 
..* Check out the powerful tools under the ‘vector’ menu, and under the ‘Processing’ menu.
..* Check out how to set up an ‘action’ for a layer (there’s a button that means the mouse cursor changes its function to one you set up).
..* Find out how to set a variable for the QGIS project – you can use this in various places like setting styles. 
Is there something you want to do but can’t, or something inconvenient… 
Look up Google. Look up http://gis.stackexchange.com/ (huge community of QGIS users). Look up the documentation ( http://qgis.org/en/docs/index.html ) - make sure you look up the most recent version as documentation struggles to keep up with the rapid development of QGIS. Look for a plugin to do what you want or to make it simpler.
