#project config

import google.generativeai as genai
genai.configure(api_key="AIzaSyDtQHc641-FyQG7UySP9BVdIMqUD46NCXI")
apple = genai.GenerativeModel("gemini-2.5-flash")
chat = apple.start_chat(history=[])
print("hi !! I'm Apple the chat-bot")
while True:
    user_input = input("user : ")
    if user_input.lower()=="bye":
        break
    response = chat.send_message(user_input)
    print("Apple :",response.text)
    
