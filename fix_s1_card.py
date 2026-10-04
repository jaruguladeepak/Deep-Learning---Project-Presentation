import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update CSS for title-card
css_replace = '''
        .title-card {
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 24px;
            padding: 4vw 6vw;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
            margin-bottom: 2vw;
            text-align: center;
            width: 85%;
            max-width: 85vw;
        }

        h1.main-title {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 6vw;
            font-weight: 700;
            letter-spacing: 0.2vw;
            margin-bottom: 1vw;
            color: #ffffff;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }

        h2.subtitle {
            font-size: 2vw;
            color: #f8fafc;
            font-weight: 400;
            line-height: 1.4;
            margin-bottom: 2vw;
            font-family: Georgia, "Times New Roman", serif;
            text-shadow: 0 2px 10px rgba(0,0,0,0.8);
        }

        .tagline {
            font-size: 1.1vw;
            color: #67e8f9;
            letter-spacing: 0.3vw;
            text-transform: uppercase;
            font-weight: 700;
            text-shadow: 0 2px 8px rgba(0,0,0,0.8);
        }

        .author-list {
            display: flex;
            justify-content: space-around;
            width: 100%;
            color: #ffffff;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 3vw;
            border-top: 1px solid rgba(255,255,255,0.15);
            padding-top: 3vw;
        }

        .author-group {
            text-align: center;
        }

        .author-label {
            font-size: 0.9vw;
            color: #67e8f9;
            text-transform: uppercase;
            letter-spacing: 0.1vw;
            margin-bottom: 1vw;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }

        .author-names {
            font-size: 1.2vw;
            line-height: 1.8;
            color: #ffffff;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }
'''

content = re.sub(r'\.title-card\s*\{.*?\.author-names\s*\{[^}]+\}', css_replace.strip(), content, flags=re.DOTALL)

# Update HTML structure to put author list inside title-card
html_start = content.find('<section class="slide active" id="slide-1">')
html_end = content.find('<!-- Slide 02: Table of Contents -->')

new_html = '''<section class="slide active" id="slide-1">
            <div class="slide-content">
                <div class="title-card">
                    <h1 class="main-title">RAILFOD23</h1>
                    <h2 class="subtitle">Intelligent Railway Foreign Object Detection<br>&amp; Safety Monitoring System</h2>
                    <div class="tagline">Detect &bull; Analyze &bull; Prevent</div>

                    <div class="author-list">
                        <div class="author-group">
                            <div class="author-label">Group No.</div>
                            <div class="author-names">XX</div>
                        </div>
                        
                        <div class="author-group">
                            <div class="author-label">Team Members</div>
                            <div class="author-names">
                                Deepak Jarugula<br>
                                Eekshitha Reddy Bakka<br>
                                Harsha Sai<br>
                                Akshaya<br>
                                Leena
                            </div>
                        </div>
                        
                        <div class="author-group">
                            <div class="author-label">Year</div>
                            <div class="author-names">
                                2026<br>
                                <span style="font-size: 0.9vw; opacity: 0.7;">Department / University Name</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        '''

if html_start != -1 and html_end != -1:
    content = content[:html_start] + new_html + content[html_end:]

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
