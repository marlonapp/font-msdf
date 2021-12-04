import os

fontsDir = os.listdir('fonts')

for path in fontsDir:
    fontDir = os.path.join('fonts', path)
    if os.path.isdir(fontDir):
        fontFamilyDir = os.listdir(fontDir)

        for file in fontFamilyDir:
            print(os.path.join(fontDir, file))
            if (file.endswith('.ttf')):
                os.system(f"msdf-bmfont {os.path.join(fontDir, file)} -i charset.txt -s 128 --texture-size 2048,2048")