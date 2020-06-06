"""""
CSI Coding Exercise script

# This script finds the nearest tall building to each random 
# point specified in gberardinelli's github project.

# This project is written in Python 3, and requires an up-to-date
# installation of geopandas, pandas, and shapely.
"""

# import needed packages
import geopandas as gpd
import pandas as pd
from shapely.ops import nearest_points
import os

# list the url of the buildings and points csv files.
url_b = 'https://gist.githubusercontent.com/gberardinelli/8567cdbcad220e46b2f8fc4e33a203a0/raw/e9d27e14fbbde4b28a6c09d077b43537310a5b0b/buildings.csv'
url_q = 'https://gist.githubusercontent.com/gberardinelli/8567cdbcad220e46b2f8fc4e33a203a0/raw/e9d27e14fbbde4b28a6c09d077b43537310a5b0b/queries.csv'

# read in the csv files as pandas data frames
buildings = pd.read_csv(url_b, error_bad_lines=False)
points = pd.read_csv(url_q, error_bad_lines=False)

# to verify data type run type()


# this function creates Geopandas Geodataframe
# with which you can run spatial operations
def create_gdf(df, x="X", y="Y"):
    return gpd.GeoDataFrame(df,
                            geometry=gpd.points_from_xy(df[y], df[x]),
                            crs={"init": "EPSG:2991"})
# use the create_gdf() function
buildings_gdf = create_gdf(buildings)
points_gdf = create_gdf(points)

# to verify data type run type()

#Find the nearest building neighbor of each random point
def calculate_nearest(row, destination, val, col="geometry"):
    # 1 - create unary union
    # https://shapely.readthedocs.io/en/latest/manual.html
    dest_unary = destination["geometry"].unary_union
    # 2 - find closest point
    nearest_geom = nearest_points(row[col], dest_unary)
    # 3 - Find the corresponding geom
    match_geom = destination.loc[destination.geometry
                == nearest_geom[1]]
    # 4 - get the corresponding value
    match_value = match_geom[val].to_numpy()[0]
    return match_value

print(list(buildings_gdf.columns.values))

# Get the nearest geometry
points_gdf["nearest_geom"] = points_gdf.apply(calculate_nearest,
                                              destination=buildings_gdf,
                                              val="geometry", axis=1)
# Get the nearest building name
points_gdf["nearest_building"] = points_gdf.apply(calculate_nearest,
                                                  destination=buildings_gdf,
                                                  val="Name", axis=1)

print(type(points_gdf))
print(list(points_gdf.columns.values))


points_gdf.to_file(filename='random_neighbors.shp')

print(os.getcwd() + "/random_neighbors.shp created. \n This contains 'nearest_building' with the geometry nearest building to each point.")