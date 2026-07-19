print("Nameste! Welcome to your ChatBot. How can I assist you today?")
print("You can ask me anything or type 'exit' to end the conversation.")

#ChatBot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, Welcome, How can I help you today?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Believe in yourself! You can achieve anything you set your mind to.",
    "happy": "Happiness is a journey, not a destination. Find joy in the little things.",
    "sad": "It's okay to feel sad sometimes. Remember, after the rain comes the rainbow."
}  

#Method/Function to get response of chatbot

def getResponseofBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am not able to answer that question. Please ask something else."


#Take user input
while True:

    userQuestion = input("You: ")
    if userQuestion.lower() == "exit":
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = getResponseofBot(userQuestion)
    print("ChatBot:", response)