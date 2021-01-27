import asyncio
import aiohttp
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
async def get_html(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    html = await response.text()

                    html_file = open("html.txt", "w")
                    html_file.write(html)
                    html_file.close()
                sys.exit()

        except aiohttp.ClientConnectorError as e:
          print('Connection Error', str(e))


url = 'https://www.google.com/'
headers = {
    'Content-Type': 'text/html',
}

loop = asyncio.get_event_loop()
loop.run_until_complete(get_html(url, headers))