file_path = "mango.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")