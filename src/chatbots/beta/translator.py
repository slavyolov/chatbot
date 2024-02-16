# Resources :

# https://medium.com/@nikitasilaparasetty/how-to-build-a-language-translator-with-text-and-audio-using-python-and-google-apis-e2697a97b969
# https://stackoverflow.com/a/65109346

import googletrans
from googletrans import Translator

# Example 1 :
translator = Translator()
translation = translator.translate("Здравейте, как се казвате?", dest='en')
print(translation.text)

# Example 2 :
translator = Translator()
translation = translator.translate("Кой е директорът на училището в Бургас?", dest='en')
print(translation.text)

# Example 3 :
translator = Translator()
translation = translator.translate("Димитрина Тодорова директор ли е?", dest='en')
print(translation.text)