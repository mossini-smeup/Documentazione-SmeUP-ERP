# C6F - Fonti future disp.finanz.
 :  : DEC T(ST) K(C6F)
## OBIETTIVO
Definisce le caratteristiche delle fonti future (ordini in corso, rate aperte, ecc..) nelle analisi di disponibilità finanziaria.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice della fonte.
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$C6FA **Origine Fonte**
È un elemento V2/C5OFF, che definisce la natura della fonte.
 :  : FLD T$C6FB **Parametro 1/2 Fonte**
Assumono un significato diverso in funzione dell'origine fonte : 
-->_Se l'origine è AP (altra applicazione)  : _
- Il primo parametro è la sigla del'appicazione (elemento della tabella B£A).
- Il secondo parametro è controllato dal programma specifico B£TC6F_xx, dove xx è la sigla dell'applicazione.

-->_Se l'origine è DF (documenti fatturabili)  : _
In questa fonte vengono riportati i documenti del ciclo esterno che sono in condizione di 'fatturabilità' (bolle, fatture), non ancora collegati alla contabilità.
Parametro 1 : 
-    Pos.1  ' ' se documento di ciclo attivo.
                '1' se documento di ciclo passivo.
-    Pos.2  ' ' se fattura.
                '1' se nota d'accredito.
-    Pos.3/4   estremi inferiore e superiore dello stato 'fatturazione' del documento (flag 19 della testata).

 Sono entrambi obbligatori. Viene controllato, inoltre, che essi siano congruenti con quanto impostato nelle posizioni 1  e 2.
_9_Esempio :  in caso di fattura attiva, possono andare da 'A' a 'D', mentre in caso di nota d'accredito passiva possono andare da 'n' a 'p'.

-->_Se l'origine è RI (rate di pagato a rischio)  : _
Vengono incluse le rate di pagato la cui natura del pagamento (flag 13) è uno dei seguenti valori : 
- C - Cessioni.
- E - Riba.
- R - R.I.D.
- T - Cambiale / Tratta Accredito.
Si veda la documentazione del campo 'data condizionamento' per l'impostazione della data di partenza del rischio.
Parametro 1 : 
-    Pos.1/2   Estremi pertinenza (oggetto V3C5SPE).
-    Pos.3/4   Estremi condizione (oggetto V3C5SCO).

-->_Se l'origine è SC (rate di dovuto aperte)  : _
Si veda la documentazione del campo 'data condizionamento' per l'impostazione della data di impostazione delle scadenze scadute.
Parametro 1 : 
-    Pos.1/2   Estremi pertinenza (oggetto V3C5SPE).
-    Pos.3/4   Estremi condizione (oggetto V3C5SCO).

-->_Se l'origine è PM (parametri) : _
Parametro 1 : 
-    Pos.1/3 :   Categoria parametri (elemento della tabella C£E) :  la griglia che definisce i due campi chiave dei parametri deve essere associata ad un'azienda (CNAZI).
-    Pos.4/6 :   Valore parametro (elemento della tabella B£N del sottosettore presente nella categoria). In questo parametro devono essere previsti la gestione delle quantità e lo sviluppo per date.
L'oggetto del parametro è l'oggetto di cui si chiede ADF (di solito cliente, fornitore, conto). Attualmente tale fonte è valida solo per disponibilità future.
Determinazione delle date risultanti : 
_7_Assunzioni : 
- Se indicata una sola data si assume la finale uguale all'iniziale.
- Se l'anno è maggiore di 9000 si intende ripetitiva per tutti gli anni quindi l'anno viene sostituito con l'anno in corso.
_7_Calcolo : 
- Si assume come limite iniziale oggi e finale la data limite se passata.
- Se le due date sono uguali si usa tale data.
- Se sono diverse si ripete la data per ogni mese fino a superare la data finale per un massimo di 12 rate.
_9_Esempi : 
- Oggi 20/02/2004 e Limite finale non impostato
Data 1 Par. Data 2 Par.   Risultato.
12012004                  Nessuno.
17039000                  Porto 9000 a 2004  e ottengo 17/03/2004.
01012004    31122004      Dal 01/03/2004 al 01/12/2004  ogni mese.
12029001    12079001      Dal 12/03/2004 al 12/07/2004  ogni mese.
21019002    21129002      Dal 21/02/2004 al 21/01/2005  ogni mese.

-->_Se l'origine è UT (fonte utente)  : _
Sono un programma ed un parametro di condizionamento, per interfacciare fonti esterne a SMEUP.

-->_Se l'origine è V5 (documenti di ciclo esterno)  : _
In questa fonte vengono riportati i documenti del ciclo esterno che non hanno ancora raggiunto una condizione di 'fatturabilità' (previsioni, ordini).
Parametro 1 : 
-    Pos.1/3   Tipo documento (obbligatorio).
-    Pos.4/6   Modello documento (facoltativo).
-    Pos.7     '1' se deve escludere i documenti  non contabilizzabili (flag 8 della testata a '9').
-    Pos.8
' ' se la data partenza del pagamento è la consegna confermata della riga.
'1' se la data partenza del pagamento è la consegna richiesta della riga.
-    Pos.9   È un elemento della tabella B£W00 :  se impostato verranno considerate solo le righe documenti con questo livello, se lasciato in bianco verranno considerate le righe con livello '2'.
-    Pos.10  Se impostato, verrà ristornato il valore totale del documento alla data della rata più bassa.
Se invece lasciato in bianco, verranno calcolate tutte le rate in base alle date di consegna e alla condizione di pagamento.

