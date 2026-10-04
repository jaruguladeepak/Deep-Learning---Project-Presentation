import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-6">
            <div class="slide-header">
                <div class="slide-number">05</div>
                <div class="slide-title">Proposed Framework <span style="font-size: 1.1vw; color: #64748b; font-weight: 400; text-transform: none; margin-left: 1vw;">End-to-End AI-Assisted Architecture</span></div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">

                <!-- Top level: Camera -> YOLO -> Analyzer -->
                <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 1.2vw;">
                    <div style="border: 1px solid var(--accent-cyan); background: rgba(0, 229, 255, 0.05); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 15vw;">
                        <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">CAMERA / INPUT</div>
                    </div>
                    
                    <div style="color: #94a3b8; font-size: 1vw; margin: 0.3vw 0;">&darr;</div>
                    
                    <div style="border: 1px solid var(--accent-cyan); background: rgba(0, 229, 255, 0.05); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 15vw;">
                        <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">YOLOv8</div>
                        <div style="font-size: 0.8vw; color: #475569;">Object Detection</div>
                    </div>
                    
                    <div style="color: #94a3b8; font-size: 1vw; margin: 0.3vw 0;">&darr;</div>
                    
                    <div style="border: 1px solid var(--accent-cyan); background: rgba(0, 229, 255, 0.05); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 22vw;">
                        <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">THREAT ANALYZER</div>
                        <div style="font-size: 0.8vw; color: #475569;">Class &bull; Confidence &bull; Zone &bull; Movement &bull; Persistence</div>
                    </div>
                </div>
                
                <!-- Split Arrows -->
                <div style="display: flex; justify-content: center; width: 40vw; margin-bottom: 0.8vw;">
                    <div style="flex: 1; text-align: right; padding-right: 3vw; color: #94a3b8; font-size: 1.2vw;">&swarr;</div>
                    <div style="flex: 1; text-align: left; padding-left: 3vw; color: #94a3b8; font-size: 1.2vw;">&searr;</div>
                </div>

                <!-- Two Columns -->
                <div style="display: flex; flex-direction: row; gap: 6vw; width: 80%; max-width: 80vw;">
                    
                    <!-- Left: Local Safety -->
                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
                        <div style="font-size: 0.9vw; font-weight: 700; color: #e11d48; letter-spacing: 0.1vw; margin-bottom: 0.8vw; font-family: 'Inter', sans-serif;">LOCAL SAFETY</div>
                        
                        <div style="border: 1px solid #e11d48; background: rgba(225, 29, 72, 0.03); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 15vw;">
                            <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">ESP32</div>
                            <div style="font-size: 0.8vw; color: #475569;">STOP / RESUME</div>
                        </div>
                        
                        <div style="color: #e11d48; font-size: 1vw; margin: 0.3vw 0;">&darr;</div>
                        
                        <div style="border: 1px solid #e11d48; background: rgba(225, 29, 72, 0.03); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 15vw;">
                            <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">L293D &rarr; MOTORS</div>
                            <div style="font-size: 0.8vw; color: #475569;">Hardware Actuation</div>
                        </div>
                    </div>

                    <!-- Right: Cloud Monitoring -->
                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
                        <div style="font-size: 0.9vw; font-weight: 700; color: var(--accent-blue); letter-spacing: 0.1vw; margin-bottom: 0.8vw; font-family: 'Inter', sans-serif;">CLOUD MONITORING</div>
                        
                        <div style="border: 1px solid var(--accent-blue); background: rgba(0, 102, 204, 0.03); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 20vw;">
                            <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">AWS IoT CORE</div>
                            <div style="font-size: 0.8vw; color: #475569;">MQTT Telemetry</div>
                        </div>
                        
                        <div style="color: var(--accent-blue); font-size: 1vw; margin: 0.3vw 0;">&darr;</div>
                        
                        <div style="border: 1px solid var(--accent-blue); background: rgba(0, 102, 204, 0.03); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 20vw;">
                            <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">IoT RULES</div>
                            <div style="font-size: 0.8vw; color: #475569;">Event Routing</div>
                        </div>

                        <div style="display: flex; justify-content: space-between; width: 20vw; margin: 0.3vw 0;">
                            <div style="color: var(--accent-blue); font-size: 1vw; text-align: right; padding-right: 3vw;">&swarr;</div>
                            <div style="color: var(--accent-blue); font-size: 1vw; text-align: left; padding-left: 3vw;">&searr;</div>
                        </div>

                        <div style="display: flex; flex-direction: row; gap: 1vw; width: 20vw; justify-content: center;">
                            <div style="flex: 1; border: 1px solid var(--accent-blue); background: rgba(0, 102, 204, 0.03); padding: 0.4vw 0.5vw; text-align: center; border-radius: 4px;">
                                <div style="font-weight: 700; font-size: 0.9vw; color: #1e293b; font-family: 'Inter', sans-serif;">DynamoDB</div>
                                <div style="font-size: 0.7vw; color: #475569;">Storage</div>
                            </div>
                            <div style="flex: 1; border: 1px solid var(--accent-blue); background: rgba(0, 102, 204, 0.03); padding: 0.4vw 0.5vw; text-align: center; border-radius: 4px;">
                                <div style="font-weight: 700; font-size: 0.9vw; color: #1e293b; font-family: 'Inter', sans-serif;">Lambda &rarr; SNS</div>
                                <div style="font-size: 0.7vw; color: #475569;">Alerting</div>
                            </div>
                        </div>
                        
                        <div style="color: #10b981; font-size: 1vw; margin: 0.3vw 0;">&darr;</div>
                        
                        <div style="border: 1px solid #10b981; background: rgba(16, 185, 129, 0.05); padding: 0.5vw 1.5vw; text-align: center; border-radius: 4px; min-width: 20vw;">
                            <div style="font-weight: 700; font-size: 1vw; color: #1e293b; font-family: 'Inter', sans-serif; letter-spacing: 0.05vw;">FastAPI &rarr; React / Vite</div>
                            <div style="font-size: 0.8vw; color: #475569;">Read-Only Monitoring Dashboard</div>
                        </div>
                    </div>
                </div>

                <!-- Bottom Callout -->
                <div style="margin-top: 1.5vw; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 1vw; width: 80%; text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; font-weight: 700; margin-bottom: 0.5vw;">
                        Local-First Safety Design
                    </div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; color: var(--text-color); font-style: italic;">
                        Immediate safety logic remains on the local AI + ESP32 path. AWS provides telemetry, persistence, and monitoring&mdash;not the primary actuator command path.
                    </div>
                </div>

            </div>
        </section>'''

# Replace slide 6
content = re.sub(r'<section class="slide" id="slide-6">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
