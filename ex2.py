# -*- coding:utf-8 -*-
# python3
import requests
from operator import itemgetter
url = 'https://raw.githubusercontent.com/OpenMindClub/DeepLearningStartUp/master/happiness_seg.txt'
f = requests.get(url)
content = f.text
content_list = content.split(' ')
result = {}
for i in range(len(content_list) - 1):
    key = '{} {}'.format(content_list[i], content_list[i + 1])
    value = result.get(key, 0)
    result[key] = value + 1
sorted_result = sorted(result.items(), key=itemgetter(1), reverse=True)
print(sorted_result[:10])
