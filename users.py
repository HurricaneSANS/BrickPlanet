import requests
from bs4 import BeautifulSoup

# Loop through profile pages 1-9000
for profile_number in range(1, 9001):
    # Make the request to the profile page
    url = f"https://www.brickplanet.com/profile/{profile_number}"
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the title tag and extract the username from it
        title_tag = soup.find('title')
        username = title_tag.text.split('|')[0].strip()

        # Write the username to the file
        with open('users.txt', 'a') as f:
            f.write(f"{username}\n")
    else:
        print(f"Error: Could not retrieve profile {profile_number}")
