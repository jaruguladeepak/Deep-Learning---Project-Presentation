import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Strip out the old #slide-1 CSS block
content = re.sub(r'#slide-1\s*\{[^}]*\}', '', content)
content = re.sub(r'#slide-1::before\s*\{[^}]*\}', '', content)
content = re.sub(r'#slide-1::after\s*\{[^}]*\}', '', content)

# 2. Add the new CSS before </style>
new_css = '''
/* New Slide 1 CSS */
.title-slide {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    padding: 5vw 7vw 4vw;
    background: #F7F8FA;
    color: #0B1F3A;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.title-kicker {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.85vw;
    font-weight: 700;
    letter-spacing: 0.16vw;
    color: #2563EB;
    margin-bottom: 1.2vw;
}

.title-main {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 6vw;
    line-height: 0.95;
    font-weight: 700;
    letter-spacing: 0.04vw;
    color: #0B1F3A;
}

.title-rule {
    width: 7vw;
    height: 3px;
    background: #2563EB;
    margin: 1.4vw 0 1.5vw;
}

.title-subtitle {
    font-family: "Times New Roman", Times, serif;
    font-size: 1.8vw;
    line-height: 1.35;
    color: #34465A;
}

.title-tags {
    margin-top: 1.5vw;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.95vw;
    font-weight: 700;
    letter-spacing: 0.08vw;
    color: #2563EB;
}

.title-footer {
    margin-top: 4vw;
}

.team-label {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.8vw;
    font-weight: 700;
    letter-spacing: 0.12vw;
    color: #2563EB;
    margin-bottom: 0.5vw;
}

.team-names {
    font-family: "Times New Roman", Times, serif;
    font-size: 1vw;
    line-height: 1.5;
    color: #1F334A;
}

.institution {
    margin-top: 0.8vw;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.85vw;
    line-height: 1.4;
    color: #667487;
}
'''
content = content.replace('</style>', new_css + '\n</style>')

# 3. Replace the HTML for Slide 1
new_html = '''<section class="slide" id="slide-1">
    <div class="title-slide">
        <div class="title-kicker">
            ACADEMIC PROJECT PRESENTATION
        </div>

        <div class="title-main">
            RAILFOD23
        </div>

        <div class="title-rule"></div>

        <div class="title-subtitle">
            Intelligent Railway Foreign Object Detection<br>
            &amp; Safety Monitoring System
        </div>

        <div class="title-tags">
            AI &nbsp;&bull;&nbsp; EDGE SAFETY &nbsp;&bull;&nbsp; CLOUD MONITORING
        </div>

        <div class="title-footer">
            <div class="team-block">
                <div class="team-label">PROJECT TEAM</div>
                <div class="team-names">
                    Deepak Jarugula<br>
                    Eekshitha Reddy Bakka<br>
                    Harsha Sai<br>
                    Akshaya<br>
                    Leena
                </div>

                <div class="institution">
                    Department of Computer Science / AI<br>
                    Woxsen University
                </div>
            </div>
        </div>
        
        <!-- absolute page number (optional if it's not rendered via JS for slide 1) -->
        <div style="position: absolute; bottom: 2vw; right: 2vw; font-family: Georgia, 'Times New Roman', serif; font-size: 1.1vw; color: #64748b;">01 / 13</div>
    </div>
</section>'''

# Replace the HTML block using non-greedy regex
content = re.sub(r'<section class="slide" id="slide-1">.*?</section>', new_html, content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide 1 completely redesigned.")
