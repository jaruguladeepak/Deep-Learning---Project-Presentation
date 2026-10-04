import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-9">
            <div class="slide-header">
                <div class="slide-number">09</div>
                <div class="slide-title">Threat Assessment &amp; Safety Control</div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                
                <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">01. Multi-Factor Threat Evaluation</h3>
                
                <!-- Factors Grid -->
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 2.5vw; margin-bottom: 3.5vw;">
                    
                    <!-- Severity -->
                    <div style="border-top: 3px solid var(--accent-blue); padding-top: 1.2vw;">
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.8vw; text-transform: uppercase; letter-spacing: 0.05vw;">Severity</div>
                        <div style="font-size: 1.1vw; font-weight: 700; color: #1e293b; margin-bottom: 1vw;">Object-specific risk</div>
                        <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.7;">
                            <span style="color: #ef4444; font-weight: 700;">Critical:</span> Person, Vehicle<br>
                            <span style="color: #10b981; font-weight: 700;">Low:</span> Bird nest, Bench
                        </div>
                    </div>
                    
                    <!-- Safety Zone -->
                    <div style="border-top: 3px solid var(--accent-blue); padding-top: 1.2vw;">
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.8vw; text-transform: uppercase; letter-spacing: 0.05vw;">Safety Zone</div>
                        <div style="font-size: 1.1vw; font-weight: 700; color: #1e293b; margin-bottom: 1vw;">Relative image position</div>
                        <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.7;">
                            <span style="color: #10b981; font-weight: 700;">&le; 60%</span> Green<br>
                            <span style="color: #f59e0b; font-weight: 700;">60&ndash;80%</span> Yellow<br>
                            <span style="color: #ef4444; font-weight: 700;">&gt; 80%</span> Red (Critical)
                        </div>
                    </div>
                    
                    <!-- Movement -->
                    <div style="border-top: 3px solid var(--accent-blue); padding-top: 1.2vw;">
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.8vw; text-transform: uppercase; letter-spacing: 0.05vw;">Movement</div>
                        <div style="font-size: 1.1vw; font-weight: 700; color: #1e293b; margin-bottom: 1vw;">Directional vector</div>
                        <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.7;">
                            Approaching &rarr; <span style="color: #ef4444; font-weight: 700;">&uarr; Risk</span><br>
                            Static &rarr; <span style="color: #f59e0b; font-weight: 700;">&rarr; Risk</span><br>
                            Away &rarr; <span style="color: #10b981; font-weight: 700;">&darr; Risk</span>
                        </div>
                    </div>
                    
                    <!-- Persistence -->
                    <div style="border-top: 3px solid var(--accent-blue); padding-top: 1.2vw;">
                        <div style="font-size: 0.9vw; color: var(--accent-blue); font-weight: 700; margin-bottom: 0.8vw; text-transform: uppercase; letter-spacing: 0.05vw;">Persistence</div>
                        <div style="font-size: 1.1vw; font-weight: 700; color: #1e293b; margin-bottom: 1vw;">Multi-frame logic</div>
                        <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.7;">
                            Multiple continuous frames confirm the threat before triggering escalation.
                        </div>
                    </div>
                    
                </div>
                
                <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">02. Edge-Level Actuation</h3>
                
                <div style="display: flex; flex-direction: row; align-items: stretch; gap: 4vw; margin-bottom: 2vw;">
                    
                    <!-- Scoring Pipeline -->
                    <div style="flex: 1; border: 1px solid rgba(0,0,0,0.1); border-radius: 6px; padding: 1.5vw 2vw; display: flex; justify-content: space-between; align-items: center; background: #ffffff;">
                        <div style="text-align: center;">
                            <div style="font-size: 0.8vw; color: #64748b; text-transform: uppercase; margin-bottom: 0.4vw; font-weight: 700;">Input</div>
                            <div style="font-weight: 700; color: #1e293b; font-size: 1.1vw;">4 Factors</div>
                        </div>
                        <div style="color: #94a3b8; font-size: 1.2vw;">&rarr;</div>
                        <div style="text-align: center;">
                            <div style="font-size: 0.8vw; color: #64748b; text-transform: uppercase; margin-bottom: 0.4vw; font-weight: 700;">Assessment</div>
                            <div style="font-weight: 700; color: var(--accent-blue); font-size: 1.1vw;">Threat Score</div>
                        </div>
                        <div style="color: #94a3b8; font-size: 1.2vw;">&rarr;</div>
                        <div style="text-align: center;">
                            <div style="font-size: 0.8vw; color: #64748b; text-transform: uppercase; margin-bottom: 0.4vw; font-weight: 700;">Action</div>
                            <div style="font-weight: 700; color: #e11d48; font-size: 1.1vw;">Safety State</div>
                        </div>
                    </div>
                    
                    <!-- Local First Safety -->
                    <div style="flex: 1.3; border-left: 4px solid #e11d48; background: rgba(225, 29, 72, 0.04); padding: 1.5vw 2vw; display: flex; align-items: center; gap: 2vw;">
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: #e11d48; text-transform: uppercase; letter-spacing: 0.1vw; font-weight: 700; white-space: nowrap;">
                            Local-First Policy
                        </div>
                        <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.15vw; color: var(--text-color); font-style: italic; line-height: 1.5;">
                            "Immediate safety logic remains strictly at the edge and does not depend on cloud availability."
                        </div>
                    </div>
                    
                </div>
                
                <div style="text-align: right; font-size: 0.85vw; color: #94a3b8; font-style: italic;">
                    * Physical L293D / motor validation remains part of hardware testing.
                </div>

            </div>
        </section>'''

# Replace slide 9
content = re.sub(r'<section class="slide" id="slide-9">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
