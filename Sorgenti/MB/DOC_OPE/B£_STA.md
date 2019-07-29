# Generalità
I programmi di stampa di liste di informazioni (liste di articoli, di ordini di vendita, di righe giacenza, di bolle entrata merci, ecc...) hanno tutti una struttura comune, che prevede un formato guida di impostazione generale, un secondo formato di impostazione delle caratteristiche di stampa (ordinamento, filtri, schemi dati e schemi valori, caratteristiche aggiuntive) e un ultimo formato di impostazioni dei parametri di esecuzione : 

![B£_04_01](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_01.png)
I formati di gestione dei programmi di stampa hanno delle leggere differenze tra di loro, giustificate dalla diversa natura delle informazioni da gestire; a titolo di esempio utilizzeremo il programma di stampa dei documenti.

# Formato impostazioni generali

1. **Modalità di esecuzione**    -->    per decidere il tipo di output : 

- Stampa
- A video
- Con trasferimento a PC (viene creato in file in formato carattere .CSV da trasferire su una cartella condivisa, il cui precorso è impostato nelle tabelle di customizzazione della comunicazione AS/400 > PC


2. **Tipo di stampa**    -->    se presente, serve per selezionare il tipo di informazioni che saranno presentate e per condizionare il formato di impostazione caratteristiche di stampa

3. **Intestazione**    -->    per scrivere una riga di intestazione (il titolo) sul report che verrà stampato

4. **Condizione libera utente**    -->    se si vogliono ottenere stampe particolari (con un layout diverso, con caratteri o formati particolari, oppure con selezioni diverse da quelle previste con le parzializzazioni standard) è possibile lanciare un programma specifico di elaborazione e/o di richiesta parametri. Questi programmi sono inseriti in un elemento di un sottosettore preciso (es. :  BR per le stampe dati base, V5 per le stampe del ciclo esterno, ecc...) della tabella B£Q.


![B£_04_02](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_02.png)
Le impostazioni (una volta definite le caratteristiche della stampa utilizzando il formato successivo) possono essere memorizzate con un nome, per essere poi richiamate successivamente.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

# Formato di impostazione caratteristiche di stampa
Uno dei formati di questo tipo è il seguente : 

![B£_04_03](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_03.png)
In questo formato si pùo : 

- definire l'ordinamento;
- definire le parzializzazioni;
- definire schemi valori e informazioni - impostare la periodicità;
- decidere se  stampare : 
-- solo le righe di totale (se previste dall'ordinamento)
-- le note di testata documento
-- le note di riga documento


## Ordinamento
Per impostare l'ordine delle righe presentate si inserisce uno dei caratteri di ricerca classici di Sme.up (>'!' / >'?') nel campo apposito e verrà presentata la lista dei campi che si possono utilizzare : 

![B£_04_04](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_04.png)
Nella colonna ">SEQUENZA" si definisce la sequenza di ordinamento (massimo 3).
Per ogni campo di ordinamento si può scegliere se ascendente o discendente (>A/>D).
Si può definire il comportamento al cambio codice (totali, codice, codice e decodifica : > ? per i valori possibili) e se fare saltare alla pagina successiva.

L'ordinamento deve essere memorizzato per poter rientrare nelle impostazioni di stampa.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

## Parzializzazioni
Per le parzializzazioni classiche vedere il documento specifico.
- [Parzializzazioni](Sorgenti/MB/DOC_OPE/B£_PAR)

Le parzializzazioni devono essere memorizzate per poter rientrare nelle impostazioni di stampa.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

### Parzializzazioni esterne
Molti programmi di stampa prevedono anche parzializzazioni ulteriori, dette parzializzazioni esterne, per utilizzare le quali devono essere stati customizzati gli scenari adatti (attività EDP).
Con il carattere di ricerca selezionare lo scenario desiderato nella relativa lista : 

![B£_04_05](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_05.png)
Dopo aver selezionato lo scenario, aprire il formato di filtro usando il carattere ">X" : 

![B£_04_06](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_06.png)
## Schemi - Valori / Informazioni
- [Schemi di visualizzazione e stampa](Sorgenti/MB/DOC_OPE/B£_SCH)

Gli schemi devono essere memorizzati per poter rientrare nelle impostazioni di stampa.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

### Periodicità
Alcuni programmi di stampa, se hanno gli schemi valori, prevedono anche la periodicità :  una stampa normale presenta, ad esempio, le quantità di articoli ordinate su varie righe (una per ogni riga ordine).
Se si desidera visualizzarle in una sola riga (es. :  totale quantità mensile), si attiva la gestione della periodicità (con il solito carattere di ricerca nell'apposito campo), presentata attraverso questo formato : 


![B£_04_07](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_07.png)
Si devono impostare : 

- la data di inizio (sono possibili le date dinamiche);
- il tipo di periodicità (cioè quanti periodi a partire dalla data inizio e quanto deve essere ampio ogni periodo);
- il numero di periodi da presentare (se si seleziona il totale per riga prevedere 1 periodo in più rispetto a quelli della periodicità);
- se e in quale periodo conteggiare le i valori scaduti (prima del primo periodo) o successivi all'ultimo;
- il totale per riga e la data da considerare;
- la formattazione dei valori.

Quest'ultima si imposta mediante il seguente formato : 


![B£_04_08](http://localhost:3000/immagini/MBDOC_OPE-B£_STA/BX_04_08.png)
Sarà necessario impostare : 

- la lunghezza dell'intestazione;
- l'intestazione di ogni campo;
- il numero di interi, decimali, punti di separazione;
- se dividere il valore per 10 / 100 / 1000 (1 / 2 / 3);
- cosa calcolare nella colonna dei totali;
- se stampare la riga anche se a zero.



Formattazione valori e periodicità devono essere memorizzate per poter rientrare nelle impostazioni di stampa.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

# Formato impostazione parametri esecuzione
- [Parametri di esecuzione](Sorgenti/MB/DOC_OGG/P_B£GPE2)
