import bs4 as bs4
import requests as requests

url = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'framebar'})
data = bs4.BeautifulSoup(url.text, 'html.parser')
populer_area = data.find(attrs={'class':'list-content'})

titles_popular = populer_area.find_all(attrs={'class':'media__title'})
images_populer = populer_area.find_all(attrs={'class':'media__image'})

#for t in titles_popular:
#    print(t.text)
#print(titles_popular)

for p in images_populer:
    print(p.find('a').find('img')['title'])