import os
import json

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    note = input("Enter your note: ")
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note saved!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note}")

def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes to delete.")
        return
    view_notes()
    try:
        index = int(input("Enter the note number to delete: ")) - 1
        if 0 <= index < len(notes):
            deleted = notes.pop(index)
            save_notes(notes)
            print(f"Deleted: {deleted}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nSimple Note-Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()