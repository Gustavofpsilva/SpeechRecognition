import speech_recognition as sr

def voice_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Convertendo voz para texto...")
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Texto: " + text)
            return text
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
            return ""
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de voz; {e}")
            return ""

if __name__ == "__main__":
    resultado = voice_to_text()
    if resultado:
        print("Texto convertido: " + resultado)
    else:
        print("Não foi possível converter a voz para texto.")
