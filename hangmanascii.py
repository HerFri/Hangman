# Hangman ASCII art source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

HANG_STAGES = [
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

HANGMANTITLE = """ 
 _                                             
| |                                                +---+    
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __      |   |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     O   |
| | | | (_| | | | | (_| | | | | | | (_| | | | |   /|\  |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   / \  |
                    __/ |                              |
                   |___/                         ========="""       

YOUWIN = """
 __     __                    _         _ 
 \ \   / /                   (_)       | |
  \ \_/ /__  _   _  __      ___ _ __   | |
   \   / _ \| | | | \ \ /\ / / | '_ \  | |
    | | (_) | |_| |  \ V  V /| | | | | |_|
    |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
                                          
                                          """

YOULOSE = """
 __     __           _                  _ 
 \ \   / /          | |                | |
  \ \_/ /__  _   _  | | ___  ___  ___  | |
   \   / _ \| | | | | |/ _ \/ __|/ _ \ | |
    | | (_) | |_| | | | (_) \__ \  __/ |_|
    |_|\___/ \__,_| |_|\___/|___/\___| (_)
                                          
                                          """

RULES = """
You have 6 tries to guess the right word.            +---+
Every _ indicates one letter of the word you          |   |
are guessing. For every wrong guess a part of         O   |
the man to be hanged will be added. If you achieve   /|\  |
to guess the right word within 6 tries,              / \  |
you can save the man of being hanged, otherwise           |
you will lose and the man is hanged.                ========="""