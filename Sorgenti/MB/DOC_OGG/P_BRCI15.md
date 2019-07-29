# Generalità
La gestione cicli in Sme.up può estendersi fino a coprire numerosi dettagli del processo di produzione.

La struttura di descrizione è la seguente : 

- Articolo
-- Fase	
--- Centro di lavoro
--- Note di fase
--- Parametri di fase (oggetti, valori, date)
---- Note di parametri di fase	
--- Macchine
---- Note di macchine
---- Parametri di macchine
----- Note di parametri di macchine
--- Attrezzi
---- Note di attrezzi
---- Parametri di attrezzi
----- Note di  parametri di attrezzi
--- Risorse produttive secondarie (per tipo)
---- Note di risorse produttive secondarie
---- Oggetti di risorse produttive secondarie (valori, note, date)

	
# Gestione cicli di lavorazione
## Gestione fasi per articolo
Per attivare la gestione delle fasi di lavorazione per un articolo si parte dal seguente formato guida : 

![BR_04_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRCI15/BR_04_01.png)
_2_Nota; rispetto ai normali formati guida esiste un comando (F15 Azioni globali) con cui si può eseguire la stessa azione di copia o cancellazione su tutte le fasi del ciclo, ad esempio con l'azione globale si può copiare un ciclo da un articolo ad un altro.

Se non si inserisce nessuna opzione e nessuna fase si accede alla lista di tutte le fasi previste dal ciclo dell'articolo : 

![BR_04_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRCI15/BR_04_02.png)
Attraverso le impostazioni (F17) si può scegliere uno schema di presentazione.

La mappa di dettaglio di una fase è la seguente : 

![BR_04_03](http://localhost:3000/immagini/MBDOC_OGG-P_BRCI15/BR_04_03.png)
	
### Descrizione dei campi

- _3_Fase, Codice, rappresenta la sequenza di applicazione nel ciclo del prodotto.

- _3_Centro di lavoro, Identifica il centro di lavoro che esegue la fase.

- _3_Tipo operazione, Gestito nella tabella BRD, identifica la tipologia dell'operazione e caratterizza il significato dei vari tempi che possono essere inseriti per una fase, qual'è l'unità di misura dei tempi, quali tempi sono obbligatori e quali facoltativi, se l'operazione è rilevante per la schedulazione e se è un milestone.

- _3_Unità di misura, Unità di misura dei tempi, derivata dal tipo operazione ma modificabile.

- _3_Tempi operazione, Fino a 6 campi tempo utilizzabili per quantificare l'operazione, il significato dei vari tempi e la loro obbligatorietà o meno è stabilito dal tipo operazione.

- _3_Dettaglio tempi, Nell'archivio delle fasi del ciclo possono essere memorizzati 9 diversi tempi. Il significato dei tempi e quali vengono visualizzati direttamente nella videata è stabilito dal tipo operazione, se si vogliono vedere e gestire tutti i 9 tempi basta inserire un carattere in questo campo e viene aperta una finestra di dettaglio con tutti i tempi.

- _3_Rilevanza operazione / Tipo milestone, Derivati dal tipo operazione ma modificabili.

- _3_Data inizio e Data fine validità, Definisce se una fase deve essere considerata solo in unparticolare intervallo di tempo, assegnandogli di conseguenza un periodo di validità. Le date diinizio e di fine sono comprese. Se una fase è attiva fino ad oggi, la data di validità della suasostituta deve essere domani. Se non vengono inserite le date, la fase assume validità assoluta.

- _3_Sviluppi operazione, Permette di andare su tutte le possibili attività / funzioni / informazioni che sono state collegate alla fase inserendo delle azioni nella tabella B£J_F2 (Funzioni sui cicli).

- Gli sviluppi possono essere : 
-- Parametri, riferiti a griglie variabili di 2 chiavi (es. articolo, articolo / fase, articolo, fase/centro,...)
-- Macchine (interne o esterne) 	
-- Note informative,
-- Risorse produttive secondarie,
-- Attrezzi, programmi macchina,
-- Micropassi (dettaglio fase)
-- ...


![BR_04_04](http://localhost:3000/immagini/MBDOC_OGG-P_BRCI15/BR_04_04.png)
_2_Nota; una trattazione più completa degli sviluppi operazione si trova nella documentazione attiva STD nel modulo 'Risorse produttive secondarie'.
