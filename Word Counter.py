from collections import Counter
import string
import heapq

def word_count():

    print("Welcome to my Word-Counter-Programm! :)\n")
    print("Give me proper sentence!\n")

    text = str(input(""))

    text = text.lower()

    for i in string.punctuation:
        text = text.replace(i, '')

    word_list = text.split()

    sum_word = 0

    for i in word_list:
        sum_word += 1

    print(f"Thats the total sum of all word: {sum_word}\n")

    often = Counter(word_list)

    print(f"Thats how often all words appear: {often}\n")

    top3 = heapq.nlargest(3, often.items(), key=lambda x: x[1])

    print(f"This are the Top3 Word: {top3}\n")

if __name__ == "__main__":
  word_count()

while True:
    try:
        again = str(input("Wanna do it again? j/n\n"))
        again = again.lower()

        if again == "j":
            word_count()
        elif again == "n":
            break
        else:
            print("Yes = j, No = n\n")

    except ValueError:
        print("Wanna do it again? j/n\n")



