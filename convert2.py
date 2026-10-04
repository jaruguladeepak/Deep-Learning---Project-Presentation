import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert to Dark Theme
content = content.replace('--bg-color: #f4f6f9;', '--bg-color: #0b0f19;')
content = content.replace('--text-color: #111827;', '--text-color: #ffffff;')
content = content.replace('--accent-cyan: #0284c7;', '--accent-cyan: #00e5ff;')
content = content.replace('--accent-blue: #2563eb;', '--accent-blue: #2979ff;')
content = content.replace('--accent-red: #e11d48;', '--accent-red: #ff1744;')
content = content.replace('--glass-bg: rgba(255, 255, 255, 0.85);', '--glass-bg: rgba(11, 15, 25, 0.7);')
content = content.replace('--glass-border: rgba(0, 0, 0, 0.15);', '--glass-border: rgba(255, 255, 255, 0.1);')
content = content.replace('background-color: #e5e7eb;', 'background-color: #000;')

content = content.replace('color: var(--text-color);', 'color: #fff;')
content = content.replace('color: #4b5563;', 'color: #cfd8dc;')
content = content.replace('rgba(0, 0, 0, 0.5)', 'rgba(255, 255, 255, 0.5)')
content = content.replace('rgba(0,0,0,0.5)', 'rgba(255,255,255,0.5)')
content = content.replace('rgba(0,0,0,0.6)', 'rgba(255,255,255,0.6)')
content = content.replace('rgba(0, 0, 0, 0.6)', 'rgba(255, 255, 255, 0.3)')
content = content.replace('rgba(0,0,0,0.2)', 'rgba(255,255,255,0.2)')
content = content.replace('rgba(0, 0, 0, 0.2)', 'rgba(255, 255, 255, 0.2)')
content = content.replace('rgba(0, 0, 0, 0.1)', 'rgba(255, 255, 255, 0.1)')
content = content.replace('rgba(0,0,0,0.1)', 'rgba(255,255,255,0.1)')
content = content.replace('rgba(0, 0, 0, 0.05)', 'rgba(255, 255, 255, 0.05)')
content = content.replace('rgba(0,0,0,0.05)', 'rgba(255,255,255,0.05)')
content = content.replace('rgba(0,0,0,0.02)', 'rgba(255,255,255,0.02)')
content = content.replace('rgba(0,0,0,0.03)', 'rgba(255,255,255,0.03)')
content = content.replace('rgba(0, 0, 0, 0.8)', 'rgba(255, 255, 255, 0.8)')
content = content.replace('color: #059669', 'color: #00e676')
content = content.replace('border-color: #059669', 'border-color: #00e676')
content = content.replace('rgba(5, 150, 105', 'rgba(0, 230, 118')
content = content.replace('rgba(217, 119, 6', 'rgba(255, 235, 59')
content = content.replace('#d97706', '#ffd600')
content = content.replace('background: rgba(0,0,0,0.05);', 'background: rgba(0,0,0,0.5);')
content = content.replace('border-left-color: #059669;', 'border-left-color: #00e676;')
content = content.replace('color:var(--accent-blue)', 'color:var(--accent-cyan)')
content = content.replace('color: var(--accent-blue)', 'color: var(--accent-cyan)')
content = content.replace('color: #e11d48', 'color: var(--accent-red)')

# 2. Disable All Animations Globally in CSS
override_css = '''
        /* OVERRIDE TO DISABLE ALL ANIMATIONS AND TRANSITIONS */
        * {
            animation: none !important;
            transition: none !important;
            transform: none !important;
        }
        
        .slide {
            transform: none !important;
        }

        .anim-item {
            opacity: 1 !important;
            transform: none !important;
            animation: none !important;
            transition: none !important;
        }

        .slide.active {
            opacity: 1 !important;
        }

        /* Slide 2 Specific CSS */
        .contents-slide {
            display: flex;
            flex-direction: column;
        }
        
        .contents-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4vw;
            margin-top: 2vw;
            flex: 1;
        }

        .contents-column {
            display: flex;
            flex-direction: column;
            gap: 2vw;
        }

        .contents-item {
            display: flex;
            align-items: flex-start;
            gap: 1.5vw;
            padding: 1.5vw 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .contents-number {
            font-size: 2vw;
            font-weight: 700;
            color: var(--accent-cyan);
            min-width: 3vw;
        }
        
        .contents-text {
            display: flex;
            flex-direction: column;
        }

        .contents-item h2 {
            margin: 0;
            font-size: 1.4vw;
            letter-spacing: 0.08em;
            color: #fff;
            text-transform: uppercase;
        }

        .contents-item p {
            margin: 0.5vw 0 0;
            color: rgba(255,255,255,0.6);
            font-size: 1vw;
        }
'''
content = content.replace('</style>', override_css + '\n    </style>')

# 3. Renumber slides from 12 back down to 2
for i in range(12, 1, -1):
    content = content.replace(f'id="slide-{i}"', f'id="slide-{i+1}"')
    content = content.replace(f'<div class="slide-number">{i}</div>', f'<div class="slide-number">{i+1}</div>')
    # Use re.sub to catch the comment blocks for slides as well
    content = re.sub(rf'Slide {i}:', f'Slide {i+1}:', content)
    # Note: I am purposely NOT touching '02 | OBJECTIVES', etc because they might not exist like that. Wait. The user requested to renumber in the prompt, but it's mainly just the ID and the slide number element.
    # The actual titles on the slide header for slides 3, 4, 5 don't have numbers in the original code, only in the user's prompt as '02 | CONTENTS'

# 4. Inject Slide 2 (Contents)
slide_2_html = '''
        <!-- Slide 2: Table of Contents -->
        <section class="slide contents-slide" id="slide-2">
            <div class="slide-header">
                <div class="slide-number">2</div>
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
# Find insertion point: after </section> of slide-1
content = content.replace('<!-- Slide 3: Introduction + Problem Statement -->', slide_2_html + '\n        <!-- Slide 3: Introduction + Problem Statement -->')

# 5. Update Total Slides to 13
content = content.replace('01 / 12', '01 / 13')
content = content.replace('const totalSlides = 12;', 'const totalSlides = 13;')

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
