import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

from test import number

key = "0b19d334cba1450aa4b00a1b8fd51607"

check_number = phonenumbers.parse(number)

number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(key)

query = str(number_location)
result = geocoder.geocode(query)

if result and len(result) > 0:
    latitude = result[0]['geometry']['lat']
    longitude = result[0]['geometry']['lng']
    print(latitude, longitude)

    map = folium.Map(location=[latitude, longitude], zoom_start=10)

    folium.Marker([latitude, longitude], popup=number_location).add_to(map)

    map.save("number_location_map.html")
else:
    print("Geocoding failed, no results found.")
