import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

jobs = soup.find_all('li')

for job in jobs:
    base_url = 'https://www.python.org'
    try:
        data = {
            'Job URL': base_url + job.find('span', {'class':'listing-company-name'}).find('a')['href'],
            'Job Title': job.find('span', {'class': 'listing-company-name'}).text.strip().replace('\n', '').replace('\t', ''),
            'Job Location': job.find('span', {'class':'listing-location'}).text.strip(),
            'Skills': job.find('span', {'class': 'listing-job-type'}).text.strip(),
            'Category': job.find('span', {'class':'listing-company-category'}).text
        }
        print(data)
      

    except AttributeError:
        pass
    
    