# create_utfgrids.py

Simple command line script to create [UTFGrid](https://github.com/mapbox/utfgrid-spec) json files from a polygon shapefile.

Usage:
```
$ ./create_utfgrids.py -h
Usage: create_utfgrids.py [options] shapefile minzoom maxzoom output_directory

Options:
  -h, --help            show this help message and exit
  -f FIELDS, --fields=FIELDS
                        Comma-seperated list of fields; default is all
```

Example:
```
$ ./create_utfgrids.py test_data/bailey_merc.shp 3 5 ecoregions -f dom_desc,div_desc

WARNING:
 This script assumes a polygon shapefile in spherical mercator projection.
  If any of these assumptions are not true, don't count on the results!
  * Processing Zoom Level 3
  * Processing Zoom Level 4
  * Processing Zoom Level 5
```

Inspect the output (for example, zoom level 5, X=20, Y=18)
```
$ cat ecoregions/5/20/18.json | python -mjson.tool
{
    "data": {
        "192": {
            "div_desc": "RAINFOREST REGIME MOUNTAINS", 
            "dom_desc": "HUMID TROPICAL DOMAIN"
        }, 
...
...
```

### Requirements

* Mapnik >= 2.0 with python bindings
* OGR python bindings
