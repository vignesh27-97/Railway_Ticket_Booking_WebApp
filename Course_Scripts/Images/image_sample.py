from PIL import Image
import os


words = Image.open('D:\Python\VSCode_PyScripts\Course_Scripts\Images\word_matrix.png')
mask = Image.open('D:\Python\VSCode_PyScripts\Course_Scripts\Images\mask.png')

size = words.size
mask = mask.resize(size)
mask.putalpha(200)
words.paste(mask,(0,0),mask)
words.show()