-->_Se l'origine è MC (movimenti contabili) : _
In questa fonte vengono riportate le informazioni provenienti da movimenti contabili, ovvero da mastrini di conto.
-   Pos. 1/2 :  Indica la pertinenza delle registrazioni contabili considerate dalla fonte
-   Pos. 3/4 :  Indica la condizione delle registrazioni contabili considerate dalla fonte
-   Pos. 5/7 :  In questo campo è possibile indicare il codice della riclassifica di appartenenza dei conti di cui verrà considerato il mastrino
-   Pos 8 e successive :  In questo cmapo è possibile indicare il codice i una riclassifica singola.

 :  : FLD T$C6FE.T$C6FB
 :  : FLD T$C6FC **Azione fonte (+/-/N)**
Definisce se il contributo della fonte è positivo, negativo oppure neutro per la disponibilità. Una fonte neutra viene riportata in un campo separato dell'analisi disponibilità.
 :  : FLD T$C6FD **Ordinamento fonte**
È un carattere che stabilisce, a pari data e nell'ambito delle fonti future, la posizione di questa fonte.
 :  : FLD T$C6FF **Presenta anche se 0**
Se impostato, mostra la riga della fonte anche se con valore a zero, unicamente nel caso di ritorno riepilogato per fonte.
 :  : FLD T$C6FG **Descrizione ridotta**
È la descrizione che può essere usata nei casi di rappresentazioni compatte.
 :  : FLD T$C6FL **Livello**
È un elemento della tabella B£W00 :  se impostato verranno considerate solo le fonti con questo livello, se lasciato in bianco verranno considerate le fonti con livello '2'.
 :  : FLD T$C6FN **Suffisso programma aggiustamento**
È il suffisso x del programma C5C6D0G_x, che viene lanciato all'atto della scrittura delle fonti di questo tipo, per modificarne il comportamento.
 :  : FLD T$C6FO **Stato minimo/massimo**
Sono significativi per le fonti interne per le quali è impostato lo stato. Se inseriti (se non impostato lo stato massimo viene assunto '99'), sono un'ulteriore parzializzazione per fonti di questo tipo.
 :  : FLD T$C6FP.T$C6FO Stato massimo
 :  : FLD T$C6FR **Riclassifica**
È un elemento della tabella 'C6*RF' :  viene usato nell'analisi disponibilità riepilogata. Per maggiori dettagli, riferirsi alla documentazione del campo corrispondente nella tabella C6E (fonti esistenti).
 :  : FLD T$C6FS **Ordinamento riclassifica**
È usato nelle analisi riepilogate. Per maggiori dettagli, riferirsi alla documentazione del campo corrispondente nella tabella C6E (fonti esistenti).
 :  : FLD T$C6F1 **Data limite**
Si può impostare una data massima per le fonti di questo tipo. È ammessa (e consigliabile) una data in forma implicita. Come limite per la fonte viene considerato il valore minimo tra questa data e la data massima, inserita all'atto del lancio dell'analisi disponibilità.
 :  : FLD T$C6F2 **Data condizionamento**
Si può impostare una data di condizionamento (preferibilmente in forma implicita), che agisce in modo diversificato nelle varie fonti.
_7_Scadenzario.
Una rata di dovuto è scaduta se la sua data scadenza avanzata dei giorni di scaduto, impostati in tabella C51, è minore o uguale a questa data (se assente si assume oggi)
_7_Rischio.
Una rata di dovuto è a rischio se la sua scadenza è maggiore o uguale a questa data (se assente si assume oggi meno i giorni di rischio impostati in tabella C51).
 :  : FLD T$C6F3 **Tipo Oggetto di Riferimento**
Questo campo viene utilizzato solo quando l'ADF viene utilizzata nell'analisi dei flussi di cassa :  in questo caso, se qui viene indicata una classe oggetto (tipicamente una classe ente o la classe dei conti contabili) solo per questa classe oggetto la fonte verrà elaborata. E' inoltre possibile indicare ad una classe una lista (sempre delle stessi classi). In questo caso nel campo codice dovrà essere indicato il codice della lista di riferimento. Solo per le istanze della classe di riferimento, appartenenti alla lista, la voce verrà elaborata.
 :  : FLD T$C6F4 **Codice Oggetto di Riferimento**
Se nel capo tipo oggetto è indicata un tipo oggetto lista, qui è possibile indicare il codice della lista da utilizzare.
 :  : FLD T$C6F5 **Fonte Esistente**
Se valorizzato forza che tutte i risultati dell'elaborazione della fonte vengano forzati come fonti esistenti e non come fonti future.
 :  : FLD T$C6F6.T$C6FB
