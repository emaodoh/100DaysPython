
import random

def game():
    lists =  [{"What is the capital city of France? \n A Paris\n B london\n C lagos\n D moscow": "A","How many planets are in our solar system? \n A 7\n B 8\n C 9\n D 10": "B","What is the largest ocean on Earth? \n A Atlantic\n B Indian\n C Pacific\n D Arctic": "C","Which element has the chemical symbol 'O'? \n A Osmium\n B Gold\n C Helium\n D Oxygen": "D","What year did the Titanic sink? \n A 1905\n B 1912\n C 1920\n D 1935": "B"}]
    random.shuffle(lists)
    while True:
        score = 0
        
        for question in lists:
            for key,value in question.items():
                    print(key)
                    answer = input("Enter your answer:  ").strip().upper()
                    if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                        if answer == value:
                            score +=1
                    else:
                        print("select from A to D")
                        break
        print (f"you scored {score}\n")
        if score >= 3:
            print("pass")
        else:
            print("fail")
        prompt = input("do you want to try again y/n:  ")
        if prompt == "y":
            continue
        else:
            break

    return "goodbye"

result = game()

print(result)