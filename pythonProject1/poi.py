# Tianze Ren tr2bx; Morgan Booth mb2ej
f = open("chickfila.csv")

chickfila_list =[]
for line in f:
    entry = line.strip().split(',')
    chickfila_list.append(entry)


user_lat = float(input("Enter your latitude: "))
user_long = float(input("Enter your longitude: "))


import math

# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist

shortest = []
for list in chickfila_list:
    lat_2 = float(list[0])
    lon_2 = float(list[1])
    shortest.append(distance_between(user_lat, user_long, lat_2, lon_2))

shortest_ = 99999999999999
for dist in shortest:
    if dist < shortest_:
        shortest_ = dist

print(shortest_)


import urllib.request

url = 'http://maps.google.com/maps?q='+


f.close()