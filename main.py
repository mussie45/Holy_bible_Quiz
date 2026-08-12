import json
import random
with open("kjv_bible_dataset.json", "r") as f:
    bible = json.load(f)
with open("bible_quiz.json", "r") as f:
    bible_que = json.load(f)


def welcome_message():
    print("\n" + "=" * 50)
    print("📖✨ WELCOME TO THE HOLY BIBLE QUIZ ✨📖")
    print("=" * 50)
    print("Test your Bible knowledge and learn more about God's Word! 🙏")
    print("Good luck and have fun! 😇")
    print("=" * 50)


def about_rules():
    print("\n" + "=" * 50)
    print("📜 BIBLE QUIZ RULES")
    print("=" * 50)
    print(""" 
1️⃣ Choose the type of quiz you want to play. 

2️⃣ Choose by Verse: 
• You will be shown a Bible verse. 
• You must choose the correct Bible reference. 
• You can choose from the New Testament, Old Testament, or both. 

3️⃣ General Questions: 
• You will be given a Bible-related question. 
• Choose the correct answer from A, B, C, or D. 
• There are three difficulty levels: 
    🟢 Easy 
    🟡 Medium 
    🔴 Hard 

4️⃣ Every correct answer gives you 1 point. 

✅5️⃣ Wrong answers do not give you a point. 

❌6️⃣ Try your best and use the quiz to improve your Bible knowledge.

 📖7️⃣ Most importantly: Learn, have fun, and read the Bible! 🙏❤️ """)
    print("=" * 50)


def q_difficulty(difficulty_leve):
    if difficulty_leve == 1:
        return bible_que["easy_questions"]
    elif difficulty_leve == 2:
        return bible_que["medium_questions"]
    else:
        return bible_que["hard_questions"]


def o_questions(difficulty_le):
    QUESTIONS_TO_PLAY = 10
    score = 0
    diff = q_difficulty(difficulty_le)
    selected_questions = random.sample(diff, QUESTIONS_TO_PLAY)
    for idx, item in enumerate(selected_questions, 1):
        print(f"\n {idx}.{item['question']}")
        for letter, text in item["options"].items():
            print(f"{letter} {text}")
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if user_answer == item['correct_option']:
            print("✅ Correct! Good job! 🎉")
            score += 1
        else:
            print("❌ Incorrect. Go and read your Bible! 📖")
            print(f"The answer was {item["correct_option"]}")
    if score < 10:
        print(f"You got {score}/{QUESTIONS_TO_PLAY}")
        print("Read your bible to improve your mark and knowledge😉")
    else:
        print(f"You got {score}/{QUESTIONS_TO_PLAY}")
        print("That means your knowledge isn't enough🫡")


def v_difficulty(difficulty):
    if difficulty == 1:
        return bible[1]
    elif difficulty == 2:
        return bible[0]
    else:
        return random.choice([bible[0], bible[1]])


def questions(Num_of_questions, difficulty_level):
    correct_answers = Num_of_questions
    for i in range(Num_of_questions):
        testament = v_difficulty(difficulty_level)
        verse = random.choice(list(testament.keys()))
        list_of_ans = [random.choice(list(testament.keys())), random.choice(list(testament.keys())),
                       random.choice(list(testament.keys())), verse]
        A = random.choice(list_of_ans)
        list_of_ans.remove(A)
        B = random.choice(list_of_ans)
        list_of_ans.remove(B)
        C = random.choice(list_of_ans)
        list_of_ans.remove(C)
        D = random.choice(list_of_ans)
        list_of_ans.remove(D)
        print(
            f"""{i + 1}. {testament[verse]}?
            A. {A}            B. {B}
            C. {C}            D. {D}
    \n""")
        Answer = input("Choose (A/B/C/D): ").lower()
        if Answer == "a" and A == verse:
            print("✅ You are correct! 🎉\n")
        elif Answer== "b" and B == verse:
            print("✅ You are correct! 🎉\n")
        elif Answer == "c" and C == verse:
            print("✅ You are correct! 🎉\n")
        elif Answer == "d" and D == verse:
            print("✅ You are correct! 🎉\n")
        else:
            print("❌ You are wrong.\n")
            correct_answers -= 1
            print(f"The answer was {verse}\n")
    print(f"You got {correct_answers}/{Num_of_questions}")


def main():
    while True:
        kinds = int(input("What kind of Quiz did u want to take\n1. Choose by verse\n2. General question\n3. About the rules\n4. Exit\nChoose(1/2/3/4): "))
        if kinds == 1:
            Numb_of_questions = int(input("How many questions you want to be asked: "))
            diffi = int(input("Do you want to test your knowledge on both of the books(the new and old testament) or in just one of them?\n1. New testament only\n2. Old testament only\n3. From both of the books\nChoose (1/2/3): "))
            questions(Numb_of_questions, diffi)
        elif kinds == 2:
            diffi = int(input("What kind of questions you want to be ask?\n1. easy\n2. medium\n3. hard\nChoose (1/2/3): "))
            o_questions(diffi)
        elif kinds == 3:
            about_rules()
        else:
            print("\n🙏 Thank you for playing!")
            print("📖 Keep reading the Bible and keep learning! ❤️")
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    welcome_message()
    main()
