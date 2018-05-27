# (c) Vojtěch Smutný 2018
# Text must be encoded to UTF-8

import re
from vocabulary import *

tokenize_regex = "([\.,?:;!\[\]{}\(\)„“‚‘»«›‹…])"

#source text directory ()
def tokenize():
    global op
    with open("input/text.txt", "r", encoding="utf-8") as f:
        file = f.read()
        op = re.sub("\n+", " ", file) #konce řádků na mezeru
        op = re.sub("("+ tokenize_regex + "|" + "\s" +  vocabulary + ")", r" \1 ", op) #tokenizace + zkratky
        op = re.sub(r"(  |   |    )", r" ", op) #dvoj a více mezery na jednu

def vert():
    global op
    op = re.sub("(" + vocabulary + r"?" ")" + "\s+", r"\1\n", op) #vyjímka pro zkratky, a mezery na konce řádků
    op = re.sub(r"^\s*$", r"", op) #nadbytečná bílá místa smazat

def printing():
    global op
    print(op)

#output directory      
def write():
    with open('output/output.txt', 'w', encoding="utf-8") as f:
        f.write(op)
      
def output():
    out = input("Print (P) or create txt file (F)?: ")
    if out == "P":
        print(op)
    if out == "F":
        write()
        print("File output.txt created")
    else:
        a = input("Do you want to stop the program (Y/N): ")
        if a == "N":
            output()
        else:
            print("script has been stopped by user")
            quit()

def main():
    q1 = input("Tokenize? (Y or N): ")
    if q1 == "Y":
        tokenize()
        q2 = input("Verticalize? (Y or N): ")
        if q2 == "Y":
            vert()
            output()
        else:
             output()
    else:
        print("script has been stopped by user")
        
main()