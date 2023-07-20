"""
This is a small script to render all dot files in this folder into png files
Input: None
Output: .png files from each dot file
"""

import os
import pydot

target_dir = os.path.dirname(os.path.realpath(__file__))

for root, _, files in os.walk(target_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.dot'):
            print('Rendering: ' + file_path + '... ', end = '') 
            (graph, ) = pydot.graph_from_dot_file(file_path)
            name = file_path.split('.')[0]
            graph.write_png(os.path.join(root, name) + '.png')
            print('Done')

print('Done')

