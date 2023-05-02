import requests
from bs4 import BeautifulSoup

# how many users
num_profiles = 10

profile_urls = [f"https://www.brickplanet.com/profile/{i}" for i in range(1, num_profiles+1)]

rankings = []

for url in profile_urls:
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    ranking_tag = soup.find('span', {'class': 'text-xs text-muted'})
    if ranking_tag is not None:
        ranking = ranking_tag.text.strip().replace("#", "").replace(",", "")
    else:
        ranking = "N/A"
    
    username_tag = soup.find('title')
    if username_tag is not None:
        username = username_tag.text.split(' | ')[0].strip()
    else:
        username = "N/A"
    
    rankings.append((ranking, username))

rankings.sort(key=lambda x: int(x[0]) if x[0].isdigit() else float('inf'))

with open('wealth.txt', 'w') as f:
    for i, (ranking, username) in enumerate(rankings):
        if ranking.isdigit():
            f.write(f"#{ranking} {username}\n")
