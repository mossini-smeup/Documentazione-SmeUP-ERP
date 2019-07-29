# EDI - EDI Iungo Export
## OBIETTIVI
Gestire i connettori con IUNGO
## SOTTOSETTORI
V5 Per i documenti
## INTRODUZIONE
L'elemento di tabella è  : 
- ** = default
- Per SS V5 = SSV5A+MODELLO
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$EDEA __Percorso Creazione XML__
Percorso dove scrivere l' XML; Deve necessariamente essere una
cartella dell'IFS dell'AS400.

 :  : FLD T$EDEB __Attiviazione Trasmissione__
Se impostato a '1' viene attivata la trasmissione a Iungo
 :  : FLD T$EDEC __Utente per SBMJOB__
In questo modo si evitano i problemi di autorizzazione
per disallineamento password as400/rete
 :  : FLD T$EDED __Coda per sbmjob__
La coda impostata deve essere MONO JOB
 :  : FLD T$EDEE __Cancella righe se non presenti nell XML__
Permette di gestire il tipo di comportamento settato in iungo
per la gestione dei record da modificare/cancellare : 
-Se ='1' Significa che le righe NON presenti nell'XML,iungo le cancella;
-Se =' ' Significa che in questo caso iungo non cancellerà le righe;
         Per annullare le righe quindi occorre mandare l'istruzione specifica.
         In questo caso Iungo tratta SOLO le righe presenti nell'XML;
         le altre le lascia invariate.
 :  : FLD T$EDEM __Suffisso EXIT creazione XML
Se impostato, viene chiamato un programma specifico per poter gestire/personalizzare
l'XML creato dal programma standard (il prototipo si chiama XXIU01_A) dove XX
è il ss/settore dalla Tabella (es. V5IU01_A, BRIU01_A)

 :  : FLD T$EDEF __HOST per FTP__
Permette di indicare l'host remoto per l'FTP.Se tale campo è compilato il file
verrà trasferito, altrimenti verrà lasciato nella cartella specificata
nel campo sopra di questa tabella.
 :  : FLD T$EDEG __Percorso Host x FTP__
Indica la certella dell'Host nella quale trasferire il file.
Attenzione.Per problemi di dimensione del campo £G53PL, prestare attenzione
a non fare troppo esteso il percorso dati.
 :  : FLD T$EDEL __Pgm x script £G53PG__
Rappresenta il suffisso del programma B£G53_XX dove XX è il valore impostato
in questo campo.
 :  : FLD T$EDEH __Utente Host x FTP__
Utente per accedere all'Host remoto
 :  : FLD T$EDEI __Password Host x FTP__
Password per accedere al Server remoto
 :  : FLD T$EDEN __Richiedi conferma a Iungo per le righe split__
Se impostato a 1, le righe create da SPLIT verranno inviate a Iungo
come ancora da Confermare dal Fornitore. Se lasciato vuoto al fornitore
non gli verrà richiesta l'ulteriore conferma per le righe create
