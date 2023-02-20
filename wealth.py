import requests
from bs4 import BeautifulSoup

# specify the number of profiles you want to scrape
num_profiles = 10

# make a list of profile URLs to scrape
profile_urls = [f"https://www.brickplanet.com/profile/{i}" for i in range(1, num_profiles+1)]

# create a list to store the rankings and usernames
rankings = []

# loop through the profile URLs and scrape the ranking and username
for url in profile_urls:
    # make a GET request to the profile page
    response = requests.get(url)
    
    # parse the HTML using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find the ranking and username using their respective HTML tags and attributes
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
    
    # add the ranking and username to the list
    rankings.append((ranking, username))

# sort the rankings list by rank, in ascending order
rankings.sort(key=lambda x: int(x[0]) if x[0].isdigit() else float('inf'))

# write the list of rankings to a file named 'wealth.txt'
with open('wealth.txt', 'w') as f:
    for i, (ranking, username) in enumerate(rankings):
        if ranking.isdigit():
            f.write(f"#{ranking} {username}\n")
