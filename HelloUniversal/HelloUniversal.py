import os
import sys

def transform_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content += " rocks"
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python HelloUniversal.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    transform_file(input_file, output_file)
    print(f"Transformed {input_file} to {output_file}")
