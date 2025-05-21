import csv
from geopy.geocoders import HereV7

def geo_code_address(address: str) -> dict:
    # herev7 api and query
    geolocator = HereV7(apikey="Enter API key here")

    location = geolocator.geocode(query=address, timeout=30)

    if location:
        return {
            "address": address,
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        print(f"⚠️ Could not find location for: {address}")
        return {
            "address": address,
            "latitude": None,
            "longitude": None
    }

# Read addresses from addresses.txt
with open("addresses.txt", "r", encoding="utf-8") as file:
    address_list = [line.strip() for line in file if line.strip()]

# Get geocoded result
#coords = geo_code_address(address)

# Print the result
#print("lat:", coords["lat"])
#print("lon:", coords["lon"])


# List to hold all results
results = []

for addr in address_list:
    result = geo_code_address(addr)
    results.append(result)
    print(f"{result['address']} -> latitude: {result['latitude']}, longitude: {result['longitude']}")

# ✅ Save to CSV file
with open("locations.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["address", "latitude", "longitude"])
    writer.writeheader()
    writer.writerows(results)

print("\n✅ Results saved to locations.csv")