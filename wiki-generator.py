import requests
import subprocess

title = "Electromagnetism"
response = requests.get(
	url=f"https://en.wikipedia.org/w/index.php?title={title}&action=raw",
)

with open(title+".wiki", "wb") as f:
	f.write(response.content)

fileout = title + ".md"
args = ['pandoc', '-s', title+".wiki", "-o", title+".md"]
subprocess.check_call(args)