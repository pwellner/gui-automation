from flask import Flask, request, jsonify
import pyautogui
import threading
import time

app = Flask(__name__)

def perform_gui_task():
    """Function to automate a simple GUI task."""
    time.sleep(2)  # Small delay to switch focus if needed
    pyautogui.hotkey('win', 'r')  # Open Run dialog
    time.sleep(1)
    pyautogui.write('notepad')  # Type 'notepad'
    pyautogui.press('enter')  # Press Enter
    time.sleep(2)
    pyautogui.write('Hello, this is an automated message!', interval=0.1)  # Type message

@app.route('/trigger', methods=['POST'])
def trigger_automation():
    """API endpoint to trigger GUI automation."""
    threading.Thread(target=perform_gui_task).start()  # Run in a separate thread
    return jsonify({"message": "GUI automation started"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
