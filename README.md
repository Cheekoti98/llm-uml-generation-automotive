# llm-uml-generation-automotive
This is an extension project of my master thesis work: Comparative analysis of LLMs for automated UML generation from automotive textual requirements
**LLM-Based UML Generation for Automotive Requirements**

This project investigates the use of Large Language Models (LLMs) for automatic generation of UML diagrams from automotive textual requirements.

The repository contains an end-to-end pipeline including prompt-based methods, fine-tuning, evaluation, and rule-based post-processing to improve structural correctness.

---

## Project Overview
- Input: Automotive textual requirements
- Output: UML diagrams (PlantUML format)
- Diagram types: Class, Use Case, Sequence, State Machine, Activity

---

## Approach
1. Prompt-based UML generation using multiple LLMs
2. Fine-tuning open-source LLMs using LoRA
3. Deterministic inference and output extraction
4. Rule-based post-processing to correct semantic inconsistencies
5. Quantitative and qualitative evaluation

---

## Repository Structure
data/ - Sample and anonymized datasets
docs/ - Documentation and thesis-related material
prompts/ - Prompt templates and examples
results/ - Generated UML outputs and evaluation summaries
src/ - Core source code


---

## Technologies Used
- Python
- Hugging Face Transformers
- LoRA / PEFT
- Google Colab
- PlantUML

---

## Status
This repository is part of an academic thesis and a personal research project.  
Code and data are anonymized and simplified for public release.

---

## License
Apache License 2.0


