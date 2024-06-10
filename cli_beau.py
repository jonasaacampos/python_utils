"""
This module contains functions that are used to make the CLI more beautiful and legible. 
"""

def clean_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def text_separator(decorator='-'):
    print(decorator * 40)