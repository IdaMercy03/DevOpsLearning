

import os

def main():
    fruits = os.environ.get("FRUITS", "")
    print(f"fruits = {fruits}")

if __name__ == "__main__":
    main()
