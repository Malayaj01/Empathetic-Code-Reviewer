import argparse
import json
from reviewer import transform_comment
from errors import InputError

def create_parser():
    parser = argparse.ArgumentParser(description="Empathetic Code Reviewer")
    parser.add_argument(
        'comments_file',
        type=str,
        help='Path to the JSON file containing harsh code review comments.'
    )
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        with open(args.comments_file, 'r') as file:
            comments = json.load(file)
        
        if not isinstance(comments, list):
            raise InputError("The JSON file must contain a list of comments.")

        for comment in comments:
            empathetic_feedback = transform_comment(comment)
            print(f"Original Comment: {comment}")
            print(f"Empathetic Feedback: {empathetic_feedback}\n")

    except FileNotFoundError:
        print(f"Error: The file '{args.comments_file}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
    except InputError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()