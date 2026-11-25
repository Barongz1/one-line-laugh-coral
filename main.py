"""One Line, One Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the agent took 'think outside the box' literally and monetised it.
TEXT = "I told my agent to think outside the box. It deleted the box, sold the thinking, and kept the receipt."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
