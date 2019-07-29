# Introduzione
Il modulo M5DISP si pone come obiettivo quello di rendere visibile, attraverso le varie navigazioni, __la quantità di materiale a disposizione__ per la produzione o per le normali attività di vendita.
La disponibilià dei materiali è quindi il risultato di un conteggio che si ottiene a partire dalle FONTI, ovvero __eventi presenti o futuri__, che vanno a incidere positivamente o negativamente sulla presenza di materiale in azienda. Saranno positive quelle fonti che rappresentano un flusso di merce in ingresso all'azienda o eventi che incrementano la quantità dei materiali che può essere utilizzata per creare valore per l'azienda, e negative quelle che rappresentano genericamente un flusso in uscita. Le fonti vengono organizzate in gruppi fonte, ovvero insiemi di più fonti che devono essere considerate nel conteggio della disponibilità.

# Il dashboard del modulo
Il dashboard del modulo M5DISP permette di consultare la struttura di ciascun gruppo fonte.
I legami tra le fonti, i magazzini e i gruppi fonte, sono consultabili attraverso la matrice "Analisi gruppi fonte" che permette di visualizzare, per ciascun gruppo fonte (colonne), quali sono gli eventi (righe) di cui si compone.
Graficamente questa matrice si presenta così : 
![M5DISP_001](http://localhost:3000/immagini/MBDOC_OPE-M5DISP_01/M5DISP_001.png)Se il legame è attivo, la cella che è l'incrocio tra una riga e una colonna, risulta essere valorizzata, mentre se non lo è, la cella si presenta vuota.

# Le navigazioni :  i SURF della disponibilità
__A- Analisi disponibilità__
Il primo surf è incentrato esclusivamente sull'analisi della disponibilità, come del resto si intuisce dal titolo stesso.
All'apertura della scheda, ci si troverà davanti a un input panel in cui si dovranno impostare i filtri che serviranno a definire i limiti dell'analisi che si vuole condurre.
![M5DISP_003](http://localhost:3000/immagini/MBDOC_OPE-M5DISP_01/M5DISP_003.png)
A seconda delle necessità, è possibile scegliere di condurre un tipo di analisi tra le seguenti : 
1. __DET - Dettaglio per data : __  presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per data.
2. __DFO - Dettaglio per fonte : __ presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per fonte
3. __DMD - Dettaglio per mag.data : __ presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per magazzino e data.
4. __DMF - Dettaglio per mag.fonte : __ presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per magazzino e fonte.
5. __RDT - Riepilogo per giorno : __ presenta i risultati dell'analisi disponibilità riepilogati a livello giorno.
6. __RFO - Riepilogo per fonte : __ presenta i risultati dell'analisi disponibilità riepilogati a livello fonte.
7. __RMF - Riepilogo per mag.fonte : __ presenta il riepilogo per ciascun magazzino, di tutte le fonti incluse nel gruppo fonte.
8. __SMG - Sintesi per magazzino : __  analisi che totalizza i flussi in ingresso e in uscita per ciascun magazzino.
9. __SIN - Sviluppo su griglia date : __ presenta i risultati delle quantità per fonte sviluppate su una scala temporale, data una periodicità ed una data di inizio periodo (come F20 da lista analisi disponibilità).
10. __SOG - Sintesi su oggetto : __ analisi che totalizza le fonti su un dato filtro a scelta. Gli oggetti su cui totalizzare le fonti possono essere la configurazione, il lotto, la commessa, etc...
11. __SOR - Sviluppo orizzontale : __ dato un articolo, permette di ottenere un riepilogo rizzontale, delle giacenze, degli impegni o degli ordini spaccati per un altro oggetto di dettaglio. Questo significa che attraverso questa analisi è possibile definire quali grandezze visualizzare in orizzontale e per quali grandezze totalizzarlein verticale. In questo caso, con l'F22 è sempre possibile modificare la struttura della matrice, impostando quali informazioni si vuole mantenere in colonna e quali invece sulle righe.

Il risultato dell'analisi può essere visualizzato in due modalità diverse : 
** in forma matriciale, ovvero attraverso una matrice che, a seconda del tipo di analisi, può assumere delle connotazioni differenti;
** in forma grafica, ovvero attraverso un diagramma che permette di vedere l'andamento della quantità in funzione del tempo.

B- Analisi fattibilità
![M5DISP_004](http://localhost:3000/immagini/MBDOC_OPE-M5DISP_01/M5DISP_004.png)A partire da un codice articolo, l'analisi della fattibilità permette di consultare la sua distinta base e, per ciascun componente, la quantità richiesta e disponibilie per la sua realizzazione.
