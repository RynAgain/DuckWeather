from WetDuck import WetDuck as wd
import json

city = 'Austin'

mycity = wd(city)

print(list(mycity.response))