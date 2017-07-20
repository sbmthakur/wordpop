import os
import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

key = redis_client.randomkey()
json_str = redis_client.get(key)
word_data = json.loads(json_str)

definition = word_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
word = word_data['results'][0]['word']

cmd = 'notify-send "' + word + '" "' + definition + '"'
print cmd
os.system(cmd)
