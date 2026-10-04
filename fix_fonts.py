import re

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove google fonts link
content = re.sub(r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Inter.*?rel="stylesheet">', '', content, flags=re.DOTALL)

# Replace 'Inter' and 'Orbitron' with Georgia
content = content.replace("font-family: 'Inter', sans-serif;", 'font-family: Georgia, "Times New Roman", serif;')
content = content.replace("font-family: 'Orbitron', sans-serif;", 'font-family: Georgia, "Times New Roman", serif;')

# The user explicitly asked for this additional CSS block:
new_css = '''
        /* =========================================================
           GLOBAL ACADEMIC TYPOGRAPHY
           ========================================================= */

        html,
        body {
            font-family: Georgia, "Times New Roman", serif;
        }

        .slide {
            font-family: Georgia, "Times New Roman", serif;
        }

        .slide h1,
        .slide h2,
        .slide h3,
        .slide h4,
        .slide p,
        .slide span,
        .slide div,
        .slide li,
        .slide td,
        .slide th,
        .slide button {
            font-family: inherit;
        }

        .slide-title {
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 700;
            letter-spacing: 0.02em;
        }

        .section-label {
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 700;
            letter-spacing: 0.04em;
        }

        p,
        li {
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 400;
        }

        .metric-value {
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 700;
        }
'''
content = content.replace('</style>', new_css + '\n    </style>')

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
