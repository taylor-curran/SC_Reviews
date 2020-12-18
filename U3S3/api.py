import requests
import bs4
import numpy as np
import pandas as pd

# Example Code

game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')
# print(soup.find('name').text)

# Task Begins

# Explore the BGG API and see if you are able to find the following information about a game:

# Name
# Max and Min Players
# Play Time
# Game Description
# Some of the game mechanics

# Docs: https://boardgamegeek.com/wiki/page/BGG_XML_API&redirectedfrom=XML_API#

tags = [tag.name for tag in soup.find_all()]

column_names = ['game_id', 
                'name', 
                'min_players',
                'max_players', 
                'playing_time',
                'description', 
                'game_mechanics']

rows = []

base_url = 'http://www.boardgamegeek.com/xmlapi/boardgame/'

for game_id in range(1, 11):
    url = base_url + str(game_id)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    game_row = [
        game_id,
        soup.find('name').text,
        int(soup.find('minplayers').text), 
        int(soup.find('maxplayers').text),
        int(soup.find('playingtime').text),
        soup.find('description').text,
        soup.find('boardgamemechanic').text
    ]
    rows.append(game_row)

# print(rows[0])

# print('\nStart DF\n')

df = pd.DataFrame(data=rows, columns=column_names)
# print(df.head())