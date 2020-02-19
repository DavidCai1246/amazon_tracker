import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/Champion-Graphic-Powerblend-Granite-Heather/dp/B078GLLX2D/ref=pd_ys_c_rfy_10287217011_1?_encoding=UTF8&pd_rd_i=B078GLLX2D&pd_rd_r=XSCYN8ZM4MWS0GT9ACVE&pd_rd_w=CgqOg&pd_rd_wg=Ftzf9&pf_rd_p=c575d4a4-ba14-478e-9bc0-a03b02569989&pf_rd_r=XSCYN8ZM4MWS0GT9ACVE&psc=1&refRID=2DFFJC5RENBJDHM51SR6'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = float(price[5:10])

    if (convertedPrice < 80):
        subject = "Price Drop"
        msg = "Price has dropped!"
        send_email(subject,msg)


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("xxx@gmail.com", "password")
        message = 'Subject:{}\n\n{}'.format(subject, msg)
        server.sendmail("xxx@gmail.com", "xxx@gmail.com", message)
        server.quit()
        print("Success")
    except:
        print("Email failed to send.")

check_price()
