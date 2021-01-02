import webbrowser
import time

text = clipboard.get_selection()
time.sleep(0.01)

site = "https://synonyme.woxikon.de/synonyme/" + text + ".php"
webbrowser.get('google-chrome').open_new_tab(site)
