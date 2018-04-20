import mapnik
m = mapnik.Map(1200,600)
m.background = mapnik.Color('steelblue')

s = mapnik.Style()
s2 = mapnik.Style()
r = mapnik.Rule()
r2 = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 5.0
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

line_symbolizer2 = mapnik.LineSymbolizer(mapnik.Color('yellow'), 1)
line_symbolizer2.stroke_width = 1.0
r2.symbols.append(line_symbolizer2)
s2.rules.append(r2)

m.append_style('My Style2',s2)
POSTGIS_TABLE = dict(
    host='localhost',
    port=5432,
    user='postgres',
    password='ebud',
    dbname='kelasgisebud',
    # table='(select ST_Buffer(ST_Centroid(geom),1) as geom, nama from sinau) as sinau',
    table='(select ST_LineMerge(ST_AsText(geom)) as geom, nama from sinau) as sinau'
    )

ds2 = mapnik.PostGIS(**POSTGIS_TABLE)
layer2 = mapnik.Layer('sinau')
layer2.datasource = ds2
layer2.styles.append('My Style2')

m.layers.append(layer2)
m.zoom_all()

mapnik.render_to_file(m,'world.png', 'png')
print "rendered image to 'world.png'"
exit()