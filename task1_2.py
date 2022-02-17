# В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в
# алфавитном порядке, разделяя пробелами.

from urllib.request import urlopen
import re
import operator

url = 'https://stepik.org/media/attachments/lesson/209719/2.html'
regex = '<code>(.*?)</code>'

html_page = urlopen(url).read().decode('utf-8')

sorted_list = sorted(re.findall(regex, html_page))
set_results = set(sorted_list)
dict_results = {}
for search_str in set_results:
    dict_results[search_str] = sorted_list.count(search_str)
#сортировка словаря
sorted_list_tupl = sorted(dict_results.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_list_tupl)

# print(sorted(sorted_tupl,key=operator.itemgetter(0)))

# print(f'length = {len(l)}')
# for s in l:
#     print(s)
