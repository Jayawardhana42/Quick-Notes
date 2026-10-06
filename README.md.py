```python
import datetime

def note_keeper():
    print("~ My Personal Scratchpad ~")
    print("Type your thoughts below. Type 'quit' when you're done.\n")
    
    while True:
        my_thought = input("What's on your mind?: ")
        
        # Check if the user wants to exit
        if my_thought.lower() == 'quit':
            print("\nAll done! Check your 'saved_notes.txt' file later.")
            break
            
        # Skip if they just pressed enter with no text
        if my_thought.strip() == "":
            print("You didn't write anything...\n")
            continue
            
        # Grab today's date and current time
        now_time = datetime.datetime.now().strftime("%Y-%m-%d [%H:%M]")
        
        # Save it into the text file
        with open("saved_notes.txt", "a", encoding="utf-8") as text_file:
            text_file.write(f"{now_time} -> {my_thought}\n")
            
        print("✔ Saved!\n")

if __name__ == "__main__":
    note_keeper()
