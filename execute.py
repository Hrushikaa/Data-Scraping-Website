
import subprocess

subprocess.run("python3 twittertrends.py && python3 youtubetrends.py && python3 cryptotrends.py", shell=True)
subprocess.run("cd merger python3 merge.py && python3 merge2.py && python3 merge3.py", shell=True)
