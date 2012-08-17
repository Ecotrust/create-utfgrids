# create_utfgrids.py

Simple command line script to create [UTFGrid](https://github.com/mapbox/utfgrid-spec) json files from a polygon shapefile.

```
$ ./create_utfgrids.py -h
Usage: create_utfgrids.py [options] shapefile minzoom maxzoom output_directory

Options:
  -h, --help            show this help message and exit
  -f FIELDS, --fields=FIELDS
                        Comma-seperated list of fields; default is all

$ ./create_utfgrids.py polygon_mercator.shp 5 8 out1 -f NAME,Shape_Length
```

### Requirements

* Mapnik >= 2.0 with python bindings
* OGR python bindings
