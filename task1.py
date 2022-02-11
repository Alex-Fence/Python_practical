from urllib.request import urlopen

lang_dict = {'Python': 0, 'C++': 0}

with urlopen('https://stepik.org/media/attachments/lesson/209717/1.html') as html_page:
    page_temp = html_page.read().decode('utf-8')
    for i in lang_dict.keys():
        count_lang = page_temp.count(i)
        if count_lang > 0:
            print(count_lang)
            lang_dict[i] += count_lang
print(lang_dict)
