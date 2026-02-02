# NLP Chatbot with Spell Checking!

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

# Initialize the stemmer
stemmer = PorterStemmer()

# Enhanced knowledge base
knowledge_base = {
    'hours': {
        'keywords': ['hour', 'open', 'close', 'time', 'schedule'],
        'response': "We're open Monday to Friday, 9 AM to 5 PM. Closed on weekends."
    },
    'return': {
        'keywords': ['return', 'refund', 'money', 'back', 'exchange'],
        'response': "You can return any item within 30 days of purchase with a receipt. Refunds take 5-7 business days."
    },
    'contact': {
        'keywords': ['contact', 'email', 'phone', 'call', 'reach'],
        'response': "You can reach us at support@example.com or call 1-800-HELP-NOW."
    },
    'order': {
        'keywords': ['order', 'track', 'status', 'package'],
        'response': "To check your order status, please provide your order number. (This is a demo, so I can't actually check!)"
    },
    'shipping': {
        'keywords': ['ship', 'deliver', 'send'],
        'response': "Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days."
    }
}

def get_word_stems(text):
    """Takes a sentence and returns a list of stemmed words."""
    words = word_tokenize(text.lower())
    stems = [stemmer.stem(word) for word in words]
    return stems

def check_match(user_stems, keywords, threshold=70):
    """
    Check if any keyword matches any user input stem.
    Now uses fuzzy matching to handle typos!
    threshold: How similar words need to be (0-100, higher = more strict)
    """
    keyword_stems = [stemmer.stem(keyword) for keyword in keywords]

    for user_stem in user_stems:
        for keyword_stem in keyword_stems:
            # Calculate similarity score (0-100)
            similarity = fuzz.ratio(user_stem, keyword_stem)

            # If similar enough, it's a match!
            if similarity >= threshold:
                return True

    return False

# Main chatbot
print("Chatbot: Hello! I'm your advanced NLP customer service assistant.")
print("Chatbot: I can understand word variations AND handle typos!")
print("Chatbot: I can help with: hours, returns, contact info, orders, and shipping.")
print("Chatbot: Type 'quit' to exit.")
print()

greeting_words = ['hello', 'hi there', 'hey', 'good morning', 'good afternoon']

while True:
    user_input = input("You: ")
    user_input_lower = user_input.lower()

    # Check if user wants to quit
    if user_input_lower == 'quit':
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Check if user is greeting us
    is_greeting = False
    for greeting in greeting_words:
        if user_input_lower == greeting or user_input_lower.startswith(greeting + ' '):
            is_greeting = True
            break

    if is_greeting:
        print("Chatbot: Hello! How can I help you today?")
        print()
        continue

    # Get stems of user input
    user_stems = get_word_stems(user_input)

    # Check our knowledge base using NLP + fuzzy matching
    found_answer = False

    for topic, info in knowledge_base.items():
        if check_match(user_stems, info['keywords'], threshold=70):
            print(f"Chatbot: {info['response']}")
            found_answer = True
            break

    if not found_answer:
        print("Chatbot: I'm not sure about that. I can help with hours, returns, contact info, orders, and shipping.")

    print()
