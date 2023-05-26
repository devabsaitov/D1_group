# pip install googletrans==4.0.0rc1

import googletrans


translator = googletrans.Translator()

trans = translator.translate(text = 'Salom dunyo' , src='uz', dest='ru')

print(trans.text)

'''
Maqsad Ahmedov
Saidkamol Axmedov
'''

