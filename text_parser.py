import sys
import json
import re

def process_text(text):
    chunks = text.strip().split('\n\n')

    results = []
    for chunk in chunks:
        lines = chunk.split('\n')
        job_data = {
            "Company": {
                "Full Name": lines[0],
                "Name": lines[2],
                "Hiring Status": None if 'Actively recruiting' not in lines[4] else 'Actively recruiting'
            },
            "Position": {
                "Title": None,
                "Level": None,
                "Type": None
            },
            "Location": {
                "Country": lines[3].split(' ')[0],
                "Type": 'Remote' if 'Remote' in lines[3] else 'On-site'
            }
        }

        # Extract position title, level and type
        position = re.search(r'(?:(Senior|Junior)/)?([\w\s]+)(?:\s-\s(.+))?', lines[1])
        if position:
            job_data["Position"]["Level"] = position.group(1)
            job_data["Position"]["Title"] = position.group(2).strip()
            job_data["Position"]["Type"] = position.group(3)

        results.append(job_data)

    return results

def main():
    text = sys.stdin.read()
    structured_data = process_text(text)
    print(json.dumps(structured_data, indent=2))

if __name__ == "__main__":
    main()
