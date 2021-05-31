import smtplib
from credentials import *

From = gmail_user
To = 'aaditkobe268@gmail.com'

Subject = 'aaa\n'
msg = """Don't freak out!! \tThis is an automated python produced test email.
If you would like to get more of these reply to this mail with a 'YEET'. If not reply to this mail with a 'Fuck-Off'.
\nThank you
 Aadit Chadda"""

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
