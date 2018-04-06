import mapnik
m = mapnik.Map(800,420)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('green')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
line_symbolizer.stroke_width = 1.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style', s)
ds = mapnik.Shapefile(file="D:\ebud\SHP_Indonesia_sungai\IND_SNG_polyline.shp")
layer = mapnik.Layer('sungai')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'sungai.png', 'png')
print "rendered image to 'sungai.png'"