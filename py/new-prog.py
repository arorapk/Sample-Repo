from msilib import change_sequence
import requests

r = requests.get("https://oracle.com")
print(r.status_code)
print("connected to server!")
