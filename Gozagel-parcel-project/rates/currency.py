from django.core.cache import cache


def convert_to_eur(currency, amount):
    # print("currency", currency)
    # print("amount", amount)
    # print("cache", cache)
    rate = cache.get(currency)
    print(rate, "rate")
    result = round((float(amount) / float(rate)), 2)
    result = format(result, ".2f")
    return result
