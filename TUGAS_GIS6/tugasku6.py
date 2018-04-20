import mapnik

## SPBU Surabaya ##
m = mapnik.Map(2400,1024)
m.background = mapnik.Color('steelblue')

#---------------------Layer1-----------------------#
layer1 = mapnik.Layer('Indonesia')
layer1.datasource = mapnik.Shapefile(file="shp/INDONESIA_PROP.shp")

sty1 = mapnik.Style()
rul1 = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#fcff00')

rul1.symbols.append(polygon_symbolizer)
sty1.rules.append(rul1)

m.append_style('Style1', sty1)
#---------------------End Layer1-----------------------#

#---------------------Layer1-----------------------#
layer2 = mapnik.Layer('Surabaya')
layer2.datasource = mapnik.Shapefile(file="shp/TNBTS.shp")
#db = dict(
#	host = 'localhost',
#	port=5432,
#	user='postgres',
#	password='ebud',
#	dbname='kelasgisebud',
#	table='(select ST_Buffer(ST_Centroid(geom),2) as geom, kode from sinau) as sinau', # ---------------- untuk poin
#   table='(select ST_LineMerge(ST_AsText(geom)) as geom, nama from sinau) as sinau'   # ---------------- untuk garis
# table='(select ST_MPolyFromText(ST_AsText(geom)) as geom, nama from sinau) as sinau' # ---------------- untuk polygn
#	)
#layer2.datasource =  mapnik.PostGIS(**db)

sty2 = mapnik.Style()
rul2 = mapnik.Rule()

# line_sby = mapnik.MarkersSymbolizer()
# line_sby.color = mapnik.Color('red')
# line_sby.width = mapnik.Expression('2')
# line_sby.height = mapnik.Expression('2')
# line_sby.allow_overlap = True

line_sby = mapnik.PolygonSymbolizer()
line_sby.fill = mapnik.Color('red')


rul2.symbols.append(line_sby)
sty2.rules.append(rul2)

m.append_style('Style2', sty2)

#---------------------End Layer1-----------------------#
#--Render--#

layer1.styles.append('Style1')
layer2.styles.append('Style2')
m.layers.append(layer1)
m.layers.append(layer2)

m.zoom_all()
mapnik.render_to_file(m,'TNBTS.pdf', 'pdf')
print "Sukses Bro"
