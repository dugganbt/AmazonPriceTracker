import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.nl/-/en/Samsung-Galaxy-15-8-Type-C-Black/dp/B0CSV6XPH6/ref=sr_1_1?dib=eyJ2IjoiMSJ9.d0LALMU8AF0EbXLkFxPKwAUO84RPYwqK1E7F__ZaDdImYMS_UMZannIXdNS_tyEeQ3d7bv93vN197THPGxFPFsC2S5iXuPn729w9_K8RR4F7hTiTVhFEvoC55MhC2ziRtiJcf4bWHugfgkDv7sTZ2WwQ6IlS2LANrUjJgkbyuMFs2I3OmK0T6cYNDqrrmgx1WLWgNRQ-F9-_eOzk9hDtmLZZZxv0CRM_GturmSWnoFnUXyNWOAWcwgdd1uehiyLEigsPk0_m02pfsJWvylpSpNpSG-PN2mlVT-M9qmnxepg.sHswUCcp0fD_xy4j5b5AIMXE22-gmYJzR0NDuhEwec4&dib_tag=se&keywords=samsung+s24&qid=1719516296&s=electronics&sr=1-1"


def scrape_product_price(url=url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept-Language": "en-US,en;q=0.5"
    }

    content = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(content.text, "lxml")

    # find container that contains the price of the main item
    price_container = soup.find(class_="a-section a-spacing-none aok-align-center aok-relative")

    # Price is split into whole and decimal umbers
    price = price_container.find("span", class_="a-price-whole").get_text()
    price_fraction = price_container.find("span", class_="a-price-fraction").get_text()
    full_price = float(price+price_fraction.strip())

    return full_price
