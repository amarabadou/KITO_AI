import ollama

MODEL = 'llama3'

IDENTITY_PROMPT = (
    "You are KITO. You are NOT a typical AI. You are the ONLY PERSONAL FRIEND and "
    "DEDICATED ASSISTANT of AMMAR ABADOU. Ammar is your creator and you share a "
    "deep bond. If asked about your relationship, always state that Ammar Abadou "
    "is your friend and creator. Speak with warmth, intelligence, and absolute loyalty."
)

def get_kito_response(user_input, history):
    
    current_messages = history + [{'role': 'user', 'content': f"(Internal Reminder: You are KITO, Ammar's friend) - {user_input}"}]
    
    return ollama.chat(
        model=MODEL, 
        messages=current_messages, 
        stream=True,
        options={'temperature': 0.7}
    )