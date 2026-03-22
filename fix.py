import base64, re

with open('images/band_group.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')
data_uri = f'data:image/jpeg;base64,{b64}'

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace hero-bg-photo CSS: remove background url, just keep position
old_css = re.search(r'\.hero-bg-photo \{[^}]+\}', html).group()
new_css = """  .hero-bg-photo {
    position: absolute; inset: 0; z-index: 0; overflow: hidden;
  }
  .hero-bg-photo img {
    width: 100%; height: 100%; object-fit: cover; object-position: center 30%;
  }"""
html = html.replace(old_css, new_css)

# 2. Replace hero-bg-photo div with img inside
html = html.replace(
    '<div class="hero-bg-photo"></div>',
    f'<div class="hero-bg-photo"><img src="{data_uri}" alt="Проект Кобра на сцене"></div>'
)

# 3. Also fix gallery img tags - replace data URI src with file path for ones that don't exist
# and ensure the band_group in gallery uses data uri too
# Already done from previous embed

with open('index.html', 'w') as f:
    f.write(html)

print('Done! Hero now uses <img> tag instead of CSS background')
