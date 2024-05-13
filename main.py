from modules import gossip
from datetime import date


base_url = 'https://www.bbc.co.uk/sport/football/gossip'

link = gossip.get_latest_gossip_link()

formatted_gossip = ''

if link:
    gossip_content = gossip.get_gossip_page(link)
    formatted_gossip = gossip.format_gossip(gossip_content)
else:
    print("No gossip link found.")

today = date.today().strftime("%B %d, %Y")

final_string = f"Footie gossip for {today}:\n{formatted_gossip}"

print(final_string)
