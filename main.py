import pandas as pd
import json

# Read JSON data with specified encoding
with open('response_1716142366470.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)