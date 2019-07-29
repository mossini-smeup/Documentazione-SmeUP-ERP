# PHN - Master tts - configurazione 2 (User)
 :  : DEC T(ST) K(PHN)
## OBIETTIVO
Informazioni aggiuntive per configurazione Master TTS.
## CONTENUTO DEI CAMPI
 :  : FLD T$PHNM __M-Lingua__
 :  : FLD T$PHNA __Sottosettore VAC__
 :  : FLD T$PHNB __N-Dim buffer AS400__
 :  : FLD T$PHNC __O-Host di backup__
 :  : FLD T$PHND __P-Porta UDP del VAC__
 :  : FLD T$PHNE __Tipo log e/o traccia__
 :  : FLD T$PHNR __R-IP VSC__
 :  : FLD T$PHNS __S-Protocollo VSC__
 :  : FLD T$PHN8 __Gruppo azioni Ricez__
 :  : FLD T$PHN7 __Metodo a ricezione__
E' il programma di struttura TTS che elabora i dati ricevuti dal master.
 :  : FLD T$PHN9 __Metodo iniziale VSC__
E' un programma di struttura TTS lanciato quando il master ha finito di configurare
Il canale VSC. Viene quindi lanciato ogni qualvolta un canale VSC viene aperto.
