from chatbot import TripAdvisor

def start_chat():
    bot = TripAdvisor()

    print("---Chat started----")
    print("---to end chat write 'exit'---")

    while True:
        user_input = input("You:")

        if user_input == "exit":
            print("Au revoir, have a nice trip!")
            print(bot.print_conversation_cost())
            break

        bot_answer = bot.response(user_input)
        print((f"TripAdvisorBot: {bot_answer}"))

if __name__ == "__main__":
    start_chat()

