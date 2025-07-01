import requests as re
from aiohttp.web_fileresponse import extension
from bs4 import BeautifulSoup as bs
import os
from PIL import Image
from IPython.display import IFrame

import pandas as pd

from urllib.parse import urljoin #for parsing wikipedia links

from fontTools.misc.cython import returns

url = "https://en.wikipedia.org/wiki/Spiking_neural_network"

response = re.get(url)
html_content = response.text
#soup = bs(html_content, 'html.parser')

#print(f"Here's what html_content contains:\n{html_content[:500]}\n\n")
#print(f"And here's what function .prettify() does:\n{soup.prettify()[:2000]}")

def find_logo(url):
    try:
        headers = response.headers
        resp = re.get(url, headers=headers)
        soup = bs(resp.text, 'html.parser')

        #tag search for wiki specifically
        logo_container = soup.find('a', {'class': 'mw-logo'})
        if logo_container:
            logo_img = logo_container.find('img')
            if logo_img:
                logo_url = logo_img['src']
                return urljoin(url, logo_url)

        #tag search for others
        logo_img = soup.find('img', {'src': True, 'alt': lambda x : x and 'logo' in x.lower()})
        if not logo_img:
            logo_img = soup.find('img', {'src': True, 'class': lambda x : x and 'logo' in x.lower()})
        #elif not logo_img:
        #   logo_img = soup.find('img', {'src': True, 'class': lambda x : x and 'mw-logo' in x.lower()})
        if logo_img:
            logo_url = logo_img.get('src')

        #if logo_url.startswith('http'):
        #   return logo_url
        #else:
        #   return f"{url.rstrip('/')}/{logo_url.lstrip('/')}"
            return urljoin(url, logo_url)

    except Exception as e:
        print(f"Error: {e}\n")
    return None

def get_extension_of_an_image(cont_type):
    if not cont_type:
        return '.bin'

    type = cont_type.split(';')[0].strip().lower()
    return_type = type.split('/')[-1].split('+')[0]

    return f".{return_type}"

logo_url = find_logo(url)
if logo_url:
    print(f"Logo is found at {logo_url}")
    r_ = re.get(logo_url, stream=True)
    if r_.status_code == 200:
        cont_t = r_.headers.get('content-type')
        extension = get_extension_of_an_image(cont_t)
        path = os.path.join(os.getcwd(), 'image_'+f'{extension}')
        with open(path, 'wb') as f:
            f.write(r_.content)
        print(f"Image saved to: {path}\n")
    else:
        print(f"Error: HTTP STATUS CODE {r_.status_code}\n")
else:
    print(f"Logo not found at {url}")

url2 = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

data = pd.read_html(url2)
table = data[2]
print(table)