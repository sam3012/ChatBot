# CustomTkinter OpenAI ChatBot Desktop Application

> [!NOTE]  
> **Historical Context:**  
> This project was developed as a college project shortly after ChatGPT launched, back when OpenAI gave free trial credits per account and `text-davinci-003` was the standard model. It is a lightweight desktop wrapper built with CustomTkinter to interact directly with raw completion prompts, preserved here as an archival project from the early days of LLM APIs.

A modern desktop chatbot application built with Python, CustomTkinter, SQLite, and the OpenAI API. It features multi-user authentication, role-based access control (Admin/User), a threaded conversational UI, and a dedicated AI tuning interface to customize system prompts and bot personas dynamically.

---

## 📸 Overview & Features

- **Modern CustomTkinter GUI:** Clean and responsive desktop UI with native system theme support.
- **Role-Based Authentication:**
  - **User Portal:** Signup and login system stored securely in a local SQLite database.
  - **Admin Portal:** Dedicated administration panel to tune bot behavior and customize system prompts in real time.
- **Context-Aware AI Conversation:** Retains ongoing conversation history and dynamically injects dialogue blocks into model prompts.
- **Threaded & Resilient Chat:** Background execution for OpenAI API calls to prevent UI freezing, backed by automatic retries on network failures.
- **Customizable Personas:** Easily switch bot behavior (e.g., Customer Support, Order Assistant, Sarcastic Assistant) directly via the Admin panel.

---

## 📁 Repository Structure

```text
ChatBot-master/
├── BackEnd/
│   └── ChatBot.py          # OpenAI API integration & CLI interface
├── DB/
│   ├── ChatBot.db          # SQLite database storage
│   └── db.py               # Database management and query operations
├── chat.ico                # Desktop application icon
├── demo.txt                # Sample system contexts and bot personas
├── prompt_chat.txt         # Active system prompt and template buffer
├── Main.py                 # Primary GUI application entry point
├── Main.exe                # Pre-built Windows executable
└── README.md               # Project documentation
```

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.8+
- **GUI Framework:** CustomTkinter / Tkinter
- **AI Backend:** OpenAI API
- **Database:** SQLite3
- **Threading & Resilience:** Python `threading`, `retry`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sam3012/ChatBot.git
cd ChatBot-master
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install customtkinter openai retry
```

---

## 🖥️ Running the Application

### Launch GUI Application

```bash
python Main.py
```

### Launch CLI Mode (Terminal Only)

```bash
python BackEnd/ChatBot.py
```

---

## 🔑 Default Credentials & Usage

### 1. Admin Access
- **Username:** `admin`
- **Password:** `admin`
- **Functionality:** Access the **Tune AI** page to modify `prompt_chat.txt` and define the bot's tone, rules, and persona.

### 2. User Access
- Users can create a new account using the **Signup** button or log in with existing credentials.
- Users can chat directly with the configured AI persona in real time.

---

## 🎭 Persona / Prompt Tuning Examples

You can test different personas by inserting any of the following templates into the Admin tuning dashboard:

| Persona | Prompt Example |
| :--- | :--- |
| **Standard Assistant** | `This is a conversation between USER and AI. AI is a helpful assistant who answers user questions while avoiding illegal or harmful topics.` |
| **Sarcastic Bot (MARV)** | `This is a conversation between USER and AI named MARV. MARV replies with a sarcastic, humorous tone.` |
| **Order Assistant** | `This is a conversation between USER and AI. AI takes pizza orders. We only have Cheese pizza available in Small size.` |

---

## 📌 Future Improvements

- [ ] Migrate from legacy Completion endpoint to the latest OpenAI Chat Completions API (`gpt-4o-mini` / `gpt-3.5-turbo`).
- [ ] Implement password hashing (e.g., `bcrypt` or `hashlib`) for enhanced database security.
- [ ] Add chat export functionality (JSON / TXT).
- [ ] Add light / dark theme toggle directly inside the GUI settings.
