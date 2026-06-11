# ClipForge — Setup Guide

## What you need before starting
- A computer (Mac, Windows, or Linux)
- Python 3 installed
- An Anthropic API key (free to get at console.anthropic.com)

---

## Step-by-step setup

### Step 1 — Download this folder
Save the entire ClipForge folder to your computer (e.g. your Desktop).

Your folder should look like this:
```
ClipForge/
├── app.py
├── start.sh        ← Mac/Linux users run this
├── start.bat       ← Windows users run this
├── SETUP.md        ← you are here
└── templates/
    └── index.html
```

---

### Step 2 — Install Python (if you don't have it)
- Go to https://www.python.org/downloads/
- Download and install Python 3
- **Windows:** Make sure to check ✅ "Add Python to PATH" during install

---

### Step 3 — Install FFmpeg (if you don't have it)

**Mac:**
- Install Homebrew first if needed: https://brew.sh
- Then run in Terminal: `brew install ffmpeg`

**Windows:**
1. Go to https://ffmpeg.org/download.html
2. Click "Windows builds" → download the zip
3. Extract it somewhere (e.g. `C:\ffmpeg`)
4. Add `C:\ffmpeg\bin` to your system PATH
   (Search "environment variables" in Windows search)

**Linux:**
```
sudo apt install ffmpeg
```

---

### Step 4 — Run ClipForge

**Mac / Linux:**
1. Open Terminal
2. Navigate to your ClipForge folder: `cd ~/Desktop/ClipForge`
3. Run: `bash start.sh`

**Windows:**
1. Double-click `start.bat`

The script will:
- Install all Python packages automatically
- Start the web server
- Open your browser to http://localhost:5050

---

### Step 5 — Use the app

1. Paste a YouTube URL
2. Enter your Anthropic API key (from console.anthropic.com → API Keys)
3. Choose how many clips you want (1–10)
4. Click **Generate Clips**
5. Watch the live progress log
6. Download your clips when done ✅

---

## Common issues

**"Python not found"**
→ Install Python from python.org and make sure to check "Add to PATH"

**"FFmpeg not found"**
→ Follow Step 3 above

**"Invalid API key"**
→ Get your key at console.anthropic.com → API Keys → Create Key

**App opens but clips fail**
→ Make sure the YouTube video is public (not private/age-restricted)

**Slow transcription**
→ Normal for long videos. A 1-hour video takes ~5-10 min on CPU.
   Open app.py and change `"base"` to `"tiny"` in the transcribe function for faster (less accurate) results.

---

## Stopping the app
Press **Ctrl+C** in the Terminal / command window.

## Where are my clips saved?
Inside the `ClipForge/jobs/` folder that gets created automatically.
Each job has its own subfolder with the clips inside.
