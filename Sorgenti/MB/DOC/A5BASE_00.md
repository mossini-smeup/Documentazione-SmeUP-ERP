# Documentazione generale
L'applicazione cespiti ha lo scopo di risolvere le problematiche relative alla determinazione degli ammortamenti dei beni di proprietà dell'azienda.

Le principali caratteristiche strutturali sono la multiaziendalità e l'impostazione a oggetti, che permettono di arricchire l'oggetto cespite con le consuete funzioni generali di ogni oggetto (note, parametri, flussi, ecc...) e di inserire l'applicazione cespiti in ambienti non Sme.up.

Da un punto di vista applicativo sono state previste le seguenti funzionalità : 

-  possibilità di calcolare, secondo la normativa vigente, l'ammortamento fiscale, civilistico e 'n' diversi ammortamenti industriali/gestionali.
Questo è ottenibile grazie all'introduzione della linea di ammortamento (simile allo scenario in pianificazione e schedulazione), che costituisce un ambiente separato in cui impostare i parametri di calcolo e registrare gli ammortamenti risultanti.
Per ogni linea si può infatti definire un piano di ammortamento esplicito relativo al singolo cespite, oppure impostare valori (in cifre o percentuali, globali o relativi ad ogni
esercizio), a livello di cespite, di categoria, o generali, con ricerca per risalita, in modo da inserire il dato al suo massimo livello ed evitare ridondanze;

- possibilità di inserire movimenti manuali per la singola linea, in modo da poter simulare rivalutazioni, svalutazioni, ecc...
La funzione di determinazione dell'ammortamento permette, per le diverse linee, di ottenere movimenti di validità annuale o mensile. E' così possibile ricavare il valore mensile del totale degli ammortamenti, per trasferirlo a prodotti di controllo di gestione;

- possibilità di ottenere, per ogni linea, analisi 'verticali' (piano di ammortamento di un singolo cespite) e 'orizzontali' (valore totale dei cespiti in un qualsiasi esercizio futuro), grazie all'elaborazione di calcolo degli ammortamenti, che registra tutta la storia futura dei cespiti presenti nel sistema;

- collegamento dalla contabilità generale, per introdurre nell'applicazione i movimenti di apertura (acquisti), e alla contabilità generale, per registrare gli ammortamenti.


# Categorie cespiti
Si inserisce la tabella categorie >A5A libera, in cui indicare il raggruppamento fiscale (tabella >V§A, fornita già compilata con le suddivisioni di legge).
Durante la creazione del cespite, è necessario inserirne anche la categoria, che verrà visualizzata, oltre al raggruppamento fiscale, nel relativo archivio anagrafico.
E' possibile deviare il raggruppamento fiscale su una tabella personale, qualora si vogliano raggruppare in modo diverso le categorie.

In alternativa, la categoria stessa può coincidere con il raggruppamento fiscale :  nella definizione dei campi della tabella >A5A impostare che il codice (campo elemento) sia un oggetto di tipo >TA/>V§A.

# Legami tra cespiti
Sono previsti due tipi di legami tra cespiti.

- _2_Raggruppamento
E' una riclassificazione dell'anagrafica che permette di totalizzare i valori di tutti i cespiti con il medesimo raggruppamento. Questa riclassifica può essere un oggetto qualsiasi, non obbligatoriamente un cespite.
Tale legame si applica tra cespiti collegati in modo blando (es. :  varie macchine di un impianto, arredamento di un ufficio, ecc...).

- _2_Dipendenza
Nell'anagrafica cespiti si può inserire il cespite master, determinando un legame più stretto del precedente :  oltre alla totalizzazione simile al raggruppamento, può essere visualizzata una scheda del cespite master, che fonde i suoi movimenti e totalizzatori (ammortamenti, fondi, ecc...) con quelli dei cespiti dipendenti.
L'ammortamento viene comunque sempre calcolato a livello di singolo cespite e la dipendenza è attiva solo ad un livello.

