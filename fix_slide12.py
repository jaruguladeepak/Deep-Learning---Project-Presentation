import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 12 REDESIGN */
        .evolution-layout {
            display: flex;
            flex-direction: column;
            gap: 1.5vw;
            height: 100%;
        }

        .evolution-top {
            display: flex;
            gap: 2vw;
        }

        .evolution-card {
            flex: 1;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.5vw;
            display: flex;
            flex-direction: column;
        }

        .ec-header {
            margin-bottom: 1vw;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding-bottom: 0.8vw;
        }

        .ec-title {
            font-size: 1.15vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.2vw;
            text-transform: uppercase;
        }

        .ec-subtitle {
            font-size: 0.8vw;
            color: var(--accent-blue);
        }

        .ec-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1vw;
            margin-bottom: 1.2vw;
        }

        .ec-stat {
            display: flex;
            flex-direction: column;
        }

        .ec-stat-val {
            font-size: 1.1vw;
            font-weight: 700;
            color: var(--text-color);
        }

        .ec-stat-lbl {
            font-size: 0.75vw;
            color: #64748b;
            text-transform: uppercase;
        }

        .ec-divider {
            height: 1px;
            background: rgba(0,0,0,0.05);
            margin-bottom: 1.2vw;
        }

        .ec-metrics {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: auto;
        }

        .ec-metric {
            text-align: center;
        }

        .ec-metric-val {
            font-size: 2vw;
            font-weight: 700;
        }

        .ec-metric-lbl {
            font-size: 0.8vw;
            color: #64748b;
        }

        .v1-val { color: var(--accent-blue); }
        .v2-val { color: #d97706; }

        .evolution-note {
            background: rgba(0,0,0,0.02);
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 6px;
            padding: 0.8vw;
            text-align: center;
            font-size: 0.82vw;
            color: var(--text-color);
        }

        .safety-pipeline-container {
            margin-top: auto;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.5vw;
        }

        .safety-pipeline {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1.2vw;
            margin-bottom: 1.5vw;
        }

        .sp-stage {
            display: flex;
            flex-direction: column;
            width: 22%;
            text-align: center;
        }

        .sp-label {
            font-size: 0.9vw;
            font-weight: 700;
            margin-bottom: 0.5vw;
        }

        .sp-stage-1 .sp-label { color: var(--accent-cyan); }
        .sp-stage-2 .sp-label { color: var(--accent-blue); }
        .sp-stage-3 .sp-label { color: #ef4444; }
        .sp-stage-4 .sp-label { color: #16a34a; }

        .sp-title {
            font-size: 1vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.3vw;
        }

        .sp-desc {
            font-size: 0.75vw;
            color: #64748b;
            line-height: 1.4;
        }

        .sp-arrow {
            color: rgba(0,0,0,0.3);
            font-size: 1.5vw;
            font-weight: 700;
        }

        .sp-summary {
            text-align: center;
            font-size: 0.95vw;
            font-weight: 700;
            color: var(--text-color);
            border-top: 1px solid rgba(0,0,0,0.05);
            padding-top: 1vw;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_12 = '''
        <!-- Slide 12: Model & System Comparison -->
        <section class="slide" id="slide-12">
            <div class="slide-header">
                <div class="slide-number">12</div>
                <div class="slide-title">Model &amp; System Comparison <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">From Object Detection to Intelligent Railway Safety Monitoring</span></div>
            </div>
            
            <div class="slide-body">
                <div class="evolution-layout">
                    
                    <div class="section-label">MODEL EVOLUTION</div>
                    
                    <div class="evolution-top">
                        <!-- V1 Card -->
                        <div class="evolution-card">
                            <div class="ec-header">
                                <div class="ec-title">V1 &middot; FOCUSED RAILWAY DETECTOR</div>
                                <div class="ec-subtitle">Primary RailFOD23 baseline</div>
                            </div>
                            
                            <div class="ec-stats">
                                <div class="ec-stat">
                                    <div class="ec-stat-val">4</div>
                                    <div class="ec-stat-lbl">Classes</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">14,615</div>
                                    <div class="ec-stat-lbl">Images</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">11,691</div>
                                    <div class="ec-stat-lbl">Train</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">2,924</div>
                                    <div class="ec-stat-lbl">Validation</div>
                                </div>
                            </div>
                            
                            <div class="ec-divider"></div>
                            
                            <div class="ec-metrics">
                                <div class="ec-metric">
                                    <div class="ec-metric-val v1-val">0.936</div>
                                    <div class="ec-metric-lbl">mAP@50</div>
                                </div>
                                <div class="ec-metric">
                                    <div class="ec-metric-val v1-val">0.794</div>
                                    <div class="ec-metric-lbl">mAP@50:95</div>
                                </div>
                            </div>
                        </div>

                        <!-- V2 Card -->
                        <div class="evolution-card">
                            <div class="ec-header">
                                <div class="ec-title">V2 &middot; EXPANDED DETECTOR</div>
                                <div class="ec-subtitle">29-class diagnostic baseline &middot; RailFOD23 + MS-COCO + Open Images</div>
                            </div>
                            
                            <div class="ec-stats">
                                <div class="ec-stat">
                                    <div class="ec-stat-val">29</div>
                                    <div class="ec-stat-lbl">Classes</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">37,445</div>
                                    <div class="ec-stat-lbl">Image/Label Pairs</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">29,956</div>
                                    <div class="ec-stat-lbl">Train</div>
                                </div>
                                <div class="ec-stat">
                                    <div class="ec-stat-val">7,489</div>
                                    <div class="ec-stat-lbl">Validation</div>
                                </div>
                            </div>
                            
                            <div class="ec-divider"></div>
                            
                            <div class="ec-metrics">
                                <div class="ec-metric">
                                    <div class="ec-metric-val v2-val">0.461</div>
                                    <div class="ec-metric-lbl">mAP@50</div>
                                </div>
                                <div class="ec-metric">
                                    <div class="ec-metric-val v2-val">0.299</div>
                                    <div class="ec-metric-lbl">mAP@50:95</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="evolution-note">
                        <strong>Different task scope:</strong> V2 expands the ontology from 4 to 29 classes and is therefore treated as a diagnostic baseline rather than a direct replacement for V1.
                    </div>

                    <div class="safety-pipeline-container">
                        <div class="section-label">FROM DETECTION TO SAFETY MONITORING</div>
                        
                        <div class="safety-pipeline">
                            <div class="sp-stage sp-stage-1">
                                <div class="sp-label">DETECT</div>
                                <div class="sp-title">YOLOv8</div>
                                <div class="sp-desc">Object + Confidence</div>
                            </div>
                            
                            <div class="sp-arrow">&rarr;</div>
                            
                            <div class="sp-stage sp-stage-2">
                                <div class="sp-label">ASSESS</div>
                                <div class="sp-title">Threat Engine</div>
                                <div class="sp-desc">Class + Zone + Movement + Persistence</div>
                            </div>
                            
                            <div class="sp-arrow">&rarr;</div>
                            
                            <div class="sp-stage sp-stage-3">
                                <div class="sp-label">RESPOND</div>
                                <div class="sp-title">ESP32</div>
                                <div class="sp-desc">STOP / RESUME</div>
                            </div>
                            
                            <div class="sp-arrow">&rarr;</div>
                            
                            <div class="sp-stage sp-stage-4">
                                <div class="sp-label">MONITOR</div>
                                <div class="sp-title">AWS + Dashboard</div>
                                <div class="sp-desc">Telemetry + Events + Status</div>
                            </div>
                        </div>
                        
                        <div class="sp-summary">
                            RailFOD23 extends object detection into an integrated safety-monitoring pipeline.
                        </div>
                    </div>

                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide" id="slide-12">.*?</section>', new_slide_12.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
