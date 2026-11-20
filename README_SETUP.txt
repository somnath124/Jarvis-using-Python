VOICE AI ASSISTANT - FIXED SETUP
================================

IMPORTANT
---------
This project should be run with Python 3.13 on Windows x64.
Do not use Python 3.14 for this project because PyAudio 0.2.14 does not
provide a CPython 3.14 Windows wheel, and Kivy 2.3.1 is also packaged here
for CPython 3.13.

STEP 1 - Install Python 3.13
----------------------------
Install Python 3.13 x64 and make sure the Python Launcher (py) is installed.
You can keep Python 3.14 installed too.

STEP 2 - Setup
--------------
Double-click:
    setup.bat

The script creates:
    venv\

and installs everything from requirements.txt.

STEP 3 - Add the Cohere API key
--------------------------------
Open .env and change:
    COHERE_API_KEY=

to:
    COHERE_API_KEY=YOUR_REAL_COHERE_KEY

Do not share your API key or upload .env to GitHub.

STEP 4 - Run
------------
Double-click:
    voiceai.bat

TROUBLESHOOTING
---------------
If the microphone fails:
1. Windows Settings -> Privacy & security -> Microphone.
2. Allow microphone access and desktop apps to access the microphone.
3. Make sure the correct microphone is selected in Windows.
4. Run check_setup.bat or:
       venv\Scripts\python.exe check_setup.py

If Cohere says the key is not configured:
- Check that .env is in the same folder as main.py.
- Make sure the line is exactly:
      COHERE_API_KEY=your_key
- Restart the assistant after changing .env.

If Python 3.14 is selected by VS Code:
- Select the interpreter:
      .\venv\Scripts\python.exe
- Do not use the global Python 3.14 interpreter for this project.
