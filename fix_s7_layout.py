import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-7">
            <div class="slide-header">
                <div class="slide-number">06</div>
                <div class="slide-title">Methodology &amp; Threat Decision Pipeline</div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                
                <!-- Pipeline Stages -->
                <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">01. Visual Detection to Actuation Pipeline</h3>
                
                <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.5vw; margin-bottom: 3.5vw;">
                    <!-- 1 -->
                    <div style="flex: 1; border: 1px solid rgba(0,0,0,0.15); padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: #ffffff;">
                        <div style="font-size: 0.8vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.4vw;">01. INPUT</div>
                        <div style="font-size: 0.9vw; color: #1e293b; font-weight: 700;">Camera / Frame</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">Visual input</div>
                    </div>
                    <div style="color: #94a3b8;">&rarr;</div>
                    <!-- 2 -->
                    <div style="flex: 1; border: 1px solid rgba(0,0,0,0.15); padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: #ffffff;">
                        <div style="font-size: 0.8vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.4vw;">02. DETECT</div>
                        <div style="font-size: 0.9vw; color: #1e293b; font-weight: 700;">YOLOv8</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">Class + Conf + BBox</div>
                    </div>
                    <div style="color: #94a3b8;">&rarr;</div>
                    <!-- 3 -->
                    <div style="flex: 1; border: 1px solid rgba(0,0,0,0.15); padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: #ffffff;">
                        <div style="font-size: 0.8vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.4vw;">03. TRACK</div>
                        <div style="font-size: 0.9vw; color: #1e293b; font-weight: 700;">Multi-object</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">IoU + Centroid</div>
                    </div>
                    <div style="color: #94a3b8;">&rarr;</div>
                    <!-- 4 -->
                    <div style="flex: 1; border: 1px solid var(--accent-blue); padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: rgba(0, 102, 204, 0.03);">
                        <div style="font-size: 0.8vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.4vw;">04. ANALYZE</div>
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700;">Threat Factors</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">Sev + Zone + Mov</div>
                    </div>
                    <div style="color: #94a3b8;">&rarr;</div>
                    <!-- 5 -->
                    <div style="flex: 1; border: 1px solid var(--accent-blue); padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: rgba(0, 102, 204, 0.03);">
                        <div style="font-size: 0.8vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.4vw;">05. DECIDE</div>
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700;">Assessment</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">Threat Score</div>
                    </div>
                    <div style="color: #94a3b8;">&rarr;</div>
                    <!-- 6 -->
                    <div style="flex: 1; border: 1px solid #e11d48; padding: 1.2vw 0.5vw; text-align: center; border-radius: 6px; background: rgba(225, 29, 72, 0.04);">
                        <div style="font-size: 0.8vw; color: #e11d48; font-weight: 700; margin-bottom: 0.4vw;">06. RESPOND</div>
                        <div style="font-size: 0.9vw; color: #e11d48; font-weight: 700;">Safety State</div>
                        <div style="font-size: 0.75vw; color: #64748b; margin-top: 0.4vw;">State + Actuation</div>
                    </div>
                </div>

                <!-- Bottom row split -->
                <div style="display: flex; gap: 5vw;">
                    
                    <!-- Left: Threat Score -->
                    <div style="flex: 1.2; padding-right: 5vw; border-right: 1px solid rgba(0,0,0,0.1);">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">02. Threat Computation</h3>
                        
                        <div style="display: flex; gap: 2vw; align-items: stretch;">
                            <div style="flex: 1; text-align: center; font-size: 1.1vw; line-height: 2; font-weight: 600; color: #334155; display: flex; flex-direction: column; justify-content: center;">
                                Severity<br>
                                <span style="color: #cbd5e1;">+</span><br>
                                Zone<br>
                                <span style="color: #cbd5e1;">+</span><br>
                                Movement<br>
                                <span style="color: #cbd5e1;">+</span><br>
                                Confidence
                            </div>
                            
                            <div style="flex: 1.5; border-left: 1px solid rgba(0,0,0,0.1); padding-left: 2.5vw; display: flex; flex-direction: column; justify-content: center;">
                                <div style="font-size: 0.8vw; color: #94a3b8; font-weight: 700; text-transform: uppercase; margin-bottom: 1vw;">Relative Image-Space Zones</div>
                                
                                <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; color: #047857; padding: 0.6vw 1vw; font-size: 0.9vw; font-weight: 700; margin-bottom: 0.6vw;">
                                    GREEN (&le; 60%)
                                </div>
                                <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; color: #b45309; padding: 0.6vw 1vw; font-size: 0.9vw; font-weight: 700; margin-bottom: 0.6vw;">
                                    YELLOW (60&ndash;80%)
                                </div>
                                <div style="background: rgba(225, 29, 72, 0.1); border-left: 3px solid #e11d48; color: #be123c; padding: 0.6vw 1vw; font-size: 0.9vw; font-weight: 700;">
                                    RED / CRITICAL (&gt; 80%)
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Right: State Machine -->
                    <div style="flex: 1;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">03. Safety State Machine</h3>
                        
                        <div style="display: flex; justify-content: flex-start; align-items: center; gap: 3vw; padding-left: 1vw;">
                            <div style="display: flex; flex-direction: column; gap: 0.4vw; align-items: center; font-size: 0.95vw; font-weight: 700;">
                                <div style="border: 1px solid #10b981; color: #10b981; padding: 0.4vw 2vw; width: 11vw; text-align: center; border-radius: 4px;">RUNNING</div>
                                <div style="color: #94a3b8; font-size: 1vw;">&darr;</div>
                                <div style="border: 1px solid #f59e0b; color: #f59e0b; padding: 0.4vw 2vw; width: 11vw; text-align: center; border-radius: 4px;">WARNING</div>
                                <div style="color: #94a3b8; font-size: 1vw;">&darr;</div>
                                <div style="border: 1px solid #ef4444; color: #ef4444; padding: 0.4vw 2vw; width: 11vw; text-align: center; border-radius: 4px;">CRITICAL</div>
                                <div style="color: #94a3b8; font-size: 1vw;">&darr;</div>
                                <div style="border: 1px solid #be123c; background: rgba(225, 29, 72, 0.05); color: #be123c; padding: 0.4vw 2vw; width: 11vw; text-align: center; border-radius: 4px;">STOPPING</div>
                                <div style="color: #94a3b8; font-size: 1vw;">&darr;</div>
                                <div style="background: #be123c; color: white; padding: 0.4vw 2vw; width: 11vw; text-align: center; border-radius: 4px;">STOPPED</div>
                            </div>
                            
                            <div style="display: flex; align-items: center; gap: 1vw;">
                                <div style="color: #94a3b8; font-size: 1.2vw;">&rarr;</div>
                                <div style="border: 1px dashed #10b981; color: #10b981; font-weight: 700; font-size: 0.95vw; padding: 0.4vw 1.5vw; border-radius: 4px;">RECOVERY</div>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>

            </div>
        </section>'''

content = re.sub(r'<section class="slide" id="slide-7">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
