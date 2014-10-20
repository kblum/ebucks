import requests
from bs4 import BeautifulSoup
import re


def get_balance(username, password):
    """
    Scrape eBucks website to get balance and return as an integer.
    """

    # create a session so that cookies are persisted between requests
    session = requests.Session()

    # post to login page to set session cookie
    login_url = 'https://www.ebucks.com/web/loginValidate.do?Action=Login'
    login_data = {'userId': username, 'password': password}
    session.post(login_url, params=login_data)

    # get contents of home page
    home_url = 'https://www.ebucks.com/web/eBucks/'
    response = session.get(home_url)
    page = response.text

    # parse contents of home page to get the balance
    soup = BeautifulSoup(page)
    balance_str = soup.find('span', {'class': 'eBucksValue'}).text.__str__()
    balance = int(re.findall('([0-9]+)', balance_str)[0])
    
    return balance
