import requests

API_URL = "https://min-api.cryptocompare.com/data/price"


def get_cryptocurrency_price(fsym):
    params = {"fsym": fsym, "tsyms": "USD"}
    response = requests.get(API_URL, params=params)
    data = response.json()
    result = f"1 {fsym} = ${data['USD']:.2f} USD"
    return result
