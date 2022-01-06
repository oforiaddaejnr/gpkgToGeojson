import os
import sys
import geopandas 

for root, dirs, files in os.walk("."):
    for filename in files:
        #print(filenanme)
        if filename.endswith(".gpkg"): #get geojson file
            geoJsonFile = os.path.join(root, filename)
            #os.startfile(geoJsonFile)
            print(geoJsonFile)
            openFile = open(geoJsonFile)
            toGeoJson = geopandas.read_file(openFile)
            toGeoJson.to_file(str(filename)+".geojson", driver='GeoJSON')