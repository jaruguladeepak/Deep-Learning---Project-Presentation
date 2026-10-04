import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title-card CSS
css_replace = '''
        .title-card {
            background: transparent;
            padding: 5vw 2vw;
            border: none;
            box-shadow: none;
            margin-bottom: 2vw;
            text-align: center;
            width: 90%;
            max-width: 90vw;
        }

        h1.main-title {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 6vw;
            font-weight: 700;
            letter-spacing: 0.2vw;
            margin-bottom: 1vw;
            color: #ffffff;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }

        h2.subtitle {
            font-size: 2.2vw;
            color: #f8fafc;
            font-weight: 400;
            line-height: 1.4;
            margin-bottom: 2vw;
            font-family: Georgia, "Times New Roman", serif;
            text-shadow: 0 2px 10px rgba(0,0,0,0.8);
        }

        .tagline {
            font-size: 1.2vw;
            color: #67e8f9;
            letter-spacing: 0.3vw;
            text-transform: uppercase;
            font-weight: 700;
            text-shadow: 0 2px 8px rgba(0,0,0,0.8);
        }

        .author-list {
            display: flex;
            justify-content: space-around;
            width: 80%;
            color: #ffffff;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 2vw;
            border-top: 1px solid rgba(255,255,255,0.3);
            padding-top: 2.5vw;
        }

        .author-group {
            text-align: center;
        }

        .author-label {
            font-size: 1vw;
            color: #67e8f9;
            text-transform: uppercase;
            letter-spacing: 0.1vw;
            margin-bottom: 1vw;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }

        .author-names {
            font-size: 1.3vw;
            line-height: 1.8;
            color: #ffffff;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }
'''

content = re.sub(r'\.title-card\s*\{.*?\.author-names\s*\{[^}]+\}', css_replace.strip(), content, flags=re.DOTALL)

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
