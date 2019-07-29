# Introduzione

Le gestione immissione batch consente di inserire registrazioni in modo sia cieco che  interattivo, a partire da registrazioni costruite interamente o parzialmente in modo automatico.

La gestione si struttura essenzialmente in due fasi : 
- costruzione dei dati in uno specifico file di transito;
- applicazione con controllo e completamento, interattivo o cieco, dei dati costruiti.

# Costruzione dei dati della registrazione

Per la costruzione dei dati relativi alla registrazione va riempito il file C5BATC0F. Questo è costiuito da alcune chiavi identificative più un campi libero che viene riempito in differenti modi a seconda della valorizzazione del campo W5TREC.

Per il dettaglio sulla struttura del file si rimanda alla relativa documentazione del file.
- [C5BATC0F File immissione BATCH](Sorgenti/MB/DOC_OGG/F_C5BATC0F)

La scrittura del file, può essere semplificata tramite l'utilizzo di alcune /COPY : 

- Scrittura della testata di registrazione : 
-- L'inizializzazione dei dati fondamentali della testata derivabili da azienda e tipo registrazione, va effettuata tramite la £C5A con funzione "CLEAR"
-- La testata va poi completata dal programma specifico almeno dei sui dati minimi :  esercizio e data registrazione
-- La scrittura nel batch può poi essere invece delegata al richiamo della /COPY £C52 chiamata passando i seguenti parametri
--- FU Funzione 'BAT'
--- ME Metodo   'WRI'
--- TP Tipo     'E4'
--- CD Codice   T5PROG (Che è stato riempito dalla £C5A)
--- RE Record   L'intero tracciato della testata
- Scrittura della riga di registrazione : 
-- L'inizializzazione dei dati fondamentali della testata derivabili da azienda e tipo registrazione, va effettuata tramite la £C52 con i seguenti parametri : 
--- FU Funzione 'BAT'
--- ME Metodo   'INZ'
--- TP Tipo     'E4'
--- CD Codice   T5PROG (Che è stato riempito dalla £C5A)
--- RE Record   L'intero tracciato della testata
-- La riga viene passata nel campo £C52RE e va poi completata dal programma specifico almeno dei sui dati minimi :  n° di riga, causale, importo, segno Dare/Avere, conto (e/o tipo contatto/soggetto), flag 11 e flag 12 se si tratta di una riga di soggetto.
-- La scrittura nel batch è delegata al richiamo della /COPY £C52 chiamata passando i seguenti parametri : 
--- FU Funzione 'BAT'
--- ME Metodo   'WRI'
--- TP Tipo     'E5'
--- CD Codice   R5PROG + RIGA
--- RE Record   L'intero tracciato della riga
- Scrittura di una rata : 
-- L'inizializzazione dei dati fondamentali della testata derivabili da azienda e tipo registrazione, va effettuata tramite la £C52 con i seguenti parametri : 
--- FU Funzione 'BAT'
--- ME Metodo   'INZ'
--- TP Tipo     'RR'
--- CD Codice   R5PROG + R5RIGA
--- RE Record   L'intero tracciato della riga di riferimento della rata
-- La rata va poi completata dal programma specifico almeno dei sui dati minimi :  importo, segno dare/avere, Oggetto di riferimento, flag 11/12, IDPA, tipo pagamento, flag 13 ecc.
-- La scrittura nel batch è delegata al richiamo della /COPY £C52 chiamata passando i seguenti parametri : 
--- FU Funzione 'BAT'
--- ME Metodo   'WRI'
--- TP Tipo     'RR'
--- CD Codice   S5IDOJ (Riempito dalla funzione di inizializzazione)
--- RE Record   L'intero tracciato della rata
- Scrittura di una riga di analitica : 
-- E' del tutto speculare a quello della rata, con la sola differenza che viene passato al posto del tipo record RR il tipo record MH.


Per le ritenute e le note di testata non sono ancora state previste delle funzioni automatiche,in questi casi perciò il file va ancora scritto esplicitamente.

E' inoltre da rilevare che se vengono dati i riferimenti necessari (codice pagamento, definizione del modello, anagrafica percipiente), i record di rate, analitica e ritenute, verrannoautomaticamente compilati, senza che sia necessario scriverli in modo esplicito.

 :  : INI Richiamo pgm di Test per inizializzazione Testata
 :  : CMD CALL TSTC5A
 :  : FIN
 :  : INI Pgm di test della £C52
 :  : CMD CALL TSTC52
 :  : FIN

# Applicazione
Una volta completati i dati fondamentali questi potranno essere applicati in contabilità tramite la /COPY £C52 chiamata con i seguenti parametri : 


- FU Funzione 'BAT'
- ME Metodo   'APP'
- TP Tipo     'E4'
- CD Codice   T5PROG (Che è stato riempito dalla £C5A)
- RE Record   L'intero tracciato della testata


Tramite questo richiamo i dati verranno, controllati ed eventualmente completati, e se risulteranno validi, spostati nei file effettivi, con contigua cancellazione dei relativi record dal file di transito.
Se la registrazione non risultasse valida, verrà ritornato un messaggio di errore.
Tutte le registrazioni non valide, salvo vengano volutamente cancellate, rimangono nel file di transito e possono poi essere gestite manualmente tramite la funzione di gestione del file.

 :  : INI Richiamo pgm di gestione file immissione batch
 :  : CMD CALL C5BCH5G
 :  : FIN
### Note
Oltre al metodo APP in questo contesto sono inoltre applicabili i seguenti metodi : 

- APM :  permette di aprire in interattivo la gestione dell'immissione delle registrazione, dopo chesono state applicate le azioni di completamento dati. Finchè la registrazione non viene confermatai dati vengono mantenuti sul file di transito. Se si abbandona la gestione i record verranno man-
tenuti sul file di transito, ma senza alcuna delle modifiche eventualmente apportate.
- PRT :  permette di stampare la registrazione
- VER :  permette di verificare la validità della registrazione
- DEL :  permette di cancellare la registrazione dal file di transito


 :  : INI Pgm di test della £C52
 :  : CMD CALL TSTC52
 :  : FIN
