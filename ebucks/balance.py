import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import re


def get_balance(username, password):
    """
    Scrape eBucks website to get balance and return as an integer.
    """

    # create opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)

    # post to login validation page
    login_url = 'https://www.ebucks.com/web/loginValidate.do?Action=Login'
    login_data = {'userId': username, 'password': password}
    opener.open(login_url, urllib.urlencode(login_data)).close()

    # get contents of home page
    home_url = 'https://www.ebucks.com/web/eBucks/'
    fp = opener.open(home_url)
    page = fp.read()
    fp.close()

    # parse contents of home page to get the balance
    soup = BeautifulSoup(page)
    balance_str = soup.find('span', {'class': 'eBucksValue'}).text.__str__()
    balance = int(re.findall('([0-9]+)', balance_str)[0])
    
    return balance
