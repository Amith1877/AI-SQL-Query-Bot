# app.py
from flask import Flask, render_template, request, jsonify
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import re

app = Flask(__name__)

# --- Database Setup ---
def get_db():
    db_user = "root"
    db_password = "your password"
    db_host = "localhost"
    db_name = "atliq_tshirts"
    return SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )

# --- LLM Setup ---
def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key="your api key",
        temperature=0.2
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question provided"})
    try:
        db = get_db()
        llm = get_llm()

        prompt = f"""You are a MySQL expert. Given the following database schema:
{db.get_table_info()}
Generate ONLY a valid MySQL SQL query (no explanation, no markdown, no backticks around the query) to answer this question:
{question}
Return only the raw SQL query, nothing else."""

        response = llm.invoke([HumanMessage(content=prompt)])
        sql_query = response.content.strip()
        sql_query = re.sub(r'```sql|```', '', sql_query).strip()

        result = db.run(sql_query)

        answer_prompt = f"""Question: {question}
SQL Query: {sql_query}
SQL Result: {result}
Give a short, clear answer in plain English based on the SQL result."""

        answer_response = llm.invoke([HumanMessage(content=answer_prompt)])

        return jsonify({
            "answer": answer_response.content.strip(),
            "sql": sql_query,
            "raw": str(result)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)