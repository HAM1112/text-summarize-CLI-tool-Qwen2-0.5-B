import argparse
import requests , json 

import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def get_summary(content):
    
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "qwen2:0.5b",
        "prompt": f"Summarize the give text: {content}",
        "stream" : False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['response']
    else:
        print(f"Error: {response.status_code}")
        return response.text



def print_text(text):
    print(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and summarize the content of a text file or a direct text input.')
    parser.add_argument('-f', '--file', type=str, help='The path to the text file to be summmearized.')
    parser.add_argument('text', type=str, nargs='?', help='The text input to be summerized.')

    args = parser.parse_args()

    if args.file:
        content = read_file(args.file)
        summurized_text = get_summary(content)

        print(f"Summary of {args.file}.")
        print(summurized_text)
    elif args.text:
        print(f"Summary of text passed.")
        summurized_text = get_summary(args.text)
        print(summurized_text)
    else:
        print("Please provide either a file path with -f or a direct text input.")
    



    
