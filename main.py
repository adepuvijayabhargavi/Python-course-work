import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading
import wikipedia

# ----------------------------
# SPEAK FUNCTION
# ----------------------------

def speak(text):

    chat_area.insert(tk.END, f"Assistant: {text}\n\n")
    chat_area.see(tk.END)

    def speak_thread():

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(
        target=speak_thread,
        daemon=True
    ).start()


# ----------------------------
# LISTEN FUNCTION
# ----------------------------

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        status_label.config(text="Listening...")
        window.update()

        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        chat_area.insert(
            tk.END,
            f"You: {command}\n\n"
        )

        chat_area.see(tk.END)

        status_label.config(text="Ready")

        return command.lower()

    except sr.UnknownValueError:

        status_label.config(text="Ready")

        speak(
            "Sorry, I didn't understand."
        )

        return ""

    except sr.RequestError:

        status_label.config(text="Ready")

        speak(
            "Speech service is unavailable."
        )

        return ""


# ----------------------------
# PROCESS COMMAND
# ----------------------------

def process_command():

    command = listen()

    if "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}"
        )

    elif "date" in command:

        today = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        speak(
            f"Today's date is {today}"
        )

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open(
            "https://www.google.com"
        )

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )

    elif "open gmail" in command:

        speak("Opening Gmail")

        webbrowser.open(
            "https://mail.google.com"
        )

    elif "open chat g p t" in command:

        speak("Opening Chat GPT")

        webbrowser.open(
            "https://chatgpt.com"
        )

    elif "your name" in command:

        speak(
            "My name is Nova. I am your personal assistant."
        )

    elif "hello" in command:

        speak(
            "Hello. How can I help you today?"
        )

    elif "who created you" in command:

        speak(
            "I was created using Python and Tkinter."
        )

    elif "bye" in command or "exit" in command:

        speak(
            "Goodbye. Have a great day."
        )

        window.after(
            2000,
            window.destroy
        )

    elif "locate" in command:

        speak("Which place do you want to locate?")

        place = listen()

        if place:

            speak(f"Locating {place}")

            url = f"https://www.google.com/maps/search/{place}"

            webbrowser.open(url)
    
    elif "play" in command:

        song = command.replace("play","")

        speak(f"Playing {song}")

        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "who is" in command:

        person = command.replace("who is","")

        try:

            info = wikipedia.summary(
            person,
            sentences=2
            )

            speak(info)

        except:

            speak("Sorry, I couldn't find that.")
    
    elif "weather" in command:

        city = listen()

        webbrowser.open(
            f"https://www.google.com/search?q=weather+{city}"
            )

    else:

        speak(
            "Sorry. I do not know that command yet."
        )


# ----------------------------
# START ASSISTANT
# ----------------------------

def start_assistant():

    threading.Thread(
        target=process_command,
        daemon=True
    ).start()


# ----------------------------
# GUI WINDOW
# ----------------------------

window = tk.Tk()

window.title(
    "Nova Voice Assistant"
)

window.geometry(
    "800x600"
)

window.configure(
    bg="#1E1E2F"
)

# ----------------------------
# TITLE
# ----------------------------

title = tk.Label(
    window,
    text="🎙️ NOVA VOICE ASSISTANT",
    font=("Arial", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
)

title.pack(
    pady=15
)

# ----------------------------
# CHAT AREA
# ----------------------------

chat_area = scrolledtext.ScrolledText(
    window,
    width=80,
    height=20,
    font=("Arial", 11),
    bg="#2A2A40",
    fg="white",
    insertbackground="white"
)

chat_area.pack(
    padx=15,
    pady=10
)

# ----------------------------
# STATUS
# ----------------------------

status_label = tk.Label(
    window,
    text="Ready",
    font=("Arial", 12),
    bg="#1E1E2F",
    fg="lightgreen"
)

status_label.pack(
    pady=10
)

# ----------------------------
# START BUTTON
# ----------------------------

listen_btn = tk.Button(
    window,
    text="🎤 Start Listening",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=start_assistant
)

listen_btn.pack(
    pady=10
)

# ----------------------------
# EXIT BUTTON
# ----------------------------

exit_btn = tk.Button(
    window,
    text="❌ Exit",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=window.destroy
)

exit_btn.pack(
    pady=10
)

# ----------------------------
# WELCOME MESSAGE
# ----------------------------

window.after(
    1000,
    lambda: speak(
        "Hello. I am Nova. Click the microphone button and speak."
    )
)

# ----------------------------
# MAIN LOOP
# ----------------------------

window.mainloop()