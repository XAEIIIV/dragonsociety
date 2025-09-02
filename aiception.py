import json
import os

# 📂 Load memory from file or start fresh
def load_memory(filename="chat_memory.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

# 💾 Save memory to file
def save_memory(memory, filename="chat_memory.json"):
    with open(filename, "w") as f:
        json.dump(memory, f, indent=4)

# 🧠 Chatbot logic with learning
def chatbot_response(user_input, memory):
    user_input = user_input.lower().strip()

    if user_input in memory:
        return memory[user_input]
    else:
        print("Bot: I don't know how to respond to that. What should I say?")
        new_response = input("You: ").strip()
        memory[user_input] = new_response
        save_memory(memory)
        return "Got it! I'll remember that."

# 💬 Main chat loop
def chat():
    memory = load_memory()
    print("Bot: Hello! I'm your learning chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Bot: Goodbye!")
            break
        response = chatbot_response(user_input, memory)
        print("Bot:", response)

# 🚀 Start the chatbot
if __name__ == "__main__":
    chat()