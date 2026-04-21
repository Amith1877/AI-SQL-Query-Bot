# 🤖 AI SQL Query Bot

An AI-powered web application that lets you ask natural language questions about your t-shirt inventory and get instant answers — no SQL knowledge required!

## 🚀 Live Demo
Ask questions like:
- "How many t-shirts are available in total?"
- "How many white Nike t-shirts do we have?"
- "What is the total inventory value?"
- "Revenue from Adidas after discounts?"

## 🛠️ Tech Stack
- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, Flask
- **AI/LLM** — Groq API (LLaMA 3.3 70B)
- **Database** — MySQL
- **ORM** — LangChain SQLDatabase

## ⚙️ Setup & Installation

### 1. Clone the repository
git clone https://github.com/Amith1877/AI-SQL-Query-Bot.git
cd AI-SQL-Query-Bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Setup MySQL Database
- Install MySQL and create a database called atliq_tshirts
- Run the SQL scripts to create tables and populate data

### 4. Add your credentials in app.py
groq_api_key = "YOUR_GROQ_API_KEY"
db_password = "YOUR_MYSQL_PASSWORD"

### 5. Run the app
python app.py

### 6. Open in browser
http://localhost:5000

## 📁 Project Structure
AI-SQL-Query-Bot/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

## 🔑 Get API Keys
- Groq API Key: https://console.groq.com
- Free to use with generous limits

## 📸 Features
- ✅ Natural language to SQL conversion
- ✅ Real time database querying
- ✅ Clean black and green UI
- ✅ Recent questions history
- ✅ SQL query transparency
- ✅ Quick suggestion buttons
- ✅ Error handling

## 🤝 Contributing
Pull requests are welcome!

## 📄 License
MIT License
