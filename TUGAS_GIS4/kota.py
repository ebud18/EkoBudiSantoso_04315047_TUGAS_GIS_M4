import mapnik
m = mapnik.Map(800,420)
m.background = mapnik.Color('white')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('yellow')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 1.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style', s)
ds = mapnik.Shapefile(file="D:\ebud\SHP_Indonesia_Kota\IND_KOT_point.shp")
layer = mapnik.Layer('kota')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kota.png', 'png')
print "rendered image to 'kota.png'"