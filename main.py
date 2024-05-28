from modules import gossip

base_url = 'https://www.bbc.co.uk/sport/football/gossip'

link = gossip.get_latest_gossip_link()

formatted_gossip = ''

if link:
    gossip_content = gossip.get_gossip_page(link)
    gossip_paragraphs = gossip.get_gossip_paragraphs(gossip_content)
    formatted_gossip = gossip.format_gossip(gossip_paragraphs)
else:
    print("No gossip link found.")


print(formatted_gossip)
