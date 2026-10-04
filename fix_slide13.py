import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject the CSS right before </style>
new_css = '''
        .conclusion-layout {
            display: grid;
            grid-template-columns: 1.55fr 1fr;
            gap: 1.5vw;
            margin-top: 1.5vw;
        }

        .conclusion-main,
        .achievements {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.5vw;
        }

        .conclusion-main h2 {
            font-size: 1.35vw;
            line-height: 1.45;
            margin: 0.7vw 0;
            color: var(--text-color);
        }

        .conclusion-main p {
            font-size: 0.9vw;
            line-height: 1.5;
            color: #4b5563;
            margin: 0;
        }

        .core-flow {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.8vw;
            margin-top: 1.2vw;
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--accent-blue);
        }

        .core-flow b {
            color: #6b7280;
        }

        .achievements {
            display: flex;
            flex-direction: column;
            gap: 0.55vw;
        }

        .achievement {
            padding: 0.55vw 0.7vw;
            border-left: 3px solid var(--accent-cyan);
            background: rgba(2, 132, 199, 0.04);
            font-size: 0.78vw;
            color: var(--text-color);
        }

        .future-section {
            margin-top: 1.2vw;
        }

        .future-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.7vw;
            margin-top: 0.7vw;
        }

        .future-item {
            padding: 0.75vw 0.9vw;
            border: 1px solid var(--glass-border);
            border-left: 3px solid var(--accent-cyan);
            border-radius: 8px;
            background: var(--glass-bg);
        }

        .future-item strong {
            display: block;
            font-size: 0.72vw;
            color: var(--text-color);
            margin-bottom: 0.3vw;
        }

        .future-item p {
            margin: 0;
            font-size: 0.65vw;
            line-height: 1.35;
            color: #64748b;
        }

        .references-strip {
            display: flex;
            align-items: center;
            gap: 1.2vw;
            margin-top: 0.9vw;
            padding: 0.65vw 0.9vw;
            border-top: 1px solid var(--glass-border);
            border-bottom: 1px solid var(--glass-border);
            font-size: 0.62vw;
            color: #64748b;
        }

        .references-strip .section-label {
            margin-right: 0.3vw;
            white-space: nowrap;
            color: var(--accent-cyan);
            font-weight: 700;
        }
        
        .section-label {
            color: var(--accent-cyan);
            font-size: 0.9vw;
            font-weight: 700;
            text-transform: uppercase;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_13 = '''
        <section class="slide" id="slide-13">

            <div class="slide-header">
                <div class="slide-number">13</div>

                <div class="slide-title">
                    CONCLUSION &amp; FUTURE SCOPE
                    <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">From Detection to Intelligent Railway Safety Monitoring</span>
                </div>
            </div>

            <!-- CONCLUSION -->
            <div class="conclusion-layout">

                <div class="conclusion-main">
                    <div class="section-label">CONCLUSION</div>

                    <h2>
                        RailFOD23 demonstrates an end-to-end academic
                        prototype for intelligent railway safety monitoring.
                    </h2>

                    <p>
                        The system integrates YOLOv8 detection, threat assessment,
                        local ESP32 safety control, AWS IoT telemetry, and a
                        read-only operations dashboard.
                    </p>

                    <div class="core-flow">
                        <span>DETECT</span>
                        <b>&rarr;</b>
                        <span>ASSESS</span>
                        <b>&rarr;</b>
                        <span>RESPOND</span>
                        <b>&rarr;</b>
                        <span>MONITOR</span>
                    </div>
                </div>

                <div class="achievements">
                    <div class="section-label">KEY ACHIEVEMENTS</div>

                    <div class="achievement">YOLOv8 foreign-object detection</div>
                    <div class="achievement">Threat assessment + safety state machine</div>
                    <div class="achievement">ESP32 STOP / RESUME communication</div>
                    <div class="achievement">AWS IoT + DynamoDB + Lambda/SNS</div>
                    <div class="achievement">React + FastAPI monitoring dashboard</div>
                </div>

            </div>

            <!-- FUTURE SCOPE -->
            <div class="future-section">

                <div class="section-label">FUTURE SCOPE</div>

                <div class="future-grid">

                    <div class="future-item">
                        <strong>01 &middot; THERMAL / IR VISION</strong>
                        <p>Improve detection under low-light and adverse visibility.</p>
                    </div>

                    <div class="future-item">
                        <strong>02 &middot; IMPROVED TRACKING</strong>
                        <p>Strengthen multi-object tracking and trajectory estimation.</p>
                    </div>

                    <div class="future-item">
                        <strong>03 &middot; REAL-WORLD DATASET</strong>
                        <p>Expand training using diverse railway environments.</p>
                    </div>

                    <div class="future-item">
                        <strong>04 &middot; EDGE OPTIMIZATION</strong>
                        <p>Explore compression, quantization and optimized inference.</p>
                    </div>

                    <div class="future-item">
                        <strong>05 &middot; CALIBRATION &amp; VALIDATION</strong>
                        <p>Add camera calibration and physical hardware validation.</p>
                    </div>

                    <div class="future-item">
                        <strong>06 &middot; FIELD TESTING</strong>
                        <p>Progress toward controlled trials and safety validation.</p>
                    </div>

                </div>

            </div>

            <!-- REFERENCES -->
            <div class="references-strip">

                <span class="section-label">REFERENCES</span>

                <span>[1] RailFOD23 Dataset, Figshare</span>
                <span>[2] Ultralytics YOLO</span>
                <span>[3] Microsoft COCO, ECCV 2014</span>
                <span>[4] Espressif ESP32 Documentation</span>
                <span>[5] AWS IoT Core Documentation</span>

            </div>

            <div style="text-align: center; font-size: 0.8vw; color: #4b5563; font-weight: 600; margin-top: auto; padding-top: 1vw; text-transform: uppercase; letter-spacing: 0.1vw;">
                RailFOD23 &nbsp;|&nbsp; AI + Edge Safety + Cloud Monitoring
            </div>

        </section>
'''

content = re.sub(r'<section class="slide" id="slide-13">.*?</section>', new_slide_13.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
