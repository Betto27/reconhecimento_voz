import speech_recognition as sr
import gtts
from playsound import playsound

"""
# Reconhecimento do audio
rec = sr.Recognizer()

#Microfone

print(sr.Microphone().list_microphone_names()) #mostra os microfones conectado no sistema

with sr.Microphone(1) as mic: #especificar a posição do microfone desejado
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto) """

with open('frase.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')
        playsound('frase.mp3')





