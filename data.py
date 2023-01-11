dict_of_cryptocurrencies = {"btc": "BTC",
                            "bnb": "BNB",
                            "eth": "Ethereum",
                            "ltc": "LiteCoin",
                            "sol": "Solana",
                            "matic": "Polygon",
                            "cake": "PancakeSwap",
                            "fet": "Fetch.ai",
                            "gmt": "STEPN",
                            "ldo": "Lido DAO", }

list_of_cryptocurrencies = list(dict_of_cryptocurrencies)


def create_available_list_message():
    res = ''
    for key, value in dict_of_cryptocurrencies.items():
        res += f'/{key} - {value}\n'
    return res


available_list_message = create_available_list_message()
