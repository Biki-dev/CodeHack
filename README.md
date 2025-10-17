## SpotifyHotkey (Windows)

A tiny Windows utility to control Spotify and YouTube with global hotkeys.

- **Shift+F1**: Toggle Spotify play/pause
- **Shift+Y**: Toggle YouTube play/pause (sends "k" to the YouTube tab)
- **ESC**: Quit the program

Works by temporarily focusing the target window, sending the relevant key, and returning focus to your previous window.

## Requirements
- **Windows 10/11**
- **Python 3.9+**
- Recommended: Run the terminal as **Administrator** so global hotkeys work reliably

## Install
1. Open PowerShell in the project directory:
```bash
cd "C:\Users\TUF\Downloads\code\CodeHack"
```
2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. Install dependencies:
```bash
pip install keyboard psutil pywinauto pyautogui pygetwindow
```

Notes:
- On first use, Windows may prompt for accessibility/keyboard permissions.
- `pywinauto` may pull in `pywin32` automatically. If not, install it manually: `pip install pywin32`.

## Usage
Run the script from PowerShell (preferably as Administrator):
```bash
python main.py
```
You should see console messages like:
- "🎧 SpotifyHotkey is running."
- Hotkey instructions
- "👋 Exiting..." when you press ESC

Keep this window open while using the hotkeys.

## Hotkeys
- **Shift+F1**: Toggle Spotify play/pause
- **Shift+Y**: Toggle YouTube play/pause
  - Looks for a window whose title contains "YouTube", or a browser titled "Chrome"/"Edge" with a YouTube tab visible
  - Sends the `k` key to YouTube to toggle play/pause
- **ESC**: Quit the program

## How it works (high level)
- Spotify: Locates the main Spotify window via process enumeration (`psutil` + `pywinauto`), focuses it, sends Space, then returns focus to your previous window.
- YouTube: Locates a window with a title matching YouTube/Chrome/Edge, focuses it, sends `k`, then returns focus.

## Troubleshooting
- **Hotkeys do nothing**:
  - Run PowerShell as **Administrator**.
  - Ensure no other app intercepts the same hotkeys.
- **"⚠️ Spotify not found."**:
  - Make sure the Spotify desktop app is running (not the web player).
  - If Spotify runs under a different user/elevation, run this script with the same elevation.
- **"⚠️ YouTube window not found"**:
  - Ensure a YouTube tab is open and the browser window title includes YouTube/Chrome/Edge.
  - The tab must be visible in the targeted window; minimized/hidden windows may not receive keys.
- **Focus flicker** is expected since the app briefly focuses Spotify/YouTube to send the key, then restores your previous window.

## Auto-start (optional)
If you want this to run on login:
- Use Windows Task Scheduler to create a task that runs `python main.py` at logon (set "Run with highest privileges").

## License
MIT
