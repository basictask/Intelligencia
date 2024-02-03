#!/usr/bin/env python
# coding: utf-8

# Small script to merge all class file pdfs into a single large pdf

import os
import re
import fitz

root_folder = '.'
output_filename = 'intelligencia_merged.pdf'

if os.path.isfile(output_filename):
    os.remove(output_filename)
    print(f'Removed {output_filename}')

# Regular expression to match directories in {number}_{text}/doc format
dir_pattern = re.compile(r'^\./(\d{1,2})_([^/]+)/doc/(\d+)_(.+)\.pdf$')

# List to store (number, path) tuples
numbered_paths = []

# Walk through the directory
for root, dirs, files in os.walk(root_folder):
    for file in files:
        # Full path of the file
        full_path = os.path.join(root, file)
        match = dir_pattern.match(full_path)
        if match:
            numbered_paths.append((int(match.group(1)), full_path))
            print(full_path)

# Sort the directories based on the number
numbered_paths.sort()

print('Paths to merge:\n', numbered_paths)
print('Running merge on paths...')

merged_document = fitz.open()

# Merge PDFs from each directory
for _, full_path in numbered_paths:
    with fitz.open(full_path) as pdf:
        for page in range(len(pdf)):
            merged_document.insert_pdf(pdf, from_page=page, to_page=page)

merged_document.save(output_filename)
merged_document.close()

print('Output successful')

