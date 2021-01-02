import webbrowser
import time

text = clipboard.get_selection()
time.sleep(0.01)

site = "https://www.linguee.de/deutsch-englisch/search?source=auto&query=" + text
webbrowser.get('google-chrome').open_new_tab(site)
