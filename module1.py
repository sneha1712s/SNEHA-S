import os
import random
import datetime
import json
import re
import csv
import collections
import urllib.request
import pickle
import time
import argparse
import sqlite3
import socket

# Example usage of some built-in modules

# 1. OS module
print("Current directory:", os.getcwd())

# 2. Random module
random_number = random.randint(1, 100)
print("Random number:", random_number)

# 3. Datetime module
current_time = datetime.datetime.now()
print("Current time:", current_time)

# 4. JSON module
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)
print("JSON data:", json_data)

# 5. Regular expression module
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
email = "example@email.com"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

# 6. CSV module
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', 30])
    writer.writerow(['Alice', 25])

# 7. Collections module
counter = collections.Counter('abracadabra')
print("Frequency of each character:", counter)

# 8. urllib module
with urllib.request.urlopen('https://www.example.com') as response:
    html = response.read()
    print("HTML content:", html)

# 9. Pickle module
data_to_pickle = {'name': 'Alice', 'age': 25}
with open('data.pkl', 'wb') as f:
    pickle.dump(data_to_pickle, f)

# 10. Time module
print("Current timestamp:", time.time())

# 11. Argparse module
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='Name of the person')
args = parser.parse_args()
print("Name from command line:", args.name)

# 12. SQLite module
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
conn.commit()
conn.close()

# 13. Socket module
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Hostname:", hostname)
print("IP Address:", ip_address)