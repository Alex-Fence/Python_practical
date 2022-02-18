from bs4 import BeautifulSoup
import requests as req

link_url = 'https://stepik.org/media/attachments/lesson/209723/3.html'

page_r = req.get(link_url)
soup = BeautifulSoup(page_r.text, 'html.parser')
sum = 0
for tag in soup.find_all("td"):
    sum += int(tag.string)
print(f'sum = {sum}')
