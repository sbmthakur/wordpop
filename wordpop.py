#!/usr/bin/env python
import os
import redis
import json
import random

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

key = redis_client.randomkey()
json_str = redis_client.get(key)
word_data = json.loads(json_str)

lexical_entries_length = len(word_data['results'][0]['lexicalEntries'])
random_entry = random.randint(0, lexical_entries_length - 1)
lexical_category = word_data['results'][0]['lexicalEntries'][random_entry]['lexicalCategory']
definition = word_data['results'][0]['lexicalEntries'][random_entry]['entries'][0]['senses'][0]['definitions'][0]

#Following try-except fetches an example sentence for the word
try:
    example_sentence = word_data['results'][0]['lexicalEntries'][random_entry]['entries'][0]['senses'][0]['examples'][0]['text']
except LookupError:
    #You will arrive here if there is no "text" key 
    example_sentence = "None"

word = word_data['results'][0]['word']

cmd = '/usr/bin/notify-send "' + word + ' | ' + lexical_category + '" "' + definition + '\n<b>Ex:</b> ' + example_sentence + '"'
print cmd
os.system(cmd)
