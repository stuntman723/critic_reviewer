url = 'http://www.metacritic.com/critic/ao-scott?filter=movies&num_items=30&sort_options=metascore'

from lxml import html
import requests

page = requests.get(url)
page_html = html.fromstring(page.text)
reviews = page_html.xpath('//*[@id="main"]/div[4]/div[3]/ol/li[2]')
print reviews

#main > div.module.reviews_module.critic_reviews_module > div.body > ol > li:nth-child(2)