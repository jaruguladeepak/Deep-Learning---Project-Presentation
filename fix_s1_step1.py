import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title Glass Box and Typography
new_title_css = '''
        /* Slide 1 Specifics */
        #slide-1 {
            background-image: url('assets/images/title.jpg');
            background-size: cover;
            background-position: center;
            justify-content: center;
            align-items: center;
        }

        #slide-1::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.85); /* Deep elegant dark overlay */
            z-index: 1;
        }

        .slide-content {
            position: relative;
            z-index: 2;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .title-card {
            background: #ffffff;
            padding: 5vw 8vw;
            border-top: 6px solid var(--accent-blue);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            margin-bottom: 4vw;
            text-align: center;
            width: 80%;
            max-width: 80vw;
        }

        h1.main-title {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 5.5vw;
            font-weight: 700;
            letter-spacing: 0.1vw;
            margin-bottom: 1.5vw;
            color: #111827; /* Dark navy/charcoal */
        }

        h2.subtitle {
            font-size: 2vw;
            color: #4b5563;
            font-weight: 400;
            line-height: 1.4;
            margin-bottom: 2vw;
            font-family: Georgia, "Times New Roman", serif;
        }

        .tagline {
            font-size: 1.1vw;
            color: var(--accent-blue);
            letter-spacing: 0.2vw;
            text-transform: uppercase;
            font-weight: 700;
        }

        .author-list {
            display: flex;
            justify-content: space-around;
            width: 80%;
            color: #f8fafc;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 1vw;
            border-top: 1px solid rgba(255,255,255,0.2);
            padding-top: 2.5vw;
        }

        .author-group {
            text-align: center;
        }

        .author-label {
            font-size: 0.9vw;
            color: var(--accent-cyan);
            text-transform: uppercase;
            letter-spacing: 0.1vw;
            margin-bottom: 1vw;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
        }

        .author-names {
            font-size: 1.2vw;
            line-height: 1.8;
            color: #e2e8f0;
        }
'''

# Remove old Slide 1 Specifics CSS
content = re.sub(r'/\*\s*Slide 1 Specifics\s*\*/.*?\.info-text\s*ul\s*li\s*\{[^}]+\}', new_title_css, content, flags=re.DOTALL)
# The above regex might fail if the end boundary isn't exact. Let's do it safer.

