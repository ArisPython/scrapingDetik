import requests
import bs4
from flask import Flask, render_template

#menggunakan flask sebagai web framework
app = Flask(__name__)

#routing ke directory index.html
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik')
def detik_populer():
    url = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'})
    data = bs4.BeautifulSoup(url.text, 'html.parser')
    populer_area = data.find(attrs={'class': 'list-content'})

    titles_popular = populer_area.find_all(attrs={'class': 'media__title'})
    images_populer = populer_area.find_all(attrs={'class': 'media__image'})

    return render_template('detik.html', images_populer=images_populer)

@app.route('/idr_rate')
def idr_rate():
    url = requests.get('http://www.floatrates.com/daily/idr.json')
    data = url.json()
    return render_template('idr_rate.html', data_json=data.values())

if __name__ == '__main__':
    app.run(debug=True)