import datetime as dt
import random
import smtplib

now = dt.datetime.now()
week_day = now.weekday()

my_email = "helloworld@gmail.com"
password = "abcdsf"

if week_day == 2:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="coconut@yahoo.com",
            msg=f"Subject: Wednesday Motivation\n\n{quote}"
        )



