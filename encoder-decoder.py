#!/usr/bin/env python3
"""encoder-decoder.py: Implementation of huffman coding"""

__author__ = "Abhyas Mall"
__email__ = "abhyas@uchicago.edu"

import os

class HuffmanCoding:

    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}

    def make_frequency_dict(text):
        pass

    def make_heap(self, frequency):
        pass

    def merge_codes(self):
        pass
    
    def make_codes(self):
        pass

    def get_encoded_text(self, text):
        pass

    def pad_encoded_text(self, encoded_text):
        pass

    def get_byte_array(self, padded_encoded_text):
        pass

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_file = filename + ".bin"

        with open(self.path, 'r') as file, open(output_file, 'wb') as output:
            text = file.read()
            text = text.rstrip() 
            frequency = make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()
            encoded_text = get_encoded_text(text)
            padded_encoded_text = pad_encoded_text(encoded_text)
            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        print("Compressed")
        return output_path