import pytest
import json
from text_parser import process_text

input_text_1 = """Ironclad, Inc.
Senior/Staff Software Engineer - AI
Ironclad
United States (Remote)
 Actively recruiting
Posted 13h ago"""
expected_json_1 = """[{
    "Company": {
      "Full Name": "Ironclad, Inc.",
      "Name": "Ironclad",
      "Hiring Status": "Actively recruiting"
    },
    "Position": {
      "Title": "Staff Software Engineer",
      "Level": "Senior",
      "Type": "AI"
    },
    "Location": {
      "Country": "United",
      "Type": "Remote"
    }
  }]"""
use_case_1 = (input_text_1, expected_json_1)

input_2 = """Pluralsight, LLC
Software Engineer (Python/Java/AWS)
Pluralsight
United States (Remote)
Posted 3d ago"""
output_2 = """[{
    "Company": {
      "Full Name": "Pluralsight, LLC",
      "Name": "Pluralsight",
      "Hiring Status": null
    },
    "Position": {
      "Title": "Software Engineer",
      "Level": null,
      "Type": "Python/Java/AWS"
    },
    "Location": {
      "Country": "United",
      "Type": "Remote"
    }
  }]"""
use_case_2 = (input_2, output_2)

test_data = [use_case_1, use_case_2]

@pytest.mark.parametrize("input_text, json_string", test_data)
def test_process_text(input_text, json_string):
    expected_json = json.loads(json_string)
    output = process_text(input_text)
    assert output == expected_json
