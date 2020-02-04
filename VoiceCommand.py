import ctypes
import speech_recognition as SR

speech_rec = SR.Recognizer()
with SR.Microphone() as source:
	print("Say a command")
	audio = speech_rec.listen(source)

try:
	cmd = speech_rec.recognize_google(audio)
except SR.UnknownValueError:
	print("Please say that clearer")
except SR.RequestError as err:
	print("Could not request results from Google; {}".format(err))

if cmd == "lock my PC":
	print("locking your PC")
	ctypes.windll.user32.LockWorkStation()
