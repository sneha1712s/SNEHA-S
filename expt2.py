file_path = "balajis.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Closing the file.")