Es. :  su un computer (cespite master) viene montato, in un secondo tempo, un nuovo disco (cespite dipendente).
L'introduzione di un cespite dipendente è una modalità di arricchire il cespite master con un'aggiunta fisica o eseguendo un movimento di rivalutazione, da eseguire separatamente per il cespite master e per il cespite dipendente.

## Partenza cespiti in corso
Sono previsti due tipi di inizio cespiti in corso.

 - _2_Cespiti usati
Si imposta in anagrafica il flag di cespite usato.
Il movimento di acquisto va eseguito per l'importo della fattura.
Per gli ammortamenti, il cespite usato si comporta integralmente come un cespite nuovo, con l'eccezione che il numero di anni per cui è possibile eseguire l'ammortamento anticipato è minore (attualmente è 1) :  deve essere inserito in tabella linea >A5C, per poter essere modificato.

 - _2_Passaggio da gestione cartacea a gestione informatica
Tutti i movimenti di capitale vanno inseriti nel dettaglio, con attenzione alla data di registrazione, che deve essere storica.
Si registra un movimento di ammortamento precedente (tipo movimento >IA) con data di fine periodo antecedente l'inizio della gestione informatica (es. :  31/12/XX). E' simile al caricamento della giacenza iniziale in una gestione di magazzino.
In presenza di ammortamenti da non includere nel fondo (ammortamento perso, quote non ammortizzabili), sarà necessario scrivere un movimento simile al precedente, ma con causale di tipo movimento >NA.
Fa eccezione la quota di ammortamento perso, da inserire con un movimento specifico a parte.

## Modalità del reperimento del numero di periodi di ammortamento già eseguiti

### Determinazione del numero di periodi con ammortamento eseguito
La funzione di scansione movimenti cespiti (>£A5F), in modalità di _2_ritorno totale, determina il numero di periodi di ammortamento già eseguiti (chiusi), in base alla presenza, in ogni esercizio, di un movimento con tipo di radice 'A'.

### Determinazione del numero di periodi con ammortamento possibile
Dalla data di inizio ammortamento (con risalita cespite-linea/cespite/data acquisto cespite/data movimento acquisto), si calcolano i periodi intercorsi tra quello iniziale e il corrente (escluso) :  si ottiene il numero di periodi per i quali era possibile eseguire l'ammortamento, indipendentemente dal fatto che si sia effettivamente eseguito.
(Infatti, impostando un record vuoto a livello di cespite/linea/esercizio, per quell'esercizio non verrà calcolato l'ammortamento).
Questo numero di periodi è utile per decidere se l'ammortamento anticipato sia eseguibile o meno.

# Calcolo mensile
Se il calcolo è mensile, ma non alla data, l'ultimo esercizio comunque spezza i mesi sul residuo, invece dovrebbe imputare la quota corretta mensile degli esercizi precedenti a tutti i mesi fino a che non si raggiunge il valore del cespite.

# Utility Cespiti
_2_ A5UT06A Travaso movimenti fiscali in linea civilistica
  :  : INI . Sorgente
  :  : CMD CALL B£VED0 PARM('A5UT06A' '' '' '' '0')
  :  : FIN
  :  : INI . Richiesta parametri
  :  : CMD CALL A5UT06A
  :  : FIN

_2_ A5UT07A Ricalcolo movimenti linea civilistica cespiti con ammort.anticipato fiscale
  :  : INI . Sorgente
  :  : CMD CALL B£VED0 PARM('A5UT07A' '' '' '' '0')
  :  : FIN
  :  : INI . Richiesta parametri
  :  : CMD CALL A5UT07A
  :  : FIN

_2_ A5UT09A Attribuzione linea mov.automatici senza linea
  :  : INI . Sorgente
  :  : CMD CALL B£VED0 PARM('A5UT09A' '' '' '' '0')
  :  : FIN
  :  : INI . Richiesta parametri
  :  : CMD CALL A5UT09A
  :  : FIN
