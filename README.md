# eBucks

Python module for scraping balance from [eBucks](https://www.ebucks.com) website.


## Installation

Clone the Git repository for the module. After the repository has been cloned it can be installed from the command line:

    python setup.py install


## Usage

    from ebucks import get_balance
    username = 'USERNAME'  # your eBucks username
    password = 'PASSWORD'  # your eBucks password
    balance = get_balance(username, password)
    print 'eBucks balance: eB {0}'.format(balance)
