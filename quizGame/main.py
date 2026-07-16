
import random

def game():
    questionBank =  [  
        {"question": "What is the capital city of France? ",
        "answer": "A","option":"\n A Paris\n B london\n C lagos\n D moscow",
        },
        {"question":"How many planets are in our solar system? ",
         "answer": "B",
         "option": "\n A 7\n B 8\n C 9\n D 10"},
         {"question":"What is the largest ocean on Earth? ",
         "answer": "C",
         "option":"\n A Atlantic\n B Indian\n C Pacific\n D Arctic"},
         {"question":"Which element has the chemical symbol 'O'? ",
         "answer": "D",
         "option":"\n A Osmium\n B Gold\n C Helium\n D Oxygen"},
         {"question": "What year did the Titanic sink? ",
         "answer": "B",
         "option": "\n A 1905\n B 1912\n C 1920\n D 1935"}
         ]
    while True:
        random.shuffle(questionBank)
        score = 0
        
        for question in questionBank:
            print(question["question"])
            print(question["option"])
            while True:
                answer = input("Enter your answer:  ").strip().upper()
                if answer in ("A","B","C","D"):
                    if answer == question["answer"]:
                        print("\033[32m correct!\033[0m")
                        score +=1
                        break
                    else:
                        print(f"\n\033[31mwrong!\033[0m\n correct answer:{question['answer']}\n")
                        break         
                else:
                    print("select from A to D")
                    continue
        percentage = (score/len(questionBank))*100
        
        if percentage == 100:
            print(f"You scored {score}/{len(questionBank)}.\nPercentage: 100%\nExcellent! 🎉")
        elif percentage >= 60:
            print(f" You scored {score}/{len(questionBank)}.\nPercentage: {percentage:.0f}%\nGood job!")
        elif percentage >= 20:
            print(f"You scored {score}/{len(questionBank)}.\nPercentage: {percentage:.0f}%\nKeep practicing.")
        else:
            print(f"\033[31mfail\033[0m\n you scored {score}\n try again. You can do better")
        prompt = input("Enter Y to try again or any other key to exit:  ").strip().lower()
        if prompt == "y":
            continue
        else:
            break

    return "goodbye"

result = game()

print(result)