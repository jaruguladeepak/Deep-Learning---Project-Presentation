import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-2" style="background: #F7F8FA; color: #0B1F3A; padding: 5vw 7vw; display: flex; flex-direction: column;">
    
    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 3.5vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.5vw; letter-spacing: 0.05vw;">
        CONTENTS
    </div>
    
    <div style="font-family: 'Times New Roman', Times, serif; font-size: 1vw; color: #2563EB; letter-spacing: 0.1vw; font-weight: 700; text-transform: uppercase; margin-bottom: 4vw;">
        Project Presentation Overview
    </div>
    
    <div style="display: flex; flex-direction: column; gap: 2.2vw; max-width: 85%; margin: 0 auto; margin-top: 2vw; width: 100%;">
        
        <!-- Row 1 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">01</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">Introduction</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">Problem Statement</div>
        </div>
        
        <!-- Row 2 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">02</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">Research Foundation</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">Objectives &bull; Literature Review</div>
        </div>

        <!-- Row 3 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">03</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">Proposed System</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">Framework &bull; Methodology</div>
        </div>
        
        <!-- Row 4 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">04</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">AI &amp; Safety</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">Dataset &bull; YOLOv8 &bull; Threat Assessment</div>
        </div>

        <!-- Row 5 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">05</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">Implementation</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">ESP32 &bull; AWS &bull; Dashboard &bull; Results</div>
        </div>

        <!-- Row 6 -->
        <div style="display: flex; align-items: baseline;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2vw; font-weight: 700; color: #2563EB; margin-right: 1.5vw;">06</div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; text-transform: uppercase; white-space: nowrap;">Conclusion</div>
            <div style="flex-grow: 1; border-bottom: 2px dotted #D9E0E8; margin: 0 1.5vw; position: relative; top: -0.4vw;"></div>
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.1vw; color: #64748B; white-space: nowrap; font-style: italic;">Future Scope &bull; References</div>
        </div>

    </div>

</section>'''

# Replace slide 2
content = re.sub(r'<section[^>]*id="slide-2"[^>]*>.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done reverting to dotted leader TOC")
