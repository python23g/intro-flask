import currencyapicom
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.environ.get('API_KEY')

client = currencyapicom.Client(API_KEY)


def converter(c: str, cs: list):
    result = client.latest(c, currencies=cs)
    
    return result

print(converter("USD", ["UZS"]))
