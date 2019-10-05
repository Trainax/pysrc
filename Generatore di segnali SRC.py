# -*- coding: cp1252 -*-

from datetime import datetime
from PythonSRC.audio_src import generate_audio_src_stereo

#Ideated, made and coded by Trainax

print "Generatore segnale SRC\n"

nomeFile=raw_input("Inserire il nome che si desidera dare al file:\nSuggerimento: utilizzare la CamelCase\n==> ")

giorno=input("Inserire il giorno:\nValori supportati: da 1 a 31\n==> ")
mese=input("Inserire il mese:\nValori supportati: da 1 a 12\n==> ")
anno=input("Inserire l'anno:\nValori supportati: da 2000 a 2099\n==> ")
ora=input("Inserire l'ora:\nValori supportati: da 0 a 23\n==> ")
minuti=input("Inserire i minuti:\nValori supportati: da 0 a 59\n==> ")

errore=0

if(giorno < 1 or giorno > 31):
    print "\nErrore! Giorno inserito non supportato!\nGiorni supportati dal 1 al 31"
    errore=1

if(mese < 1 or mese > 12):
    print "\nErrore! Mese inserito non supportato!\nMesi supportati dal 1 al 12"
    errore=1

if(anno < 2000 or anno > 2099):
    print "\nErrore! Anno inserito non supportato!\nAnni supportati dal 2000 al 2099"
    errore=1

if(ora < 0 or ora > 23):
    print "\nErrore! Ora inserita non supportata!\nOre supportate da 0 a 23"
    errore=1

if(minuti < 0 or minuti > 59):
    print "\nErrore! Minuti inseriti non supportati!\nMinuti supportati da 0 a 59"
    errore=1

if(errore==0):
    orologio=datetime(anno, mese, giorno, ora, minuti)
    print orologio.strftime("\nGenerazione del segnale orario del %d/%m/%Y delle ore %H:%M")
    generate_audio_src_stereo(nomeFile+'.wav', orologio)
    print "\nIl file audio '" + nomeFile + "' è stato generato correttamente"

else:
    print "\nImpossibile generare il segnale orario!"
