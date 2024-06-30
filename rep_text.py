

def unicode():
    if 'A' == 65:
        print("True")
    else:
        print("False")

unicode()

def raw_strings(string):
    print(string)

raw_strings(r'what \n "what"\t\n')

def char_decoder(char):
    print(ord(char))

char_decoder("강")

def num_decoder(num):
    print(chr(num))

num_decoder(44053)