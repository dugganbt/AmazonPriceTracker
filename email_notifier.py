import smtplib
import os
from dotenv import load_dotenv

path = os.path.join("Web scraping projects", "AmazonPriceTracker")

# load environment variables for email
load_dotenv(os.path.join(path,".env"))

# Access the environment variables
from_email = os.getenv('from_email')
password = os.getenv('password')
to_email = os.getenv('to_email')


def send_email(from_email=from_email, to_email=to_email, password=password, subject="", message=""):

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # securing the connection, messages sent will be encrypted
            connection.login(user=from_email, password=password)

            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
            msg=f"Subject:{subject}\n\n {message}"
            )