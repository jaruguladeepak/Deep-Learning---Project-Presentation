import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 2 REDESIGN - STEP BY STEP */
        .s2-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            padding: 2vw 0;
            width: 100%;
        }

        .s2-timeline {
            position: relative;
            display: flex;
            justify-content: space-between;
            width: 100%;
            padding: 0 2vw;
        }

        .s2-line {
            position: absolute;
            top: 50%;
            left: 5vw;
            right: 5vw;
            height: 3px;
            background: linear-gradient(to right, rgba(0,0,0,0.05), var(--accent-blue), rgba(0,0,0,0.05));
            transform: translateY(-50%);
            z-index: 1;
        }

        .s2-step {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-rows: 1fr auto 1fr;
            gap: 1.5vw;
            width: 13vw;
            align-items: center;
            justify-items: center;
        }

        .s2-marker {
            grid-row: 2;
            width: 3.5vw;
            height: 3.5vw;
            border-radius: 50%;
            background: var(--glass-bg);
            border: 3px solid var(--accent-blue);
            color: var(--accent-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2vw;
            font-weight: 700;
            font-family: Georgia, "Times New Roman", serif;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        .s2-content-top {
            grid-row: 1;
            align-self: end;
            text-align: center;
        }

        .s2-content-bottom {
            grid-row: 3;
            align-self: start;
            text-align: center;
        }

        .s2-title {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.5vw;
            text-transform: uppercase;
        }

        .s2-desc {
            font-size: 0.75vw;
            color: #64748b;
            line-height: 1.4;
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
                <div class="s2-container">
                    <div class="s2-timeline">
                        <div class="s2-line"></div>
                        
                        <!-- Step 1 -->
                        <div class="s2-step">
                            <div class="s2-content-top">
                                <div class="s2-title">INTRODUCTION</div>
                                <div class="s2-desc">Problem Statement</div>
                            </div>
                            <div class="s2-marker">01</div>
                            <div></div>
                        </div>
                        
                        <!-- Step 2 -->
                        <div class="s2-step">
                            <div></div>
                            <div class="s2-marker">02</div>
                            <div class="s2-content-bottom">
                                <div class="s2-title">RESEARCH FOUNDATION</div>
                                <div class="s2-desc">Objectives &middot; Research Gap &middot; Literature Review</div>
                            </div>
                        </div>
                        
                        <!-- Step 3 -->
                        <div class="s2-step">
                            <div class="s2-content-top">
                                <div class="s2-title">PROPOSED SYSTEM</div>
                                <div class="s2-desc">Framework &middot; Methodology &middot; Working</div>
                            </div>
                            <div class="s2-marker">03</div>
                            <div></div>
                        </div>
                        
                        <!-- Step 4 -->
                        <div class="s2-step">
                            <div></div>
                            <div class="s2-marker">04</div>
                            <div class="s2-content-bottom">
                                <div class="s2-title">AI &amp; SAFETY</div>
                                <div class="s2-desc">Dataset &middot; YOLOv8 &middot; Threat Assessment</div>
                            </div>
                        </div>
                        
                        <!-- Step 5 -->
                        <div class="s2-step">
                            <div class="s2-content-top">
                                <div class="s2-title">IMPLEMENTATION</div>
                                <div class="s2-desc">ESP32 &middot; AWS &middot; Dashboard &middot; Results</div>
                            </div>
                            <div class="s2-marker">05</div>
                            <div></div>
                        </div>
                        
                        <!-- Step 6 -->
                        <div class="s2-step">
                            <div></div>
                            <div class="s2-marker">06</div>
                            <div class="s2-content-bottom">
                                <div class="s2-title">CONCLUSION</div>
                                <div class="s2-desc">Comparison &middot; Future Scope &middot; References</div>
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
