import requests
import json

# Problem 2
def find_restaurant_near_you():
  # get user input
  type_of_restaurant = input("Enter a type of restaurant (i.e. Indian): ")
  city = input("Enter an city you want to find restaurants near (i.e. Irvine): ")
  address = input("Enter an address from the city that you want to find restaurants near (i.e. 101 Main Street): ")

  # Encode address to query string
  address = address.replace(" ", "+")

  # get Geocoding API and make request
  geocoding_api = 'https://api.tomtom.com/search/2/geocode/.json?key=T0TfatiwhgFzWJgTrNglxs32j8pC6jCq'
  data2 = requests.get(geocoding_api, params={'query': address})
  data2 = data2.json()

  try:
    # Parse JSON for latitude and longitude of address
    address_lat = data2['results'][0]['position']['lat']
    address_long = data2['results'][0]['position']['lon']
  
    # get Search API and make request
    search_api = 'https://api.tomtom.com/search/2/poiSearch/.json?key=T0TfatiwhgFzWJgTrNglxs32j8pC6jCq'
    data3 = requests.get(search_api,
                    params = {
                        'query': type_of_restaurant,
                        'lat': address_lat,
                        'lon': address_long,
                        'radius': '20000.0',
                        'categorySet': '7315'}).json()


    # append restaurants to list (json file already sorted by distance, 3rd API not needed)
    restaurants = []
    for i in range(10):
      restaurants.append(data3['results'][i]['poi']['name'])

    print("Restaurants near you sorted by distance:", restaurants)

  except IndexError:
    print("Invalid restaurant cuisine or city/address entered.")


find_restaurant_near_you()
