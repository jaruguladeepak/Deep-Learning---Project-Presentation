import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide active" id="slide-1" style="padding: 0;">
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

# Replace slide-1 by matching class="slide" or class="slide active"
content = re.sub(r'<section class="slide(?: active)?" id="slide-1">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done replacing HTML")
