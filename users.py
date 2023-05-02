import requests
import time
from bs4 import BeautifulSoup

#how many users
for profile_number in range(1, 15000):
    url = f"https://www.brickplanet.com/profile/{profile_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        profile_id = url.split('/')[-1]

        title_tag = soup.find('title')
        username = title_tag.text.split('|')[0].strip()

        with open('users.txt', 'a') as f:
            f.write(f"ID: {profile_id} Username: {username}\n")

        time.sleep(1.5)
    else:
        print(f"Error: Could not retrieve profile {profile_number}")
