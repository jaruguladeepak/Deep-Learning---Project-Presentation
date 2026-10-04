import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Strip out the previous Slide 2 CSS
css_pattern = r'/\* SLIDE 2 REDESIGN - STEP BY STEP \*/.*?(?=</style>)'
content = re.sub(css_pattern, '', content, flags=re.DOTALL)

# Add new editorial CSS
new_css = '''
        /* SLIDE 2 REDESIGN - EDITORIAL LIST */
        .s2-editorial-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
        }

        .s2-editorial-list {
            display: grid;
            grid-template-columns: 4vw 1fr;
            column-gap: 2vw;
            width: 75%;
            font-family: Georgia, "Times New Roman", serif;
        }

        .s2-row {
            display: contents; /* Allows grid layout to ignore this wrapper */
        }

        .s2-num {
            font-size: 2.2vw;
            color: var(--accent-blue);
            font-weight: 700;
            text-align: right;
            padding-top: 1.5vw;
            padding-bottom: 1.5vw;
            border-bottom: 1px solid rgba(0,0,0,0.06);
        }

        .s2-text {
            padding-top: 1.5vw;
            padding-bottom: 1.5vw;
            border-bottom: 1px solid rgba(0,0,0,0.06);
        }
        
        .s2-row:last-child .s2-num,
        .s2-row:last-child .s2-text {
            border-bottom: none;
        }

        .s2-head {
            font-size: 1.5vw;
            color: var(--text-color);
            font-weight: 700;
            margin-bottom: 0.4vw;
            text-transform: uppercase;
            letter-spacing: 0.05vw;
        }

        .s2-sub {
            font-size: 1.2vw;
            color: #64748b;
        }
'''

content = content.replace('</style>', new_css + '\n    </style>')

new_slide_2 = '''
        <section class="slide contents-slide" id="slide-2">
            <div class="slide-header">
                <div class="slide-number">02</div>
                <div class="slide-title">Contents <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">Project Presentation Overview</span></div>
            </div>

            <div class="slide-body">
                <div class="s2-editorial-container">
                    <div class="s2-editorial-list">
                        
                        <div class="s2-row">
                            <div class="s2-num">01</div>
                            <div class="s2-text">
                                <div class="s2-head">INTRODUCTION</div>
                                <div class="s2-sub">Problem Statement</div>
                            </div>
                        </div>

                        <div class="s2-row">
                            <div class="s2-num">02</div>
                            <div class="s2-text">
                                <div class="s2-head">RESEARCH FOUNDATION</div>
                                <div class="s2-sub">Objectives &bull; Research Gap &bull; Literature Review</div>
                            </div>
                        </div>

                        <div class="s2-row">
                            <div class="s2-num">03</div>
                            <div class="s2-text">
                                <div class="s2-head">PROPOSED SYSTEM</div>
                                <div class="s2-sub">Framework &bull; Methodology &bull; Working</div>
                            </div>
                        </div>

                        <div class="s2-row">
                            <div class="s2-num">04</div>
                            <div class="s2-text">
                                <div class="s2-head">AI &amp; SAFETY</div>
                                <div class="s2-sub">Dataset &bull; YOLOv8 &bull; Threat Assessment</div>
                            </div>
                        </div>

                        <div class="s2-row">
                            <div class="s2-num">05</div>
                            <div class="s2-text">
                                <div class="s2-head">IMPLEMENTATION</div>
                                <div class="s2-sub">ESP32 &bull; AWS &bull; Dashboard &bull; Results</div>
                            </div>
                        </div>

                        <div class="s2-row">
                            <div class="s2-num">06</div>
                            <div class="s2-text">
                                <div class="s2-head">CONCLUSION</div>
                                <div class="s2-sub">Comparison &bull; Future Scope &bull; References</div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide contents-slide" id="slide-2">.*?</section>', new_slide_2.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
