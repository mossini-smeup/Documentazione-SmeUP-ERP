# SFP - Passo di ottimizzazione
 :  : DEC T(ST) K(SFP)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM CODICE
 :  : FLD T$DESC DESCRIZIONE
 :  : FLD TPA,1  __PARAMETRO NN (1/6)__
Possono essere impostati fino a 6 parametri numerici il cui significato viene decodificato dalla tabella SF*Pn (1/6).
Questi parametri vengono passati al programma (normalmente specifico di ogni azienda) come condizionatori.
 :  : FLD TPA,2.TPA,1 PARAMETRO 02
 :  : FLD TPA,3.TPA,1 PARAMETRO 03
 :  : FLD TPA,4.TPA,1 PARAMETRO 04
 :  : FLD TPA,5.TPA,1 PARAMETRO 05
 :  : FLD TPA,6.TPA,1 PARAMETRO 06
 :  : FLD T$PALF __CODICE DI ORDINAMENTO__
Controllato nella tabella SF*CO
 :  : FLD T$PGPA __PROGRAMMA SPECIFICO DEL PASSO__

