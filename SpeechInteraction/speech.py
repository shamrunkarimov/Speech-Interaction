import speech_recognition as sr
import webbrowser
import requests
import json



def goldie(baliq):
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        #print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        #print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            #print("Say something!")
            with m as source: audio = r.listen(source)
            #print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                #print(value)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    #print("You said {}".format(value))
                    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170713T100944Z.f8dfa509de7b79ed.b2647d540ea02b2f1dddd850ce9e60d89e9f6a71&text=' + value + '&lang=' + baliq)
                    jsonfile = json.loads(r.text)
                    #print("italian translation...")
                    #print(value + '=' + jsonfile['text'][0])
                    return value + '=' + jsonfile['text'][0]
                    break
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                #return "Oops! Didn't catch that"
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


