"""
geo_functions.py

This script contains geospatial functions for various geographical calculations.
It includes functions to calculate the distance between two geographical points
find the midpoint of two geographical points, and check if a point lies within
a given radius of another point.
Author: Onoduagu Ifeanyi
Date:2024-06-20
"""

import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points on the Earth's surface

    Parameters:
       lat1 (float): Latitude of the first point in degrees.
       lon1 (float): Longitude of the first point in degrees.
       lat2 (float): Latitude of the second point in degrees.
       lon2 (float): Longitude of the second point in degrees.
        Returns:
       float: Distance between the two points in kilometers.

    Example:
         >>>haversine_distance(52.2296756, 21.0122287, 41.8919300, 12.5113300)
         1317.1353847863466
    """
     # Convert latitude and longitude from degrees to radians
     lat1, lon1, lat2, lon2= map(math.radians, [lat1, lon1, lat2, lon2])

     # Haversine formula
     dlat = lat2 - lat1
     dlon = lon2 - lon1
     a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2 
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

     # Radius of Earth in Kilometers
     r = 6371
     return r * c  
   def geographic_midpoint(lat1, lon1, lat2, lon2):
       """
       Calculate the geographic midpoint between two points on the Earth's surface.
       Parameters:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.
    Returns:
        tuple: Latitude and longitude of the midpoint in degrees.

    Example:
     >>> geographic_midpoint(52.2296756, 21.0122287, 41.8919300, 12.5113300)
      (47.06635824043988, 16.890625582246215)
       """
       # Convert latitude and longitude from degrees to radians
       lat1, lon1 = map(math.radians, [lat1, lon1])
       lat2, lon2 = map(math.radians, [lat2, lon2])

       # Cartesian ccoordinate for the two points
       x1, y1, z1 = math.cos(lat1) * math.cos(lon1), math.cos(lat1) * math.sin(lon1), math.sin(lat1)
       x2, y2, z2 = math.cos(lat2) * math.cos(lon2), math.cos(lat2) * math.sin(lon2), math.sin(lat2)

       # Midpoint in Cartesian coordinates
       x, y, z = (x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2

       # Convert midpoint back to latitude and longitude
       lon_mid = math.atan2(y, x)
       hyp = math.sqrt(x * x + y * y)
       lat_mid = math.atan2(z, hyp)

       return math.degrees(lat_mid), math.degrees(lon_mid)

    def is_within_radius(lat1, lon1, lat2, lon2, radius):       """
       check if a point (lat2, lon2) is within a certain radius of another point (lat1, lon1).
           Parameters:            lat1 (float): Latitude of the first point in degrees.
            lon2 (float): Longitude of the first point in degrees.
            lat2 (float): Latitude of the second point in degrees.
            lon2 (float): Longitude of the second point in degrees.
            radius (float): Radius in kilometer

       Returns:
             bool: True if the second point is within the radius of the point, False otherwise.

       Example:
               >>> is within_radius(52.2296756, 21.0122287, 52.406374, 16.9251681, 300)
                False
         """   
         return haversine_distance(lat1, lon1, lat2, lon2)  <= radius     







