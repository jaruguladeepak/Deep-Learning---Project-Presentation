import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Slide 8 flex-direction
content = content.replace('<div class="slide-body" style="display: flex; gap: 3vw; height: 100%;">', '<div class="slide-body" style="display: flex; flex-direction: row; gap: 3vw; height: 100%;">')

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
