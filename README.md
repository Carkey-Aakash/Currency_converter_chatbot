# 💱 Currency Converter Chatbot

An intelligent **Currency Converter Chatbot** built using **Dialogflow, Python Flask, and ExchangeRate-API**. The chatbot understands natural language, extracts currency and amount information, performs real-time currency conversion, and responds conversationally to users.

The chatbot is not limited to currency conversion. It can also handle common conversational questions and interactions such as greetings, help, appreciation, compliments, and questions about the chatbot itself.

The chatbot is also integrated with **Telegram**, allowing users to access the same conversational experience through a messaging platform.

---
## 🎥 Project Demos

Here are short demo videos showing how the Currency Converter Chatbot works on different platforms.

### 🌐 Web Demo

A demonstration of the chatbot running through the **Dialogflow Web Demo**, including currency conversion and conversational interactions.

▶️ **[Watch Web Demo Video](https://github.com/user-attachments/assets/e76a4e66-d256-4223-acaa-60e8d703fdc9)**

### 📱 Telegram Demo

A demonstration of the same chatbot integrated with **Telegram**, showing currency conversion and conversational interactions.

▶️ **[Watch Telegram Demo Video](https://github.com/user-attachments/assets/d28137f0-348f-416e-bd6e-73136e73007f)**

🤖 **Telegram Bot:** The chatbot is also available on Telegram.

**Bot Username:** `@Akash_karki_bot`

---

##  Features

### 💱 Currency Conversion

Users can convert different currencies using natural language.

Examples:

```text
Convert 100 USD to NPR
Convert 50 CAD to AUD
Convert 1000 INR to NPR
How much is 20 USD in EUR?
Convert 500 Nepalese rupees to Indian rupees
```

The chatbot identifies the:

* Amount
* Source currency
* Target currency

and returns the converted amount using the ExchangeRate-API.

### Conversational Features

The chatbot can also respond to common conversations, including:

* Greetings
* Help
* Thank you
* Well done / appreciation
* Who are you?
* Who made you?
* Who is your boss?
* Can you get smarter?
* you're beautiful. I love you.
* Goodbye
* Other common conversational messages

This makes the chatbot more interactive instead of functioning only as a currency conversion tool.

---

# Dialogflow Integration

**Dialogflow** is used as the Natural Language Processing (NLP) layer of the chatbot.

It understands the user's message and determines what the user wants to do.

### Intents

Different **intents** are created to handle different types of conversations.

Examples include:

```text
Currency Conversion
Greeting
Help
Thank You
Well Done
Who Are You
Who Made You
Who Is Your Boss
Are You Smarter
Are You Beautiful
Goodbye
Fallback
```

Each intent contains training phrases that help Dialogflow recognize different ways users may express the same request.

For example:

```text
Convert 100 USD to NPR
100 dollars in Nepali rupees
How much is 100 USD in NPR?
Convert 100 American dollars into NPR
```

These different phrases can be mapped to the currency conversion intent.

---

# 🏷️ Dialogflow Entities

Entities are used to extract important information from the user's message.

For currency conversion, the chatbot uses entities for information such as:

### Amount & Source Currency

The chatbot extracts the amount and source currency from the user's request.

Example:

```text
Convert 100 USD to NPR
```

Dialogflow extracts:

```text
Amount: 100
Source Currency: USD
Target Currency: NPR
```

### Currency Entity

Currency names and their synonyms can be configured so that users can use different expressions.

For example:

```text
NPR
Nepali rupee
Nepalese rupee
Nepali rupees
Nepalese rupees
```

Similarly, currencies such as USD, INR, EUR, CAD, AUD and others can be recognized using their common names and synonyms.

---

# 🔗 Dialogflow Fulfillment & Flask Webhook

For currency conversion, Dialogflow sends the extracted information to a **Flask webhook**.

The overall flow is:

```text
User
  │
  ▼
Dialogflow
  │
  ├── Detect Intent
  │
  ├── Extract Entities
  │
  ▼
Flask Webhook
  │
  ▼
ExchangeRate-API
  │
  ▼
Converted Amount
  │
  ▼
Flask Response
  │
  ▼
Dialogflow
  │
  ▼
User
```

The Flask application receives the request from Dialogflow, extracts the currency information, sends the conversion request to ExchangeRate-API, and returns the result to Dialogflow.

---

# ⚙️ Backend – Flask

Python **Flask** is used to create the webhook server.

The Flask application:

1. Receives the request from Dialogflow.
2. Extracts the source currency.
3. Extracts the amount.
4. Extracts the target currency.
5. Sends the request to ExchangeRate-API.
6. Receives the converted amount.
7. Creates a response.
8. Sends the response back to Dialogflow.

Example:

```text
Input:
Convert 100 USD to NPR

Extracted:
Source = USD
Amount = 100
Target = NPR

API Result:
Converted amount

Chatbot Response:
100.0 USD is 15291.61 NPR
```

---

# 🌐 ExchangeRate-API Integration

The chatbot uses **ExchangeRate-API** to obtain currency conversion results.

Instead of manually maintaining exchange rates, the Flask backend sends the source currency, target currency, and amount to the API.

Example API request concept:

```text
Source Currency → USD
Target Currency → NPR
Amount → 100
```

The API returns the conversion result, which is then sent back to the user through Dialogflow.

---

# 📱 Telegram Integration

The chatbot is also integrated with **Telegram**.

This allows users to interact with the Currency Converter Chatbot through Telegram instead of only using the Dialogflow interface.

Example:

```text
User:
Convert 50 CAD to AUD

Bot:
50.0 CAD is 50.23 AUD
```

The Telegram integration demonstrates how the chatbot can be connected to an external messaging platform.

---

# 🌍 ngrok Integration

During local development, **ngrok** is used to expose the Flask server to the internet.

Since the Flask application runs locally, Dialogflow cannot directly access:

```text
http://127.0.0.1:5000
```

ngrok creates a temporary public URL that forwards requests to the local Flask server.

Architecture:

```text
Dialogflow
     │
     ▼
 Public ngrok URL
     │
     ▼
Local Flask Server
     │
     ▼
ExchangeRate-API
```

This allows Dialogflow to communicate with the locally running Flask webhook during development and testing.

---


