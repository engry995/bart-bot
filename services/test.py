from time import sleep
from bestchange import BestChange

p1 = BestChange('555')
print(p1.difference_with_first_by_btc_usdt)



p2 = BestChange('884')
print(p2.difference_with_first_by_btc_usdt)

sleep(5)
p3 = BestChange('686')
print(p3.difference_with_first_by_btc_usdt)
