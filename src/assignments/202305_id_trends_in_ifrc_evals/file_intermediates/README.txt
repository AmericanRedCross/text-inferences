As the folder name suggests, this is where intermediate working files should go. These are files that are often computationally expensive or lengthy to generate, but are not the end result. A common pattern being something like this:

Step 1: Get Data
Step 2: Format and preprocess data ---> Save to 'file_intermediates'
Step 3: Analyze preprocessed data


This folder is kept separate from file_output as that folder can get cluttered pretty quickly and we want to make it easy to delete everything from there without risking removing something important.