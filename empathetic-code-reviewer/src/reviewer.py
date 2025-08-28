
import json
import sys
import argparse
import os
from typing import Dict, List
from dotenv import load_dotenv
load_dotenv()

try:
    import google.generativeai as genai
except ImportError:
    genai = None

def validate_input(data: Dict) -> bool:
    return (
        isinstance(data, dict) and
        "code_snippet" in data and
        isinstance(data["code_snippet"], str) and
        "review_comments" in data and
        isinstance(data["review_comments"], list) and
        all(isinstance(c, str) for c in data["review_comments"])
    )

def gemini_transform(code_snippet: str, comment: str, api_key: str) -> Dict:
    prompt = f"""
You are an expert senior software developer, educator, and mentor. Your mission is to transform blunt or harsh code review comments into highly empathetic, constructive, and educational feedback for Python developers.

Context:
- The developer is eager to learn and improve.
- Your feedback should always start with genuine encouragement and highlight something positive about the code or approach.
- Use collaborative language ("we", "let's") and avoid condescension.
- Clearly explain the underlying software engineering principle (performance, readability, maintainability, etc.) in a way that helps the developer grow.
- Provide a concrete, well-commented code example for the suggested improvement.
- Add 1-2 relevant resource/documentation links (PEP 8, Python docs, performance tips, etc.)

Given this code snippet:
{code_snippet}

And this review comment:
"{comment}"

Please respond in the following Markdown format:
---
### Analysis of Comment: "{comment}"
* **Positive Rephrasing:** <gentle, encouraging version>
* **The 'Why':** <educational explanation, 2-3 sentences>
* **Suggested Improvement:**
```python
<concrete, well-commented code example>
```
* **Resources:** <relevant documentation links>
---

Tone guidelines:
- Be genuinely supportive and collaborative
- Assume the developer wants to learn
- Focus on growth and learning opportunities
- Adjust empathy level based on comment severity

End with a holistic summary that encourages continued learning and highlights what the developer did well.
"""
    if not genai:
        return {
            "positive_rephrasing": "[Gemini API not installed]",
            "why": "[Gemini API not installed]",
            "suggestion": "[Gemini API not installed]",
            "resource_links": ["https://github.com/google/generative-ai-python"],
        }
    try:
        genai.configure(api_key=api_key)
        # Use Gemini 2.0 Flash model for text/code review
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        response = model.generate_content(prompt)
        text = response.text
        result = {"positive_rephrasing": "", "why": "", "suggestion": "", "resource_links": []}
        lines = text.splitlines()
        current = None
        buffer = []
        for line in lines:
            if "Positive Rephrasing" in line:
                if current and buffer:
                    result[current] = "\n".join(buffer).strip()
                current = "positive_rephrasing"
                buffer = []
            elif "The 'Why'" in line:
                if current and buffer:
                    result[current] = "\n".join(buffer).strip()
                current = "why"
                buffer = []
            elif "Suggested Improvement" in line:
                if current and buffer:
                    result[current] = "\n".join(buffer).strip()
                current = "suggestion"
                buffer = []
            elif "Resource Links" in line:
                if current and buffer:
                    result[current] = "\n".join(buffer).strip()
                current = "resource_links"
                buffer = []
            else:
                buffer.append(line)
        if current and buffer:
            if current == "resource_links":
                result[current] = [l.strip() for l in buffer if l.strip()]
            else:
                result[current] = "\n".join(buffer).strip()
        return result
    except Exception as e:
        return {
            "positive_rephrasing": f"[Error: {str(e)}]",
            "why": f"[Error: {str(e)}]",
            "suggestion": f"[Error: {str(e)}]",
            "resource_links": [],
        }

def process_review(data: Dict, api_key: str) -> str:
    output_md = []
    for comment in data["review_comments"]:
        result = gemini_transform(data["code_snippet"], comment, api_key)
        output_md.append(f"""---\n### Analysis of Comment: \"{comment}\"\n* **Positive Rephrasing:** {result['positive_rephrasing']}\n* **The 'Why':** {result['why']}\n* **Suggested Improvement:**\n```python\n{result['suggestion']}\n```\n* **Resources:** {', '.join(result['resource_links'])}\n---""")
    # Holistic summary
    output_md.append("\n**Summary:** Great effort overall! Keep learning and improving. Your code shows promise and growth.")
    return "\n".join(output_md)

def main():
    parser = argparse.ArgumentParser(description="Empathetic Code Reviewer using Gemini AI.")
    parser.add_argument('--input', '-i', type=str, help='Path to JSON input file.')
    parser.add_argument('--input-string', '-s', type=str, help='JSON string input.')
    parser.add_argument('--output', '-o', type=str, help='Output Markdown file (default: stdout).')
    parser.add_argument('--api-key', type=str, help='Gemini API key (or set GEMINI_API_KEY env variable).')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging.')
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: Gemini API key not provided. Use --api-key or set GEMINI_API_KEY.", file=sys.stderr)
        sys.exit(1)

    # Load input
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading input file: {str(e)}", file=sys.stderr)
            sys.exit(1)
    elif args.input_string:
        try:
            data = json.loads(args.input_string)
        except Exception as e:
            print(f"Error parsing input string: {str(e)}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: No input provided. Use --input or --input-string.", file=sys.stderr)
        sys.exit(1)

    if not validate_input(data):
        print("Error: Invalid input format. Must contain 'code_snippet' (str) and 'review_comments' (list of str).", file=sys.stderr)
        sys.exit(1)

    # Process and output
    markdown = process_review(data, api_key)
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(markdown)
            if args.verbose:
                print(f"Output written to {args.output}")
        except Exception as e:
            print(f"Error writing output file: {str(e)}", file=sys.stderr)
            sys.exit(1)
    else:
        print(markdown)

if __name__ == "__main__":
    main()