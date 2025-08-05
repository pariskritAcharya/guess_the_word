import random



arr=[
"apple",
"banana",
"orange",
"strawberry",
"grape",
"watermelon",
"pineapple",
"mango",
"kiwi",
"blueberry",
"raspberry",
"blackberry",
"peach",
"pear",
"plum",
"lemon",
"lime",
"coconut",
"avocado",
"apricot",
"cherry",
"pomegranate",
"fig",
"guava",
"lychee",
"papaya",
"dragonfruit",
"passionfruit",
"tangerine",
"cranberry",
"acorn",
"bacon",
"cabbage",
"daffodil",
"eagle",
"feather",
"garden",
"hammer",
"igloo",
"jungle",
"kettle",
"ladder",
"mountain",
"notebook",
"octopus",
"pillow",
"quiver",
"rainbow",
"saddle",
"table",
"umbrella",
"volcano",
"whisper",
"xylophone",
"yacht",
"zipper",
"airplane",
"bicycle",
"computer",
"diamond",
"elephant",
"fountain",
"guitar",
"helicopter",
"island",
"jigsaw",
"keyboard",
"lantern",
"microscope",
"necklace",
"ostrich",
"penguin",
"quicksand",
"rocket",
"sandwich",
"telescope",
"unicorn",
"vegetable",
"waterfall",
"xylitol",
"yellow",
"zebra",
"astronaut",
"butterfly",
"chocolate",
"dinosaur",
"escalator",
"firefly",
"galaxy",
"hamburger",
"instrument",
"jackal",
"kangaroo",
"labyrinth",
"magazine",
"nightingale",
"oxygen",
"pyramid",
"quadrilateral",
"rhombus",
"supermarket",
"television",
"university",
"vacation",
"waffle",
"xmas",
"yogurt",
"zookeeper"
]




def hide_word(word):
    hidden_word ="#"*len(word)
    hidden_word= list(hidden_word)
    word_list=list(word)
    i=int(len(word)/3)
    for x in range(i):
        rand=random.randrange(0,len(word))
        hidden_word[rand]=word_list[rand]
    return "".join(hidden_word)



def check_word(word,hidden_word,user):
    if len(user)==len(word):
        if user == word:
            print(word," won")
            return word
        word_C=list(word)
        hidden_word_C=list(hidden_word)
        user_C=list(user)
        for i in range(len(word)):
            if user_C[i]==word_C[i]:
                hidden_word_C[i]=word_C[i]
        print("".join(hidden_word_C))
        return "".join(hidden_word_C)
    else:
        print("type again\n",hidden_word)
        return hidden_word


while True:
    word=arr[random.randrange(0,len(arr))]
    hang_man_word=hide_word(word)
    print(hang_man_word)
    i=0
    while True:
        if hang_man_word== word:
            break
        print(i+1)
        i+=1
        user = input("")
        hang_man_word=check_word(word,hang_man_word,user)

