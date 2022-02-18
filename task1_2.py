# В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в
# алфавитном порядке, разделяя пробелами.

from urllib.request import urlopen
import re
import collections

url = 'https://stepik.org/media/attachments/lesson/209719/2.html'
regex = '<code>(.*?)</code>'

html_page = urlopen(url).read().decode('utf-8')

sorted_list = sorted(re.findall(regex, html_page))
counter_list = collections.Counter(sorted_list)

res_str = str()
for element in counter_list.most_common(15):  # most_common( ) самые популярные
    res_str += str(element[0]) + ' '
print(res_str)

# #сортировка словаря требуется import operator
# sorted_list_tupl = sorted(dict_results.items(), key=operator.itemgetter(1), reverse=True)
