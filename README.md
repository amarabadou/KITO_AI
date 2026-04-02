# KITO – AI Assistant with Persistent Memory and Voice Interaction
KITO is a local AI assistant powered by LLaMA3 that supports real-time conversation, voice interaction, and persistent memory.  Unlike basic chatbots, KITO is designed to simulate long-term interaction by storing and retrieving past conversations using semantic similarity, allowing more contextual and human-like responses over time.


- Persistent Memory: Stores conversations in a local SQLite database and reloads them on startup.
- Semantic Memory Retrieval: Uses embeddings (Sentence Transformers) to retrieve relevant past conversations.
- Real-Time Streaming Responses: Generates responses token-by-token using LLaMA3 via Ollama.
- Voice Interaction (TTS): Converts responses into natural speech using Microsoft Edge TTS.
- Asynchronous Audio Processing: Smooth audio playback using threading and queues.
- Visualizer: Dynamic animation reflecting assistant activity.
- Basic Authentication System: Password-based access control

# How It Works
1. User Input: User sends a message in the terminal.
2. Memory Retrieval: The system searches past conversations using semantic similarity.
3. Context Injection: Relevant past memories are injected into the prompt.
4. LLM Processing: Request is sent to LLaMA3 via Ollama.
5. Streaming Output: Response is displayed token-by-token.
6. Voice Generation: Response is converted into speech asynchronously.
7. Persistence: Both user input and assistant response are stored in the database.

# Technologies Used

- Python 3.10+
- Ollama (LLaMA3)
- SQLite
- Sentence Transformers
- NumPy
- Edge-TTS
- Pygame
- Colorama

# Installation & Setup
1. Clone the repository:
- git clone https://github.com/amarabadou/KITO_AI.git
- cd KITO-AI/KITO_AI
2. Install dependencies:
   pip install -r requirements.txt
3. Pull the Ollama model:
   ollama pull llama3
4. run KITO:
   python main.py

# Authentication
KITO uses a passcode-based access system. The default password hash is stored in the code. To change the password, modify the USER_PASSWORD_HASH value.

# Limitations

- Memory retrieval is linear (not optimized for large datasets)
- Basic security (not production-level)
- Terminal-based interface only
- No filtering of irrelevant stored data

# Author
Ammar Abadou Computer Science student

