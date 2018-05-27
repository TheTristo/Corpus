''' ANOTACE nefunguje protoze musim mit zvlast regex pro vertikalizovany text a pro nevertikalizovany

def an_word():
    global op
    op = re.sub(r"(\w*)", r"<w>\1</w>", op)

def an_s():
    global op
    op = re.sub("(\b((?!=|\.).)+(.)\b[.!?]", r"<s>\1</s>", op)

def anottate():Y
    a = input("Annotation on: Word level (W), Sentence level (S) or both (B)? If changed your mind write anything else.")
    if a == "W":
        print("Word level annotation")
        an_word()
        output()
    if a == "S":
        print("Sentence level annotation")
        an_s()
        output()
    if a == "B":
        print("Word and sentence level annotation")
        an_word()
        an_s()
        output()
    else:
        print("No annotation")
        output()
'''