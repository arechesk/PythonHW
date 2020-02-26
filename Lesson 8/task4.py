import re

if __name__ == "__main__":
    pattern = r"""\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}"""
    match = re.search(pattern, "1991-04-12T10:44:11+07:08 (ISO формат)")
    print(match.group(0))

