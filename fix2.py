import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

slide_2_html = '''
        <!-- Slide 02: Table of Contents -->
        <section class="slide contents-slide" id="slide-2">
            <div class="slide-header">
                <div class="slide-number">02</div>
                <div class="slide-title">Contents <span style="font-size: 1.2vw; color: #cfd8dc; font-weight: 400; text-transform: none; margin-left: 1vw;">Project Presentation Overview</span></div>
            </div>

            <div class="contents-grid">
                <div class="contents-column">
                    <div class="contents-item">
                        <span class="contents-number">01</span>
                        <div class="contents-text">
                            <h2>INTRODUCTION</h2>
                            <p>Problem Statement</p>
                        </div>
                    </div>
                    <div class="contents-item">
                        <span class="contents-number">02</span>
                        <div class="contents-text">
                            <h2>RESEARCH FOUNDATION</h2>
                            <p>Objectives &bull; Research Gap &bull; Literature Review</p>
                        </div>
                    </div>
                    <div class="contents-item">
                        <span class="contents-number">03</span>
                        <div class="contents-text">
                            <h2>PROPOSED SYSTEM</h2>
                            <p>Framework &bull; Methodology &bull; Working</p>
                        </div>
                    </div>
                </div>

                <div class="contents-column">
                    <div class="contents-item">
                        <span class="contents-number">04</span>
                        <div class="contents-text">
                            <h2>AI &amp; SAFETY</h2>
                            <p>Dataset &bull; YOLOv8 &bull; Threat Assessment</p>
                        </div>
                    </div>
                    <div class="contents-item">
                        <span class="contents-number">05</span>
                        <div class="contents-text">
                            <h2>IMPLEMENTATION</h2>
                            <p>ESP32 &bull; AWS &bull; Dashboard &bull; Results</p>
                        </div>
                    </div>
                    <div class="contents-item">
                        <span class="contents-number">06</span>
                        <div class="contents-text">
                            <h2>CONCLUSION</h2>
                            <p>Comparison &bull; Future Scope &bull; References</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Find insertion point: Before id="slide-3"
content = content.replace('<!-- Slide 02: Introduction + Problem Statement -->', slide_2_html + '\n        <!-- Slide 03: Introduction + Problem Statement -->')

# Note: The comments were originally "Slide 02:". My script earlier replaced "Slide {i}:" which didn't match "Slide 02:"
# Let's fix ALL the comments to match the new numbering
comments = [
    ('<!-- Slide 02: Introduction + Problem Statement -->', '<!-- Slide 03: Introduction + Problem Statement -->'),
    ('<!-- Slide 03: Objectives & Research Gap -->', '<!-- Slide 04: Objectives & Research Gap -->'),
    ('<!-- Slide 04: Literature Review -->', '<!-- Slide 05: Literature Review -->'),
    ('<!-- Slide 05: Proposed Framework -->', '<!-- Slide 06: Proposed Framework -->'),
    ('<!-- Slide 06: Methodology / Working -->', '<!-- Slide 07: Methodology / Working -->'),
    ('<!-- Slide 07: Dataset & AI Model -->', '<!-- Slide 08: Dataset & AI Model -->'),
    ('<!-- Slide 08: Threat Assessment & Safety Control -->', '<!-- Slide 09: Threat Assessment & Safety Control -->'),
    ('<!-- Slide 09: AWS Cloud & Safety Operations Center -->', '<!-- Slide 10: AWS Cloud & Safety Operations Center -->'),
    ('<!-- Slide 10: Implementation & Results -->', '<!-- Slide 11: Implementation & Results -->'),
    ('<!-- Slide 11: Implementation & Results -->', '<!-- Slide 11: Implementation & Results -->'), # wait, it was slide 10 originally?
    ('<!-- Slide 12: Model & System Comparison -->', '<!-- Slide 12: Model & System Comparison -->'),
    ('<!-- Slide 13: Conclusion & Future Scope -->', '<!-- Slide 13: Conclusion & Future Scope -->'),
]
for old, new in comments:
    content = content.replace(old, new)
    
# Wait, let's just use regex to fix comments and insert the HTML before id="slide-3"
# The most reliable way:
idx = content.find('<section class="slide" id="slide-3">')
if idx != -1:
    # Find the comment right before it
    comment_idx = content.rfind('<!--', 0, idx)
    if comment_idx != -1:
        content = content[:comment_idx] + slide_2_html + '\n        ' + content[comment_idx:]
    else:
        content = content[:idx] + slide_2_html + '\n        ' + content[idx:]

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
