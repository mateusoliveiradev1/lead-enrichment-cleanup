import sys, re

def validate(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print(f"VALID: {email}")
        sys.exit(0)
    else:
        print(f"INVALID_FORMAT: {email}")
        sys.exit(1)

if __name__ == "__main__":
    validate(sys.argv[1])
