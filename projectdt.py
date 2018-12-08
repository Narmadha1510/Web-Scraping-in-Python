from urllib.request import urlopen
html = urlopen("https://www.indeed.com/viewjob?jk=d88f3bb95f1a4466")
print(html)
site = html.read()
print(site)
from bs4 import BeautifulSoup
soup = BeautifulSoup(site, 'html.parser')
print(soup.prettify())
print(soup.meta)
soup.meta.decompose()
print(soup.prettify())
for i in soup.find_all("div"):
    i.decompose()
for i in soup.find_all("meta"):
    i.decompose()
    print(soup.prettify())
text = soup.get_text()
print(text) 
# breaking text into lines and removing excess whitespace
lines = [line.strip() for line in text.splitlines()]
#removing blank lines
lines = [l for l in lines if l != '']
for l in lines:
  print(l)
  #concatenating into one string
cleaned = ' '.join(lines)
print(cleaned)   
def get_text(url):
    html = urlopen(url)
    
    site = html.read()
    soup = BeautifulSoup(site, 'html.parser')
    for i in soup.find_all("div"):
        i.decompose()
    for i in soup.find_all("meta"):
        i.decompose()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines()) 
    lines = [l for l in lines if l != '']
    cleaned = ' '.join(lines)
    return(cleaned)
url = 'https://www.indeed.com/jobs?q=data+scientist'
html = urlopen(url)
site = html.read()
soup = BeautifulSoup(site, 'html.parser')
print(soup.prettify())
results = soup.find(id = 'resultsCol')
print(results)
page_urls = [link.get('href') for link in results.find_all('a')]
print(page_urls)
#keeping only strings that contain '/rc/'
page_urls = [link for link in page_urls if '/rc/' in  
     str(link)]
print(page_urls)
#array to store job ids
ids = []
for link in page_urls:
    #finding locations in the string to start and stop
    start = link.find('jk=') + 3
    end = link.find('&fccid=')
    
    #appending id to the array
    ids.append(link[start:end])
    
print(ids)
def get_links(url):
    html = urlopen(url)
    
    site = html.read()
    soup = BeautifulSoup(site, 'html.parser')
    results = soup.find(id = 'resultsCol')
    page_urls = [link.get('href') for link in results.find_all('a')]
    page_urls = [link for link in page_urls if '/rc/' in 
          str(link)]
    
    ids = []
    for link in page_urls:
        start = link.find('jk=') + 3
        end = link.find('&fccid=')
        ids.append(link[start:end])
    return(ids)
    url = 'https://www.indeed.com/jobs?q=data+scientist'
html = urlopen(url)
site = html.read()
soup = BeautifulSoup(site, 'html.parser')
results = soup.find(id = 'resultsCol')
print(results)
#grabbing the id tag for the search count
count_string = soup.find(id = 'searchCount')
print(count_string)
#getting just the text in the string
count_string = count_string.get_text()
#splitting the string by white spaces and keeping only the last value
count = count_string.split(' ')[-1]
#removing the punctuation
count = count.replace(',', '')
#converting to a number
count = (count)
print(count)
