# eBucks

Python module for scraping balance from [eBucks](https://www.ebucks.com) website.


## Usage

    from ebucks import get_balance
    username = 'USERNAME'  # your eBucks username
    password = 'PASSWORD'  # your eBucks password
    balance = get_balance(username, password)
    print 'eBucks balance: eB {0}'.format(balance)
