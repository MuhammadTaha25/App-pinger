import requests
import sys

APP_URL = "https://your-streamlit-app-url.streamlit.app/"  # apna app URL yahan daalo

SLEEP_MARKER = "yes get this app back up."  # case-insensitive check

def main():
    try:
        r = requests.get(APP_URL, timeout=15)
        text = r.text.lower()
        if SLEEP_MARKER.lower() in text:
            print("Website is NOT active (sleep mode).")
            sys.exit(2)
        else:
            print("Website is active.")
            sys.exit(0)
    except Exception as e:
        print("Ping failed:", e)
        sys.exit(3)

if __name__ == "__main__":
    main()
