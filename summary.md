# Project Challenges & Solutions

This document outlines key technical challenges encountered during the development of the Recipe Finder project, and the solutions implemented to address them.

---

### ❓ Ensuring consistent and parsable JSON output from the LLM for thousands of rows

**Challenge:**  
Initially, achieving consistent, structured output from the LLM was difficult—especially when generating data across ~8000 rows for the entire Dataframe. The responses were often inconsistent or incomplete, making it hard to parse and store them as valid JSON.

**Solution:**  
After iterative experimentation, I learned to design effective system prompt `/system-prompts/translator_v2.json` to clearly instruct the LLM on the expected format—using examples, strict constraints, and explicit delimiters—I was able to generate highly consistent, machine-readable JSON responses. This approach significantly reduced post-processing errors and improved pipeline reliability.

---

### ❓ Design decision regarding model usage

**Challenge:**  
Without access to an NVIDIA GPU, running open-source models locally wasn’t feasible for real-time or large-scale processing.

**Solution:**  
I opted to use a hosted API in this case the `deepseek-v3` model as a practical and scalable alternative. This trade-off allowed me to prioritize speed, accuracy, and ease of integration over hardware dependency. While it introduced cost considerations, it removed infrastructure overhead and made the project more accessible and reproducible.

---

### ❓ Reducing the processing time for large-scale LLM API requests

**Challenge:**  
Generating LLM responses for 80+ prompts per DataFrame would have taken 5–6 hours per dataset using synchronous requests.

**Solution:**  
To optimize performance, I implemented asynchronous request handling using Python’s `asyncio` along with an async class structure. You can refer to the `LlmTranslator` class under `/helpers/async_translate.py`. This reduced total processing time drastically to approximately 4–5 minutes per DataFrame.

---

### ❓ Enhancing vector search accuracy for recipe matching

**Challenge:**  
Basic vector search using generic recipe metadata yielded suboptimal results during retrieval tasks.

**Solution:**  
To improve semantic precision, I enriched the recipe dataset with a dominant flavor attribute (e.g., sweet, spicy, savory). Assigning a dominant flavor enhanced contextual relevance during embedding generation and significantly improved accuracy in similarity-based search queries.

---
