import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
/* BRUTALIST SLIDE 1 CSS */
.brutalist-slide {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    background: #e2e8f0; 
    color: #000000;
    display: flex;
    flex-direction: column;
    font-family: "Arial Black", "Impact", sans-serif;
    padding: 2vw;
}

.brut-inner {
    border: 0.4vw solid #000;
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #ffffff;
    box-shadow: 0.8vw 0.8vw 0 #000;
}

.brut-header {
    display: flex;
    justify-content: space-between;
    border-bottom: 0.4vw solid #000;
    padding: 1vw 2vw;
    font-size: 1.2vw;
    text-transform: uppercase;
    background: #0000FF;
    color: #FFF;
}

.brut-title-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-bottom: 0.4vw solid #000;
    padding: 2vw;
    background: #FFFF00; /* Harsh yellow */
}

.brut-title {
    font-size: 11vw;
    line-height: 0.85;
    letter-spacing: -0.4vw;
    margin: 0;
    text-align: center;
    color: #000;
}

.brut-subtitle {
    font-size: 2.2vw;
    background: #000;
    color: #FFF;
    padding: 0.5vw 1.5vw;
    margin-top: 2vw;
    text-transform: uppercase;
    text-align: center;
    border: 0.2vw solid #000;
}

.brut-footer {
    display: flex;
    height: 30%;
    background: #FFF;
}

.brut-col {
    flex: 1;
    border-right: 0.4vw solid #000;
    padding: 1.5vw 2vw;
    display: flex;
    flex-direction: column;
}
.brut-col:last-child {
    border-right: none;
}

.brut-label {
    font-family: 'Courier New', Courier, monospace;
    font-weight: 900;
    font-size: 1vw;
    margin-bottom: 1vw;
    background: #000;
    color: #FFF;
    display: inline-block;
    padding: 0.2vw 0.5vw;
    align-self: flex-start;
}

.brut-text {
    font-size: 1.1vw;
    line-height: 1.4;
    text-transform: uppercase;
    font-family: "Arial Black", "Impact", sans-serif;
}
'''

content = content.replace('</style>', new_css + '\n</style>')

new_html = '''<section class="slide active" id="slide-1" style="padding: 0;">
    <div class="brutalist-slide">
        <div class="brut-inner">
            <!-- Header -->
            <div class="brut-header">
                <div>ACADEMIC PROJECT</div>
                <div>SYSTEM / 2026</div>
            </div>

            <!-- Main Title Area -->
            <div class="brut-title-container">
                <div class="brut-title">RAILFOD23</div>
                <div class="brut-subtitle">INTELLIGENT RAILWAY DETECTOR</div>
            </div>

            <!-- Footer Details -->
            <div class="brut-footer">
                
                <div class="brut-col">
                    <div class="brut-label">ACTION</div>
                    <div class="brut-text" style="font-size: 2vw; color: #0000FF; line-height: 1.1;">
                        DETECT.<br>ANALYZE.<br>PREVENT.
                    </div>
                </div>

                <div class="brut-col">
                    <div class="brut-label">TEAM_MEMBERS</div>
                    <div class="brut-text">
                        DEEPAK JARUGULA<br>
                        EEKSHITHA REDDY BAKKA<br>
                        HARSHA SAI<br>
                        AKSHAYA<br>
                        LEENA
                    </div>
                </div>

                <div class="brut-col">
                    <div class="brut-label">META_DATA</div>
                    <div class="brut-text">
                        GROUP NO: XX<br>
                        YEAR: 2026<br><br>
                        DEPARTMENT OF COMP_SCI / AI<br>
                        WOXSEN UNIVERSITY
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>'''

# Replace slide-1
content = re.sub(r'<section class="slide(?: active)?" id="slide-1">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done replacing HTML")
