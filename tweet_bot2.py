#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import *
import random

ACCESS_TOKEN = "852120657575981056-RHohe17l1xLVl4X2mbtNZ8vOcv6jRnj"
ACCESS_TOKEN_SECRET = "kvHttuh0485chyrG0AYdnbtRtHzBAG1rXL9ZATXczj93l"
CONSUMER_KEY = "HjNtvFJVtsmuGy8D0BLSSfmBz"
CONSUMER_SECRET = "VmZESUHpiNvz9UNnKHDhIJL8BsluM5xpJQYe0C622UbXsLcZrO"


t = Twitter(auth=OAuth(ACCESS_TOKEN,
                       ACCESS_TOKEN_SECRET,
                       CONSUMER_KEY,
                       CONSUMER_SECRET)
            )

list = ["わりとつかれた", "シベ６はエモ", "まはりたい", "コンニャクたべたい", "おなかすいた", "おなすい", "ぺこぺぐらい", "今日のごはんなに？", "ぺぐらい", "まほろ", "まはろ", "あり", "わーい", "ともみのうでにく．", "おにくがたべたい．", "とごってるってなんだよ", "いぇーい", "いつも携帯いじってばっかでごめんね", "まむまむ", "Hello, world!!!"]
i = random.randint(0,len(list))
str = t.statuses.update(status=list[i])
# これは確認用本番ではコメントアウト
#print(str)