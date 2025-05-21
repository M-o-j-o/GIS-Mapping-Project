from geopy.geocoders import Nominatim

def geo_code_address(address: str) -> dict:
    # Create user agent for Nominatim which is a requirement
    geolocator = Nominatim(user_agent="GEO_CODE_DEMO")

    location = geolocator.geocode(
        query=address,
        country_codes=["UG"],
    )
    if location:
        return {
            "lat": location.latitude,
            "lon": location.longitude
        }
    else:
        raise ValueError(f"Could not find location for address: {address}")

# Address to look up
address = "Jinja Road Police Station"

# Get geocoded result
coords = geo_code_address(address)

# Print the result
print("lat:", coords["lat"])
print("lon:", coords["lon"])
