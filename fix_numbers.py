import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix id="slide3" to id="slide-3"
content = content.replace('id="slide3"', 'id="slide-3"')

# Regex to find all slide numbers and fix them
def fix_slide_numbers(match):
    # Match contains the entire slide section up to slide-number
    # We want to match: <section class="slide" id="slide-X"> ... <div class="slide-number">YY</div>
    # But it's easier to find id="slide-(\d+)" and then replace the next slide-number
    pass

import re
# We can just iterate over each slide and fix its slide-number
slides = re.split(r'(<section [^>]*id="slide-\d+"[^>]*>)', content)
# slides[0] is everything before the first section
# slides[1] is <section ... id="slide-2">
# slides[2] is the content of slide 2
# etc.

new_content = slides[0]
for i in range(1, len(slides), 2):
    section_tag = slides[i]
    slide_content = slides[i+1]
    
    # Extract the number from id="slide-X"
    m = re.search(r'id="slide-(\d+)"', section_tag)
    if m:
        slide_num = int(m.group(1))
        # Format as 02, 03, etc.
        formatted_num = f"{slide_num:02d}"
        
        # Replace the slide-number div in this slide's content
        slide_content = re.sub(r'<div class="slide-number">\d+</div>', f'<div class="slide-number">{formatted_num}</div>', slide_content, count=1)
        
    new_content += section_tag + slide_content

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("done")
