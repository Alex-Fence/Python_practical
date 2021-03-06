# Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте,
# сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа,
# разделённых пробелом.

import xml.etree.ElementTree as ET

# import wget
# url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
# wget.download(url)

root_node = ET.parse('map1.osm').getroot()

tags = {'yes': 0, 'no': 0}
for child in root_node:
    if child.tag == 'node':
        is_tag = False
        for sub_child in child:
            if sub_child.tag == 'tag':
                is_tag = True
        if is_tag:
            tags['yes'] += 1
        else:
            tags['no'] += 1
print(f"yes = {tags['yes']} no = {tags['no']}")
