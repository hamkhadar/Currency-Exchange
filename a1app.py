"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Hameedah Khadar [hjk63]
Date:   25 Sept 2019
"""
import a1


currency_from = input('Enter source currency: ')
currency_to = input ('Enter target currency: ')
amount_from= str(input('Enter original amount: '))
result = a1.exchange(currency_from, currency_to, amount_from)
print('You can exchange '+str(amount_from)+ ' '+currency_from+ " for " + str(result)+' ' +currency_to+ '.')
