import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

slides = re.findall(r'<section[^>]*id="(slide-\d+)"[^>]*>.*?(?:<div class="slide-number">([^<]+)</div>)?.*?(?:<div class="slide-title">([^<]+))?', content, flags=re.DOTALL | re.IGNORECASE)

for match in slides:
    print(f"ID: {match[0]}, Number: {match[1]}, Title: {match[2][:30] if match[2] else 'None'}")
