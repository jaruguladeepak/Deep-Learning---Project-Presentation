import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 9 REDESIGN */
        .s9-layout {
            display: flex;
            flex-direction: column;
            height: 100%;
            gap: 1vw;
        }

        .s9-pipeline-container {
            display: flex;
            justify-content: center;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.5vw;
            margin-bottom: 0.5vw;
        }

        .s9-pipeline {
            display: flex;
            align-items: flex-start;
            gap: 1.5vw;
        }

        .s9-stage {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            background: #ffffff;
            border: 1px solid rgba(0,0,0,0.1);
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            border-radius: 8px;
            padding: 1vw 1.5vw;
            width: 14vw;
        }

        .s9-stage-assess {
            width: 17vw;
            border-top: 4px solid var(--accent-blue);
            transform: scale(1.05);
            z-index: 2;
        }

        .s9-stage-detect { border-top: 4px solid var(--accent-cyan); }
        .s9-stage-decide { border-top: 4px solid #d97706; width: 17vw; }

        .s9-stage-num {
            font-size: 0.7vw;
            font-weight: 700;
            color: #64748b;
            margin-bottom: 0.3vw;
        }

        .s9-stage-title {
            font-size: 1vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.8vw;
        }

        .s9-stage-subtitle {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--accent-blue);
            margin-bottom: 0.5vw;
        }

        .s9-list {
            list-style: none;
            padding: 0;
            margin: 0;
            font-size: 0.8vw;
            color: #4b5563;
            line-height: 1.5;
        }

        .s9-arrow {
            display: flex;
            align-items: center;
            color: rgba(0,0,0,0.3);
            font-size: 2vw;
            font-weight: 700;
            height: 10vw;
        }

        .s9-decide-flow {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }

        .s9-states {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.4vw;
            font-size: 0.7vw;
            font-weight: 700;
            margin: 0.5vw 0;
        }

        .s9-state { padding: 0.2vw; border-radius: 4px; }
        .s9-st-run { color: #10b981; }
        .s9-st-warn { color: #d97706; }
        .s9-st-crit { color: #ef4444; }
        .s9-st-stop { color: #991b1b; }
        .s9-st-rec { color: var(--accent-blue); }

        .s9-local-resp {
            margin-top: 1vw;
            padding: 0.6vw;
            background: rgba(239, 68, 68, 0.05);
            border: 1px solid rgba(239, 68, 68, 0.2);
            border-radius: 8px;
            width: 100%;
        }

        .s9-lr-title {
            font-size: 0.8vw;
            font-weight: 700;
            color: #ef4444;
            margin-bottom: 0.4vw;
        }

        .s9-factors-container {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.2vw 2vw;
        }

        .s9-factors-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2vw;
        }

        .s9-factor-col {
            display: flex;
            flex-direction: column;
        }

        .s9-fc-title {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--accent-blue);
            border-bottom: 2px solid rgba(0,0,0,0.1);
            padding-bottom: 0.5vw;
            margin-bottom: 0.8vw;
        }

        .s9-fc-sub {
            font-size: 0.8vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.5vw;
        }

        .s9-fc-desc {
            font-size: 0.75vw;
            color: #64748b;
            line-height: 1.4;
        }

        .s9-local-callout {
            margin-top: auto;
            background: rgba(239, 68, 68, 0.03);
            border: 1px solid rgba(239, 68, 68, 0.15);
            border-left: 4px solid #ef4444;
            border-radius: 8px;
            padding: 1.2vw 2vw;
            display: flex;
            align-items: center;
        }

        .s9-lc-title {
            font-size: 0.9vw;
            font-weight: 700;
            color: #ef4444;
            width: 15vw;
        }

        .s9-lc-text {
            font-size: 0.85vw;
            color: #4b5563;
            flex: 1;
        }

        .s9-footnote {
            font-size: 0.6vw;
            color: #94a3b8;
            font-style: italic;
            text-align: right;
            margin-top: 0.2vw;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_9 = '''
        <!-- Slide 9: Threat Assessment & Safety Control -->
        <section class="slide" id="slide-9">
            <div class="slide-header">
                <div class="slide-number">09</div>
                <div class="slide-title">Threat Assessment &amp; Safety Control <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">From Object Detection &rarr; Threat Evaluation &rarr; Local Safety Response</span></div>
            </div>
            
            <div class="slide-body">
                <div class="s9-layout">
                    
                    <div class="section-label" style="text-align: center; margin-bottom: 0.2vw;">THREAT DECISION PIPELINE</div>
                    
                    <div class="s9-pipeline-container">
                        <div class="s9-pipeline">
                            
                            <!-- 1. DETECT -->
                            <div class="s9-stage s9-stage-detect">
                                <div class="s9-stage-num">01 &middot; DETECT</div>
                                <div class="s9-stage-title">YOLOv8</div>
                                <ul class="s9-list">
                                    <li>Class</li>
                                    <li>Confidence</li>
                                    <li>Bounding Box</li>
                                </ul>
                                <div style="font-size: 0.7vw; color: #94a3b8; margin-top: 1vw;">Detects candidate objects from the input frame.</div>
                            </div>
                            
                            <div class="s9-arrow">&rarr;</div>
                            
                            <!-- 2. ASSESS -->
                            <div class="s9-stage s9-stage-assess">
                                <div class="s9-stage-num">02 &middot; ASSESS</div>
                                <div class="s9-stage-title">THREAT ANALYZER</div>
                                <ul class="s9-list">
                                    <li>Severity</li>
                                    <li style="color: rgba(0,0,0,0.2);">+</li>
                                    <li>Safety Zone</li>
                                    <li style="color: rgba(0,0,0,0.2);">+</li>
                                    <li>Movement</li>
                                    <li style="color: rgba(0,0,0,0.2);">+</li>
                                    <li>Persistence</li>
                                    <li style="color: rgba(0,0,0,0.2);">+</li>
                                    <li>Confidence</li>
                                </ul>
                                <div style="margin: 0.5vw 0; color: rgba(0,0,0,0.3);">&darr;</div>
                                <div style="font-size: 0.75vw; font-weight: 700; color: var(--text-color);">Threat Score</div>
                                <div style="font-size: 0.7vw; color: #64748b; margin-top: 0.2vw;">LOW &rarr; MEDIUM &rarr; HIGH &rarr; CRITICAL</div>
                            </div>
                            
                            <div class="s9-arrow">&rarr;</div>
                            
                            <!-- 3. DECIDE -->
                            <div class="s9-stage s9-stage-decide">
                                <div class="s9-stage-num">03 &middot; DECIDE</div>
                                <div class="s9-stage-title">SAFETY STATE</div>
                                
                                <div class="s9-decide-flow">
                                    <div class="s9-states">
                                        <span class="s9-state s9-st-run">RUNNING</span> &rarr;
                                        <span class="s9-state s9-st-warn">WARNING</span> &rarr;
                                        <span class="s9-state s9-st-crit">CRITICAL</span> &rarr;
                                        <span class="s9-state s9-st-stop">STOPPING</span> &rarr;
                                        <span class="s9-state s9-st-stop">STOPPED</span> &rarr;
                                        <span class="s9-state s9-st-rec">RECOVERY</span>
                                    </div>
                                    
                                    <div style="margin: 0.3vw 0; color: rgba(0,0,0,0.3);">&darr;</div>
                                    
                                    <div class="s9-local-resp">
                                        <div class="s9-lr-title">LOCAL RESPONSE</div>
                                        <div style="font-size: 0.75vw; color: var(--text-color); font-weight: 700; margin-bottom: 0.2vw;">STOP / RESUME</div>
                                        <div style="font-size: 0.75vw; color: #4b5563;">ESP32 Safety Controller</div>
                                        <div style="font-size: 0.75vw; color: #4b5563;">Motor-Control Interface</div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                    
                    <div class="section-label" style="text-align: left; margin-bottom: 0.2vw; margin-top: 0.5vw;">THREAT FACTORS</div>
                    
                    <div class="s9-factors-container">
                        <div class="s9-factors-grid">
                            
                            <div class="s9-factor-col">
                                <div class="s9-fc-title">SEVERITY</div>
                                <div class="s9-fc-sub">Object-specific risk</div>
                                <div class="s9-fc-desc">
                                    <strong style="color: #ef4444;">Critical:</strong> Person, vehicle<br>
                                    <strong style="color: #10b981;">Low:</strong> Bird nest, bench
                                </div>
                            </div>
                            
                            <div class="s9-factor-col">
                                <div class="s9-fc-title">SAFETY ZONE</div>
                                <div class="s9-fc-sub">Relative image position</div>
                                <div class="s9-fc-desc">
                                    <strong style="color: #10b981;">&le; 60%</strong> Green<br>
                                    <strong style="color: #d97706;">60&ndash;80%</strong> Yellow<br>
                                    <strong style="color: #ef4444;">&gt; 80%</strong> Red
                                </div>
                            </div>
                            
                            <div class="s9-factor-col">
                                <div class="s9-fc-title">MOVEMENT</div>
                                <div class="s9-fc-sub">Directional vector</div>
                                <div class="s9-fc-desc">
                                    Approaching &rarr; <strong>&uarr;</strong> Risk<br>
                                    Static &rarr; <strong>&rarr;</strong> Risk<br>
                                    Away &rarr; <strong>&darr;</strong> Risk
                                </div>
                            </div>
                            
                            <div class="s9-factor-col">
                                <div class="s9-fc-title">PERSISTENCE</div>
                                <div class="s9-fc-sub">Multi-frame confirmation</div>
                                <div class="s9-fc-desc">
                                    Multiple continuous frames confirm the threat before escalation.
                                </div>
                            </div>
                            
                        </div>
                    </div>
                    
                    <div class="s9-local-callout">
                        <div class="s9-lc-title">LOCAL-FIRST SAFETY</div>
                        <div class="s9-lc-text"><strong>Immediate safety logic remains at the edge and does not depend on cloud availability.</strong></div>
                    </div>
                    
                    <div class="s9-footnote">* Physical L293D/motor validation remains part of hardware testing.</div>
                    
                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide" id="slide-9">.*?</section>', new_slide_9.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
