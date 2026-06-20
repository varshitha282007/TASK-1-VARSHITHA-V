

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey! How can I help you?",
    "how are you": "I am doing well. Thanks for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "help": "You can greet me, ask my nameor ask how I am doing .",
    "thanks": "You're welcome!",
    "thank you": "Glad to help!",
    "bye": "Goodbye!"
}

print(" AI Chatbot Started ")
print("Type 'exit' to quit.\n")

while True:

  
    raw_input_text = input("You: ")
    clean_input = raw_input_text.lower().strip()

    
    if clean_input == "exit":
        print("Bot: Goodbye!")
        break

    # Knowledge Base + Fallback
    reply = responses.get(
        clean_input,
        "I do not understand. Please try another question."
    )

    print("Bot:", reply)