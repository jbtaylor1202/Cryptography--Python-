#-*-coding:utf8;-*-
#qpy:3
#qpy:console

inputText = input('Please enter text: ')
inputText = inputText.upper()
outputText = ''

mode = ""
while mode not in("e","d"):
    mode = str(input ('Enter "e" for encryption or "d" for decryption: '))

key = ""
while key not in range(1,25):
    key = int(input('Enter a key between 1 and 26: '))


Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for symbol in inputText:
    if symbol in Letters:
        num=Letters.find(symbol)
        if mode == 'e':
            num=num+key
        elif mode == 'd':
            num=num-key
            

        if num >=len(Letters):
            num=num-len(Letters)
        elif num <0:
            num=num+len(Letters)


        outputText = outputText + Letters[num]

    else:
        outputText = outputText + symbol


print(outputText)

