
## Funzioni/Metodi
* **SND**       Invia messaggio push
** **APP**       ad app mobile

## Parametri di input
### Destinatario (£K17I_DT)
Utente (TAB£U) a cui inviare un messaggio.
I device a cui inviare messaggi sono salvati nel parametro esteso multiplo dell'utente K/£U1/£01 .
### Subsez. A38  (£K17I_SB)
Subsezione che punta al LOA38 che interfaccia il servizio di messaggistica.
Se non specificato utilizza il 01.S00.B00 che interfaccia l'app ufficiale Sme.UP Mobile con il
servizio Firebase Cloud Messaging di Google.
### Esec.batch   (£K17I_BT)
Se diverso da blank causa l'esecuzione in batch dell'invio dei messaggi, anziché in interattivo.
### Oggetto (£K17I_SJ)
Titolo del messaggio
### Corpo   (£K17I_BD)
Testo del messaggio
### Link (SV)  (£K17I_LK)
Link contenuto nel messaggio (ancora in sviluppo)
### Fun  (SV)  (£K17I_FN)
Fun da eseguire (ancora in sviluppo)
