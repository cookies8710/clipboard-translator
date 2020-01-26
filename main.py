#!/usr/bin/python3

import pyperclip
import time
from googletrans import Translator

translator = Translator()
current = pyperclip.paste()
last = current
print("Monitoring clipboard content")
while True:
    current = pyperclip.paste()
    if current != last:
        last = current
        to_translate = current.replace('-\n', '').replace('\n', ' ') # join splitted words and lines 
        print("{2}\n{0}\n\n->\n\n{1}".format(current, translator.translate(to_translate).text, 80*'='))

    time.sleep(1)

print("Done.")
