# wordpop

Show a word and its meaning in a notification on my Ubuntu machine.

## Getting Started

### Prerequisites

Wordpop fetches word and its data from redis. The redis instance must store data in `key:value` form. Keys are of the form `word:<word>` and data is stringified json that I get from [Oxford Dictionaries API](https://developer.oxforddictionaries.com/). This is the same data store that is populated through my other project [define](https://github.com/sbmthakur/define).

```
$redis-cli get word:felon
"{\"metadata\":{\"provider\":\"Oxford University Press\"},\"results\":[{\"id\":\"felon\",\"language\":\"en\",\"lexicalEntries\":[{\"entries\":[{\"etymologies\":[\"Middle English: from Old French, literally \xe2\x80\x98wicked, a wicked person\xe2\x80\x99 (oblique case of fel \xe2\x80\x98evil\xe2\x80\x99), from medieval Latin fello, fellon-, of unknown origin. Compare with felon\"],\"grammaticalFeatures\":[{\"text\":\"Singular\",\"type\":\"Number\"}],\"homographNumber\":\"100\",\"senses\":[{\"definitions\":[\"a person who has committed a felony.\"],\"domains\":[\"Crime\",\"Law\"],\"id\":\"m_en_gbus0355980.005\"}]},{\"etymologies\":[\"Middle English: perhaps a specific use of felon; medieval Latin fello, fellon- had the same sense\"],\"grammaticalFeatures\":[{\"text\":\"Singular\",\"type\":\"Number\"}],\"homographNumber\":\"300\",\"senses\":[{\"crossReferenceMarkers\":[\"archaic term for whitlow\"],\"crossReferences\":[{\"id\":\"whitlow\",\"text\":\"whitlow\",\"type\":\"another term for\"}],\"id\":\"m_en_gbus0355990.005\"}]}],\"language\":\"en\",\"lexicalCategory\":\"Noun\",\"pronunciations\":[{\"audioFile\":\"http://audio.oxforddictionaries.com/en/mp3/felon_gb_1.mp3\",\"dialects\":[\"British English\"],\"phoneticNotation\":\"IPA\",\"phoneticSpelling\":\"\xcb\x88f\xc9\x9bl\xc9\x99n\"}],\"text\":\"felon\"},{\"entries\":[{\"grammaticalFeatures\":[{\"text\":\"Positive\",\"type\":\"Degree\"}],\"homographNumber\":\"101\",\"senses\":[{\"definitions\":[\"cruel; wicked.\"],\"id\":\"m_en_gbus0355980.009\",\"notes\":[{\"text\":\"attributive\",\"type\":\"grammaticalNote\"}],\"registers\":[\"archaic\"]}]}],\"language\":\"en\",\"lexicalCategory\":\"Adjective\",\"pronunciations\":[{\"audioFile\":\"http://audio.oxforddictionaries.com/en/mp3/felon_gb_1.mp3\",\"dialects\":[\"British English\"],\"phoneticNotation\":\"IPA\",\"phoneticSpelling\":\"\xcb\x88f\xc9\x9bl\xc9\x99n\"}],\"text\":\"felon\"}],\"type\":\"headword\",\"word\":\"felon\"}],\"synonyms\":\"none\",\"antonyms\":\"none\"}"
```

# screenshot

![Screenshot](/screenshot.png?raw=true "Wordpop screenshot")

This is work under progress. Please report any suggestions or issues. 
