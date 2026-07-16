# 🤖 Multi-Agent AI Research Assistant

An advanced multi-agent system built with LangChain and Llama-3.3-70b (via Groq Cloud) that acts as a fully automated research and content writing team. It takes any complex topic and generates deep, structured Markdown reports.

## 🧠 How It Works (The Multi-Agent Workflow)
The application splits the workflow into two specialized AI agents executing sequentially:
1. **🕵️‍♂️ Senior Research Analyst Agent:** Scours the semantic space, structures raw factual points, extracts critical data insights, and outlines recent developments.
2. **✍️ Professional Tech Writer Agent:** Consumes the raw research output and compiles it into a highly polished, comprehensive Markdown report with clear headings, introductions, and conclusions.

## 🚀 Features
- **Multi-Agent Orchestration:** Simulates an industry-grade collaborative workflow.
- **Deep Analytical Insights:** Leverages Llama-3.3-70b-versatile for high-reasoning output.
- **Beautiful UI:** Live state expansions and progressive updates powered by Streamlit.
- **Production Ready:** Clean environment segregation using `.env` configs.

## 🛠️ Tech Stack
- **Framework:** LangChain (Prompt Templates, Sequential Chains)
- **LLM Provider:** Groq Cloud (Llama 3.3)
- **UI Architecture:** Streamlit
- **Environment Management:** python-dotenv

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/subhu770/Multi-Agent-Researcher.git](https://github.com/subhu770/Multi-Agent-Researcher.git)
   cd Multi-Agent-Researcher

   Create & Activate Virtual Environment:
   python -m venv myenv
.\myenv\Scripts\Activate.ps1

Install Dependencies:
pip install streamlit langchain langchain-groq python-dotenv

Set up Environment Variables:
GROQ_API_KEY=your_groq_api_key_here

Run the Application:
streamlit run app.py
