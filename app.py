import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# App Configuration
st.set_page_config(page_title="Multi-Agent Researcher", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Agent AI Research Assistant")
st.write("Enter a topic, and our specialized AI Agents will research and write a report for you!")

# User input
topic = st.text_input("What topic do you want to research?", placeholder="e.g., Quantum Computing Trends in 2026")

if st.button("Start Research 🚀") and topic:
    if not groq_api_key:
        st.error("Please add your GROQ_API_KEY in the .env file!")
    else:
        # Initialize LLM
        llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key, temperature=0.5)
        
        # --- AGENT 1: Senior Research Analyst ---
        st.subheader("🕵️‍♂️ Agent 1: Senior Research Analyst working...")
        research_status = st.empty()
        research_status.info(f"Gathering points and deep insights on: '{topic}'...")
        
        research_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert Senior Research Analyst. Your job is to break down the given topic into critical facts, recent developments, and deep technical points. Provide an exhaustive list of factual insights."),
            ("human", f"Perform deep research on this topic: {topic}")
        ])
        
        research_chain = research_prompt | llm
        research_notes = research_chain.invoke({}).content
        research_status.success("Research gathered successfully!")
        
        with st.expander("Show Raw Research Notes"):
            st.write(research_notes)
            
        # --- AGENT 2: Tech Writer ---
        st.subheader("✍️ Agent 2: Professional Tech Writer working...")
        writer_status = st.empty()
        writer_status.info("Compiling raw facts into a beautiful Markdown report...")
        
        writer_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a professional Tech Writer. Your job is to take raw research notes and transform them into a comprehensive, beautifully structured, and highly engaging article/report using Markdown formatting with proper headings, bullet points, and an introduction/conclusion."),
            ("human", f"Transform these raw research notes into a professional report:\n\n{research_notes}")
        ])
        
        writer_chain = writer_prompt | llm
        final_report = writer_chain.invoke({}).content
        writer_status.success("Final report generated successfully!")
        
        # Display Final Result
        st.markdown("---")
        st.header("📋 Final Research Report")
        st.markdown(final_report)