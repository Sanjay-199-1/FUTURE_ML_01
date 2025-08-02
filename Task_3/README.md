# 🤖 Task 3 – Customer Support Chatbot using Dialogflow

As part of my internship at **FUTUREINTERNS** as a Machine Learning Intern, I built a **24/7 AI-powered chatbot** using **Dialogflow**, mimicking real-world use cases like Amazon, Flipkart, and Zomato customer support.

---

## 🎯 Objective

To develop a virtual assistant that can:
- Answer FAQs like "Where is my order?"
- Handle return and refund queries
- Be integrated into websites or messaging platforms
- Simulate real-world customer support

---

## 🧠 Skills Learned

- 🤖 How Dialogflow intents and NLP mapping work
- 💬 Designing real-world conversation flows
- 🌐 Connecting chatbot to backend via Flask webhook
- ⚙️ Using ngrok for local testing
- 📦 Preparing project for GitHub deployment

---


---

## 🔧 Technologies Used

- **Dialogflow ES** – For building the chatbot
- **Python + Flask** – Webhook for dynamic replies
- **ngrok** – Expose local Flask app to Dialogflow
- **GitHub** – For version control and sharing
- **Linux** – Development on Ubuntu

---

## 💬 Sample Intents

| Intent        | Example User Query      | Bot Response |
|---------------|-------------------------|--------------|
| `greeting`     | "Hi", "Hello"            | Hello! How can I help you today? |
| `order_status` | "Where is my order?"     | Your order is in transit... |
| `return_policy`| "How to return a product?" | You can return your item within 7 days... |

---

## ⚙️ How to Run the Webhook Locally

```bash
# Navigate to webhook directory
cd Task_3/webhook

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py


