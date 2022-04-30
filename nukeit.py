import re
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 nukeit.py <directory_to_clean>")
    sys.exit(1)

path = sys.argv[1]
pattern = r'\.photoslibrary|\.jpg|\.jpeg|\.JPG|\.png|\.key|\.jpg|\.jpeg|\.jpe|\.jif|\.jfif|\.jfi|\.png|\.gif|\.webp|\.tiff|\.tif|\.psd|\.raw|\.arw|\.cr2|\.nrw|\.k25|\.bmp|\.dib|\.heif|\.heic|\.ind|\.indd|\.indt|\.jp2|\.j2k|\.jpf|\.jpx|\.jpm|\.mj2|\.svg|\.svgz|\.ai|\.eps'

for root, subFolders, files in os.walk(path):
    for fileName in files:
        if re.search(pattern, fileName):
            print(f"Skipped {os.path.join(root, fileName)}")
        else:
            os.remove(os.path.join(root, fileName))
            print(f"Deleted {os.path.join(root, fileName)}")
