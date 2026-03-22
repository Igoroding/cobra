import base64

with open('images/band_group.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')

data_uri = f'data:image/jpeg;base64,{b64}'

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace("url('images/band_group.jpg')", f"url('{data_uri}')")
html = html.replace('src="images/band_group.jpg"', f'src="{data_uri}"')

with open('index.html', 'w') as f:
    f.write(html)

print(f'Done! Embedded {len(b64)} bytes of base64')
