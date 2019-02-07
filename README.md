# Pywebview + Flask + Pyinstaller ==> Desktop apps
Desktop apps with looks like webapps with the help of pywebview (facilitates using HTML/CSS/JS in the interface), Flask (to build the routes to the logic) and Pyinstaller (to build it as a standalone desktop app)



If you encounter "Failed to execute script" when packing the app with pyinstaller try to:
1.Copy this 2 files:
- WebBrowserInterop.x64.dll
- WebBrowserInterop.x86.dll
From:
PythonXX\Lib\site-packages\webview\lib
To Python root:
C:\\PythonXX
