#  Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".

text = 'АБВя люблюАБВ учиАБВться'
print(text.translate({ord(i): None for i in 'АБВ'}))