import argparse
import json
from reviewer import transform_comments
from errors import InputError

def main():
    parser = argparse.ArgumentParser(description="Transform harsh code review comments into constructive feedback.")
    parser.add_argument('input_file', type=str, help='Path to the JSON file containing harsh comments.')
    parser.add_argument('output_file', type=str, help='Path to the JSON file where empathetic feedback will be saved.')

    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as infile:
            comments = json.load(infile)

        feedback = transform_comments(comments)

        with open(args.output_file, 'w') as outfile:
            json.dump(feedback, outfile, indent=4)

        print(f"Empathetic feedback has been saved to {args.output_file}.")

    except FileNotFoundError:
        print(f"Error: The file {args.input_file} was not found.")
    except json.JSONDecodeError:
        print("Error: The input file is not a valid JSON.")
    except InputError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()