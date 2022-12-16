import re
import requests
import json
from nltk.corpus import wordnet
intents = ['hi', 'buy', 'goodbye', 'thanks', 'options', 'noanswer']
responses = {
'hi': 'Hello! How can I help you?',
'buy': 'Call external API',
'goodbye': 'Bye! Come back again soon.',
'thanks': 'Happy to help!',
'options': 'I can help you find any product that you would like buy.', 'noanswer': 'I dont quite understand. Could you repeat that?'
}
patterns = {}
for word in intents:
synonyms = []
for w in wordnet.synsets(word):
for l in w.lemmas():
name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', l.name()) synonyms.append(name)
patterns[word] = set(synonyms)
keywords = {} keywordsAndSyn = {}
keywords['hi'] = [] keywords['buy'] = [] keywords['goodbye'] = [] keywords['thanks'] = [] keywords['options'] = []
for synonym in list(patterns['hi']): keywords['hi'].append('.*\\b'+synonym+'\\b.*')
for synonym in list(patterns['buy']): keywords['buy'].append('.*\\b'+synonym+'\\b.*')
for synonym in list(patterns['goodbye']): keywords['goodbye'].append('.*\\b'+synonym+'\\b.*')
for synonym in list(patterns['thanks']):
RULE BASED CHATBOT
keywords['thanks'].append('.*\\b'+synonym+'\\b.*')
for synonym in list(patterns['options']): keywords['options'].append('.*\\b'+synonym+'\\b.*')
for intent, keys in keywords.items(): keywordsAndSyn[intent]=re.compile('|'.join(keys))
print ("Welcome to ChatBuy. What are you looking for?") while (True):
userInput = input().lower() if userInput == 'quit':
print ("Thank you for visiting us. Hope you had a good time!")
break
match = None
for intent,pattern in keywordsAndSyn.items():
if re.search(pattern, userInput): match = intent
key = 'noanswer'
if match in responses:
key = match
if (responses[key] == 'Call external API'):
print("Enter product name")
product_name = input().lower()
searchCall = 'https://dummyjson.com/products/search?q=' + product_name response = requests.get(searchCall)
jsonResponse = json.dumps(response.json(), indent = 2)
print("These are some products available")
print(jsonResponse)
else:
print (responses[key])
