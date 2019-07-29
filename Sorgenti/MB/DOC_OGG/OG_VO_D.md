# OGGETTO VOCE
 E' composto dai seguenti campi : 
 - Codice della voce (10 caratteri)
 - Descrizione della voce (35 caratteri)
 - Contenuto della voce (testo libero)

### SIGLA OGGETTO in TA/*CNTT
 'VO'                               £FUNT1

### CHIAVE PRIMARIA
 'MEMBRO'                           £FUNP1
 'ID VOCE'                          £FUNK1

### Modalità di descrizione di una voce
 Le voci sono contenute all'interno dei membri del source-file DOC_VOC.
 Ogni membro contiene voci correlate da un determinato contesto (Es. in un membro xxyyyy sono contenute le voci
 dell'applicazione xx e del modulo yyyy). Qualora si vogliano separare uleriormente le voci, si aggiunge un suffisso : 
 xxyyyy_A, xxyyyy_B, ecc...

 La sintassi di definizione delle voci è la seguente : 

 :  : VOC Id="VOCE1" Txt="DEC DI VOCE 1"
 Contenuto della voce1 riga 1
 Contenuto della voce1 riga 2
 Contenuto della voce1 riga 3
 :  : VOC Id="VOCE2" Txt="DEC DI VOCE 2"
 Contenuto della voce2
 ecc...

Nel contenuto di una voce (parte compresa tra due tag  :  : VOC) si possono inserire tag di documentazione attiva
(titoli, elenchi puntati, ecc...)


 Se si richiama una voce all'interno di Looc.Up viene aperta una scheda con due etichette
 indicanti il Nome_Membro e il Id_Voce; nella parte sottostante viene mostrato il
 relativo contenuto in formato HTML.




