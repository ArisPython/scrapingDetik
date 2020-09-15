import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.7428423980614e-5,"date":"Tue, 15 Sep 2020 00:00:01 GMT","inverseRate":14830.540904938},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.6797127033015e-5,"date":"Tue, 15 Sep 2020 00:00:01 GMT","inverseRate":17606.524347943}}

for i in json_data.values():
    print(i['code'])
    print(i['name'])
    print(i['date'])
    print(i['inverseRate'])