#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from colorama import init, Fore, Style
from core.ai_engine import AIEngine
from core.scanner import Scanner

init(autoreset=True)

def show_banner():
    with open("banner.txt", "r", encoding="utf-8") as f:
        print(Fore.RED + f.read())
        print(Style.RESET_ALL)

def main():
    show_banner()
    print(f"{Fore.GREEN}[+] Tool Cybersecurity v2.0 | AI Mode Active")
    
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Uso: python main.py --scan <IP> o --ai")
        sys.exit(1)
    
    if "--scan" in sys.argv:
        target = sys.argv[sys.argv.index("--scan") + 1]
        scanner = Scanner(target)
        scanner.run()
    elif "--ai" in sys.argv:
        ai = AIEngine()
        ai.deep_scan()
    else:
        print(f"{Fore.RED}[!] Argumento no válido.")

if __name__ == "__main__":
    main()
