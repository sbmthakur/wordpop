#!/usr/bin/env python
import os
import redis
import json
import random

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#Oxford API usually returns a list of synonyms
#Here we are only returning the first one
def fetch_synonym(synonyms):
    if synonyms != "none":
        return synonyms.split(',')[0]
    else:
        return None

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

synonym = fetch_synonym(word_data['synonyms'])

#This is done fot the sake of formatting
#If no synonym exists then simlpy make it a blank string
if synonym:
    synonym = ' | ' + synonym
else:
    synonym = ''

cmd = '/usr/bin/notify-send "' + word + ' | ' + lexical_category + synonym + '" "' + definition + '\nEx: ' + example_sentence + '"'
print cmd
os.system(cmd)
