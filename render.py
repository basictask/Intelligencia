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
        file_dir = os.path.abspath(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))[0] + '.png'
        target_name = os.path.join(file_dir, file_name)
	
        if file_path.endswith('.dot'):
            print('Rendering: ' + file_path + '... ', end = '') 
            (graph, ) = pydot.graph_from_dot_file(file_path)
            graph.write_png(file_dir)
            print('Done')

print('Done')

