import re
with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Variables
content = content.replace('--bg-color: #0b0f19;', '--bg-color: #f4f6f9;')
content = content.replace('--text-color: #ffffff;', '--text-color: #111827;')
content = content.replace('--accent-cyan: #00e5ff;', '--accent-cyan: #0284c7;')
content = content.replace('--accent-blue: #2979ff;', '--accent-blue: #2563eb;')
content = content.replace('--accent-red: #ff1744;', '--accent-red: #e11d48;')
content = content.replace('--glass-bg: rgba(11, 15, 25, 0.7);', '--glass-bg: rgba(255, 255, 255, 0.85);')
content = content.replace('--glass-border: rgba(255, 255, 255, 0.1);', '--glass-border: rgba(0, 0, 0, 0.15);')
content = content.replace('background-color: #000;', 'background-color: #e5e7eb;')

# Lighten text colors manually set to white/gray
content = content.replace('color: #fff;', 'color: var(--text-color);')
content = content.replace('color: #ffffff;', 'color: var(--text-color);')
content = content.replace('color: #cfd8dc;', 'color: #4b5563;')
content = content.replace('color: #cfd8dc', 'color: #4b5563')
content = content.replace('rgba(255, 255, 255, 0.5)', 'rgba(0, 0, 0, 0.5)')
content = content.replace('rgba(255,255,255,0.5)', 'rgba(0,0,0,0.5)')
content = content.replace('rgba(255,255,255,0.6)', 'rgba(0,0,0,0.6)')
content = content.replace('rgba(255,255,255,0.4)', 'rgba(0,0,0,0.6)')
content = content.replace('rgba(255,255,255,0.3)', 'rgba(0,0,0,0.6)')
content = content.replace('rgba(255, 255, 255, 0.3)', 'rgba(0, 0, 0, 0.6)')
content = content.replace('rgba(255,255,255,0.2)', 'rgba(0,0,0,0.2)')
content = content.replace('rgba(255, 255, 255, 0.2)', 'rgba(0, 0, 0, 0.2)')
content = content.replace('rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.1)')
content = content.replace('rgba(255,255,255,0.1)', 'rgba(0,0,0,0.1)')
content = content.replace('rgba(255, 255, 255, 0.05)', 'rgba(0, 0, 0, 0.05)')
content = content.replace('rgba(255,255,255,0.05)', 'rgba(0,0,0,0.05)')
content = content.replace('rgba(255,255,255,0.02)', 'rgba(0,0,0,0.02)')
content = content.replace('rgba(255,255,255,0.03)', 'rgba(0,0,0,0.03)')
content = content.replace('rgba(255, 255, 255, 0.8)', 'rgba(0, 0, 0, 0.8)')
content = content.replace('color: #00e676', 'color: #059669')
content = content.replace('border-color: #00e676', 'border-color: #059669')
content = content.replace('rgba(0, 230, 118', 'rgba(5, 150, 105')
content = content.replace('rgba(255, 235, 59', 'rgba(217, 119, 6') # Darker yellow/amber
content = content.replace('#ffd600', '#d97706') # Darker yellow
content = content.replace('background: rgba(0,0,0,0.5);', 'background: rgba(0,0,0,0.05);')
content = content.replace('border-left-color: #00e676;', 'border-left-color: #059669;')
content = content.replace('color:var(--accent-cyan)', 'color:var(--accent-blue)')
content = content.replace('color: var(--accent-cyan)', 'color: var(--accent-blue)')
content = content.replace('color: var(--accent-red)', 'color: #e11d48')

with open('c:/Users/deepu/OneDrive/Desktop/DL PPT/RailFOD23_Presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
