import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Strip any existing title-slide or slide-1 CSS
content = re.sub(r'\.title-slide\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-kicker\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-main\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-rule\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-subtitle\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-tags\s*\{[^}]*\}', '', content)
content = re.sub(r'\.title-footer\s*\{[^}]*\}', '', content)
content = re.sub(r'\.team-label\s*\{[^}]*\}', '', content)
content = re.sub(r'\.team-names\s*\{[^}]*\}', '', content)
content = re.sub(r'\.institution\s*\{[^}]*\}', '', content)

# Remove old main-title CSS that might be causing the glow
content = re.sub(r'h1\.main-title\s*\{[^}]*\}', '', content)

# Add the new CSS provided by the user
new_css = '''
/* New Slide 1 Academic CSS */
.title-slide {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    padding: 4.5vw 7vw 3.5vw;
    background: #F7F8FA;
    color: #0B1F3A;
    display: flex;
    flex-direction: column;
}

.title-kicker {
    text-align: center;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.82vw;
    font-weight: 700;
    letter-spacing: 0.14vw;
    color: #2563EB;
    margin-bottom: 1vw;
}

.title-main {
    text-align: center;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 5.5vw;
    line-height: 1;
    font-weight: 700;
    color: #0B1F3A;
    letter-spacing: 0.03vw;
    text-shadow: none; /* Force remove any glow */
}

.title-rule {
    width: 6vw;
    height: 2px;
    background: #2563EB;
    margin: 1.1vw auto 1.2vw;
}

.title-subtitle {
    text-align: center;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.55vw;
    line-height: 1.4;
    color: #34465A;
}

.title-tags {
    text-align: center;
    margin-top: 1.2vw;
    font-family: "Times New Roman", Times, serif;
    font-size: 0.9vw;
    font-weight: 700;
    letter-spacing: 0.08vw;
    color: #2563EB;
}

.title-info {
    margin-top: auto;
    padding-top: 2.5vw;
    border-top: 1px solid #D9E0E8;
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    column-gap: 8vw;
}

.info-label {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.75vw;
    font-weight: 700;
    letter-spacing: 0.1vw;
    color: #2563EB;
    margin-bottom: 0.55vw;
}

.team-names {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.95vw;
    line-height: 1.55;
    color: #0B1F3A;
}

.detail-row {
    margin-bottom: 0.8vw;
}

.detail-value {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.95vw;
    color: #0B1F3A;
}

.detail-secondary {
    color: #64748B;
}
'''
content = content.replace('</style>', new_css + '\n</style>')

new_html = '''<section class="slide" id="slide-1" style="padding: 0;">
    <div class="title-slide">
        
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; padding-bottom: 2vw;">
            <div class="title-kicker">ACADEMIC PROJECT PRESENTATION</div>
            <div class="title-main">RAILFOD23</div>
            <div class="title-rule"></div>
            <div class="title-subtitle">
                Intelligent Railway Foreign Object Detection<br>
                &amp; Safety Monitoring System
            </div>
            <div class="title-tags">DETECT &bull; ANALYZE &bull; PREVENT</div>
        </div>

        <div class="title-info">
            <!-- Left: Team -->
            <div>
                <div class="info-label">PROJECT TEAM</div>
                <div class="team-names">
                    Deepak Jarugula<br>
                    Eekshitha Reddy Bakka<br>
                    Harsha Sai<br>
                    Akshaya<br>
                    Leena
                </div>
            </div>
            
            <!-- Right: Details -->
            <div>
                <div class="detail-row">
                    <div class="info-label">GROUP NO.</div>
                    <div class="detail-value">XX</div>
                </div>
                <div class="detail-row">
                    <div class="info-label">YEAR</div>
                    <div class="detail-value">2026</div>
                </div>
                <div class="detail-row">
                    <div class="info-label">DEPARTMENT / UNIVERSITY</div>
                    <div class="detail-value">
                        Department of Computer Science / AI<br>
                        <span class="detail-secondary">Woxsen University</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Slide Number (absolute) -->
        <div style="position: absolute; bottom: 2vw; right: 2vw; font-family: Georgia, 'Times New Roman', serif; font-size: 1.1vw; color: #64748b;">01 / 13</div>
    </div>
</section>'''

# Replace slide-1
content = re.sub(r'<section class="slide" id="slide-1">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
