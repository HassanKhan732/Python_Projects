import random

words = ["apple","banana","mango","peach","grape","orange","cherry","melon","papaya","pear","plum","kiwi","apricot","guava","fig","date","lemon","lime","coconut","berry","strawberry","raspberry","blueberry","blackberry","pineapple","watermelon","pomegranate","lychee","tangerine","cranberry","cat","dog","tiger","lion","elephant","zebra","monkey","horse","giraffe","bear","rabbit","sheep","goat","cow","buffalo","camel","fox","wolf","leopard","kangaroo","parrot","eagle","sparrow","owl","peacock","crow","hen","duck","pigeon","flamingo","car","bus","train","plane","ship","bicycle","motorcycle","truck","scooter","jeep","submarine","helicopter","tram","rocket","taxi","boat","van","cart","cruise","tractor","table","chair","lamp","mirror","window","door","sofa","bed","pillow","blanket","curtain","fan","light","bottle","plate","cup","glass","clock","drawer","shelf","computer","laptop","keyboard","mouse","screen","mobile","charger","pen","book","notebook","tablet","router","printer","camera","speaker","microphone","monitor","battery","software","network","river","mountain","forest","beach","island","desert","rain","cloud","storm","sunshine","wind","earth","tree","flower","leaf","stone","volcano","lake","waterfall","ocean","pakistan","india","china","japan","korea","nepal","iran","afghanistan","turkey","malaysia","indonesia","thailand","france","germany","spain","italy","brazil","argentina","canada","mexico","doctor","teacher","engineer","pilot","driver","nurse","farmer","chef","police","firefighter","scientist","artist","writer","singer","actor","lawyer","mechanic","architect","barber","soldier","run","walk","jump","swim","dance","sing","write","read","speak","listen","think","cook","drive","fly","draw","build","play","learn","teach","smile","happy","sad","angry","afraid","surprised","tired","excited","lonely","nervous","bored","calm","jealous","proud","relaxed","confused","worried","shy","hopeful","grateful","brave","shirt","pants","jacket","shoes","socks","cap","tie","scarf","gloves","belt","dress","skirt","coat","shorts","hoodie","uniform","sweater","boots","watch","ring","bread","butter","cheese","rice","pasta","pizza","burger","sandwich","salad","soup","egg","meat","fish","chicken","cake","cookie","chocolate","icecream","noodles","fries","garden","school","office","market","library","hospital","road","bridge","village","city","country","map","flag","tower","window","kitchen","floor","roof","wall","corner","dream","music","color","sound","shadow","mirror","smoke","fire","rainbow","snow","friend","family","child","mother","father","brother","sister","neighbor","guest","baby"]

length = len(words)
random_word_index = random.randint(0, length - 1)
word = words[random_word_index]
word_length = len(word)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
display_word = ['_'] * word_length

num_reveal = random.randint(1, min(3, word_length))
revealed_indices = random.sample(range(word_length), num_reveal)
for idx in revealed_indices:
    display_word[idx] = word[idx]
    guessed_letters.append(word[idx])

hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

print("Welcome to Hangman!")
print("The word is:", ' '.join(display_word))
print(hangman_stages[wrong_guesses])

while wrong_guesses < max_wrong_guesses and '_' in display_word:
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good guess!")
        for i in range(word_length):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")
    
    print("\nWord:", ' '.join(display_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(hangman_stages[wrong_guesses])

if '_' not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
