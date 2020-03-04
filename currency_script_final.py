import requests
import time
from datetime import datetime

def dcoin_latest(dcoin):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/' + dcoin)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def rcoin_latest(rcoin):
    r = requests.get('http://data.fixer.io/api/latest?access_key=d6837361bdbaafc52c41865cb3c286f9')
    data = [r.json()]
    currencies = data[0]['rates']
    return (currencies[rcoin])

def gcoin_latest():
    g = requests.get('https://metals-api.com/api/latest?access_key=35qm7qi7td53qrkjg7q58f501nwa0dd958sjdrorive4mx5r21y2qw6t8ym5')
    g_data = [g.json()]
    metal_value = g_data[0]['rates']
    temp = (1 / float (metal_value['XAU']))
    return temp

def main():

    try:
        
        print ('Welcome to the currency tracker! \n(press ctrl + c to quit)')
        time.sleep(2)
        print ('\nOver what time interval(in seconds) would you like to track? ')
        timey1 = float(input('Enter: '))
        time.sleep(1)
        timey = timey1


        while True:
            current_time = time.time()
            future_time = current_time + float (timey)

            while (current_time < future_time):
                current_time = time.time()
                date_time = datetime.now()
                print ('The date and time is: ' + str(date_time))
                bitcoin = dcoin_latest('bitcoin')
                litecoin = dcoin_latest('litecoin')
                ethereum = dcoin_latest('ethereum')
                gold = gcoin_latest()
                canadian_dollar = rcoin_latest('CAD')
                gbp = rcoin_latest('GBP')
                dollar_euro = rcoin_latest('USD')
                dollar_to_cad = (dollar_euro)/canadian_dollar
                dollar_to_gbp = dollar_euro/gbp
                
                print ( 'The value of Bitcoin is: ' + str(bitcoin) + ' USD\n' +
                        'The value of Litecoin is: ' + str(litecoin) + ' USD\n' +
                        'The value of Ethereum is: ' + str(ethereum) + ' USD\n' +
                        'The vale of Gold is: ' + str(gold) + ' USD\n' +
                        'The value of the Canadian dollar is: ' + str(dollar_to_cad) + ' USD\n' +
                        'The value of the British pound is: ' + str(dollar_to_gbp) + ' USD\n' +
                        'The value of the Euro is: ' + str(dollar_euro) + ' USD\n\n' )
                time.sleep(int(timey-1))
                print ("\nAt date and time: " + str(date_time) +'\nThe value of Bitcoin was ' + 
                        str(bitcoin) + ' USD' + '\nAfter ' + str(timey) + " seconds\n" +
                        'The new value is: ' + str(dcoin_latest('bitcoin')) + ' USD')
                new_value = (dcoin_latest('bitcoin')/bitcoin)
                print ('\nThe bitcoin value increased/decreased by a factor of ' + str(new_value) + '\n')
                time.sleep(1)



    except KeyboardInterrupt:
        print ('\nDone.')


main()



