import os
import sys
from collections import namedtuple

data_dir = os.path.abspath(os.path.dirname(__file__) + '/../data')

Projection = namedtuple('Projection', ['authority', 'srid', 'proj4', 'wkt'])
projection = Projection(
        'USER',
        200100,
        '+proj=aea +lat_1=39 +lat_2=45 +lat_0=42 +lon_0=-74 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs',
        'PROJCS["North_America_Albers_Equal_Area_Conic",GEOGCS["GCS_North_American_1983",DATUM["North_American_Datum_1983",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Albers_Conic_Equal_Area"],PARAMETER["False_Easting",0],PARAMETER["False_Northing",0],PARAMETER["longitude_of_center",-74],PARAMETER["Standard_Parallel_1",39],PARAMETER["Standard_Parallel_2",45],PARAMETER["latitude_of_center",42],UNIT["Meter",1],AUTHORITY["USER","200100"]]'
        )

class HiddenPrints(object):
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, *args):
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr
