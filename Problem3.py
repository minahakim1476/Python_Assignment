import random
lives = 5
words = ["frontend" , "backend" , "github" , "python"]
while lives > 0:
    word = random.choice(words)
    Scrambled_word = ''.join(random.sample(word , len(word)))
    print("Scarmbled word: " , Scrambled_word)
    guess = input("enter your guess: ")
    if guess == word:
        print("congrats you won!")
        break
    else:
        lives -= 1
        print("try again, you lives " , lives ," left")