print("bot:hello this your chatbot here")
while True:
    user=input("you:").lower()
    if "hi" in user or "hello" in user:
        print("bot: hello ")
    elif "name" in  user:
        print("bot: iam bot")
    elif "bye" in user:
        print("bot:bye")
        break
    else:
        print("i can't understand")        