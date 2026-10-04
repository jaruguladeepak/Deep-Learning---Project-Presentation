import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''<section class="slide" id="slide-8">
            <div class="slide-header">
                <div class="slide-number">08</div>
                <div class="slide-title">Dataset &amp; V2 Ontology Expansion</div>
            </div>

            <div class="slide-body" style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
                
                <div style="display: flex; flex-direction: row; gap: 4vw; margin-bottom: 2vw; flex: 1; align-items: stretch;">
                    
                    <!-- Left Column: Strategy -->
                    <div style="flex: 1; padding-right: 4vw; border-right: 1px solid rgba(0,0,0,0.1); display: flex; flex-direction: column; justify-content: center;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">Dataset Construction</h3>
                        
                        <p style="font-size: 1.2vw; line-height: 1.6; color: var(--text-color); margin-bottom: 2vw;">
                            The original V1 ontology was highly constrained. To create a robust diagnostic baseline, the dataset was expanded using supplementary sources.
                        </p>
                        
                        <div style="border-left: 3px solid var(--accent-blue); padding-left: 1.5vw; margin-bottom: 1.5vw;">
                            <div style="font-weight: 700; color: #1e293b; font-size: 1.1vw; margin-bottom: 0.3vw;">MS-COCO Integration</div>
                            <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.5;">Relevant classes were selected and annotations were converted to YOLO format.</div>
                        </div>
                        
                        <div style="border-left: 3px solid #10b981; padding-left: 1.5vw;">
                            <div style="font-weight: 700; color: #1e293b; font-size: 1.1vw; margin-bottom: 0.3vw;">Open Images Integration</div>
                            <div style="font-size: 1.05vw; color: var(--text-color); line-height: 1.5;">Additional hazard classes were curated to form a comprehensive safety monitoring dataset.</div>
                        </div>
                    </div>

                    <!-- Right Column: Classes -->
                    <div style="flex: 1.6; padding-left: 1vw; display: flex; flex-direction: column; justify-content: center;">
                        <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.3vw; color: var(--accent-blue); margin-bottom: 1.5vw; text-transform: uppercase; letter-spacing: 0.1vw;">Final V2 Ontology &mdash; 29 Classes</h3>
                        
                        <div style="display: flex; gap: 1.5vw;">
                            <!-- RailFOD23 -->
                            <div style="flex: 1; background: rgba(0, 229, 255, 0.04); border-top: 3px solid var(--accent-cyan); padding: 1.5vw;">
                                <div style="font-size: 0.85vw; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 1vw;">RailFOD23 (4)</div>
                                <div style="font-size: 1.05vw; line-height: 1.9; color: #334155;">
                                    bird_nest<br>
                                    plastic_bag<br>
                                    debris<br>
                                    balloon
                                </div>
                            </div>
                            
                            <!-- MS-COCO -->
                            <div style="flex: 1.3; background: rgba(0, 102, 204, 0.03); border-top: 3px solid var(--accent-blue); padding: 1.5vw;">
                                <div style="font-size: 0.85vw; font-weight: 700; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 1vw;">MS-COCO (14)</div>
                                <div style="font-size: 1.05vw; line-height: 1.9; color: #334155;">
                                    person &bull; car &bull; truck<br>
                                    bus &bull; motorcycle &bull; bicycle<br>
                                    train &bull; cow &bull; horse<br>
                                    sheep &bull; dog &bull; traffic_light<br>
                                    stop_sign &bull; bench
                                </div>
                            </div>
                            
                            <!-- Open Images -->
                            <div style="flex: 1.3; background: rgba(16, 185, 129, 0.04); border-top: 3px solid #10b981; padding: 1.5vw;">
                                <div style="font-size: 0.85vw; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 1vw;">Open Images (11)</div>
                                <div style="font-size: 1.05vw; line-height: 1.9; color: #334155;">
                                    box &bull; tire &bull; barrel<br>
                                    ladder &bull; helmet &bull; waste_container<br>
                                    tool &bull; wheel &bull; wheelchair<br>
                                    cart &bull; luggage_bags
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>
                
                <!-- Bottom Callout -->
                <div style="border-top: 1px solid rgba(0,0,0,0.1); padding-top: 1.5vw; text-align: center;">
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1vw; color: var(--accent-blue); text-transform: uppercase; letter-spacing: 0.1vw; margin-bottom: 0.8vw; font-weight: 700;">
                        Normalization Process
                    </div>
                    <div style="font-family: Georgia, 'Times New Roman', serif; font-size: 1.2vw; color: var(--text-color); font-style: italic; max-width: 85%; margin: 0 auto; line-height: 1.5;">
                        "4 + 14 + 11 = 29 total classes. Source annotations were standardized to YOLO format and rigorously quality-controlled prior to dataset integration."
                    </div>
                </div>

            </div>
        </section>'''

# Replace slide 8
content = re.sub(r'<section class="slide" id="slide-8">.*?</section>', new_html.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
