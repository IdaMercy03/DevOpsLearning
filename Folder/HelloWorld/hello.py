
# def main():
#     print("Hello World!")
#     print("This is my child action.")
#     print("Executed using the parent workflow.")

# if __name__ == "__main__":
#     main()

import os

def main():
    fruits = os.environ.get("FRUITS", "")

    print("Python output:")
    print(f"fruits = {fruits}")

if __name__ == "__main__":
    main()
