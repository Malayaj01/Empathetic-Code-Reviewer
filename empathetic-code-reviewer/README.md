# Empathetic Code Reviewer

## Overview
Empathetic Code Reviewer is a Python CLI tool that transforms harsh or blunt code review comments into empathetic, educational, and constructive feedback using Google Gemini AI. It helps developers learn and grow by providing actionable suggestions, explanations, and resource links in a supportive tone.

## Features
- Converts critical code review comments into positive, growth-oriented feedback
- Uses Gemini 2.0 Flash model for fast, high-quality text generation
- Batch or single comment processing (with quota-aware design)
- Output in Markdown format for easy sharing
- CLI interface with file or string input
- Robust error handling for API and input issues
- Customizable prompt engineering for tone and accuracy
- Resource/documentation links for further learning
- Holistic summary to encourage continued improvement

## Installation
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd empathetic-code-reviewer
   ```
2. **Create and activate a Python virtual environment:**
   ```sh
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # On Windows PowerShell
   # Or
   source .venv/bin/activate    # On Linux/Mac
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. **Obtain a Gemini API key:**
   - Go to [Google Cloud Console → Credentials](https://console.cloud.google.com/apis/credentials)
   - Create an API key for the Gemini API
2. **Set up your `.env` file:**
   ```env
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

## Usage
### Command Line
```sh
python empathetic-code-reviewer\src\reviewer.py --input empathetic-code-reviewer\sample_input.json
python empathetic-code-reviewer\src\reviewer.py --input-string '{"code_snippet": "...", "review_comments": ["..."]}'
python empathetic-code-reviewer\src\reviewer.py --input empathetic-code-reviewer\sample_input.json --output review_analysis.md
```

#### Arguments
- `--input` / `-i`: Path to JSON input file
- `--input-string` / `-s`: JSON string directly
- `--output` / `-o`: Output file path (default: stdout)
- `--api-key`: API key (or use environment variable)
- `--verbose` / `-v`: Detailed logging

## Input Format
```json
{
  "code_snippet": "def process_data(data):\n    result = []\n    for item in data:\n        if item > 0:\n            result.append(item * 2)\n    return result",
  "review_comments": [
    "This is slow and inefficient",
    "Use list comprehension instead",
    "Variable names could be more descriptive"
  ]
}
```

## Output Format (Markdown)
For each comment:
- **Positive Rephrasing**
- **The 'Why'**
- **Suggested Improvement** (with code)
- **Resources**
- Holistic summary at the end

## Example Output
```
---
### Analysis of Comment: "This is slow and inefficient"
* **Positive Rephrasing:** "This code is a great start..."
* **The 'Why':** "Using list comprehensions..."
* **Suggested Improvement:**
```python
def process_data(data):
    result = [item * 2 for item in data if item > 0]
    return result
```
* **Resources:** [PEP 8](https://peps.python.org/pep-0008/), [Python Docs](https://docs.python.org/3/)
---

**Summary:** Great effort overall! Keep learning and improving. Your code shows promise and growth.
```

## Testing
- Unit tests are in the `tests/` directory
- Run with `pytest` or your preferred test runner

## Troubleshooting
- **Quota errors:** Wait for quota reset or upgrade your API plan
- **API key errors:** Generate a new key and update `.env`
- **Model errors:** Use `models/gemini-2.0-flash` for best compatibility

## Architecture
- `src/reviewer.py`: Main logic and AI integration
- `src/markdown_generator.py`: Markdown formatting (optional)
- `src/cli.py`: CLI interface (optional)
- `config.py`: API keys and configuration
- `requirements.txt`: Dependencies
- `sample_input.json`: Example input
- `tests/`: Unit tests

## Resources
- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [PEP 8 – Python Style Guide](https://peps.python.org/pep-0008/)
- [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

## License
MIT