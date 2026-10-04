import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-4">
            <div class="slide-header">
                <div class="slide-number">04</div>
                <div class="slide-title">Objectives &amp; Research Gap</div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                
                <div style="display: flex; flex-direction: row; gap: 5vw; margin-bottom: 2vw; flex: 1; align-items: stretch;">
                    
                    <!-- Left Column: Objectives -->
                    <div style="flex: 1; display: flex; flex-direction: column;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 2vw; text-transform: uppercase; letter-spacing: 0.1vw; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 0.5vw;">Objectives</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2vw 1.5vw; flex: 1;">
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">01.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Detect</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Detect railway foreign objects using YOLOv8.</div>
                            </div>
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">02.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Classify</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Identify different object categories from visual input.</div>
                            </div>
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">03.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Assess</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Evaluate threat using class, confidence, position, and movement.</div>
                            </div>
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">04.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Respond</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Generate local STOP/RESUME commands through ESP32.</div>
                            </div>
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">05.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Monitor</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Transmit telemetry and events through AWS IoT Core.</div>
                            </div>
                            <div>
                                <div style="display: flex; align-items: baseline; gap: 0.5vw; margin-bottom: 0.4vw;">
                                    <span style="font-weight: 700; color: var(--accent-blue); font-size: 1.2vw;">06.</span>
                                    <span style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">Visualize</span>
                                </div>
                                <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.5;">Provide a centralized Railway Safety Operations Center.</div>
                            </div>
                        </div>
                    </div>

                    <!-- Right Column: Research Gap -->
                    <div style="flex: 1; display: flex; flex-direction: column;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 2vw; text-transform: uppercase; letter-spacing: 0.1vw; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 0.5vw;">Research Gap</h3>
                        
                        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
                            <div style="border-left: 3px solid #e11d48; padding: 1.5vw; background: rgba(225, 29, 72, 0.03); margin-bottom: 1.5vw;">
                                <div style="font-size: 0.9vw; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 0.8vw;">Existing Approaches</div>
                                <div style="font-size: 1.2vw; font-weight: 600; color: #1e293b; margin-bottom: 1vw;">Detection &rarr; Object Identified</div>
                                <ul style="font-size: 1.1vw; line-height: 1.6; color: var(--text-color); list-style-type: none; padding-left: 0.5vw; margin: 0;">
                                    <li style="margin-bottom: 0.5vw; position: relative;"><span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span> Detection without threat assessment</li>
                                    <li style="margin-bottom: 0.5vw; position: relative;"><span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span> Limited consideration of movement/persistence</li>
                                    <li style="margin-bottom: 0.5vw; position: relative;"><span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span> AI and hardware often treated separately</li>
                                    <li style="margin-bottom: 0; position: relative;"><span style="color: #e11d48; position: absolute; left: -1vw; font-weight: bold;">&bull;</span> Limited centralized event monitoring</li>
                                </ul>
                            </div>
                            
                            <div style="border-left: 3px solid var(--accent-blue); background: rgba(0, 102, 204, 0.04); padding: 1.5vw;">
                                <div style="font-size: 0.9vw; font-weight: 600; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 0.8vw;">RailFOD23 Proposed Flow</div>
                                <div style="font-size: 1.3vw; font-weight: 600; color: var(--accent-blue);">
                                    Detect &rarr; Assess &rarr; Respond &rarr; Monitor
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>
                
                <!-- Bottom Callout -->
                <div style="background: rgba(0, 102, 204, 0.04); border-left: 4px solid var(--accent-blue); padding: 1.5vw 2vw; display: flex; align-items: center; gap: 2vw;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; font-weight: 700; white-space: nowrap;">
                        Key Contribution
                    </div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--text-color); font-style: italic; line-height: 1.5;">
                        "Integrates AI detection, intelligent threat assessment, local safety-control logic, and cloud observability into a single prototype architecture."
                    </div>
                </div>

            </div>
        </section>'''

content = re.sub(r'<section class="slide" id="slide-4">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
