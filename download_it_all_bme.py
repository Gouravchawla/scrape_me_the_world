import requests
from bs4 import BeautifulSoup
import lxml

root_url = 'http://bmeurl.com'


def crawl(url):
    r = requests.get(root_url+url)
    print '\nSaving File {}'.format(url)
    with open(url[1:]+'.txt', 'a') as file_write:
        file_write.write(r.content)

if __name__ == '__main__':        
    # Create a requests object with target page
    r = requests.get(root_url)

    # Make soup
    soup = BeautifulSoup(r.content, 'lxml')

    # Find all the anchors
    anchors = soup.find_all("a")

    # Iterate over anchors and get page contents of all those pages
    for anchor in anchors:
        if anchor['href'].startswith('/6'):
            crawl(anchor['href'])
