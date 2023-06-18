import sys
import json
import re

def parse_company(lines: list[str]):
    company_name_full = lines[0]
    company_name_short = lines[2]
    hiring_status = None if 'Actively recruiting' not in lines[4] else 'Actively recruiting'
    return {
                "Full Name": company_name_full,
                "Name": company_name_short,
                "Hiring Status": hiring_status,
            }

def parse_position(lines: list[str]):

    position_type = lines[1].split(' ')[-1].replace('(',"").replace(')', "")
        
    # Extract position title, level and type
    position = re.search(r'(?:(Senior|Junior)/)?([\w\s]+)(?:\s-\s(.+))?', lines[1])
    position_level = position.group(1) if position is not None else None
    position_title = position.group(2).strip() if position is not None else None
    position_type = position_type if position_type is not None else position.group(3)
    
    return {
                "Title": position_title,
                "Level": position_level,
                "Type": position_type,
            }

def parse_location(lines: list[str]):
    raw_country = lines[3]
    country = None if raw_country is None else raw_country.split(' ')[0]

    location_type = 'Remote' if 'Remote' in lines[3] else 'On-site'
    return {
                "Country": country,
                "Type": location_type
            }

def process_text(text: str):
    chunks = text.strip().split('\n\n')

    results = []
    for chunk in chunks:
        lines = chunk.split('\n')       

        job_data = {
            "Company": parse_company(lines),
            "Position": parse_position(lines),
            "Location": parse_location(lines)
        }

        

        results.append(job_data)

    return results

def main():
    text = sys.stdin.read()
    structured_data = process_text(text)
    print(json.dumps(structured_data, indent=2))

if __name__ == "__main__":
    main()
