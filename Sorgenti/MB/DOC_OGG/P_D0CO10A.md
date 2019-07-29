## Parametrizzazione - ESECUZIONE
![D0BASE_62](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO10A/D0BASE_62.png)Sono possibili le seguenti impostazioni : 
 * **Contesto** :   Tipo Oggetto contesto del calcolo del costo MEDIO è esclusivamente l'oggetto >Articolo, oggetto su cui si scatenano eventi di diversa natura : 
** Documenti di Acquisto
** Documenti di Conto Lavoro
** Ordini di Produzione
*** Fasi Interne
*** Fasi Esterne
** Ordini di Smontaggio
** Cannibalizzazioni
** Riutilizzi parziali
** Differenze Inventariali
** Rimanenze di magazzino
 * **Tipo costo**; è il tipo costo che sarà memorizzato sul quale convergeranno le totalizzazioni dei costi di dettaglio sia a valore che a quantità, che dovrà : 
** Essere un elemento della tabella TCO
** Essere associato ad un tema (tabella **D5O**) con una struttura del costo (tabella **IGI**) che prevede un campo «quantità di riferimento del costo».
** Tutti i costi che concorreranno alla determinazione di un costo medio devono essere popolati a totale (tabella **TCO**)
 * **OggCal No AR**;
Deve essere impostato a "1" quando l'oggetto di calcolo di low-level code non è AR articolo ma collio o lotto.
Si verifica quando nelle impostazioni D0CJ01P il campo "Costi per oggetto specifico" è diverso da blanks
 * **Data**; è la data a fronte della quale saranno impostati date e/o periodi elaborare i movimenti e memorizzare i costi, la stessa data viene utilizzata nelle eventuali scansioni distinta e ciclo. I campi condizionati da tale data sono : 
** **Primo Periodo** :  è il periodo con cui viene memorizzato il costo
*** Per un periodo tipo annuale avremo un codice anno
*** Per un periodo tipo mese avremo un anno/mese
** **Secondo Periodo** :  è il periodo con cui viene assunta una eventuale rimanenza di periodo precedente
*** Per un periodo tipo annuale avremo un codice anno
*** Per un periodo tipo mese, se campo **"Rimanenza Iniziale"** = **1**(Esercizio Precedente),  avremo un anno
*** Per un periodo tipo mese, se campo **"Rimanenza Iniziale"** = **2**(Periodo Consolidato),  verrà assunto il progressivo di rimanenza al periodo richiesto ed in subordine la rimanenza annuale
*** Per un periodo tipo mese, se campo **"Rimanenza Iniziale"** = ***BLANKS**, avremo un anno/mese
** **Eventi elaborati** ed **Eventi Calcolati** :  Questo è il periodo dei movimenti di magazzino che viene considerato. Tali periodi divergeranno solo quando, in un costo Progressivo annuale, si deciderà di assumere un periodo calcolato diverso dall'inizio dell'anno, in quel caso infatti (anche se verranno considerati tutti gli eventi ai fini della definizione di una rimanenza) gli eventi calcolati saranno solo quelli dal primo giorno del periodo sucessivo a quello di riperimento del costo consolidato.
* **Riman. Iniziali** :  valori possibili sono : 
** ***BLANKS** :  la rimanenza iniziale, se richiesta, viene assunta in base all'impostazione del tipo costo, annuale o periodica (mensile).
** **1** :  questa opzione è valida solo per tipi costo con pediodo P=Periodo (mese) e forza la ripresa della rimanenza a fine anno precedente
** **2** :  questa opzione è valida solo per tipi costo con pediodo P=Periodo (mese) ed ha queste caratteristiche : 
*** Permette di inserire un periodo diverso per la ripresa di un costo consolidato.
*** Non assume direttamente le rimanenze ma, in prima istanza reperisce il costo che si sta calcolando consolidato al periodo richiesto,  risalendo alle rimanenze dell'anno precedente, in base alle impostazioni della tabella TCO.

_7_ Documentazione in fase di Completamento

