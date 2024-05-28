import requests
from bs4 import BeautifulSoup

base_url = 'https://www.bbc.co.uk/sport/football/gossip'


def get_latest_gossip_link():
    response = requests.get(base_url)
    response.encoding = 'utf-8'
    gossip_html = BeautifulSoup(response.text, 'html.parser')

    gossip_items = gossip_html.find_all('a', class_="ssrcss-zmz0hi-PromoLink exn3ah91")

    first_gossip_link = gossip_items[0].get('href')

    return first_gossip_link


def get_gossip_page(gossip_url):
    gossip_page = requests.get('https://www.bbc.co.uk/' + gossip_url)
    gossip_page.encoding = 'utf-8'

    gossip_html = BeautifulSoup(gossip_page.text, 'html.parser')

    return gossip_html


def get_gossip_paragraphs(gossip_content):
    target_paragraphs = gossip_content.select('div[class="ssrcss-7uxr49-RichTextContainer e5tfeyi1"] > p')

    return target_paragraphs

def format_gossip(gossip):
    if not gossip:
        return ''

    headline = gossip[0].get_text()
    formatted_gossip = ''

    for i in range(1, len(gossip)):
        g = gossip[i]
        formatted_gossip += f"{i + 1} - {g.get_text().strip('external')}\n"

    return headline + '\n' + formatted_gossip
