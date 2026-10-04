import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix slide 5
content = re.sub(r'(<section class="slide" id="slide-5">.*?)<div class="slide-number">04</div>', r'\1<div class="slide-number">05</div>', content, flags=re.DOTALL)

# Fix slide 6
content = re.sub(r'(<section[^>]*id="slide-6"[^>]*>.*?)<div class="slide-number">05</div>', r'\1<div class="slide-number">06</div>', content, flags=re.DOTALL)

# Fix slide 7
content = re.sub(r'(<section class="slide" id="slide-7">.*?)<div class="slide-number">06</div>', r'\1<div class="slide-number">07</div>', content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("fixed slide numbers")
