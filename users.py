import requests
import time
from bs4 import BeautifulSoup

# Loop through profile pages 1-9000
for profile_number in range(1, 15000):
    # Make the request to the profile page
    url = f"https://www.brickplanet.com/profile/{profile_number}"
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the profile ID from the URL
        profile_id = url.split('/')[-1]

        # Find the title tag and extract the username from it
        title_tag = soup.find('title')
        username = title_tag.text.split('|')[0].strip()

        # Write the profile ID and username to the file
        with open('users.txt', 'a') as f:
            f.write(f"ID: {profile_id} Username: {username}\n")

        # Wait for 3 seconds before making the next request
        time.sleep(1.5)
    else:
        print(f"Error: Could not retrieve profile {profile_number}")
