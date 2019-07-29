# A£I - MODALITÀ DI INOLTRO
 :  : DEC T(ST) K(A£I)
## CONTENUTO DEI CAMPI
 :  : FLD T$PGMI **Programma di inoltro**
Programma utilizzato per la diffusione della lista di distribuzione ai destinatari.
Sono disponibili i seguenti programmi standard : 
-_7_B£IRTEM per l'inoltro mediante email via SmeNs
-_7_B£IRTMSG per l'inoltro mediante SNDMSG via sistema operativo
 :  : FLD T$A£I1 **Parametri di inoltro**
Parametri utilizzati dal programma inoltro definito nell'apposito campo di questa tabella, durante l'esecuzione della distribuzione della lista.
Se il programma di inoltro è**B£IRTEM**il significato dei parametri è il seguente : 
- Parametro 1 :  Nome dell'host che eseguirà l'invio della mail tramite SmeNs nonché elemento della tabella B§H che verrà passato all'api £G53.
- Parametro 2 :  Dominio di posta, ovvero parte "a destra" del carattere "@" negli indirizzi e-mail; se indicato verrà assunto come default purché non presente tra i destinatari nella lista di distrbuzione.
- Parametro 3 :  Percorso del testo allegato all'email ed elemento della tabella B§D.


