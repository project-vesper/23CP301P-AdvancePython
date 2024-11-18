import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json

class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f"Error: {self.filename} not found."

class InvalidInputDataError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Error: Invalid input data encountered: {self.data}"

class DiskSpaceFullError(Exception):
    def __str__(self):
        return "Error: Disk Full. Cannot write data to the output file."


def readFile(filename):

    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(filename)
        
        with open(filename, 'r') as file:
            data = file.read()
        if not isinstance(data, str):
            raise InvalidInputDataError(data)
        return data
    except FileNotFoundError as e:
        print(e)
    except InvalidInputDataError as e:
        print(e)

def processTextData(data):
    try:
        words = data.split()
        word_count = Counter(words)
        char_count = Counter(data)
        wordcloud = WordCloud(width=800, height=400).generate(data)

        # Save the word cloud image
        wordcloud.to_file("wordcloud.png")
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()

        return {"word_count": dict(word_count), "char_count": dict(char_count)}

    except Exception as e:
        print(e)

def saveOutputData(output_path, processed_data):
    try:
        if os.statvfs('/').f_bavail * os.statvfs('/').f_frsize < 1024:
            raise DiskSpaceFullError()
        
        with open(output_path, 'w') as outfile:
            json.dump(processed_data, outfile, indent=4)
        print(f"Processed data has been saved to '{output_path}'.")
    except DiskSpaceFullError as e:
        print(e)
    except Exception as e:
        print(e)
        print("An unexpected error occurred while saving the output file.")
    
if __name__ == "__main__":
    file_path = input("Enter the file path of the input file: ")
    output_path = "processed_data.json"
    
    data = readFile(file_path)
    if data is None:
        exit()
    
    processed_data = processTextData(data)
    
    saveOutputData(output_path, processed_data)
    