def parse_json(input_string):
    import json
    try:
        return json.loads(input_string)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON input: " + str(e))

def validate_json(data):
    if not isinstance(data, dict):
        raise ValueError("JSON input must be an object.")
    # Add more validation rules as needed

def format_markdown(text):
    return f"**{text}**"  # Simple markdown formatting example

def extract_comments(data):
    return data.get("comments", [])

def transform_comment(comment):
    # Placeholder for transformation logic
    return f"Empathetic feedback for: {comment}"