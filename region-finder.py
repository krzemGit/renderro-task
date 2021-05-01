import requests
from requests.exceptions import HTTPError

# SETTINGS
LOCATIONS = {'USA': 'us-east-2 (Ohio)', 'EUR': 'eu-central-1 (Frankfurt)'}

# mapping the codes to loactions
COUNTRY_CODES = {
    'BR': 'USA',
    'DE': 'EUR',
    'IL': 'EUR',
    'PL': 'EUR',
    'US': 'USA'
}
GEO_API_URL = 'https://ipwhois.app/json/'


# DATA HANDLING FUNCTION
def print_location(country_code):
    # data error handling - gates
    if country_code is None:
        return print('Could not found your country code, please try again or contact your IT specialist!')

    if country_code not in COUNTRY_CODES.keys():
        return print('Your region is not supported by this script, sorry!')

    locations_no = len(LOCATIONS.values())
    location_result = LOCATIONS[COUNTRY_CODES[country_code]]

    # printing data
    return print(f'The nearest of the {locations_no} locations we have is {location_result}')


# EXECUTION
# api call
try:
    res = requests.get(GEO_API_URL)
    res.raise_for_status()

# http error handling
except HTTPError as http_err:
    # print(f'Http error occured: {http_err}') - version for more sophisticated users
    print('API is not available')

except Exception as err:
    # print(f'Other error occured {err}') - version for more sophisticated users
    print('API is not available')


# HANDLING DATA
else:
    code = res.json().get('country_code', None)

    print_location(code)
