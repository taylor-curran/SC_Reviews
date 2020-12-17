import requests
import bs4
import lxml

game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, lxml)
# soup = bs4.BeautifulSoup(result.text, features='lxml')

# print(soup.find('name').text)
print(soup.prettify())