## Ordine produzione
>Se l'origine è OP (ordine di produzione)
Parametro 1 : 
-    Pos.1/3   Tipo Ordine (opzionale);
-    Pos.4     Si imposta la data fonte a cui si riferisce la fonte. Se la fonte è
.              'attuale' la data è comunque a zero, se invece è attiva la
.              rettifica, essa viene eseguita a partire da questa data.
.              Si può scegliere tra le seguenti date : 
.              -- ' ' fine richiesta.
.              -- '1' inizio richiesto.
.              -- '2' ordine.
.              -- '3' inserimento.
.              -- '4' (*) data fine schedulata a capacità finita, nello scenario
.                         impostato nel param.3.
.              -- '5' (*) data fine schedulata a capacità infinita al più presto,
.                         nello scenario impostato nel param.3.
.              (*) Se non si riesce a reperire questa data, o essa è a zero, viene
.                  assunta la data fine richiesta
Parametro 2 : 
-    Pos.1     Se impostato la fonte è disponibile (con data 0);
-    Pos.2     Se impostato, l'oggetto di riferimento sostituisce l'oggetto dello
.              stesso tipo, sia nella parzializzazione sia nel ritorno della fonte.
.              Se, ad esempio, è stato impostato questo flag e l'oggetto di
.              riferimento è un ente, viene considerato come ente intestatario
.              dell'ordine l'oggetto di riferimento e non quello presente nel campo
.              ente dell'archivio degli ordini in corso. Questa modalità può essere
.              utile nella pianificazione 'logistica' in cui, nell'ordine pianificato
.              sono contenuti due enti :  l'esecutore dell'ordine e il destinatario
.              dello stesso. A seconda della situazione, si deve considerare il
.              primo oppure il secondo.
.               Sono trattate le seguenti sostituzioni : 
.               - Ente.
.               - Commessa.
.               - Testata documento.
.               - Riga documento.
-    Pos.3     Se impostato, presenta gli ordini con residuo effettivo maggiore di
.              0 ma con residuo teorico (al netto dello scarto previsto residuo)
.              a 0.
-    Pos.4     Data rettificata :  se impostato, e se non si è scelto che la fonte è
.              disponibile (posizione 1 del parametro 2), la data della fonte verrà
.              avanzata dei giorni di rettifica. Verranno usati i giorni di
.              rettifica di produzione memorizzati (e modificabili) nell'ordine di
.              produzione. Verrà inoltre usato il calendario del magazzino su cui si
.              sta eseguendo l'analisi disponibilità. Per maggiori dettagli
.              riferirsi al campo, con lo stesso significato, nel paragrafo relativo
.              all'origine V5.
.    Pos.5     Si imposta se si desidera un ritorno MFP (si può selezionare se per
.              contenitore o per giorno).
.    Pos.6     Si inserisce un valore 1,2,... 9,A In tal modo viene assunta, se
.              presente, la data libera (1 - 10), corrispondente al valore impostato.
.              Se essa è a zero, ci si riconduce alla modalità normale di
.              assegnazione data (definita in precedenza).
.              **NB** :  il flag 'fonte disponibile' ha la priorità su questa
.              impostazione.
Parametro 3 : 
-    Pos.1/10  Scenario da cui acquisire la data schedulata (se non impostato si
.               assume '**').

