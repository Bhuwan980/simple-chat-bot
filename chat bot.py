# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:46:31 2021

@author: victor
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# making the chatbot object

chatbot = ChatBot("Bhuwan's ChatBot")

conversation = ["what is your name",
                "my name is bhu-bot.",
                "how old are you",
                "I don't have age",
                "where do you live", 
                "i live in our computer!!!!",
                "who is your creator",
                "Bhuwan Bahadur Neupane. Who is the future ML Engineer.",                
                "what can you do for me",
                "I can recommend you some moveis.",
                "hello",
                "Hi there!",
                "how are you doing",
                "I'm doing great.",
                "that is good to hear",
                "Thank you.",
                "You're welcome.",
                "hi",
                "Hey, What's up?",
                "good",
                "nice to hear that"
]
# making the trainer with the help of listtrainer

trainer = ListTrainer(chatbot)

##trainig the conversation
trainer.train(conversation)
while True:
    
    
    query = input('ask me anything: ')
    if query=='e':
        break
    response = chatbot.get_response(query)
    print("you: ", query)
    print('bot: ',response)