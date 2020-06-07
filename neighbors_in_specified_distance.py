"""
CSI Coding Exercise BONUS

# This script finds the buildings within a user specified
# distance of random points. If the user does not specify a
# valid value the default is 1000 ft.

# The output of the script shows the point's nearby
# buildings and their height ranking in the console.

# This project is written in Python 3, and requires an up-to-date
# installation of geopandas & pandas.
"""

# This allows the user to specify a distance in the console
distance = input("Type the distance in feet you want to buffer around the random points: ")
if type(distance) != float:
    try: distance = float(distance)
    except:
        print("that's not a number!")
        distance = 1000
print("Using the distance ", distance)


# import needed packages
import geopandas as gpd
import pandas as pd



# list the url of the buildings and points csv files.
url_b = 'https://gist.githubusercontent.com/gberardinelli/8567cdbcad220e46b2f8fc4e33a203a0/raw/e9d27e14fbbde4b28a6c09d077b43537310a5b0b/buildings.csv'
url_q = 'https://gist.githubusercontent.com/gberardinelli/8567cdbcad220e46b2f8fc4e33a203a0/raw/e9d27e14fbbde4b28a6c09d077b43537310a5b0b/queries.csv'

# read in the csv files as pandas data frames
buildings = pd.read_csv(url_b, error_bad_lines=False)
points = pd.read_csv(url_q, error_bad_lines=False)
# this function creates Geopandas Geodataframe
# with which you can run spatial operations
def create_gdf(df, x="X", y="Y"):
    return gpd.GeoDataFrame(df,
                            geometry=gpd.points_from_xy(df[y], df[x]),
                            crs={"init": "EPSG:2991"})

# make your Geodataframes
buildings_gdf = create_gdf(buildings)
points_gdf = create_gdf(points)

# Loop through the points
for index, row in points_gdf.iterrows():
    # buffer around random point
    buffer = points_gdf.buffer(distance)[index]
    # print point name
    print("Buildings within " + str(distance) + " feet of " + row["Name"])
    pt = []

    # loop through buildings
    for b_index, b_row in buildings_gdf.iterrows():
        # check if building is in buffer
        if b_row.geometry.within(buffer):
            # add the building name and rank to pt
            pt.append([b_row["Name"], b_row["Rank"]])
        # create a DataFrame of buildings in buffer
        df = pd.DataFrame(pt, columns=["name", "height rank"])
    if df.empty:
        print("none")
    else:
        print(df)