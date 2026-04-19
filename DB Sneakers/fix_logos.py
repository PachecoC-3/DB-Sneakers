import re

path = r'C:\Users\xcxp279\.gemini\antigravity\scratch\claude_code\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace About logo
content = re.sub(r'<div id="page-about".*?<img src="data:image/png;base64,.*?" alt="DB Sneakers">', 
                 '<div id="page-about" class="page-sec"><div class="pg-wrap"><div class="pg-hero"><img src="assets/img/logo_graffiti.png" alt="DB Sneakers" style="width:180px;margin-bottom:20px">', 
                 content, flags=re.DOTALL)

# Replace Footer logo
content = re.sub(r'<div class="ft-brand"><img src="data:image/png;base64,.*?" alt="DB Sneakers">', 
                 '<div class="ft-brand"><img src="assets/img/logo_graffiti.png" alt="DB Sneakers" style="width:120px;margin-bottom:15px">', 
                 content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
