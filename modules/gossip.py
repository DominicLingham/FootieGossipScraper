import requests
from bs4 import BeautifulSoup

base_url = 'https://www.bbc.co.uk/sport/football/gossip'


def get_latest_gossip_link():
    response = requests.get(base_url)
    gossip_html = BeautifulSoup(response.text, 'html.parser')

    gossip_items = gossip_html.find_all('a', class_="ssrcss-zmz0hi-PromoLink exn3ah91")

    first_gossip_link = gossip_items[0].get('href')

    return first_gossip_link


def get_gossip_page(gossip_url):
    gossip_page = requests.get('https://www.bbc.co.uk/' + gossip_url)

    gossip_html = BeautifulSoup(gossip_page.text, 'html.parser')

    target_paragraphs = gossip_html.select('p[data-reactid*="paragraph"]:not([data-reactid*="paragraph-0"])')

    return target_paragraphs


def format_gossip(gossip):
    formatted_gossip = ''
    for g in gossip:
        formatted_gossip += f"{gossip.index(g) + 1} - {g.get_text().strip('external-link')}\n"
    return formatted_gossip
