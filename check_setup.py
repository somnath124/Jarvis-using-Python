"""Local installation diagnostic for the Voice AI Assistant."""

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

print("Python:", sys.version.replace("\n", " "))
print("Executable:", sys.executable)

if sys.version_info[:2] != (3, 13):
    print("WARNING: This project is configured for Python 3.13.")

packages = [
    "cohere",
    "decouple",
    "pyttsx3",
    "speech_recognition",
    "pyaudio",
    "PIL",
    "kivy",
]

failed = False
for package in packages:
    try:
        module = importlib.import_module(package)
        version = getattr(module, "__version__", "installed")
        print(f"OK  {package}: {version}")
    except Exception as exc:
        failed = True
        print(f"FAIL {package}: {exc}")

try:
    import cohere
    print("OK  Cohere ClientV2:", hasattr(cohere, "ClientV2"))
    if not hasattr(cohere, "ClientV2"):
        failed = True
except Exception:
    failed = True

if not (ROOT / ".env").exists():
    print("WARNING: .env does not exist. Copy .env.example to .env.")

print()
if failed:
    print("Some dependencies are missing or broken.")
    sys.exit(1)

print("All required Python packages imported successfully.")
