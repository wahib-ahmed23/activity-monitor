import time
import psutil
import win32gui
import win32process


def get_active_window():
    hwnd = win32gui.GetForegroundWindow()

    if hwnd == 0:
        return None

    window_title = win32gui.GetWindowText(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:
        process = psutil.Process(pid)

        return {
            "process": process.name(),
            "pid": pid,
            "title": window_title
        }

    except psutil.NoSuchProcess:
        return None


last_window = None

print("Activity Monitor Started...\n")

while True:

    current_window = get_active_window()

    if current_window != last_window:

        print("=" * 60)
        print(f"Application : {current_window['process']}")
        print(f"PID         : {current_window['pid']}")
        print(f"Window      : {current_window['title']}")
        print("=" * 60)

        last_window = current_window

    time.sleep(1)