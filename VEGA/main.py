import os
import eel
import engine.features as features
import engine.command as command
import subprocess


from engine.features import *
from engine.command import *
from engine.auth import recoganize
def start():

    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call(['device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    try:
        os.system('start msedge.exe --app="http://localhost:8002/index.html"')
    except:
        print("Could not open browser automatically")

    eel.start('index.html', mode=None, host='localhost', port=8002, block=True)
