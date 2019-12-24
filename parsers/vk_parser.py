from datetime import datetime
import calendar

import vk_api

from json_utils import save_json_to_file

SECONDS_IN_DAY = 86400
VK_SERVICE_TOKEN = '6a7e76c16a7e76c16a7e76c1b46a10b35e66a7e6a7e76c1347cefb511e37d1cafda7b3d'
DRUGS = ['Аторвастатин', 'Сувардио', 'Аторвастатин-СЗ', 'Липримар']


def get_vk_reviews(query, start_time, end_time):
    vk = vk_api.VkApi(token=VK_SERVICE_TOKEN)
    news = vk.method('newsfeed.search', values={
        'q': query,
        'extended': 0,
        'count': 200,
        'start_time': start_time,
        'end_time': end_time
    })
    texts = [{'comment': item['text']} for item in news['items']]
    return texts


start_time = calendar.timegm(datetime.now().timetuple())
for drug_name in DRUGS:
    for i in range(100):
        end_time = start_time
        start_time -= SECONDS_IN_DAY
        texts = get_vk_reviews(drug_name, start_time, end_time)
        save_json_to_file(f'../data/{drug_name}_vk-{end_time}.json', texts)
