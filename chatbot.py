from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of ChatBot
chatbot = ChatBot(
    'CustomBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'  # Using SQLite as backend
)

trainer = ListTrainer(chatbot)

# Train the bot with custom data
trainer.train([
    "Hi",
    "Hello, how can I assist you?",
    "How are you?",
    "I'm doing well, thank you for asking!",
    "Goodbye",
    "See you later!"
])

def chat():
    print("Hello! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("Bot:", response)

if __name__ == '__main__':
    chat()