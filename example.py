import requestsTLS.requestsTLS as requestsTLS

requestsTLS.intializeServer()

url = "https://www.mediamarkt.de/api/v1/graphql?operationName=GetSelectProduct&variables=%7B%22hasMarketplace%22%3Atrue%2C%22id%22%3A%222764236%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22a98839cdbc0ac9746ca9d1b0b48c26e3355e73a09c11f136876c9c3c5679717c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Media%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22contentful%22%3Atrue%7D%7D"
headers = {
  'authority': 'www.mediamarkt.de',
  'x-operation': 'GetSelectProduct',
  'apollographql-client-name': 'pwa-client',
  'x-cacheable': 'true',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
  'x-mms-salesline': 'Media',
  'content-type': 'application/json',
  'accept': '*/*',
  'x-flow-id': '4617979b-d4af-4871-96e3-e89495f0e781',
  'apollographql-client-version': '1.62.0',
  'x-mms-language': 'de',
  'x-mms-country': 'DE',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.mediamarkt.de/de/product/_samsung-galaxy-a52s-5g-128gb-black-ne-128-gb-awesome-black-dual-sim-2764236.html',
  'accept-language': 'en-US,en;q=0.9'
}

response = requestsTLS.get(url, headers=headers)
print(response.text)