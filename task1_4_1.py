# В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
# Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения.
# Для доступа к ячейкам используйте возможности BeautifulSoup.

from bs4 import BeautifulSoup
import requests as req

link_url = 'https://stepik.org/media/attachments/lesson/209723/5.html'

page_r = req.get(link_url)
soup = BeautifulSoup(page_r.text, 'html.parser')
sum = 0
for tag in soup.find_all("td"):
    sum += int(tag.string)
print(f'sum = {sum}')
