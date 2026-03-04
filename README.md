# LangChain Models

A hands-on repository exploring the **Model I/O** layer of LangChain, covering Large Language Models (LLMs), Chat Models, and Embedding Models. This project demonstrates how to integrate and interact with various AI model providers using a clean, modular Python structure.

---

## Project Structure

```
LangChain-models/
├── 1. LLMs/                  # Traditional large language model demos
├── 2. Chat Models/           # Dialogue-optimized chat model integrations
├── 3. Embedding Models/      # Text embedding & semantic similarity
├── requirements.txt          # Python dependencies
├── test.py                   # Quick test/sanity-check script
└── .gitignore
```

---

## Contents

### 1. LLMs
Basic demonstrations of traditional large language models — prompt-in, text-out. These models are suited for straightforward completions and text generation tasks.

### 2. Chat Models
Integrations with dialogue-optimized models from providers such as **OpenAI**, **Anthropic (Claude)**, **Google Gemini**, and **Hugging Face**. Chat models support multi-turn conversations and are the preferred choice for interactive, instruction-following tasks.

### 3. Embedding Models
Scripts that convert text into high-dimensional vector representations using models from **OpenAI** and **Hugging Face**. Includes document similarity search using cosine similarity — a foundational building block for Retrieval-Augmented Generation (RAG) and semantic search.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys for the model providers you intend to use

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/shruti353/LangChain-models.git
cd LangChain-models
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_gemini_key
HF_TOKEN=your_huggingface_token
```

> Note: The `.env` file is listed in `.gitignore`. Do not commit API keys to version control.

---

## Tech Stack

| Tool / Library | Purpose |
|---|---|
| [LangChain](https://www.langchain.com/) | Framework for building LLM-powered applications |
| [OpenAI](https://platform.openai.com/) | GPT models and text embeddings |
| [Anthropic](https://www.anthropic.com/) | Claude chat models |
| [Google Generative AI](https://ai.google.dev/) | Gemini models |
| [Hugging Face](https://huggingface.co/) | Open-source LLMs and local embedding models |
| [scikit-learn](https://scikit-learn.org/) | Cosine similarity for document search |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## Key Concepts

| Concept | Description |
|---|---|
| LLMs | General-purpose models for text completion |
| Chat Models | Fine-tuned for multi-turn dialogue and instruction following |
| Embeddings | Vector representations of text enabling semantic search |
| Cosine Similarity | Measures similarity between text embeddings for document retrieval |

---

## License

This project is open-source and available for learning and experimentation purposes.