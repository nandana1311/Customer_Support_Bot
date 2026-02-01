# 🤖 NLP Customer Service Chatbot with Spell Checking

A beginner-friendly **NLP-based customer service chatbot** built using **Python, Streamlit, NLTK, and Fuzzy Matching**.  
This project demonstrates how simple Natural Language Processing techniques such as **tokenization, stemming, and fuzzy keyword matching** can be used to build an intelligent rule-based chatbot.

The chatbot can answer common customer service questions about:
- Business hours  
- Returns & refunds  
- Contact information  
- Order status  
- Shipping details  

This project is designed mainly for **learning purposes**, focusing on understanding how chatbots work internally rather than relying on heavy AI models.

---

## 🚀 Features

- Terminal-style chat UI using **Streamlit**
- Rule-based knowledge base
- NLP preprocessing using **NLTK**
- Word stemming with **Porter Stemmer**
- **Fuzzy matching** for handling spelling mistakes
- Greeting detection
- Polite fallback responses

---

## 🛠 Technologies Used

- Python 3.8+
- Streamlit
- NLTK (Natural Language Toolkit)
- FuzzyWuzzy

---

## 📂 Project Structure

```
chatbot.py
README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/nlp-customer-service-chatbot.git
cd nlp-customer-service-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```
pip install streamlit nltk fuzzywuzzy python-Levenshtein
```

### 4. Run the Application

```
streamlit run chatbot.py
```

---

## 💬 How It Works

1. User types a message.
2. Input is converted to lowercase.
3. Sentence is tokenized into words.
4. Words are stemmed using Porter Stemmer.
5. Each stem is compared with stored keyword stems.
6. Fuzzy matching allows small spelling mistakes.
7. Best matching topic response is returned.

---

## 🧠 Example Questions

```
What time do you open?
How can I return a product?
Track my order
Give me your phone number
How long does shipping take?
```

---

## 🖼 Sample Output

```
Hello! How can I help you today?
User: What time do you open?
Bot: We're open Monday to Friday, 9 AM to 5 PM. Closed on weekends.
```

---

## 🔧 Customization

You can easily add new topics inside the `knowledge_base` dictionary:

```python
'payment': {
   'keywords': ['pay', 'payment', 'card'],
   'response': 'We accept credit cards, debit cards, and UPI.'
}
```

---

## 📚 Learning Outcomes

- Understand rule-based chatbots
- Learn NLP basics (tokenization, stemming)
- Handle user spelling mistakes
- Build interactive apps using Streamlit

---

## 🌱 Future Improvements

- Store conversations in database
- Add TF-IDF based matching
- Add simple ML classifier
- Deploy online
- Add voice input/output

---

## 👤 Author

Nandana S Nair

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

⭐ If you like this project, consider giving it a star on GitHub!

