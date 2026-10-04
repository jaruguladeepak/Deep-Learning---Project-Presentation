import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-6">
    <div class="slide-header">
        <div class="slide-number">05</div>
        <div class="slide-title">Proposed Framework <span style="font-size: 1.1vw; color: #64748b; font-weight: 400; text-transform: none; margin-left: 1vw;">End-to-End AI-Assisted Architecture</span></div>
    </div>

    <div class="slide-body" style="padding-top: 2vw;">
        
        <!-- Top: Core AI Pipeline -->
        <div style="border: 1px solid #0B1F3A; padding: 1.5vw; margin-bottom: 2vw; background: #fff;">
            <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.8vw; font-weight: 700; color: #2563EB; letter-spacing: 0.1vw; margin-bottom: 1.5vw; text-transform: uppercase;">
                Primary Vision &amp; Analysis Pipeline
            </div>
            
            <div style="display: flex; align-items: center; justify-content: space-between; padding: 0 2vw;">
                <!-- Step 1 -->
                <div style="text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.3vw;">CAMERA INPUT</div>
                    <div style="font-family: 'Times New Roman', Times, serif; font-size: 1vw; color: #64748B; font-style: italic;">Real-time video feed</div>
                </div>
                
                <div style="flex-grow: 1; border-top: 1px dashed #0B1F3A; margin: 0 2vw; position: relative; top: -1vw;">
                    <div style="position: absolute; right: -0.5vw; top: -0.4vw; font-size: 0.8vw; color: #0B1F3A;">&#x25B6;</div>
                </div>

                <!-- Step 2 -->
                <div style="text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.3vw;">YOLOv8 AI</div>
                    <div style="font-family: 'Times New Roman', Times, serif; font-size: 1vw; color: #64748B; font-style: italic;">Object Detection</div>
                </div>

                <div style="flex-grow: 1; border-top: 1px dashed #0B1F3A; margin: 0 2vw; position: relative; top: -1vw;">
                    <div style="position: absolute; right: -0.5vw; top: -0.4vw; font-size: 0.8vw; color: #0B1F3A;">&#x25B6;</div>
                </div>

                <!-- Step 3 -->
                <div style="text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.6vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.3vw;">THREAT ANALYZER</div>
                    <div style="font-family: 'Times New Roman', Times, serif; font-size: 1vw; color: #64748B; font-style: italic;">Class &bull; Zone &bull; Persistence</div>
                </div>
            </div>
        </div>

        <!-- Split into Actuation and Telemetry -->
        <div style="display: flex; gap: 2vw;">
            
            <!-- Local Actuation -->
            <div style="flex: 1; border: 1px solid #0B1F3A; padding: 1.5vw; background: #fff;">
                <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.8vw; font-weight: 700; color: #2563EB; letter-spacing: 0.1vw; margin-bottom: 1.5vw; text-transform: uppercase;">
                    Local Safety Actuation (Edge)
                </div>
                
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.4vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.2vw;">ESP32 MCU</div>
                        <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.9vw; color: #64748B; font-style: italic;">STOP / RESUME Signal</div>
                    </div>
                    
                    <div style="flex-grow: 1; border-top: 1px dotted #0B1F3A; margin: 0 1vw; position: relative; top: -0.8vw;">
                        <div style="position: absolute; right: -0.4vw; top: -0.3vw; font-size: 0.6vw; color: #0B1F3A;">&#x25B6;</div>
                    </div>

                    <div style="text-align: right;">
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.4vw; font-weight: 700; color: #0B1F3A; margin-bottom: 0.2vw;">L293D + MOTORS</div>
                        <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.9vw; color: #64748B; font-style: italic;">Hardware Braking</div>
                    </div>
                </div>
            </div>

            <!-- Cloud Telemetry -->
            <div style="flex: 1; border: 1px solid #0B1F3A; padding: 1.5vw; background: #fff;">
                <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.8vw; font-weight: 700; color: #2563EB; letter-spacing: 0.1vw; margin-bottom: 1.5vw; text-transform: uppercase;">
                    Cloud Telemetry &amp; Monitoring
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1vw;">
                    <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 0.8vw;">
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; font-weight: 700; color: #0B1F3A;">AWS IoT Core</div>
                        <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.9vw; color: #64748B; font-style: italic;">MQTT Ingestion</div>
                    </div>
                    <div style="border-bottom: 1px solid #E2E8F0; padding-bottom: 0.8vw;">
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; font-weight: 700; color: #0B1F3A;">DynamoDB / SNS</div>
                        <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.9vw; color: #64748B; font-style: italic;">Storage &amp; Alerts</div>
                    </div>
                    <div style="grid-column: 1 / -1; padding-top: 0.5vw;">
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; font-weight: 700; color: #0B1F3A;">FastAPI &amp; React UI</div>
                        <div style="font-family: 'Times New Roman', Times, serif; font-size: 0.9vw; color: #64748B; font-style: italic;">Read-Only Global Operations View</div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Footer Callout -->
        <div style="margin-top: 2vw; border-top: 1px solid #D9E0E8; padding-top: 1vw; text-align: center;">
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: #2563EB; text-transform: uppercase; letter-spacing: 0.1vw; font-weight: 700; margin-bottom: 0.5vw;">
                LOCAL-FIRST SAFETY DESIGN
            </div>
            <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: #34465A; font-style: italic;">
                Immediate safety logic remains on the local AI + ESP32 path. AWS provides telemetry, persistence, and monitoring&mdash;not the primary actuator command path.
            </div>
        </div>

    </div>
</section>'''

# Replace slide 6
content = re.sub(r'<section[^>]*id="slide-6"[^>]*>.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done redesigning slide 6")
