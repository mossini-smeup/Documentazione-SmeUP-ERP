#
COLLEGAMENTO REMOTO TRA AS/400
1.   L'opzione 08 e eseguibile solo da QSECOFR o da un utente abilitato a operazioni di sistema.
2.   Esiste la possibilità di fallimento nella creazione di una linea. Infatti esiste un parametro che identifica gli indirizzi di stazione che devono cambiare da collegamento a collegamento. Nella tabella B£6 è inserito un controllo per tale problema quindi l'errore può nascere se precedentemente all'utilizzo dell tool si è creato dei collegamenti.
3.   Quando si desidera fare un collegamento via modem, sia il chiamante che il chiamato devono predisporsi per tale operazione che consiste : 
A.   CHIAMANTE : 
-    Se la linea con il destionatario non è ancora stata creata deve essere creata e in questa sede devono essere specificati i seguenti parametri :  Descrizione della linea che è una scritta testuale che descrive la linea con l'azienda che si stà chiamando.
-    Se la linea con tale azienda è stata precedentemente creata basta immettere 02 nel campo opzioni e ricercare in tabella il nome dell'azienda che sio desidera chiamare.
_    Una volta attivata la linea si può effettuare il pass-throught e attendere di collegarsi.
-    Una volta teminato il collegamento è bene disattivare la linea immettendo 05 nel campo opzioni e ricercando o digitando il nome dell'azienda chiamata.
B.   CHIAMATO : 
-    Anche il chiamato deve creare la linea con il cliente e attivarla. Al termine dell'operazione deve anch'esso disattivarla.
_    Una particolarità che deve svolgere il chiamato è l'opzione 08 che permette di mettere l'AS/400 in stato di attesa chiamata. Per questa operazione vedere riferimenti precedenti.
