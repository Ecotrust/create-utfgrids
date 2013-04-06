#!/usr/bin/env python
# -*- coding: utf-8  -*-
import globalmaptiles
import os
from shapely.geometry import box, mapping
from fiona import collection

mercator = globalmaptiles.GlobalMercator()

minzoom = 0
maxzoom = 4
bbox = [-20037508.34, -20037508.34, 20037508.34, 20037508.34]  # the whole world in mercator?

outdir = "output"
if not os.path.exists(outdir):
    os.makedirs(outdir)
tilefilename = os.path.join(outdir, "tile_bounds_zoom%s.shp")
schema = {'geometry': 'Polygon',
          'properties': {
              'x': 'int',
              'y': 'int',
              'z': 'int',
              'minx': 'float',
              # 'miny': 'float',
              # 'maxx': 'float',
              # 'maxy': 'float',
          }
          }

for tz in range(minzoom, maxzoom+1):
    with collection(tilefilename % tz, "w", "ESRI Shapefile", schema) as output:
        print " * Processing Zoom Level %s ..." % (tz,)
        tminx, tminy = mercator.MetersToTile(bbox[0], bbox[1], tz)
        tmaxx, tmaxy = mercator.MetersToTile(bbox[2], bbox[3], tz)
        for ty in range(tminy, tmaxy+1):
            for tx in range(tminx, tmaxx+1):
                # Use top origin tile scheme (like OSM or GMaps)
                ymax = 1 << tz
                invert_ty = ymax - ty - 1
                tilebounds = mercator.TileBounds(tx, ty, tz)

                poly = box(*tilebounds)
                output.write({
                    'properties': {
                        'x': tx,
                        'y': invert_ty,
                        'z': tz,
                        # 'minx': float(tilebounds[0]),
                        # 'miny': float(tilebounds[1]),
                        # 'maxx': float(tilebounds[2]),
                        # 'maxy': float(tilebounds[3]),
                    },
                    'geometry': mapping(poly)
                })
