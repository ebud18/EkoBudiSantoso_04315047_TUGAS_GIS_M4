import mapnik
m = mapnik.Map(8000,4000)
m.background = mapnik.Color('#0764fe')

s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#fff600')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 1)
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Propinsi]'), 'DejaVu Sans Bold',13,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('white')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)
s.rules.append(r)

#------------------------Eko Budi Santoso--------------------------#

#highlight = mapnik.PolygonSymbolizer()
#highlight.fill = mapnik.Color('#2aff00')
#Indonesia = mapnik.Rule()
#Indonesia.filter = mapnik.Expression("[NAME]='jawa tengah'")
#Indonesia.symbols.append(highlight)
#s.rules.append(jawa tengah)

#---------------------------Teknik Informatika-----------------------#

m.append_style('My Style1', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('propinsi')
layer.datasource = ds
layer.styles.append('My Style1')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()


m.append_style('My Style2', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\peta_jatim\Peta Jawa Timur Shp/jatim.shp")
layer = mapnik.Layer('jatim')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('red')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#ff5a00'), 1)
line_symbolizer.stroke_width = 0.01
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\peta_jatim\Peta Jawa Timur Shp/jatim_desa.shp")
layer = mapnik.Layer('desa')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#7dfdff'), 1)
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\SHP_Indonesia_sungai/IND_SNG_region.shp")
layer = mapnik.Layer('sungai1')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style5', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\SHP_Indonesia_sungai/IND_SNG_polyline.shp")
layer = mapnik.Layer('sungai2')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

# polygon_symbolizer = mapnik.PolygonSymbolizer()
# polygon_symbolizer.fill = mapnik.Color('green')
# r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style6', s)
ds = mapnik.Shapefile(file="C:\Users\Ebud\Documents\GIS\TUGAS_5\peta_jatim\Peta Jawa Timur Shp/jatim_kab.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds
layer.styles.append('My Style6')
m.layers.append(layer)


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


m.zoom_all()
mapnik.render_to_file(m,'6_layer.pdf', 'pdf')
print "rendered image to '6_layer.pdf'"