# CodeAlpha Task 4 - Basic Chatbot

def chatbot_response(message):

    if message == "hello":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I am a simple Python chatbot."

    elif message == "what can you do":
        return "I can respond to some basic messages."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# Welcome message
print("===================================")
print("        BASIC PYTHON CHATBOT")
print("===================================")
print("Type 'bye' to end the conversation.")


# Main chatbot loop
while True:

    # Get message from the user
    user_message = input("\nYou: ").lower()

    # Get chatbot response
    response = chatbot_response(user_message)

    # Display chatbot response
    print("Bot:", response)

    # End the conversation when the user says bye
    if user_message == "bye":
        break