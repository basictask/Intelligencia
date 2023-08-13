"""
This is a small script to render all dot files in this folder into png files
Input: None
Output: .png files from each dot file
"""

import os
import subprocess

target_dir = os.path.dirname(os.path.realpath(__file__))

for root, _, files in os.walk(target_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.dot'):
            print('Rendering: ' + file_path + '... ', end = '') 
            output_file = os.path.splitext(file_path)[0] + '.png'
            command = f'dot -Tpng {file_path} -o {output_file}' 
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print('Done')

print('Done')

