import edge_tts
import pygame
import asyncio
import queue
import threading
import time
import os
import random
import sys
from colorama import Fore, Style

audio_queue = queue.Queue()
is_talking = False

async def generate_voice(text, filename):
    communicate = edge_tts.Communicate(text, "en-US-AndrewNeural", rate="+5%")
    await communicate.save(filename)

def audio_worker():
    global is_talking
    pygame.mixer.init()
    while True:
        text = audio_queue.get()
        if text is None: break
        try:
            filename = "kito_speech.mp3"
            asyncio.run(generate_voice(text, filename))
            sound = pygame.mixer.Sound(filename)
            is_talking = True
            channel = sound.play()
            while channel.get_busy(): time.sleep(0.05)
            is_talking = False
            if os.path.exists(filename): os.remove(filename)
        except: pass
        audio_queue.task_done()

def terminal_visualizer():
    symbols = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    while True:
        if is_talking:
            bars = "".join([random.choice(symbols) for _ in range(35)])
            sys.stdout.write("\033[s\033[1;1H" + f"{Fore.MAGENTA} [ KITO ACTIVE ]: {bars} {Style.RESET_ALL}\033[K" + "\033[u")
        else:
            sys.stdout.write("\033[s\033[1;1H" + f"{Style.DIM}{Fore.WHITE} [ ONLINE - READY...]: . . . . . {Style.RESET_ALL}\033[K" + "\033[u")
        sys.stdout.flush()
        time.sleep(0.1)