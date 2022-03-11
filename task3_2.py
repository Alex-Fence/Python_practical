# Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте,
# сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа,
# разделённых пробелом.

import xml.etree.ElementTree as ET

# import wget
# url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
# wget.download(url)

root_node = ET.parse('map1.osm').getroot()
print(root_node)
for child in root_node:
    if child.tag == 'node':
        print(f'teg={child.tag}, attr={child.attrib}')
