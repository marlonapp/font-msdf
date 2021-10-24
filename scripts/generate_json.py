import os
import json

fontsDir = os.listdir('fonts')

fontJson = {}

for path in fontsDir:
    fontDir = os.path.join('fonts', path)
    if os.path.isdir(fontDir):
        fontJson[path] = {}
        fontFamilyDir = os.listdir(fontDir)

        for file in fontFamilyDir:
            print(os.path.join(fontDir, file))
            if (file.endswith('.fnt')):
                url = os.path.join(fontDir, file).replace('\\', '/')
                fontJson[path][file.replace('.fnt', '')] = f"https://raw.githubusercontent.com/marlonapp/font-msdf/master/{url}"

with open('fonts/list.json', 'w') as file:
    file.write(json.dumps(fontJson, indent=2))