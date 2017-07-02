import requests
import json

result = open ("result3.txt",'w')
r = requests.get("http://recommender.scarabresearch.com/merchants/123DB8D9CCA58C7C/?pv=1983198083&xp=1&f=f%3AHOME_1%2Cl%3A20%2Co%3A0%7Cf%3AHOME_2%2Cl%3A20%2Co%3A0%7Cf%3AHOME_3%2Cl%3A20%2Co%3A0&cv=1&ca=&cp=1&vi=2C311E9EC2F00293&p=270366%7C1498493496&ti=2%2C4270%2C3266%2C3185%2C%2C%7Cl%2C%2C3127%2C3276%2C3280%2C%2C3383%2C3503%2C4252%2C%2C%7Cr%2C%2C4282%2C4285%2C4287%2C%2C4377%2C4491%2C4496%2C4604%2C4276")
# schema = r.json()["schema"]
# print(schema)
products = list(r.json()["products"].values())
for i in products:
    if i[4] != i[6]:
        href = i[7]
        oldPrice = i[6]
        finalPrice = i[4]
        result.write('{:<11}  {:<11}  {:<100}'.format(oldPrice,finalPrice,href)+'\n')
