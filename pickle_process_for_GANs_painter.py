#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:01:42 2024


"""

import os
import pickle


# this process is used to store all the images into one pickle for monet and a separate pickle for the photos.
# this makes loading the images into google colab easier

def pickle_images(directory, output_file):
    # Dictionary to store image data
    images_data = {}
    
    # Initialize the counter
    counter = 0

    # Loop through all files in the directory
    for file_name in os.listdir(directory):
        print(file_name)
        if file_name.endswith('.jpg'):
            # Full path to the file
            file_path = os.path.join(directory, file_name)
            
            # Read the binary data of the image
            with open(file_path, 'rb') as image_file:
                images_data[file_name] = image_file.read()
                counter += 1  # Increment the counter
                # Check if the counter is divisible by 1000
                if counter % 1000 == 0:
                    print(f"Processing file number: {counter}")

    # Pickle the dictionary containing the images
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(images_data, pickle_file)

    print(f"Saved {len(images_data)} images to {output_file}")
    


# Example usage
#directory = '/Users/leblapi1/Code/GANs/Painter/gan-getting-started/monet_jpg/'
#output_file = 'all_monet.pickle'

#directory = '/Users/leblapi1/Code/GANs/Painter/gan-getting-started/photo_jpg/'
#output_file = 'all_photo.pickle'


directory = '/Users/leblapi1/Code/GANs/Painter/gan-getting-started/combined/'
output_file = 'all_combined.pickle'


pickle_images(directory, output_file)
