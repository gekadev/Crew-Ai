# CrewAI Modular Workflow Project

This project demonstrates how to build modular workflows using the modern CrewAI framework.  
It defines two crews: a base crew and a second crew with **4 specialized agents** that work together to process topics, generate content, and evaluate results.

## 🔹 Workflow Overview
1. **Input Agent** – Accepts the topic and sets the workflow in motion.  
2. **Keyword Instruction Agent** – Extracts or generates topic-specific keywords using Pydantic validation.  
3. **Story Generation Agent** – Creates a story or article based on the validated keywords.  
4. **Evaluation Agent** – Reviews the story’s quality, accuracy, and structure.  
5. **Performance & Reporting Agent** – Collects outputs from all agents, evaluates overall performance, and generates a final structured report.  

## 🔹 Features
- Modular agent design with CrewAI’s modern approach.  
- Automated keyword validation via Pydantic.  
- Story creation pipeline with built-in quality checks.  
- Final performance evaluation and **Markdown report generation**.  
- Extensible design for scaling with more agents or custom workflows.  

## 🔹 Use Cases
- Automated report or article generation.  
- AI-assisted content workflows.  
- Research & evaluation pipelines.  
- Demonstrations of CrewAI in modular AI agent design.  

---
