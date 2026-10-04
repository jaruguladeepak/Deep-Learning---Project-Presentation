import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

slide_2_html = '''
        <!-- Slide 02: Table of Contents -->
        <section class="slide contents-slide" id="slide-2">
            <div class="slide-header">
                <div class="slide-number">02</div>
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

# First, fix the comments that didn't get updated properly
# The file has:
# <!-- Slide 02: Introduction
# <!-- Slide 03: Objectives
# <!-- Slide 04: Literature
# <!-- Slide 05: Proposed
# <!-- Slide 06: Methodology
# <!-- Slide 07: Dataset
# <!-- Slide 08: Threat
# <!-- Slide 09: AWS
# <!-- Slide 11: Implementation  (wait, 10 is missing, skipped to 11?)
# Let's fix the numbering manually to make sure it's perfect.

# We will just replace 'id="slide-X"' and '<div class="slide-number">X</div>' again just to be safe, but wait, we already did it for ids and div.slide-number!
# Let's check what ids we currently have.
