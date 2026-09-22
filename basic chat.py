
def chartbot():
   print(" basic chatbot")
   print("type 'bye' to exit")


   while True:
        user=input("you: ").lower()

        if  user in ["hello" ,"hi" ,"hey"]:
            print("bot: hi!")

        elif user=="what is your name":
             print("bot: My name is basic chatbot !")

        elif user=="how are you":
             print("bot: i'm fine. thanks!")

        elif user=="bye":
             print("bot: Goodbye!")
             break

        else:
                 print(" bot: sorry,i don't understand.")
chartbot()