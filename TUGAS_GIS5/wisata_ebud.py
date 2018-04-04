import mapnik
m = mapnik.Map(800,420)
m.background = mapnik.Color('steelblue')


s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('green')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 1)
line_symbolizer.stroke_width = 1.0
r.symbols.append(line_symbolizer)

s.rules.append(r)

m.append_style('My Style', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\sby/SURABAYA.shp")
layer = mapnik.Layer('jatim')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

#pin poin
s = mapnik.Style()
r = mapnik.Rule()

point_sym = mapnik.MarkersSymbols()
point_sym.filename = 'C:\Users\Ebud\Documents\GIS\TUGAS_5/gambar.png'
point_sym.width = mapnik.Expression("20")
point_sym.height = mapnik.Expression("20")
point_sym.allow_overlap = True
r.symbols.append(point_sym)

text_sym = mapnik.TextSymbolizer(mapnik.Expression('[NAME'), 'DejaVu Sans Bold',10,mapnik.Color('black'))
text_sym.halo_radius = 1
text_sym.allow_overlap = True
text_sym.avoid_edges = False
r.symbols.append(text_sym)

s = mapnik.Style()
r = mapnik.Rule()

ds = mapnik.MemoryDataSource()
f = mapnik.Feature(mapnik.Context(), 1)
f['NAME'] = 'Taman Bungkul'
f.add_geometries_from_wkt("POINT(-7.290902 112.739419)")
ds.add_feature(f)

player = mapnik.Layer('airport_layer')
player.datasource = ds
player.styles.append('airport point')
m.layers.append(player)

m.zoom_all()
mapnik.render_to_file(m,'wisata.pdf', 'pdf')
print "rendered image to 'wisata.pdf'"




#-------menambahkan gambar pada pin poin------#

#s = mapnik.Style()
#r = mapnik.Rule()

#point_sym = mapnik.MarkersSymbols()
#point_sym.filename = 'images/gambar.png'
#point_sym.width = mapnik.Expression("20")
#point_sym.height = mapnik.Expression("20")
#point_sym.allow_overlap = True
#r.symbols.append(point_sym)

#text_sym = mapnik.TextSymbolizer(mapnik.Expression('[NAME'), 'DejaVu Sans Bold',10,mapnik.Color('black'))
#text_sym.halo_radius = 1
#text_sym.allow_overlap = True
#text_sym.avoid_edges = False
#r.symbols.append(text_sym)

#s = mapnik.Style()
#r = mapnik.Rule()

#ds = mapnik.MemoryDataSource()
#f = mapnik.Feature(mapnik.Context(), 1)
#f['NAME'] = 'Soekarno Hatta'
#f.add_geometries_from_wkt("POINT(-92.289595 34.746481)")
#ds.add_feature(f)

#player = mapnik.Layer('airport_layer')
#player.datasource = ds
#player.styles.append('airport point')
#m.layers.append(player)

#--------------Eko Budi Santoso-Teknik Informatika-04315047----------------------------------#
