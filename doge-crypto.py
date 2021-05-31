import requests as requests
from bs4 import BeautifulSoup
from credentials import *
import time
import datetime
import smtplib
import sqlite3
# Plugins, Packages and Imports ^^^

while True:
    # Scrapping Price of Dogecoin
    link = requests.get('https://coinmarketcap.com/currencies/dogecoin/').text

    soup = BeautifulSoup(link, 'lxml')
    widget = soup.find('h1', class_='sc-16r8icm-0 kXPxnI priceTitle___1cXUG')
    price = soup.find('div', class_='priceValue___11gHJ').text.replace(' ', '')
    # Preparing scrapped content for forced conversion
    price = price.strip('$')
    
    # Scrapping pricing of AUD in comparison USD
    money = requests.get('https://wise.com/in/currency-converter/usd-to-aud-rate').text
    
    inside = BeautifulSoup(money, 'lxml')
    block = inside.find('h3', class_='cc__source-to-target')
    change = block.find('span', class_='text-success').text
    
    # Converting Scrapped 'str' from website to floating point
    price = float(price)
    change = float(change)
    
    # Buying price of customer at AUD
    buying = price * change
    
    # Creating time-stamp of discovery
    time_now = str(datetime.datetime.now().time())

    # Adding discovered price to data-base along with its respective time-stamp
    db = sqlite3.connect('dogecoin-tracker.sqlite')
    db.execute("CREATE TABLE IF NOT EXISTS dogeprice(time TEXT, price INTEGER)")
    db.execute("INSERT INTO dogeprice VALUES(?, ?)", (time_now, buying))
    db.commit()
    
    print()
    
    # Printing out the database
    cursor = db.cursor()
    cursor.execute("SELECT * FROM dogeprice")
    for timer, pricer in cursor:
        print(timer, '\t', pricer)
        print()

    cursor.close()
    db.close()

    # Sending Email to Purchaser
    if buying < 0.21: # Buy when Low
        # showing encountered price
        print("Current Doge-coin price: ", buying)
        
        From = gmail_user
        To = 'aaditkobe268@gmail.com'

        Subject = 'Doge-Coin price \n'
        msg = """The price of Dogecoin is now {0}.
        It is a very low price and you have been adiviced to purchase it as soon as possible
        As you never know when Elon Musk decides to tweet next!
        \n\nThank you \nAadit Chadda""".format(buying)

        email_text = Subject + msg
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            # server.starttls()
            print("Server connected!")
            server.login(gmail_user, gmail_password)
            print("Account Logged-in")
            server.sendmail(From, To, email_text)
            server.close()
            print("Mail Sent!")
        except:
            print("Something went wrong")
        break
    elif buying > 0.69: # Sell when High
        # showing encountered price
        print("Current Doge-coin price: ", buying)
    
        From = gmail_user
        To = 'aaditkobe268@gmail.com'

        Subject = 'Doge-Coin price \n'
        msg = """The price of Dogecoin is now {0}.
        It is a high price. Looks like Elon Just Tweeted about Doge.
        You have been advised to sell you Dogecoin before the Meme wave ends
        \n\nThank you \nAadit Chadda""".format(buying)

        email_text = Subject + msg
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            # server.starttls()
            print("Server connected!")
            server.login(gmail_user, gmail_password)
            print("Account Logged-in")
            server.sendmail(From, To, email_text)
            server.close()
            print("Mail Sent!")
        except:
            print("Something went wrong")
        break
    else: # Do nothing if a good offer is not there
        pass
    # Relapse Time for web-pages to reload
    time.sleep(45)

# presenting scrapped content with respect to time

print()
print("-" * 75)
print()

print("AC-24 Productions")
