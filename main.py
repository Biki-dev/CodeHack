import keyboard
import configparser
import psutil
from pywinauto import Application, findwindows
import pyautogui
import pygetwindow as gw
import time

def toggle_youtube():
    last = gw.getActiveWindow()
    for app in ["YouTube", "Chrome", "Edge"]:
        wins = gw.getWindowsWithTitle(app)
        if wins:
            win = wins[0]
            try:
                win.activate()
                time.sleep(0.25)
                pyautogui.press('k')
            except:
                pass
            if last:
                try:
                    last.activate()
                except:
                    pass
            print("🎥 YouTube toggled")
            return
    print("⚠️ YouTube window not found")


def main():
    print("🎧 SpotifyHotkey is running.")
    print("    Press Shift+F1 to Play/Pause Spotify.")
    print("    Press Shift+y to Play/Pause YouTube.")
    print("    Press ESC to quit.")

    keyboard.add_hotkey("shift+F1", toggle_play_pause)
    keyboard.add_hotkey('shift+y', toggle_youtube, suppress=True)


    keyboard.wait("esc")
    print("👋 Exiting...")


def get_spotify_window():
    """Find and return the main Spotify window."""
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] and 'spotify.exe' in proc.info['name'].lower():
            try:
                hwnd = findwindows.find_window(process=proc.info['pid'])
                app = Application(backend='uia').connect(handle=hwnd)
                return app.top_window()
            except Exception:
                continue
    return None


def toggle_play_pause():
    """Toggle Spotify play/pause and return to last window."""
    last = gw.getActiveWindow()
    window = get_spotify_window()

    if not window:
        print("⚠️ Spotify not found.")
        return

    try:
       
        window.set_focus()
        time.sleep(0.25)

    
        window.type_keys("{SPACE}")
        print("⏯️ Spotify toggled")


        if last:
            time.sleep(0.25)
            try:
                last.activate()
            except Exception:
                pass
    except Exception as e:
        print(f"❌ Error: {e}")



if __name__ == "__main__":
    main()

