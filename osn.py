import subprocess


files = ["new.py", "main.py"]
for file in files:
    subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)