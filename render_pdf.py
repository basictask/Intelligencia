"""
This is a small script to render all the tex files into pdfs. 
The script traverses all the folders and subfolders recursively and renders each tex file into a pdf using the shell of the system
Input: None
Output: .pdf files from each dot file
"""

import os
import subprocess

target_dir = os.path.dirname(os.path.realpath(__file__))

for root, _, files in os.walk(target_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.tex'):
            print('Rendering: ' + file_path + '... ', end = '') 
            output_file = os.path.splitext(file_path)[0] + '.png'
            command = f'pdflatex {file_path}' 
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print('Done')

print('Done')

