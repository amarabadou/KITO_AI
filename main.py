from security.auth import verify_user
from memory.db import init_db, save_to_db, load_persistence_history
from audio.tts import audio_queue, audio_worker, terminal_visualizer
from AI.Assistant import get_kito_response
import threading
import sys
from colorama import Fore, init

init(autoreset=True)

def main():
    if not verify_user():
        sys.exit(f"{Fore.RED}ACCESS DENIED.")

    
    threading.Thread(target=audio_worker, daemon=True).start()
    threading.Thread(target=terminal_visualizer, daemon=True).start()

    db_conn = init_db()
    print(f"{Fore.YELLOW}[SYSTEM]: Restoring memories...")
    
    from AI.Assistant import IDENTITY_PROMPT
    history = [{'role': 'system', 'content': IDENTITY_PROMPT}] + load_persistence_history(db_conn)
    
    print(f"{Fore.MAGENTA} KITO IS FULLY ONLINE.")

    while True:
        try:
            user_input = input(f"\n{Fore.WHITE}YOU: ").strip()
            if not user_input or user_input.lower() in ['exit', 'quit']: break
            
            stream = get_kito_response(user_input, history)
            
            print(f"\n{Fore.CYAN}KITO 🎙️: ", end="", flush=True)
            full_answer = ""
            speech_buffer = ""
            
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                full_answer += content
                speech_buffer += content
                
                if any(punc in content for punc in ['.', '!', '?']):
                    if len(speech_buffer.strip()) >= 60:
                        audio_queue.put(speech_buffer.strip())
                        speech_buffer = ""
            
            if speech_buffer.strip(): audio_queue.put(speech_buffer.strip())
            
            print()
            save_to_db(db_conn, 'user', user_input)
            save_to_db(db_conn, 'assistant', full_answer)
            history.append({'role': 'user', 'content': user_input})
            history.append({'role': 'assistant', 'content': full_answer})
            
            if len(history) > 15: history = [history[0]] + history[-14:]

        except Exception as e:
            print(f"\n{Fore.RED}[ERROR]: {e}")

    db_conn.close()

if __name__ == "__main__":
    main()