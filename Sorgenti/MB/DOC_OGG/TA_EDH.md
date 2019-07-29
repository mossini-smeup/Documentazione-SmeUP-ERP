# EDI - EDI Iungo Import
## OBIETTIVI
Gestire i connettori con IUNGO
## SOTTOSETTORI
V5 Per i documenti
## INTRODUZIONE
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$EDHA __Percorso Lettura XML__
Percorso in dove leggere  i file XML generati da Iungo;
Deve necessariamente essere una cartella dell'IFS dell'AS400.

 :  : FLD T$EDHB __Attiviazione Trasmissione__
Se impostato a '1' viene attivata la ricezione da Iungo
 :  : FLD T$EDHC __ORA STOP SENT.HHMMSS__
Indica l'ora della giornata alla quale l'eventuale programma sentinella
per l'importazione, viene terminato. Se non impostato il programma non
termina.
 :  : FLD T$EDHD __Secondi di Ritardo scansione cartella__
Indica ogni quanti secondi viene eseguita la lettura della cartella
dei file XML per l'importazione in SMEUP
 :  : FLD T$EDHF __HOST per FTP__
Permette di indicare l'host remoto per l'FTP.Se tale campo è compilato il file
verrà trasferito, altrimenti verrà lasciato nella cartella specificata
nel campo sopra di questa tabella.
 :  : FLD T$EDHG __Percorso Host x FTP__
Indica la certella dell'Host dalla quale prelevare il file.
Attenzione.Per problemi di dimensione del campo £G53PL, prestare attenzione
a non fare troppo esteso il percorso dati.
 :  : FLD T$EDHL __Pgm x script £G53PG__
Rappresenta il suffisso del programma B£G53_XX dove XX è il valore impostato
in questo campo.
 :  : FLD T$EDHH __Utente Host x FTP__
Utente per accedere all'Host remoto
 :  : FLD T$EDHI __Password Host x FTP__
Password per accedere al Server remoto
