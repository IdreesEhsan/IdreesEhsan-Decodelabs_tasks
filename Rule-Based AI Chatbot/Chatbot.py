# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training | Batch 2026
# ============================================

# KNOWLEDGE BASE

response = {
    "hello":        "Hi there! How can I help you today?",
    "hi":           "Hey! Great to see you.",
    "how are you":  "I'm just a bot, but I'm running perfectly!",
    "what is ai":   "AI is the simulation of human intelligence by machines.",
    "your name":    "I'm DecoBot, your rule-based assistant!",
    "help":         "I can answer questions about AI. Try asking 'what is ai'."
}

print("Bot: Hello! I'm DecoBot. Type 'exit' to quit.\n")

# INPUT LOOP — The heartbeat
while True:

    # PHASE 1: Input & Sanitization
    raw_input_text = input("You: ")
    clean_input_text = raw_input_text.lower().strip()

    # EXIT STRATEGY — Clean break command
    if clean_input_text == "exit" or clean_input_text == 'bye':
        print("Bot: Session terminated. GoodBye!")
        break

    # PHASE 2 & 3: Process + Generate Response
    reply = response.get(clean_input_text, "I do not understand. Could you rephrase?")
    print("Bot: ", reply)