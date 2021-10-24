import os

fontsDir = os.listdir('fonts')

for path in fontsDir:
    fontDir = os.path.join('fonts', path)
    if os.path.isdir(fontDir):
        fontFamilyDir = os.listdir(fontDir)

        for file in fontFamilyDir:
            print(os.path.join(fontDir, file))
            if (file.endswith('.ttf')):
                os.system(f"msdf-bmfont {os.path.join(fontDir, file)} -s 42 --texture-size 1024,1024")