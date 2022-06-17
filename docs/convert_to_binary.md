# convert to binary

## pyinstaller

We should use pyinstaller 3.6 locally. `pip install pyinstaller==3.6` as to be consistent with the GitHub Action.

### The following works when using pyinstaller 5.1
pyinstaller -F  src\run.py

### The following command works when using pyinstaller 3.6 (use by the GitHub action: ackMcKew/pyinstaller-action-windows) 
cd src
pyinstaller --clean -y --dist ../dist/ --workpath ../build ./run.spec