import bs4,requests,os,sys

domain=sys.argv[1]
content_list=[]
with open(f'recon/{domain}/crawler_output','w') as file:
    pass

from urllib.parse import urljoin
def request(url):
    try:
        html=requests.get(url,allow_redirects=False,timeout=2)
        return html.content
    except:
        return ''

def crawl(url):

    try:
        html=request(url)
        soup=bs4.BeautifulSoup(html,'html.parser')
        for a in soup.find_all('a',href=True):
            link=urljoin(url,a['href'])

            if link not in content_list:
                content_list.append(link)
                print("[+] Found URL: {}".format(link))
                with open(f'recon/{domain}/crawler_output','a') as file:
                    file.write(link + '\n')
                crawl(link)

    except KeyboardInterrupt:
        exit(0)

with open(f'recon/{domain}/subdomains','r') as file:
    subdomains=file.read().splitlines()
    for subdomain in subdomains:
        url=f"https://{subdomain}"
        crawl(url)
       
