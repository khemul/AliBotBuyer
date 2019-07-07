import requests
from bs4 import BeautifulSoup



# input type="text" id="fm-login-id"
# input type="password" id="fm-login-password"

s = requests.Session()

DATA = {'loginId': 'first.buy.bot@gmail.com', 'password': 'alioB7yjjRi'}
URL_LOGIN = 'https://login.aliexpress.com/buyer_ru.htm?spm=a2g0v.best.1000002.7.7f1azV7tzV7tV3&return=https%3A%2F%2Fbest.aliexpress.com%2F%3Flan%3Den%26spm%3Da2g0v.best.1000002.1.5072aa3Aaa3ABN&from=lighthouse&random=8D0A95BA25052DA07CB8C70255156EA7'

r = s.post(URL_LOGIN, data=DATA)


URL = 'https://best.aliexpress.com/?lan=en&spm=a2g0v.best.1000002.1.5072aa3Aaa3ABN'
r = s.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
soup.find(cl)


s.cookies



