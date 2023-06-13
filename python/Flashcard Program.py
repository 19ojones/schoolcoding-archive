import tkinter as tk
from tkinter import messagebox

flashcards = {}  # Dictionary to store flashcards

def add_flashcard():
    title = title_entry.get()
    definition = definition_entry.get()
    if title and definition:
        flashcards[title] = definition
        messagebox.showinfo("Success", "Flashcard added!")
        title_entry.delete(0, tk.END)
        definition_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Error", "No flashcards available.")
        return

def check_answer():
    user_title = title_entry.get()
    expected_title = test_title
    if user_title.lower() == expected_title.lower():
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Incorrect! The correct answer is: {expected_title}")
    answer_window.destroy()

def test_flashcards():
    test_definition = list(flashcards.values())[0]
    test_title = list(flashcards.keys())[0]
    answer_window = tk.Toplevel(root)
    answer_window.title("Flashcard Test")
    question_label = tk.Label(answer_window, text=f"What is the title for definition: '{test_definition}'?")
    question_label.pack()
    title_entry = tk.Entry(answer_window)
    title_entry.pack()
    submit_button = tk.Button(answer_window, text="Submit", command=check_answer)
    submit_button.pack()

# Create main window
root = tk.Tk()
root.title("Flashcard Program")

# Create title entry and label
title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0, sticky=tk.W)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

# Create definition entry and label
definition_label = tk.Label(root, text="Definition:")
definition_label.grid(row=1, column=0, sticky=tk.W)
definition_entry = tk.Entry(root)
definition_entry.grid(row=1, column=1)

# Create test flashcards button
test_button = tk.Button(root, text="Test Flashcards", command=test_flashcards)
test_button.grid(row=3, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
