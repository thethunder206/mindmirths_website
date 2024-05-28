import re
import random

response = {
    "hello": ["Hello, how have you been?", "Hello! How are you?"],
    "i'm (.*)": ["Why are you {}?", "How long have you been {}?"],
    "i (.*) myself": ["Why do you {} yourself?", "What makes you think you {} yourself?"],
    "(.*) sorry (.*)": ["There's no need to apologize.", "What are you apologizing for?"],
    "(.*) friend (.*)": ["Tell me more about your friend.", "How do your friends make you feel?"],
    "(.*) kill (.*)": ["If you are facing suicidal thoughts know that you are not alone, contact this help line immediatly: 1-767. Please immediatly contact our mental health specialist for free in the top panel", "Try to think about good things in your life, contact the mental health specialist for free in the top panel"],
    # "i feel (.*)": ["Why do you feel {}?", "How long have you been feeling {}?"],
    "i am (.*)": ["Why do you say you're {}?", "How long have you been {}?"],
    "yes": ["You seem quite sure.", "Ok, but can you elaborate."],
    "no": ["Why not?", "Ok, but can you elaborate a bit?"],
    " (.*) ": ["Please tell me more.", "Can you elaborate on that?"],
    "": ["Why do you think that?", "Please tell me more."]
}

with open('negative_words.txt', "r") as word_list:
    negative_words = word_list.read().split('\n')

with open('positive_words.txt', "r") as word_list:
    positive_words = word_list.read().split('\n')

print(negative_words)
print(positive_words)

negative_counter = 0
def match_response(input_text):
    global negative_counter
    user_input_split = user_input.split(' ')
    for i in user_input_split:
        if 'depres' in i:
            depression_list =["Everyone comes to this stage at a point in their life, please contact a mental health specialist for free in the top panel", "Contact our mental health specialist in the top panel for free"]
            return depression_list[random.choice([0, 1])]
        elif 'anxi' in i:
            depression_list =["Everyone comes to this stage at a point in their life, please contact a mental health specialist for free in the top panel", "Contact our mental health specialist in the top panel for free"]
            return depression_list[random.choice([0, 1])]
        elif i in positive_words:
            return f"Intriguing! Please tell me why you feel {i}"
        elif i in negative_words:
            negative_counter += 1
            print(negative_counter)
            negative_words_response = [f"I'm sorry you feel this way! Please tell me why you feel {i}", f"Everyone feels {i} at a point in their life and it is important to reach out when needed", "It will get better, don't give up"]
            if negative_counter <2:
                return negative_words_response[random.choice([0, 1, 2])]
            else:
                return "I recommend you do contact the mental health specialist for free in the top panel"

    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text.lower())

        if matches:
            chosen_response = response_list[random.choice([1, 0])]
            return chosen_response.format(*matches.groups())
    # return "I'm sorry I don't understand what you're saying."

# def match_response(input_text):
#     for pattern, response_list in response.items():
#         matches = re.match(pattern, input_text.lower())
#         for i in user_input:
#             if i in positive_words:
#                 return f"Intriguing! Please tell me why you feel {i}"
#             elif i in negative_words:
#                 return f"I'm sorry you feel this way! Please tell me why you feel {i}"
#             break
#
#         if matches:
#             chosen_response = random.choice(response_list)
#             return chosen_response.format(*matches.groups())
#     return "I'm sorry I don't understand what you're saying."

print("Welcome to the Mental Health Chat Bot")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print ("Mental Health Chat Bot: Goodbye.")
        break
    else:
        print("Mental Health Chat Bot: "+match_response(user_input))
