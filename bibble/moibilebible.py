import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import requests
import pickle
import json
import re
import random




def appender(word):
	favs = []
	pickle_in = open('passages.pickle', 'rb')
	favs = pickle.load(pickle_in)
	pickle_in.close()

	
	favs.append(word)

	print('total verses in bank: ', len(favs))
	

	

	
	pickle_out = open('passages.pickle', 'wb')
	pickle.dump(favs, pickle_out)
	pickle_out.close()
	texter(favs)
	


def texter(bank):
	print (len(bank))
	number = random.randint(0, len(bank) - 1)
	verse = bank[number]
	url = 'https://maker.ifttt.com/trigger/get-verses/with/key/klVzGE694kL9d8sHgn1Ac2FpOtMoHsTTzlfgQZqCAu6'
	data = { "value1" : verse, "value2" : "", "value3" : "" }
	requests.post(url, data = data)








def go(book, verse):
	text = ''
	URL = 'https://api.esv.org/v3/passage/text/?include-short-copyright=false&include-headings=false&include-verse-numbers=false&include-first-verse-numbers=false&include-footnotes=false&include-footnote-body=false&include-headings=false&q='
	key = '71b09f9fe87636a5f6556e26f323e5d2c5ae7579'

	half = (book + '+' + verse)
	cURL = (URL + half)
	print('working')

	passage = requests.get(cURL, headers={"Authorization":key}).text
	passage = json.loads(passage)
	passage = passage['passages']
	formatt = ''
	for sub in passage:
		formatt = (formatt + (re.sub('\n', ' ', sub)))
	passage = formatt
	print(passage)
	appender(passage)









class Grid(Widget):
	book = ObjectProperty(None)
	verse = ObjectProperty(None)

	def submit(self):
		go(self.book.text, self.verse.text)
		self.book.text = ''
		self.verse.text = ''
		


class bibleApp(App):
	def build(self):
		return Grid()

if __name__ == '__main__':
	bibleApp().run()







