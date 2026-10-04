import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
        /* SLIDE 10 REDESIGN (AWS ARCHITECTURE) */
        .s10-layout {
            display: flex;
            flex-direction: column;
            height: 100%;
            gap: 1.5vw;
        }

        .s10-arch-container {
            display: flex;
            justify-content: center;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 2vw 1.5vw;
            margin-bottom: 0.5vw;
        }

        .s10-arch-flow {
            display: flex;
            align-items: flex-start;
            gap: 2vw;
        }

        .s10-arch-block {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 1.2vw;
            border-radius: 8px;
            background: #ffffff;
            border: 1px solid rgba(0,0,0,0.1);
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            min-width: 14vw;
        }

        .s10-ab-edge { border-top: 4px solid var(--accent-cyan); }
        .s10-ab-aws { border-top: 4px solid var(--accent-blue); }
        .s10-ab-data { border-top: 4px solid #d97706; }
        .s10-ab-mon { border-top: 4px solid #10b981; }

        .s10-ab-title {
            font-size: 1vw;
            font-weight: 700;
            margin-bottom: 1vw;
            color: var(--text-color);
        }

        .s10-ab-node {
            font-size: 0.85vw;
            font-weight: 700;
            color: var(--text-color);
            padding: 0.6vw 1vw;
            background: rgba(0,0,0,0.03);
            border-radius: 6px;
            margin-bottom: 0.5vw;
            width: 100%;
        }

        .s10-ab-desc {
            font-size: 0.75vw;
            color: #64748b;
            margin-top: 0.5vw;
            line-height: 1.3;
        }

        .s10-arch-arrow {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: rgba(0,0,0,0.3);
            font-size: 1.5vw;
            font-weight: 700;
            margin-top: 2vw;
        }

        .s10-arrow-label {
            font-size: 0.7vw;
            color: #64748b;
            margin-bottom: 0.2vw;
        }

        .s10-local-stop {
            margin-top: 1.2vw;
            padding: 0.6vw;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.2);
            border-radius: 6px;
            color: #ef4444;
            font-weight: 700;
            font-size: 0.8vw;
            width: 100%;
        }

        .s10-branch {
            display: flex;
            gap: 1vw;
            width: 100%;
            margin-top: 0.2vw;
        }

        .s10-branch-col {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .s10-service-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5vw;
            margin-bottom: 1vw;
        }

        .s10-service-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            padding: 1vw;
            border-radius: 8px;
            text-align: center;
        }

        .s10-sc-title {
            font-size: 0.9vw;
            font-weight: 700;
            color: var(--accent-blue);
            margin-bottom: 0.3vw;
        }

        .s10-sc-sub {
            font-size: 0.75vw;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.3vw;
        }

        .s10-sc-desc {
            font-size: 0.75vw;
            color: #64748b;
        }

        .s10-bottom-notes {
            display: flex;
            flex-direction: column;
            gap: 0.8vw;
            margin-top: auto;
        }

        .s10-note {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            padding: 1vw 1.5vw;
            border-radius: 8px;
            display: flex;
            align-items: center;
        }

        .s10-note-local { border-left: 4px solid #ef4444; }
        .s10-note-read { border-left: 4px solid var(--accent-blue); }

        .s10-note-title {
            font-size: 0.85vw;
            font-weight: 700;
            width: 15vw;
            color: var(--text-color);
        }

        .s10-note-text {
            font-size: 0.85vw;
            color: #4b5563;
            flex: 1;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

new_slide_10 = '''
        <!-- Slide 10: AWS Cloud & Safety Operations Center -->
        <section class="slide" id="slide-10">
            <div class="slide-header">
                <div class="slide-number">10</div>
                <div class="slide-title">AWS Cloud &amp; Safety Operations Center <span style="font-size: 1.2vw; color: #4b5563; font-weight: 400; text-transform: none; margin-left: 1vw;">Cloud Telemetry, Event Persistence &amp; Centralized Monitoring</span></div>
            </div>
            
            <div class="slide-body">
                <div class="s10-layout">
                    
                    <div class="section-label" style="text-align: center; margin-bottom: 0.5vw;">EDGE &rarr; AWS CLOUD &rarr; OPERATIONS</div>
                    
                    <div class="s10-arch-container">
                        <div class="s10-arch-flow">
                            
                            <!-- 1. EDGE AI -->
                            <div class="s10-arch-block s10-ab-edge">
                                <div class="s10-ab-title">EDGE AI</div>
                                <div class="s10-ab-node">Python + YOLOv8</div>
                                <div class="s10-ab-node">Threat Analyzer</div>
                                <div class="s10-local-stop">&darr; ESP32 Local Stop</div>
                                <div class="s10-ab-desc">Object detection, threat assessment, local safety logic</div>
                            </div>
                            
                            <div class="s10-arch-arrow">
                                <div class="s10-arrow-label">MQTT</div>
                                <div>&rarr;</div>
                            </div>
                            
                            <!-- 2. AWS IoT CORE -->
                            <div class="s10-arch-block s10-ab-aws">
                                <div class="s10-ab-title">AWS IoT CORE</div>
                                <div class="s10-ab-node">MQTT / TLS Broker</div>
                                <div class="s10-ab-desc" style="margin-top: 1.5vw;">Receives edge telemetry and safety events</div>
                            </div>
                            
                            <div class="s10-arch-arrow">
                                <div class="s10-arrow-label">Rules</div>
                                <div>&rarr;</div>
                            </div>
                            
                            <!-- 3. EVENT PROCESSING -->
                            <div class="s10-arch-block s10-ab-data" style="min-width: 18vw;">
                                <div class="s10-ab-title">EVENT PROCESSING</div>
                                <div class="s10-branch">
                                    <div class="s10-branch-col">
                                        <div class="s10-ab-node">DynamoDB</div>
                                        <div class="s10-ab-desc">Event persistence<br>Monitoring data</div>
                                    </div>
                                    <div class="s10-branch-col">
                                        <div class="s10-ab-node">Lambda &rarr; SNS</div>
                                        <div class="s10-ab-desc">Critical alerts<br>Notification path</div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="s10-arch-arrow">
                                <div class="s10-arrow-label">API</div>
                                <div>&rarr;</div>
                            </div>
                            
                            <!-- 4. SAFETY OPERATIONS CENTER -->
                            <div class="s10-arch-block s10-ab-mon">
                                <div class="s10-ab-title">OPERATIONS CENTER</div>
                                <div class="s10-ab-node">FastAPI</div>
                                <div style="color: rgba(0,0,0,0.3);">&darr;</div>
                                <div class="s10-ab-node">React / Vite</div>
                                <div class="s10-ab-desc">Read-only monitoring dashboard</div>
                            </div>
                            
                        </div>
                    </div>
                    
                    <div class="s10-service-row">
                        <div class="s10-service-card">
                            <div class="s10-sc-title">AWS IoT Core</div>
                            <div class="s10-sc-sub">MQTT Telemetry</div>
                            <div class="s10-sc-desc">Edge connection</div>
                        </div>
                        <div class="s10-service-card">
                            <div class="s10-sc-title">DynamoDB</div>
                            <div class="s10-sc-sub">Persistence</div>
                            <div class="s10-sc-desc">State storage</div>
                        </div>
                        <div class="s10-service-card">
                            <div class="s10-sc-title">Lambda</div>
                            <div class="s10-sc-sub">Processing</div>
                            <div class="s10-sc-desc">Rule execution</div>
                        </div>
                        <div class="s10-service-card">
                            <div class="s10-sc-title">SNS</div>
                            <div class="s10-sc-sub">Alerts</div>
                            <div class="s10-sc-desc">Push notifications</div>
                        </div>
                    </div>
                    
                    <div class="s10-bottom-notes">
                        <div class="s10-note s10-note-local">
                            <div class="s10-note-title">LOCAL-FIRST SAFETY</div>
                            <div class="s10-note-text"><strong>Immediate safety logic remains at the edge;</strong> AWS provides telemetry, persistence, alerting and centralized monitoring.</div>
                        </div>
                        <div class="s10-note s10-note-read">
                            <div class="s10-note-title">READ-ONLY MONITORING</div>
                            <div class="s10-note-text"><strong>The dashboard does not send STOP/RESUME or other actuator commands.</strong></div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>
'''

content = re.sub(r'<section class="slide" id="slide-10">.*?</section>', new_slide_10.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
