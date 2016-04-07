#-*-coding:utf8;-*-
#qpy:3
#qpy:console

plainText = input('Please enter message for encryption: ')
codedText = ''

i = len(plainText)-1

while i >= 0:
    codedText = codedText + plainText[i]
    i=i-1


print(codedText)
