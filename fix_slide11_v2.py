import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 11 REDESIGN (V2 Focused) */
        .s11-layout {
            display: grid;
            grid-template-columns: 1fr 1.6fr;
            gap: 2vw;
            height: 100%;
        }

        .s11-tech-stack {
            display: flex;
            flex-direction: column;
            gap: 1vw;
        }

        .s11-tech-item {
            padding: 1vw 1.2vw;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            display: flex;
            flex-direction: column;
        }

        .s11-tech-ai { border-left: 4px solid var(--accent-cyan); }
        .s11-tech-embed { border-left: 4px solid #ef4444; }
        .s11-tech-cloud { border-left: 4px solid var(--accent-blue); }
        .s11-tech-web { border-left: 4px solid #10b981; }

        .s11-tech-title {
            font-size: 1vw;
            font-weight: 700;
            margin-bottom: 0.4vw;
            color: var(--text-color);
            text-transform: uppercase;
        }

        .s11-tech-tools {
            font-size: 0.85vw;
            font-weight: 700;
            color: var(--accent-blue);
        }

        .s11-inference-timing {
            margin-top: auto;
            padding: 1vw;
            background: rgba(0,0,0,0.02);
            border-radius: 8px;
            font-size: 0.8vw;
            text-align: center;
            color: #4b5563;
        }

        .s11-results {
            display: flex;
            flex-direction: column;
            gap: 1vw;
        }

        .s11-v2-section {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 2vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            border-top: 4px solid #d97706;
        }

        .s11-hero-container {
            text-align: center;
            margin-bottom: 1.5vw;
        }

        .s11-hero-val {
            font-size: 3.5vw;
            font-weight: 700;
            line-height: 1;
            margin-bottom: 0.5vw;
        }

        .s11-hero-lbl {
            font-size: 1.2vw;
            font-weight: 700;
            color: var(--text-color);
        }

        .s11-v2-supp {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            width: 100%;
            text-align: center;
            border-top: 1px solid rgba(0,0,0,0.05);
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding: 1.2vw 0;
            margin-bottom: 1.5vw;
        }

        .s11-v2-supp-item {
            display: flex;
            flex-direction: column;
        }

        .s11-v2-supp-lbl {
            font-size: 0.75vw;
            text-transform: uppercase;
            color: #64748b;
            margin-bottom: 0.5vw;
        }

        .s11-v2-supp-val {
            font-size: 1.2vw;
            font-weight: 700;
            color: var(--text-color);
        }

        .s11-v2-dataset {
            text-align: center;
            background: rgba(0,0,0,0.02);
            padding: 0.8vw 1.5vw;
            border-radius: 6px;
            width: 80%;
        }

        .s11-v1-reference {
            background: rgba(2, 132, 199, 0.03);
            border: 1px solid rgba(2, 132, 199, 0.1);
            border-radius: 12px;
            padding: 1.2vw 2vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            border-left: 4px solid var(--accent-blue);
        }

        .s11-diff-note {
            text-align: center;
            font-size: 0.8vw;
            color: #4b5563;
            padding: 0.8vw;
            background: rgba(0,0,0,0.03);
            border-radius: 6px;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_11 = '''
        <!-- Slide 11: Implementation & Results -->
        <section class="slide" id="slide-11">
            <div class="slide-header">
                <div class="slide-number">11</div>
                <div class="slide-title">Implementation &amp; Results <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">V1 Baseline and V2 Expanded Detection Results</span></div>
            </div>
            
            <div class="slide-body">
                <div class="s11-layout">
                    
                    <!-- Left: Technology Stack -->
                    <div class="s11-tech-stack">
                        <div class="section-label" style="margin-bottom: 0.5vw;">TECHNOLOGY STACK</div>
                        
                        <div class="s11-tech-item s11-tech-ai">
                            <div class="s11-tech-title">AI / COMPUTER VISION</div>
                            <div class="s11-tech-tools">Python &middot; YOLOv8 Nano &middot; OpenCV</div>
                        </div>

                        <div class="s11-tech-item s11-tech-embed">
                            <div class="s11-tech-title">EMBEDDED</div>
                            <div class="s11-tech-tools">ESP32 &middot; PlatformIO &middot; Wokwi &middot; L293D</div>
                        </div>

                        <div class="s11-tech-item s11-tech-cloud">
                            <div class="s11-tech-title">CLOUD</div>
                            <div class="s11-tech-tools">AWS IoT Core &middot; MQTT &middot; DynamoDB &middot; Lambda &middot; SNS</div>
                        </div>

                        <div class="s11-tech-item s11-tech-web">
                            <div class="s11-tech-title">WEB</div>
                            <div class="s11-tech-tools">FastAPI &middot; React / Vite</div>
                        </div>

                        <div class="s11-inference-timing">
                            <strong>&sim;3.8 ms/frame</strong> &mdash; reported V1 inference timing
                        </div>
                    </div>

                    <!-- Right: Results -->
                    <div class="s11-results">
                        
                        <!-- V2 Hero -->
                        <div class="s11-v2-section">
                            <div class="section-label" style="text-align: center; color: #d97706;">V2 &middot; 29-CLASS DIAGNOSTIC BASELINE</div>
                            <div style="text-align: center; font-size: 0.8vw; color: #64748b; margin-bottom: 1.5vw; margin-top: 0.3vw;">
                                29 classes &middot; 29,956 train &middot; 7,489 validation
                            </div>
                            
                            <div class="s11-hero-container">
                                <div class="s11-hero-val" style="color: #d97706;">46.1%</div>
                                <div class="s11-hero-lbl">mAP@50</div>
                            </div>
                            
                            <div class="s11-v2-supp">
                                <div class="s11-v2-supp-item">
                                    <div class="s11-v2-supp-lbl">PRECISION</div>
                                    <div class="s11-v2-supp-val">0.554</div>
                                </div>
                                <div class="s11-v2-supp-item">
                                    <div class="s11-v2-supp-lbl">RECALL</div>
                                    <div class="s11-v2-supp-val">0.459</div>
                                </div>
                                <div class="s11-v2-supp-item">
                                    <div class="s11-v2-supp-lbl">mAP@50:95</div>
                                    <div class="s11-v2-supp-val">0.299</div>
                                </div>
                            </div>
                            
                            <div class="s11-v2-dataset">
                                <div style="font-size: 0.8vw; font-weight: 700; margin-bottom: 0.3vw; color: var(--text-color);">V2 DATASET: 37,445 image/label pairs</div>
                                <div style="font-size: 0.75vw; color: #64748b;">RailFOD23 (4) + MS-COCO (14) + Open Images (11)</div>
                            </div>
                        </div>
                        
                        <!-- V1 Reference -->
                        <div class="s11-v1-reference">
                            <div style="font-size: 0.85vw; font-weight: 700; color: var(--accent-blue); margin-bottom: 0.3vw; text-transform: uppercase;">
                                V1 &middot; 4-CLASS RAILFOD23 REFERENCE
                            </div>
                            <div style="font-size: 0.75vw; color: #64748b; margin-bottom: 0.8vw;">
                                14,615 images &middot; 40,541 bounding boxes
                            </div>
                            <div style="display: flex; gap: 3vw; font-size: 0.9vw;">
                                <div><strong>93.6%</strong> mAP@50</div>
                                <div><strong>79.4%</strong> mAP@50:95</div>
                            </div>
                        </div>
                        
                        <div class="s11-diff-note">
                            <strong>Different task scopes &mdash;</strong> V2 is an expanded diagnostic baseline, not a direct replacement for V1.
                        </div>
                        
                    </div>
                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide" id="slide-11">.*?</section>', new_slide_11.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
