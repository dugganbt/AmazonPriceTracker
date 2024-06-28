from amazon_scraper import scrape_product_price, url
from email_notifier import send_email

# Set a lower price threshold for sending the price update
price_threshold = 700

price = scrape_product_price(url=url)
print("Current price", price)

if price < price_threshold:
    send_email(subject="Price update", message=f"Price for your product is {price} ! \n\n Find it here: {url}")
    print("Price email sent!")