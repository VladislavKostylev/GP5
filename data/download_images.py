import os
import pandas as pd
import requests

df = pd.read_csv('data/ozon_mens_clothing_2025.csv', sep=';', encoding='utf-8-sig', usecols=['SKU', 'Niche', 'Thumb'], nrows=2_000_000)
df = df.dropna(subset=['Thumb', 'Niche'])
df = df[df['Thumb'].str.startswith('http')]
df['Niche'] = df['Niche'].str.split('/').str[-1].str.strip()
df = df[df['Niche'].str.contains('мужск', case=False, na=False)]

top = df['Niche'].value_counts().head(8).index
parts = []
for label, niche in enumerate(top):
    part = df[df['Niche'] == niche].head(3750).copy()
    part['label'] = label
    parts.append(part[['SKU', 'Niche', 'Thumb', 'label']])

index = pd.concat(parts, ignore_index=True)
index.to_csv('data/cnn_index.csv', index=False)

os.makedirs('data/images', exist_ok=True)

for _, row in index.iterrows():
    path = 'data/images/' + str(row['SKU']) + '.jpg'
    if os.path.exists(path):
        continue
    try:
        request = requests.get(row['Thumb'], timeout=10)
        if request.status_code == 200:
            with open(path, 'wb') as file:
                file.write(request.content)
    except Exception:
        pass

print('готово')