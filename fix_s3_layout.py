import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-3">
            <div class="slide-header">
                <div class="slide-number">03</div>
                <div class="slide-title">Introduction &amp; Problem Statement</div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                
                <div style="display: flex; flex-direction: row; gap: 4vw; margin-bottom: 2vw; flex: 1; align-items: center;">
                    
                    <!-- Left Column: Introduction -->
                    <div style="flex: 1; padding-right: 4vw; border-right: 1px solid rgba(0,0,0,0.1);">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.2vw; text-transform: uppercase; letter-spacing: 0.1vw;">Introduction</h3>
                        
                        <p style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); margin-bottom: 1vw;">
                            Railway infrastructure requires continuous monitoring to identify foreign objects and potential hazards.
                        </p>
                        <p style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); margin-bottom: 1vw;">
                            Traditional monitoring approaches can be difficult to scale across large railway environments and may depend heavily on manual observation.
                        </p>
                        
                        <p style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); margin-bottom: 0.8vw;">
                            <strong>RailFOD23</strong> combines:
                        </p>
                        <ul style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); list-style-type: none; padding-left: 1vw; margin: 0;">
                            <li style="margin-bottom: 0.5vw; position: relative;">
                                <span style="color: var(--accent-blue); position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>AI-based object detection</strong>
                            </li>
                            <li style="margin-bottom: 0.5vw; position: relative;">
                                <span style="color: var(--accent-blue); position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Intelligent threat assessment</strong>
                            </li>
                            <li style="margin-bottom: 0.5vw; position: relative;">
                                <span style="color: var(--accent-blue); position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Local safety-control logic</strong>
                            </li>
                            <li style="margin-bottom: 0.5vw; position: relative;">
                                <span style="color: var(--accent-blue); position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Cloud-based telemetry and monitoring</strong>
                            </li>
                        </ul>
                    </div>

                    <!-- Right Column: Problem Statement -->
                    <div style="flex: 1;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.2vw; text-transform: uppercase; letter-spacing: 0.1vw;">Problem Statement</h3>
                        
                        <p style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); margin-bottom: 1.2vw;">
                            Railway foreign objects can vary in:
                        </p>
                        
                        <ul style="font-size: 1.2vw; line-height: 1.5; color: var(--text-color); list-style-type: none; padding-left: 1vw; margin: 0;">
                            <li style="margin-bottom: 1vw; position: relative;">
                                <span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Type</strong> &mdash; different objects create different levels of risk
                            </li>
                            <li style="margin-bottom: 1vw; position: relative;">
                                <span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Position</strong> &mdash; threat depends on where the object appears
                            </li>
                            <li style="margin-bottom: 1vw; position: relative;">
                                <span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Movement</strong> &mdash; approaching objects may become more critical
                            </li>
                            <li style="margin-bottom: 1vw; position: relative;">
                                <span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Persistence</strong> &mdash; temporary detections should be distinguished from sustained hazards
                            </li>
                            <li style="margin-bottom: 1vw; position: relative;">
                                <span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span>
                                <strong>Response requirements</strong> &mdash; critical conditions need a local safety response
                            </li>
                        </ul>
                    </div>
                    
                </div>
                
                <!-- Bottom Callout -->
                <div style="border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2vw; text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 0.8vw; font-weight: 700;">
                        Research Problem
                    </div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.4vw; color: var(--text-color); font-style: italic; max-width: 80%; margin: 0 auto; line-height: 1.5;">
                        "How can railway foreign objects be detected and intelligently assessed while maintaining a local safety-response path and providing centralized monitoring?"
                    </div>
                    
                    <div style="margin-top: 1.2vw; font-size: 1.1vw; font-weight: 600; color: #4b5563; display: flex; justify-content: center; align-items: center; gap: 1vw;">
                        <span>Detect</span>
                        <span style="color: var(--accent-blue);">&rarr;</span>
                        <span>Assess</span>
                        <span style="color: var(--accent-blue);">&rarr;</span>
                        <span>Respond</span>
                        <span style="color: var(--accent-blue);">&rarr;</span>
                        <span>Monitor</span>
                    </div>
                </div>

            </div>
        </section>'''

# Replace slide3
content = re.sub(r'<section class="slide" id="slide3">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
