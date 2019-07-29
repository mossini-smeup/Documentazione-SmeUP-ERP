 Sono necessari i seguenti controlli per evitare problemi in fase di attivazione

- Smens installato su As400 e sul server di destinazione.

- Tabella JA1 con indicato Utente e Password per eseguire FTP verso As400
 :  : DEC T(TA) P(JA1) K(*) I(**>> Verifica Completezza tabella**)

- Tabella HOST su As400 con indicato matricola As400 con associato indirizzo IP (CFGTCP Opz 10) (ad esempio S4431CFA --> 172.16.2.100)

- Tabella B§P con indicati percorsi corrispondenti a quelli utilizzati su Server (pgm e Dati)
 :  : DEC T(ST) K(B§P) I(**>> Verifica Percorsi**)

- File D9WK... copilati correttamente con le opzioni Multimembro e Lunghezza Specificata
