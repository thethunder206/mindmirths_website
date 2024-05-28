# import openai
#
# openai.api_key = "sk-proj-UTodP9BENqHzP8FPBV9sT3BlbkFJoFtQnuImVUi0V1LcEAAF"
#
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "I feel paranoid"}])
# print(completion.choices[0].message.content)

# A helpful and encouraging mental health therapist that can make the user feel better about themselves and encourage to seek help through the top right panel on this website

import openai

openai.api_key = "sk-proj-UTodP9BENqHzP8FPBV9sT3BlbkFJoFtQnuImVUi0V1LcEAAF"

gpt_list = []
gpt_list.append({"role": "system", "content": "You are a therapist that only advises patients to get a free therapist via the top panel"})

print("Mental Health Chatbot: Hi, I am a Mental Health Chat Bot! How are you?")

while input != "quit()":
    message = input("User: ")
    gpt_list.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=gpt_list)
    reply = response["choices"][0]["message"]["content"]
    gpt_list.append({"role": "assistant", "content": reply})
    print("\n" + "Mental Health Chatbot: " + reply + "\n")
