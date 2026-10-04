import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = '''
        <!-- Slide 14: Thank You -->
        <section class="slide" id="slide-14" style="padding: 0;">
            <div class="minimal-slide">
                <div class="min-inner">
                    <!-- Header -->
                    <div class="min-header">
                        <div>Deep Learning - Project Presentation</div>
                        <div>End of Presentation</div>
                    </div>

                    <!-- Main Title Area -->
                    <div class="min-title-container">
                        <div class="min-title" style="letter-spacing: 0.2vw;">THANK YOU</div>
                        <div class="min-subtitle">Any Questions?</div>
                    </div>

                    <!-- Footer Details -->
                    <div class="min-footer">
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
                                Section: DS-Tigers<br>
                                Year: 2026<br>
                                B.Tech CSE<br>
                                Woxsen University
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Insert new slide before slide counter
content = content.replace('<!-- Slide Counter -->', new_slide + '\n        <!-- Slide Counter -->')

# Update total slides in JS and HTML
content = content.replace('01 / 13</div>', '01 / 14</div>')
content = content.replace('const totalSlides = 13;', 'const totalSlides = 14;')
content = content.replace('totalSlides < 10 ?', 'slides.length < 10 ?')

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("added slide 14")
