import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-13">
            <div class="slide-header">
                <div class="slide-number">13</div>
                <div class="slide-title">Conclusion &amp; Future Scope <span style="font-size: 1.1vw; color: #64748b; font-weight: 400; text-transform: none; margin-left: 1vw;">From Detection to Intelligent Railway Safety Monitoring</span></div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
                
                <div style="display: flex; flex-direction: row; gap: 5vw; flex: 1;">
                    
                    <!-- Left: Conclusion & Achievements -->
                    <div style="flex: 1; padding-right: 5vw; border-right: 1px solid rgba(0,0,0,0.1); display: flex; flex-direction: column;">
                        
                        <div style="margin-bottom: 3.5vw;">
                            <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">Conclusion</h3>
                            
                            <div style="font-size: 1.3vw; font-weight: 700; color: #1e293b; line-height: 1.5; margin-bottom: 1.2vw; font-family: Georgia, 'Times New Roman', serif;">
                                RailFOD23 demonstrates an end-to-end academic prototype for intelligent railway safety monitoring.
                            </div>
                            <div style="font-size: 1.1vw; color: var(--text-color); line-height: 1.6;">
                                The system successfully integrates YOLOv8 detection, multi-factor threat assessment, local ESP32 safety control, AWS IoT telemetry, and a read-only operations dashboard.
                            </div>
                        </div>

                        <div>
                            <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">Key Achievements</h3>
                            
                            <ul style="list-style: none; padding: 0; margin: 0; font-size: 1.05vw; color: #334155; line-height: 1.5;">
                                <li style="margin-bottom: 1vw; display: flex; align-items: flex-start;">
                                    <span style="color: var(--accent-blue); margin-right: 0.8vw; font-size: 1.2vw;">&bull;</span>
                                    <span><strong>YOLOv8</strong> foreign-object detection pipeline</span>
                                </li>
                                <li style="margin-bottom: 1vw; display: flex; align-items: flex-start;">
                                    <span style="color: var(--accent-blue); margin-right: 0.8vw; font-size: 1.2vw;">&bull;</span>
                                    <span><strong>Threat assessment</strong> logic and safety state machine</span>
                                </li>
                                <li style="margin-bottom: 1vw; display: flex; align-items: flex-start;">
                                    <span style="color: var(--accent-blue); margin-right: 0.8vw; font-size: 1.2vw;">&bull;</span>
                                    <span><strong>ESP32</strong> localized STOP / RESUME communication</span>
                                </li>
                                <li style="margin-bottom: 1vw; display: flex; align-items: flex-start;">
                                    <span style="color: var(--accent-blue); margin-right: 0.8vw; font-size: 1.2vw;">&bull;</span>
                                    <span><strong>AWS IoT</strong> + DynamoDB + Lambda/SNS cloud integration</span>
                                </li>
                                <li style="display: flex; align-items: flex-start;">
                                    <span style="color: var(--accent-blue); margin-right: 0.8vw; font-size: 1.2vw;">&bull;</span>
                                    <span><strong>React + FastAPI</strong> read-only monitoring dashboard</span>
                                </li>
                            </ul>
                        </div>

                    </div>

                    <!-- Right: Future Scope -->
                    <div style="flex: 1.1; display: flex; flex-direction: column;">
                        
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.1vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">Future Scope</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5vw; flex: 1;">
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">01 &middot; THERMAL / IR VISION</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Improve detection under low-light and adverse visibility.</div>
                            </div>
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">02 &middot; IMPROVED TRACKING</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Strengthen multi-object tracking and trajectory estimation.</div>
                            </div>
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">03 &middot; REAL-WORLD DATASET</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Expand training using diverse railway environments.</div>
                            </div>
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">04 &middot; EDGE OPTIMIZATION</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Explore compression, quantization and optimized inference.</div>
                            </div>
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">05 &middot; CALIBRATION &amp; VALIDATION</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Add camera calibration and physical hardware validation.</div>
                            </div>
                            
                            <div style="background: #ffffff; border-left: 3px solid var(--accent-cyan); padding: 1.2vw 1.5vw; border-radius: 4px; border-top: 1px solid rgba(0,0,0,0.05); border-right: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: var(--accent-cyan); font-weight: 700; margin-bottom: 0.6vw;">06 &middot; FIELD TESTING</div>
                                <div style="font-size: 0.95vw; color: var(--text-color); line-height: 1.5;">Progress toward controlled trials and safety validation.</div>
                            </div>
                            
                        </div>

                    </div>
                    
                </div>
                
                <!-- Bottom Area -->
                <div style="margin-top: 3vw; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 1.5vw;">
                    
                    <div style="display: flex; align-items: center; justify-content: center; gap: 2.5vw; font-size: 0.8vw; color: #64748b; margin-bottom: 1.5vw;">
                        <span style="font-weight: 700; color: var(--accent-blue); letter-spacing: 0.05vw;">REFERENCES</span>
                        <span>[1] RailFOD23 Dataset, Figshare</span>
                        <span>[2] Ultralytics YOLO</span>
                        <span>[3] Microsoft COCO, ECCV 2014</span>
                        <span>[4] Espressif ESP32 Documentation</span>
                        <span>[5] AWS IoT Core Documentation</span>
                    </div>

                    <div style="text-align: center; font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: #4b5563; text-transform: uppercase; letter-spacing: 0.2vw;">
                        RAILFOD23 &nbsp;&bull;&nbsp; AI + EDGE SAFETY + CLOUD MONITORING
                    </div>
                </div>

            </div>
        </section>'''

# Replace slide 13
content = re.sub(r'<section class="slide" id="slide-13">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
