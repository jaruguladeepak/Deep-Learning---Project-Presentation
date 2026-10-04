import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide contents-slide" id="slide-2" style="padding: 0;">
    <div class="minimal-slide">
        <div class="min-inner">
            <!-- Header -->
            <div class="min-header">
                <div>Academic Project Presentation</div>
                <div>Contents / Overview</div>
            </div>

            <!-- Body Area -->
            <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr 1fr;">
                
                <!-- 01 -->
                <div style="border-bottom: 1px solid #111827; border-right: 1px solid #111827; padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">01</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">Introduction</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">Problem Statement</div>
                </div>

                <!-- 02 -->
                <div style="border-bottom: 1px solid #111827; padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">02</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">Research Foundation</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">Objectives &bull; Research Gap &bull; Literature Review</div>
                </div>

                <!-- 03 -->
                <div style="border-bottom: 1px solid #111827; border-right: 1px solid #111827; padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">03</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">Proposed System</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">Framework &bull; Methodology &bull; Working</div>
                </div>

                <!-- 04 -->
                <div style="border-bottom: 1px solid #111827; padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">04</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">AI &amp; Safety</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">Dataset &bull; YOLOv8 &bull; Threat Assessment</div>
                </div>

                <!-- 05 -->
                <div style="border-right: 1px solid #111827; padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">05</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">Implementation</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">ESP32 &bull; AWS &bull; Dashboard &bull; Results</div>
                </div>

                <!-- 06 -->
                <div style="padding: 3vw; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 1vw; font-weight: 700; color: #6b7280; margin-bottom: 0.8vw;">06</div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 2vw; font-weight: 700; color: #111827; margin-bottom: 0.5vw; text-transform: uppercase;">Conclusion</div>
                    <div style="font-size: 1.1vw; color: #4b5563; font-style: italic;">Comparison &bull; Future Scope &bull; References</div>
                </div>

            </div>
        </div>
    </div>
</section>'''

# Replace slide 2 
content = re.sub(r'<section[^>]*id="slide-2"[^>]*>.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done replacing slide 2")
