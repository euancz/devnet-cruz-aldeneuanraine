"""
Module 2 — Activity: File Sorting with os and shutil
Student: Alden Euan Raine B. Cruz
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
its just a simple file sorting program it checks the 
files of Renejay folder and then they will be sorted 
based on their .jpg .pdf .txt and they will go to their
respective folder like for example the jpg will go to images



============================================
KEY VOCABULARY
============================================
- os module: the one that checks the files and folders 
- shutil module: the one that moves files from one to another
- file path: location of the file or folder
- directory: another word for a folder


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder = "Renejay"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if file.endswith(".jpg"):
        shutil.move(file_path, folder + "/Images/" + file)

    elif file.endswith(".pdf"):
        shutil.move(file_path, folder + "/Documents/" + file)

    elif file.endswith(".txt"):
        shutil.move(file_path, folder + "/Text/" + file)

print("Files sorted!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
the mistake i made is how i declared the folder path and how
i was trying to use the loop i was integrating it wrong


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
it could help me organize my files from school in my computer since
my computer is a mess and it would be a pain to sort it manually 

"""
