#!/usr/bin/env python3
"""
Project 18 – WPA Cracker
Cracks a WPA handshake using a wordlist.
"""
import sys
import subprocess
import os

def crack_handshake(cap_file, wordlist):
    if not os.path.exists(cap_file):
        print(f"[!] {cap_file} not found.")
        return
    if not os.path.exists(wordlist):
        print(f"[!] Wordlist {wordlist} not found.")
        return
    print(f"[*] Cracking {cap_file} with {wordlist}...")
    cmd = ["aircrack-ng", "-w", wordlist, cap_file]
    subprocess.run(cmd)

if __name__ == "__main__":
    cap_file = sys.argv[1] if len(sys.argv) > 1 else "handshake.cap"
    wordlist = sys.argv[2] if len(sys.argv) > 2 else "wordlist.txt"
    crack_handshake(cap_file, wordlist)