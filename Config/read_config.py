import json
import os

with open("config/values.json", encoding="utf-8") as file:
    data = json.load(file)

with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write(f"a={data['a']}\n")
    output.write(f"fruits={data['fruits']}\n")