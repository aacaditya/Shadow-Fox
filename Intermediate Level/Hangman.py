#Hangman: Implement the wordguessing game with visual progress and hints.
#Here , I have used a list of country names that player has to guess in 7 attempts.
import random
countries = ["argentina", "brazil", "colombia", "denmark", "finland", "hungary", "iceland", "jamaica", "kazakhstan", "lebanon","malaysia", "mongolia", "morocco", "netherlands", "portugal","senegal", "slovakia", "tanzania", "uzbekistan", "zimbabwe"
]

target = random.choice(countries).upper()  #selects a random country from list and converts it into uppercase.


hidden_word = ["_"] * len(target)

print("Secret Country selected : "," ".join(hidden_word)) #prints underscores for no. of alphabets in the selected country.
count = 7
value = False

while count>0:
    print("Guess a letter ", count, " chances remaining.")
    guess = input("Guess a letter : ")
    guess = guess.upper()
    
    if len(guess) == 1 and guess.isalpha() :
       a =1
    else :
        print("Invalid guess! Please enter a single letter.")
        continue
    
    if guess in target : 
        print("Nice guess! You found a new letter! ")
        for i in range(len(target)):
            if target[i]==guess:
                hidden_word[i]=guess
       
    else : 
        count = count - 1
        print("Wrong guess!",count," chances remaining.")
    
    print("Word Progress : "," ".join(hidden_word))

    if "_" not in hidden_word:
        print("Congratulations ! You guessed the country : ",target)
        value = True
        break

if value == False:
   print("GAME OVER ! The correct country was : ", target)
