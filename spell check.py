#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.corpus import words

nltk.download("words")

class SpellingChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()
        
        self.old_spaces = 0

        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")

        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

        if space_count != self.old_spaces:
            self.old_spaces = space_count
            for word in content.split():
                word = re.sub(r"[^\w]", "", word.lower())
                if word not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")

SpellingChecker()


# In[ ]:





# In[2]:


import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.corpus import words

nltk.download("words")

class SpellingChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.spell = nltk.corpus.words.words()  # Load the list of English words

        self.root.mainloop()

    def check(self, event):
        # Get the text from the text widget
        input_text = self.text.get("1.0", "end-1c")
        
        # Tokenize the input_text into words
        words = re.findall(r'\b\w+\b', input_text)

        # Check each word against the list of English words
        misspelled_words = [word for word in words if word.lower() not in self.spell]

        # Highlight misspelled words
        self.highlight_misspelled(misspelled_words)

    def highlight_misspelled(self, misspelled_words):
        # Clear previous tags
        self.text.tag_remove("misspelled", "1.0", "end")

        # Apply tag to misspelled words
        for word in misspelled_words:
            start = "1.0"
            while True:
                start = self.text.search(word, start, stopindex="end")
                if not start:
                    break
                end = f"{start}+{len(word)}c"
                self.text.tag_add("misspelled", start, end)
                start = end

        # Configure the tag for highlighting
        self.text.tag_configure("misspelled", background="red")

SpellingChecker()


# In[3]:


get_ipython().system('pip install textblob')

from tkinter import *
from textblob import TextBlob

# Function to clear both the text entry boxes


def clearAll():

	# whole content of text entry area is deleted
	word1_field.delete(0, END)
	word2_field.delete(0, END)

# Function to get a corrected word


def correction():

	# get a content from entry box
	input_word = word1_field.get()

	# create a TextBlob object
	blob_obj = TextBlob(input_word)

	# get a corrected word
	corrected_word = str(blob_obj.correct())

	# insert method inserting the
	# value in the text entry box.
	word2_field.insert(10, corrected_word)


# Driver code
if __name__ == "__main__":

	# Create a GUI window
	root = Tk()

	# Set the background colour of GUI window
	root.configure(background='light green')

	# Set the configuration of GUI window (WidthxHeight)
	root.geometry("400x150")

	# set the name of tkinter GUI window
	root.title("Spell Corrector")

	# Create Welcome to Spell Corrector Application: label
	headlabel = Label(root, text='Welcome to Spell Corrector Application',
					fg='black', bg="red")

	# Create a "Input Word": label
	label1 = Label(root, text="Input Word",
				fg='black', bg='dark green')

	# Create a "Corrected Word": label
	label2 = Label(root, text="Corrected Word",
				fg='black', bg='dark green')

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	# padx keyword argument used to set padding along x-axis .
	headlabel.grid(row=0, column=1)
	label1.grid(row=1, column=0)
	label2.grid(row=3, column=0, padx=10)

	# Create a text entry box
	# for filling or typing the information.
	word1_field = Entry()
	word2_field = Entry()

	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	word1_field.grid(row=1, column=1, padx=10, pady=10)
	word2_field.grid(row=3, column=1, padx=10, pady=10)

	# Create a Correction Button and attached
	# with correction function
	button1 = Button(root, text="Correction", bg="red", fg="black",
					command=correction)

	button1.grid(row=2, column=1)

	# Create a Clear Button and attached
	# with clearAll function
	button2 = Button(root, text="Clear", bg="red",
					fg="black", command=clearAll)

	button2.grid(row=4, column=1)

	# Start the GUI
	root.mainloop()


# In[ ]:




