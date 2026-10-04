import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the brutalist CSS block
content = re.sub(r'/\* BRUTALIST SLIDE 1 CSS \*/.*?(?=</style>)', '', content, flags=re.DOTALL)

# Add minimal CSS
new_css = '''
/* MINIMALIST SLIDE 1 CSS */
.minimal-slide {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    background: #ffffff;
    color: #111827;
    display: flex;
    flex-direction: column;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 3vw;
}

.min-inner {
    border: 1px solid #111827;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.min-header {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #111827;
    padding: 1.5vw 2vw;
    font-size: 0.8vw;
    text-transform: uppercase;
    letter-spacing: 0.1vw;
    font-weight: 600;
}

.min-title-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid #111827;
    padding: 2vw;
}

.min-title {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 8vw;
    line-height: 1;
    letter-spacing: -0.1vw;
    margin: 0;
    text-align: center;
    color: #111827;
}

.min-subtitle {
    font-size: 1.2vw;
    color: #4b5563;
    margin-top: 1.5vw;
    text-transform: uppercase;
    letter-spacing: 0.1vw;
    text-align: center;
}

.min-footer {
    display: flex;
    height: 35%;
}

.min-col {
    flex: 1;
    border-right: 1px solid #111827;
    padding: 2vw;
    display: flex;
    flex-direction: column;
}
.min-col:last-child {
    border-right: none;
}

.min-label {
    font-size: 0.75vw;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1vw;
    color: #6b7280;
    margin-bottom: 1.5vw;
}

.min-text {
    font-size: 1vw;
    line-height: 1.6;
    color: #111827;
}
'''

content = content.replace('</style>', new_css + '\n</style>')

new_html = '''<section class="slide active" id="slide-1" style="padding: 0;">
    <div class="minimal-slide">
        <div class="min-inner">
            <!-- Header -->
            <div class="min-header">
                <div>Academic Project Presentation</div>
                <div>System / 2026</div>
            </div>

            <!-- Main Title Area -->
            <div class="min-title-container">
                <div class="min-title">RAILFOD23</div>
                <div class="min-subtitle">Intelligent Railway Foreign Object Detection &amp; Safety Monitoring System</div>
            </div>

            <!-- Footer Details -->
            <div class="min-footer">
                
                <div class="min-col">
                    <div class="min-label">Action Pipeline</div>
                    <div class="min-text" style="font-size: 1.4vw; font-family: Georgia, serif; font-style: italic; color: #4b5563;">
                        Detect.<br>Analyze.<br>Prevent.
                    </div>
                </div>

                <div class="min-col">
                    <div class="min-label">Project Team</div>
                    <div class="min-text">
                        Deepak Jarugula<br>
                        Eekshitha Reddy Bakka<br>
                        Harsha Sai<br>
                        Akshaya<br>
                        Leena
                    </div>
                </div>

                <div class="min-col">
                    <div class="min-label">Details</div>
                    <div class="min-text">
                        Group No: XX<br>
                        Year: 2026<br><br>
                        Department of Computer Science / AI<br>
                        Woxsen University
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>'''

# Replace ANY section with id="slide-1"
content = re.sub(r'<section[^>]*id="slide-1"[^>]*>.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESSFULLY REPLACED SLIDE 1 WITH MINIMALIST DESIGN")
