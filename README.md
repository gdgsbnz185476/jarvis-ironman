# Jarvis Ironman OS

A local AI assistant inspired by Iron Man's Jarvis.
![Jarvis Screenshot](assets/jarvis.png)
## Features

- Voice recognition
- AI conversation using Groq API
- Memory system
- Autonomous task routing
- Tool execution layer
- Modular architecture
- macOS voice synthesis

## Tech Stack

- Python
- SpeechRecognition
- Groq API
- Flask
- PyAudio

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/jarvis-ironman.git
cd jarvis
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_key_here
```

Run:

```bash
python start.py
```

## Future Goals

- React dashboard UI
- Wake word system
- Multi-agent planning
- Vision support
- Desktop app mode
