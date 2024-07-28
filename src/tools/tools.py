import re

def extract_name_and_year(title):
    name_match = re.match(r'(.*) \(\d{4}\)', title)
    year_match = re.search(r'\((\d{4})\)', title)
    name = name_match.group(1) if name_match else title
    year = year_match.group(1) if year_match else None
    return name, year