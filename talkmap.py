

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob # Se utiliza para buscar archibos md en el directorio actual
import getorg # Genera mapas interactivos
from geopy import Nominatim # Geocodificación de las ubicaciones definidas en los archivos Markdown

g = glob.glob("*.md") # Buscar archivos con la extensión .md 


geocoder = Nominatim() # Localiza las ubicaciones
# Almacena información sobre las ubicaciones de charlas
location_dict = {}
location = ""
permalink = ""
title = ""

# Busca cada archivo .md y los abre en modo lectura ('r') 
for file in g:
    with open(file, 'r') as f:
        lines = f.read() # Almacena contenido en lines
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
           
        location_dict[location] = geocoder.geocode(location)
        print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




