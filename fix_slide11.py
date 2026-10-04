import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 11 REDESIGN */
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
            padding: 0.8vw 1.2vw;
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
            margin-bottom: 0.3vw;
        }

        .s11-tech-desc {
            font-size: 0.75vw;
            color: #64748b;
        }

        .s11-inference-timing {
            margin-top: 1vw;
            padding: 0.8vw;
            background: rgba(0,0,0,0.02);
            border-radius: 8px;
            font-size: 0.8vw;
            text-align: center;
        }

        .s11-timing-label {
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.3vw;
            font-size: 0.75vw;
        }

        .s11-results {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 2.5vw;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .s11-result-context {
            text-align: center;
            margin-bottom: 1.5vw;
        }

        .s11-rc-top {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--accent-blue);
            text-transform: uppercase;
            margin-bottom: 0.4vw;
        }

        .s11-rc-bot {
            font-size: 0.8vw;
            color: #64748b;
        }

        .s11-hero-container {
            text-align: center;
            margin-bottom: 2vw;
        }

        .s11-hero-val {
            font-size: 3vw;
            font-weight: 700;
            color: #059669;
            line-height: 1;
            margin-bottom: 0.5vw;
        }

        .s11-hero-lbl {
            font-size: 1.2vw;
            font-weight: 700;
            color: var(--text-color);
        }

        .s11-supp-metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            width: 100%;
            text-align: center;
            border-top: 1px solid rgba(0,0,0,0.05);
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding: 1.5vw 0;
            margin-bottom: 2vw;
        }

        .s11-supp-item {
            display: flex;
            flex-direction: column;
        }

        .s11-supp-lbl {
            font-size: 0.75vw;
            text-transform: uppercase;
            color: #64748b;
            margin-bottom: 0.5vw;
        }

        .s11-supp-val {
            font-size: 1.2vw;
            font-weight: 700;
            color: var(--text-color);
        }

        .s11-class-table-container {
            width: 100%;
            margin-top: auto;
        }

        .s11-class-title {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 1vw;
            text-transform: uppercase;
            text-align: left;
        }

        .s11-class-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.8vw;
        }

        .s11-class-table th {
            text-align: right;
            padding-bottom: 0.8vw;
            border-bottom: 2px solid rgba(0,0,0,0.1);
            color: #64748b;
            font-weight: 700;
        }

        .s11-class-table th:first-child {
            text-align: left;
        }

        .s11-class-table td {
            padding: 0.7vw 0;
            text-align: right;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            color: var(--text-color);
        }

        .s11-class-table td:first-child {
            text-align: left;
        }

        .s11-class-table tr:last-child td {
            border-bottom: none;
        }

        .s11-highlight {
            font-weight: 700;
            color: var(--accent-blue);
        }

        .s11-training-ctx {
            margin-top: 1vw;
            text-align: right;
            font-size: 0.7vw;
            color: #94a3b8;
            font-style: italic;
            width: 100%;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_11 = '''
        <!-- Slide 11: Implementation & Results -->
        <section class="slide" id="slide-11">
            <div class="slide-header">
                <div class="slide-number">11</div>
                <div class="slide-title">Implementation &amp; Results <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">Prototype Implementation and V1 Detection Performance</span></div>
            </div>
            
            <div class="slide-body">
                <div class="s11-layout">
                    
                    <!-- Left: Technology Stack -->
                    <div class="s11-tech-stack">
                        <div class="section-label" style="margin-bottom: 0.5vw;">TECHNOLOGY STACK</div>
                        
                        <div class="s11-tech-item s11-tech-ai">
                            <div class="s11-tech-title">AI / COMPUTER VISION</div>
                            <div class="s11-tech-tools">Python &middot; YOLOv8 Nano &middot; OpenCV</div>
                            <div class="s11-tech-desc">Detection &middot; bounding boxes &middot; confidence estimation</div>
                        </div>

                        <div class="s11-tech-item s11-tech-embed">
                            <div class="s11-tech-title">EMBEDDED</div>
                            <div class="s11-tech-tools">ESP32 &middot; PlatformIO &middot; Wokwi &middot; L293D</div>
                            <div class="s11-tech-desc">Local STOP / RESUME safety-control path</div>
                        </div>

                        <div class="s11-tech-item s11-tech-cloud">
                            <div class="s11-tech-title">CLOUD</div>
                            <div class="s11-tech-tools">AWS IoT Core &middot; MQTT &middot; DynamoDB &middot; Lambda &middot; SNS</div>
                            <div class="s11-tech-desc">Telemetry &middot; event persistence &middot; critical-event processing</div>
                        </div>

                        <div class="s11-tech-item s11-tech-web">
                            <div class="s11-tech-title">WEB</div>
                            <div class="s11-tech-tools">FastAPI &middot; React / Vite</div>
                            <div class="s11-tech-desc">Read-only Railway Safety Operations Center</div>
                        </div>

                        <div class="s11-inference-timing">
                            <div class="s11-timing-label">REPORTED INFERENCE TIMING</div>
                            <div style="color: #4b5563;">&sim;3.8 ms/frame</div>
                        </div>
                    </div>

                    <!-- Right: Results -->
                    <div class="s11-results">
                        <div class="section-label" style="margin-bottom: 1.5vw; width: 100%; text-align: left;">V1 YOLOv8n &mdash; DETECTION PERFORMANCE</div>
                        
                        <div class="s11-result-context">
                            <div class="s11-rc-top">V1 &middot; 4-CLASS RAILFOD23 DETECTOR</div>
                            <div class="s11-rc-bot">14,615 images &middot; 40,541 bounding boxes</div>
                        </div>

                        <div class="s11-hero-container">
                            <div class="s11-hero-val">93.6%</div>
                            <div class="s11-hero-lbl">mAP@50</div>
                        </div>

                        <div class="s11-supp-metrics">
                            <div class="s11-supp-item">
                                <div class="s11-supp-lbl">PRECISION</div>
                                <div class="s11-supp-val">0.909</div>
                            </div>
                            <div class="s11-supp-item">
                                <div class="s11-supp-lbl">RECALL</div>
                                <div class="s11-supp-val">0.871</div>
                            </div>
                            <div class="s11-supp-item">
                                <div class="s11-supp-lbl">mAP@50:95</div>
                                <div class="s11-supp-val">0.794</div>
                            </div>
                        </div>

                        <div class="s11-class-table-container">
                            <div class="s11-class-title">CLASS-LEVEL PERFORMANCE</div>
                            <table class="s11-class-table">
                                <thead>
                                    <tr>
                                        <th>Class</th>
                                        <th>Precision</th>
                                        <th>Recall</th>
                                        <th>mAP@50</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Bird Nest</strong></td>
                                        <td>0.992</td>
                                        <td>0.970</td>
                                        <td class="s11-highlight">0.992</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Plastic Bag</strong></td>
                                        <td>0.831</td>
                                        <td>0.822</td>
                                        <td class="s11-highlight">0.892</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Debris</strong></td>
                                        <td>0.937</td>
                                        <td>0.860</td>
                                        <td class="s11-highlight">0.935</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Balloon</strong></td>
                                        <td>0.878</td>
                                        <td>0.831</td>
                                        <td class="s11-highlight">0.924</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        
                        <div class="s11-training-ctx">V1 training result &middot; 50 epochs</div>
                    </div>
                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide" id="slide-11">.*?</section>', new_slide_11.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
