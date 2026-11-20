from pathlib import Path
import os

from decouple import AutoConfig

BASE_DIR = Path(__file__).resolve().parent
config = AutoConfig(search_path=str(BASE_DIR))

from act.actions import (
    open_calculator,
    open_camera,
    open_cmd,
    open_excel,
    open_notepad,
    open_ppt,
    open_website,
    open_word,
    take_screenshot,
)
from aim.conv import converse
from audio.speech import listen, speak


BOT_NAME = os.getenv("VA_NAME") or config("VA_NAME", default="Virtual Assistant")

status_callback = None
stop_requested = False


def run_assistant(callback=None):
    global stop_requested, status_callback
    stop_requested = False
    status_callback = callback

    def update(text):
        print(text)
        if status_callback:
            status_callback(text)

    greeting = f"I am your {BOT_NAME}. How may I help you?"
    update(greeting)
    speak(greeting)

    while not stop_requested:
        update("🎤 Listening...")
        query = listen()

        if not query:
            continue

        query = query.strip().lower()
        update("🧠 Recognizing...")

        intent = None
        if "open" in query and "notepad" in query:
            intent = "ACTION_OPEN_NOTEPAD"
        elif "open" in query and "calculator" in query:
            intent = "ACTION_OPEN_CALCULATOR"
        elif "open" in query and "word" in query:
            intent = "ACTION_OPEN_WORD"
        elif "open" in query and "excel" in query:
            intent = "ACTION_OPEN_EXCEL"
        elif "open" in query and ("powerpoint" in query or "ppt" in query):
            intent = "ACTION_OPEN_PPT"
        elif "open" in query and ("cmd" in query or "command prompt" in query):
            intent = "ACTION_OPEN_CMD"
        elif "open" in query and "camera" in query:
            intent = "ACTION_OPEN_CAMERA"
        elif "screenshot" in query or "take screenshot" in query:
            intent = "ACTION_TAKE_SCREENSHOT"
        elif "open" in query and "website" in query:
            intent = "ACTION_OPEN_WEBSITE"
        elif query in {"exit", "shutdown", "stop", "goodbye", "quit"}:
            intent = "ACTION_EXIT"

        if intent is None:
            update("🤖 Thinking...")
            response = converse(query)
            update(response)
            speak(response)
            continue

        update(f"Intent: {intent}")

        try:
            action_msg = f"⚙️ {intent.removeprefix('ACTION_').replace('_', ' ').title()}"
            update(action_msg)

            if intent == "ACTION_OPEN_NOTEPAD":
                open_notepad()
            elif intent == "ACTION_OPEN_WORD":
                open_word()
            elif intent == "ACTION_OPEN_EXCEL":
                open_excel()
            elif intent == "ACTION_OPEN_PPT":
                open_ppt()
            elif intent == "ACTION_OPEN_CALCULATOR":
                open_calculator()
            elif intent == "ACTION_OPEN_WEBSITE":
                open_website()
            elif intent == "ACTION_OPEN_CMD":
                open_cmd()
            elif intent == "ACTION_OPEN_CAMERA":
                open_camera()
            elif intent == "ACTION_TAKE_SCREENSHOT":
                take_screenshot()
            elif intent == "ACTION_EXIT":
                speak("Shutting down. Goodbye!")
                stop_requested = True

        except Exception as exc:
            print(f"Action error: {exc}")
            update("❌ The command could not be completed.")
            speak("Sorry, something went wrong while trying to execute that command.")


if __name__ == "__main__":
    run_assistant()
