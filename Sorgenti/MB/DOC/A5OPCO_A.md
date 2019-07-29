# Impostazione
_2_Definizione conti rilevanti
 :  : DEC T(ST) P() K(C5B&AZ) I(_7_Piano dei conti  >>)

_2_Definizione delle causali rilevanti
 :  : DEC T(ST) P() K(A5F&AZ) I(_7_Causali collegate >>)

_2_Impostazione piani ammortamento delle linee
 :  : INI _7_Set'n'play Creazione Registrazioni Automatiche >> 
 :  : CMD CALL C5N000G PARM('OF' 'W F' 'AZ')
 :  : FIN

# Elaborazioni
 :  : INI _7_Generazione movimenti automatici >> 
 :  : CMD CALL A5GA01G
 :  : FIN

 :  : INI _7_Stampa libro cespiti/Chiusura >> 
 :  : CMD CALL A5ST03A
 :  : FIN

 :  : INI _7_Riallineamento Fondo Ammortamento fiscale >> 
 :  : CMD CALL A5UT12A
 :  : FIN

## Interrogazioni
 :  : INI _7_Scheda Cespiti >> 
 :  : CMD CALL A5SK01G
 :  : FIN
 :  : INI _7_Interrogazione/Stampa Movimenti >> 
 :  : CMD CALL A5ST02A
 :  : FIN
 :  : INI _7_Interrogazione/Stampa Cespiti>> 
 :  : CMD CALL A5ST01A
 :  : FIN
 :  : INI _7_Controllo differenze valori linee >> 
 :  : CMD CALL A5ST04A
 :  : FIN
 :  : INI _7_Controllo Plafond manutenzioni >> 
 :  : CMD CALL A5UT11A
 :  : FIN
 :  : INI _7_Stampa Prospetto Rivalutazioni >> 
 :  : CMD CALL A5ST05A
 :  : FIN
