import requests
import sys

"""
    This method makes an http call to pull down html from a url and save it as text file.

    ...

    Attributes
    ----------
    url : str
        a string that represents the url to fetch html froms
    headers : dict
        a dictionary object that includes the necessary headers for the http request

"""
def get_html(url, headers):
    try:
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            html_file = open("html.txt", "w")
            html_file.write(r.text)
            html_file.close()
        sys.exit()
    except requests.exceptions.HTTPError as err:
        print (err.response.text)
    
url = 'https://www.google.com/'
headers = {
    'Content-Type': 'text/html',
}

get_html(url, headers)
