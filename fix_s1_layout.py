import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Slide 1 CSS block
# We know it starts with /* Slide 1 Specifics */
# and ends right before /* Slide 2 Specifics */ or /* Slide 2 REDESIGN
start_idx = content.find('/* Slide 1 Specifics */')
end_idx = content.find('/* SLIDE 2 REDESIGN - EDITORIAL LIST */')

if start_idx != -1 and end_idx != -1:
    old_css = content[start_idx:end_idx]
    
    new_css = '''/* Slide 1 Specifics */
        #slide-1 {
            background-image: url('assets/images/title.jpg');
            background-size: cover;
            background-position: center;
            justify-content: center;
            align-items: center;
        }

        #slide-1::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.85); /* Deep elegant dark overlay */
            z-index: 1;
        }

        .slide-content {
            position: relative;
            z-index: 2;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .title-card {
            background: #ffffff;
            padding: 5vw 8vw;
            border-top: 6px solid var(--accent-blue);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            margin-bottom: 4vw;
            text-align: center;
            width: 80%;
            max-width: 80vw;
        }

        h1.main-title {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 5.5vw;
            font-weight: 700;
            letter-spacing: 0.1vw;
            margin-bottom: 1.5vw;
            color: #111827; /* Dark navy/charcoal */
        }

        h2.subtitle {
            font-size: 2vw;
            color: #4b5563;
            font-weight: 400;
            line-height: 1.4;
            margin-bottom: 2vw;
            font-family: Georgia, "Times New Roman", serif;
        }

        .tagline {
            font-size: 1.1vw;
            color: var(--accent-blue);
            letter-spacing: 0.2vw;
            text-transform: uppercase;
            font-weight: 700;
        }

        .author-list {
            display: flex;
            justify-content: space-around;
            width: 80%;
            color: #f8fafc;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 1vw;
            border-top: 1px solid rgba(255,255,255,0.2);
            padding-top: 2.5vw;
        }

        .author-group {
            text-align: center;
        }

        .author-label {
            font-size: 0.9vw;
            color: var(--accent-cyan);
            text-transform: uppercase;
            letter-spacing: 0.1vw;
            margin-bottom: 1vw;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
        }

        .author-names {
            font-size: 1.2vw;
            line-height: 1.8;
            color: #e2e8f0;
        }
        
        '''
    
    content = content[:start_idx] + new_css + content[end_idx:]

# Now replace the HTML for Slide 1
html_start = content.find('<section class="slide active" id="slide-1">')
html_end = content.find('<!-- Slide 02: Table of Contents -->')

new_html = '''<section class="slide active" id="slide-1">
            <div class="slide-content">
                <div class="title-card">
                    <h1 class="main-title">RAILFOD23</h1>
                    <h2 class="subtitle">Intelligent Railway Foreign Object Detection<br>&amp; Safety Monitoring System</h2>
                    <div class="tagline">Detect &bull; Analyze &bull; Prevent</div>
                </div>

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
        </section>
        
        '''

if html_start != -1 and html_end != -1:
    content = content[:html_start] + new_html + content[html_end:]

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
