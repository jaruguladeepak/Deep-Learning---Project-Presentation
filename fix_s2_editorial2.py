import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

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
