# CQ1 - Personalizzazione controllo qualità 1
 :  : DEC T(ST) K(CQ1)
## OBIETTIVO
Questa tabella, contiene alcune scelte di personalizzazione dell'applicazione. Con tali scelte si può condizionare il modo di esecuzione dei programmi.
## CONTENUTO DEI CAMPI
 :  : FLD T$TICO **Tipo Costo da Utilizzare**
Campo controllato dalla tabella 'TCO' (Tipo costo). Indica il tipo di costificazione del gestionale a cui il programma si deve riferire per le valorizzazioni. I campi possibili sono : 
'1'  Costo 1
'2'  Costo 2
'3'  Costo 3
 :  : FLD T$LICO **Livello Costi (1..5)**
Questo campo indica il LIVELLO del costo da assumere per la valorizzazione dell'articolo.
Può assumere i seguenti valori : 
'1'  Costo Primo
'2'  Costo Diretto
'3'  Costo Industriale
'4'  Costo Generale
'5'  Prezzo di listino
Tali costi vengono prelevati dagli archivi del calcolo costi del gestionale.
 :  : FLD T$RMPI **Esec. Inter. Mag. PR**
Campo di esecuzione del movimento a magazzino del gestionale.
Può assumere i valori : 
' '  Non genera nessun movimento
'X'  A seguito di una dichiarazione di collaudo il programma genera la movimentazione delle quantità del lotto nei vari magazzini.
 :  : FLD T$MALI **Mantenimento livelli**
Campo predisposto per futuri utilizzi.
 :  : FLD T$RAGA **Raggruppamento articoli in entrata acquisti**
Indica se il programma di creazione automatica dei lotti di acquisto deve generare un lotto per ogni riga della bolla del materiale in entrata o deve effettuare un raggruppamento per articolo. Questo campo può assumere i valori : 
' '  Genera in automatico un lotto per ogni riga della bolla in entrata.
'X'  Genera un lotto cumulativo di più righe della stessa bolla per lo stesso articolo in entrata.
 :  : FLD T$ATTP **Strumenti di misura versione Ridotta**
Campo che stabilisce la versione degli strumenti di misura da utilizare. Puo' assumere i seguenti valori : 
b Strumenti di Misura versione estesa.
X Strumenti di Misura versione ridotta.
 :  : FLD T$FSCA **Fattore di scarto 1**
Campo numerico di DEFAULT che indica al sistema la % di scarto della quantità del lotto. Questo campo viene utilizzato qualora nell'anagrafica del gestionale non dia stata assegnata all'articolo la propria % di scarto. (es :  0,1 indica che su un lotto di 1000pz prevedo di scartarne 1).
 :  : FLD T$RICL **Numero riclassifica**
Campo controllato dalla tabella 'CLR' (Riclassifiche). Indica la tipologia di riclassifica di DEFAULT che il programma deve utilizzare per l'analisi degli articoli.
 :  : FLD T$CATS **Controllo categoria**
Utilizzato per definire il tipo di controllo da eseguire nella costruzione delle categorie. Può assumere i valori seguenti : 
b    Il codice categoria deve esistere obbligatoriamente anche nell'anagrafico articoli.
1    Il codice può esistere nell'anagrafico articoli. Funziona la ricerca alfabetica che permette la scelta ma sono ammessi anche codici non esistenti nell'anagrafico.
2    Il codice categoria è totalmente libero.
 :  : FLD T$PGCF **Progr.Classe Funzionale**
Questo campo è controllato nella verifica della presenza del programma. È il programma da richiamare per ottenere la classe funzionale dell'articolo. Questo programma orienta il Q9000 nella ricerca del campo della Classe Funzionale nell'archivio Anagrafico del programma gestionale.
 :  : FLD T$PGCA **Progr.Classe Abilitazione**
Questo campo è controllato nella verifica della presenza del programma. Viene attivato solo se non è prevista l'installazione del Modulo 'GESTIONE ARTICOLO/FORNITORE' del Q9000. È il programma da richiamare per ottenere la classe di abilitazione del fornitore. La classe di abilitazione è
determinata in funzione del fornitore e dell'articolo fornito.
 :  : FLD T$DOCU **Documento mod.Artic.**
Questo campo è controllato dalla tabella 'CQ0' (Tipo Documento - Gestione). Serve per indicare al Q9000, quale fra tutti i documenti inseriti risulta essere associato ad un DISEGNO TECNICO o Specifica TECNICA per poterne gestire il livello di modifica direttamente attraverso il modulo della gestione richieste di intervento.
 :  : FLD T$CONT **Gestione Contenitori**
Se non è bianco, durante la dichiarazione di Quantità e contenitori (programma CQBC50) è possibile precisare, oltre al numero dei contenitori (cosa che è possibile anche se il campo Gestione Contenitori è bianco), anche il tipo di contenitore e le quantità per ognuno di essi.
 :  : FLD T$GSCO **Gestione Scarti x Contenitore**
In combinazione con il campo precedente, il valore 'X' in questo campo permette di registrare le quantità scartate per ogni contenitore in seguito alle operazioni di collaudo. In pratica verranno riproposti i contenitori dichiarati dalla precedente fase di Dichiarazione Quantità e Contenitori e verrà richiesto il dettaglio delle quantità scartate per ciascuno di essi.
Questa possibilità può essere utile a chi gestisce il magazzino ad ubicazioni dinamiche.
 :  : FLD T$NUNC **Gestione Numeratore N.C**
Se 'X' in immissione non conformità verrà generato un numero di documento automatico.
 :  : FLD T$CQ1A **Indici su D5**
Il valore SI indica che la base dati storici, per la parte dinamica della valutazione del Fornitore, è sull'archivio Costi per Oggetto (D5COSO0F); in caso contrario la parte dinamica viene gestita dalla gestione Indici
 :  : FLD T$CQ1B **Cicli di Collaudo**
Attiva interfaccia Cicli di Collaudo, se non specificato assunto SM
 :  : FLD T$CQ1C **Integrazione magazzino con CRP**
Questo flag indica se attivare i collegamenti di magazzino secondo le modalità espresse dalla tabella CRP
 :  : FLD T$CQ1F **Collaudatore automatico**
Se impostato in fase di dichiarazione di collaudo del lotto verrà impostato automaticamente il campo collaudatore con il valore impostato nel campo "Matricola Dipendente" della tabella B£U Utenti.
 :  : FLD T$CQ1G **No Delete Lotto in Scollegamento**
Se impostato in fase di scollegamento documento se si è in modifica del documento il lotto non viene cancellato
 :  : FLD T$CQ1H **IDOJ documento**
Attivando la gestione "IDOJ documento" si vuole ottenere una identificazione più corretta dei documenti accedendo per
numero. L'attivazione è subordinata all'applicazione della ptf CQ10726.
 :  : FLD T$CQ1I **Valore**
Attivando la gestione a valore, si ottine la documentazione dell'oggetto documentale attraverso il significato degli oggetti della griglia. Se non attivato la documentazione avviene attraverso i codici della griglia.
