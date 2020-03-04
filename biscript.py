import requests
import cutie
#TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'



def dcoin_latest(dcoin):
  
  #TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
  response = requests.get('https://api.coinmarketcap.com/v1/ticker/' + dcoin)
  response_json = response.json()
  
  return float(response_json[0]['price_usd'])

def rcoin_latest(rcoin):
    r = requests.get('http://data.fixer.io/api/latest?access_key=d6837361bdbaafc52c41865cb3c286f9')
    data = [r.json()]
    currencies = data[0]['rates']
    return (currencies[rcoin])
'''
def gcoin_latest():
    g = requests.get('https://metals-api.com/api/latest?access_key=35qm7qi7td53qrkjg7q58f501nwa0dd958sjdrorive4mx5r21y2qw6t8ym5')
    g_data = [g.json()]
    metal_value = g_data[0]['rates']
    temp = (1 / float (metal_value[XAU]))
    return temp
''' 


dcoin = input ('ENTER CRPYTO: ')
rcoin = input ('ENTER CURRENCY: ')
print (dcoin_latest(dcoin))

'''
gcoin = input ('ENTER GOLD: ')
'''


'''
want to be able to give value readings over time intervals for various currencies
want to alert user of dramatic changes
after x amount of hours, report % change
want to use gui module for ease of use

'''


"""
def percent_change_24h(crypto):
    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()

    return float(response_json[0]['percent_change_24h'])

def percent_change_7d(crypto):
    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()

    return float(response_json[0]['percent_change_7d'])

def get_crypt_currency():
    print ('What crypto currency are you interested in?')
    crypto = input ('Enter here: ')
    return crpyto

def get_currency():
    print ('What currency are you interested in... Dollars, Euros, or ')
    currency = input ('Enter here: ')
    return currency

#get_crypt_currency()
print (latest_price())

#latest_price(bitcoin)
"""

'''

Try


except
'''