#!/usr/bin/env python

import urllib
import json
import sys
import os

accessToken = 'TOKENVALUE'
userId = sys.argv[1]
limit=100

url='https://graph.facebook.com/'+userId+'/posts?access_token='+acessToken+'&limit='+str(limit)
data=json.load(urllib.urlopen(url))
id=0

print str(id)

for item in data['data']
    time=item['created_time'][11:19]
    date=item['created_time'][5:10]
    year=item['created_time'][0:4]

if 'shares' in item:
    num_share=item['shares']['count']
else:
    num_share=0
if 'likes' in item:
    num_like=item['likes']['count']
else:
    num_like=0

id+=1

print str(id)+'\t'+time.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+year.encode('utf-8')+'\t'+str(num_share)+'\t'+str(num_like)
