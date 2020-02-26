import re

if __name__ == "__main__":
    pattern = r"""^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,12}$"""
    passwd = "aaZZa44@"
    print(re.match(pattern, passwd))
