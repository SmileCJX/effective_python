#! python3
# downloadPicture.py - 下载所有漫画
import requests,os,bs4

url = 'http://xkcd.com'  # starting url
os.makedirs('./xkcd',exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.

    # Download the image.

    # Save the image to ./xkcd

    # Get the Prev button's url.

print('Done.')