* **Estrazione**
** __Programma__; programma di estrazione articoli da utilizzare lhkhkhkjhjk
** __Parametro__; parametri di condizionamento del programma di cui sopra (vedi paragrafo successivo)
** __Lista articoli__; permette di limitare il calcolo ad una lista di articoli precedentemente creata
* **Calcolo costi elementari**
** __Flusso__; elemento della tab. B£H che richiama il flusso di programmi per la costruzione
** __Costruzione - Elementi__; selezionando il bottone si apre la lista delle azioni richiamate dal flusso di costruzione
** __Costruzione - MDV calcolo__; ffffffffff
** __Costruzione - VisualizzazioneHHHHH__; dddddddd
* **Memorizzazioni**
** __Documentazione__; permette di memorizzare la documentazione del calcolo, valori possibili :  blank = No, 1 = Si
* **Flussi**
** __Pre / Post__; elementi della Tab. B£H che rappresentano flussi di elaborazioni da lanciare rispettivamente prima e dopo il calcolo costo medio ponderato

Sul piede del formato ci sono dei comandi funzione con il seguente significato : 
* **F06 = Conferma**, lancia l'elaborazione
* **F11 = Parametri esecuzione**, apre le impostazioni GPE (gestione parametri esecuzione)
* **F14 = Autorizzazioni**, apre la gestione autorizzazioni per la classe = ABILITA e la funzione = D0CO10A che regolano la possibilità per l'utente di utilizzare il programma
* **F15 = Memorizza Impostazioni**, permette di salvare le impostazioni eseguite nell'apposito formato con il nome indicato in questo campo coni chiave i seguenti elementi : 
* Contesto
** Tipo Costo

### Formato impostazioni parametri programma estrazione
![D0BASE_63](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO10A/D0BASE_63.png)* **LLC Ricalcolo**; permette di lanciare il ricalcolo del Low Level Code a monte del calcolo costo, valori possibili  :  blank = NO, 1 = Si
* **LLC Tipo distinta articolo**; tipo distinta da utilizzare in casi ricalcolo del Low Level Code
* **OAV Causali movimenti**; vvvvvvvv
* **Costi con configurazione**; valori possibili  :  blank = NO, 1 = Si
* **Cancellazione costo se non uniccccccc**; hhhhhhhhhhhhh, valori possibili  :  blank = NO, 1 = Si


OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

# Doc operativa
## Obiettivo
Calcolare i costi medi di un Articolo

## Esempio di parametri di lancio

|  Nam="ESE01" |
| 
| .COL Cod="C01" Txt="Contesto" unAut="1" |
| ---|----|
| 
| .COL Cod="C02" Txt="Tipo Calcolo" LunAut="1" |
| 
| .COL Cod="C03" Txt="Tipo Costo" LunAut="1" |
| 
| .COL Cod="C04" Txt="MDV per il calcolo" LunAut="1" |
| AR|1|STD|UNI| |
| AR|2|CRI|-| |
| AR|3|STD|-| |
|  |
| ### Casi gestibili |
| 1° Tipo Calcolo :  |
| Per ogni AR fa il calcolo del costo standard con MDV "UNI" ed utilizza la quantità passata |
| 2° Tipo Calcolo :  |
| Per ogni AR NON fa il calcolo ma fa una G55 con metodo TOT ed assume la quantità dalla G55 ignorando quella passata. |
| 3° Tipo Calcolo :  |
| Per ogni AR NON fa il calcolo ma fa una G55 e moltiplica la £55D per la quantità passata e imposta la quantità dov'è presente l'elemento £Q del costo da calcolare. |
|  |
| Questo metodo, oltre a permettere il calcolo del costo medio ponderato con le rimanenze, permette anche di avere costi medi di aree fiscali diverse, per tutta una serie di movimenti, piuttosto che mediare vari costi totali anche solo sul contesto AR e non per forza con i contesti DR/OR/CM. |
|  |
|  |
| # Doc tecnica |
| ## Obiettivo |
| Calcolare i costi medi di un articolo |
|  |
| ## Programmi |
|  |
| ### Nomenclatura dei Programmi |
|  |
|  La nomenclatura dei programmi del calcolo dei costi rispecchia la seguente |
|  codifica :  |
| _7_DO  >XX  _9_ZZ  _1_Xp |
|  |
| _7_DO = Area Costi |
|  |
|  |
| ### Flusso dei Programmi |
| La sintesi del flusso di lancio (D0CO10) può essere così sintetizzata :  |
|  |
| 