# utils.py

import asyncio
import sys
import time
import threading

async def print_slow(text, delay=0.5):
    print(text)
    await asyncio.sleep(delay)

async def print_slow_multiline(text, delay=0.003):
    lines = text.split('\n')
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

async def print_threaded(text, delay=0.05):
    for line in text.splitlines():
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        time.sleep(delay)

async def run_in_threads(*args):
    threads = []
    for text, delay in args:
        thread = threading.Thread(target=print_threaded, args=(text, delay))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

async def print_progress_bar(duration=3, bar_length=50):
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        bar = '█' * i + '-' * (bar_length - i)
        sys.stdout.write(f"\r|{bar}| {percent:.2f}%")
        sys.stdout.flush()
        await asyncio.sleep(duration / bar_length)
    print()

async def print_warning_bar(duration=3, bar_length=50):
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        bar = '█' * i + '-' * (bar_length - i)
        sys.stdout.write(f"\r\033[93m|{bar}| {percent:.2f}%\033[0m")
        sys.stdout.flush()
        await asyncio.sleep(duration / bar_length)
    print()