# Gestione KIT Articoli

# Gestione KIT Articoli
Al fine di gestire la vendita di articoli composti che sono la risultante di altri articoli accorpati per una specifica esigenza (es. lista nozze, cestini, composizioni, bouquet, ecc.) sono stai introdotti i KIT Articoli. La gestione del Kit prevede l'utilizzo di un articolo fittizio 'Padre' che verrà utilizzato per la selezione in Cassa e una serie di articoli reali 'Figli' che compongono il Kit e sui quali verranno imputate le vendite e le relative movimentazioni di magazzino.

## Configurazione Applicativa
Per abilitare l'utilizzo dei Kit dal Menu _Utiilità>Configurazione>Gestione Configurazione Applicativa
selezionare 02 Articoli, scheda Articoli, impostare il flag Gestione KIT su SI

Poi, dal Menu _Utilità > Configurazione>Gestione Configurazione  Applicativa_, 09 Cassa Slave, nella scheda Altri Parametri (3), impostare Modalità Gestione Kit in Cassa su
 * Versione 1 - Creazione KITF :  il Kit viene suddiviso nei suoi componenti solo sui movimenti di magazzino
 * Versione 2 - Esplosione componenti in stampa scontrino :  il Kit viene esploso anche sullo scontrino. Questa impostazione è consigliata nel caso in cui i componenti abbiamo aliquota Iva diversa.
I dettagli sulla differenza di comportamento sono descritti in Vendita del Kit

## Creazione del KIT
Creiamo dapprima un articolo che funga da Padre (o utilizziamone uno già inserito). Compiliamo e confermiamo i dati fino all'ultima scheda, compilando obbligatoriamente il campo Aliquota Iva nella prima scheda. Nell'ultima scheda selezioniamo 09-Listini di Vendita per attribuire il prezzo di vendita dell'intero Kit. ....
A questo punto facciamo in modo che l'articolo diventi un Padre di Kit selezionando 14-Kit. Si apre la griglia con l'elenco degli articoli Figli. Inseriamo un articolo col tasto F6.
Vengono richiesti i seguenti campi, tutti obbligatori : 
 * Indice di modifica :  rappresenta la versione del Kit. Può succedere che un kit subisca delle variazioni, ovvero che un componente venga sostituito da uno simile o eliminato, oppure che altri articoli Figlio vengano aggiunti al Kit. L'indice di modifica permette di tenere traccia degli articoli che compongono il Kit nelle varie versioni. Una versione del Kit è composta quindi da tutti gli articoli che hanno lo stesso Indice di Modifica.
 * Sequenza :  l'ordine di presentazione di questo articolo Figlio all'interno del Kit
 * Articolo :  l'articolo figlio. Deve essere già inserito nell'anagrafica articoli
 * Quantità :  quanti pezzi di questo articolo entrano a far parte del Kit.
Confermiamo con Invio e procediamo con l'inserimento degli altri Figli.
Gli articoli Figlio sono componenti di Kit (anche più di uno) ma rimangono comunque articoli veri e propri vendibili singolarmente. L'articolo Padre invece può svolgere solo la parte di Padre di Kit.

## Vendita del KIT
 * Versione 1 - Creazione KITF
Leggiamo in Cassa il codice a barre dell'articolo Padre. L'articolo viene visualizzato col relativo prezzo, sotto vengono visualizzati gli articoli Figli con prezzo pari a 0.
Nel caso in cui ci siano più versioni (Indici di Modifica diversi) il sistema propone la griglia con la visualizzazione di tutte le versioni del Kit per la selezione di quella che si intende inserire nello scontrino.
Sullo scontrino fiscale viene registrato il solo Padre con relativo prezzo di listino.
A livello di magazzino vengono invece scaricati SOLO i Figli con il prezzo uguale alla quota parte del kit con cui sono stati venduti, calcolato come descritto successivamernte in Determinazione prezzo Articolo Figlio.

Se vengono passati in Cassa gli articoli che compongono il KIT, negli articoli e nella quantità che lo costituiscono, alla pressione del tasto Subtotale il Kit viene riconosciuto dal sistema e mostrato nello scontrino. Premendo SubTotale tra l'inserimento di due articoli Figlio il sistema mantiene la vendita separata.

 * Versione 2 - Esplosione componenti in stampa scontrino
Leggiamo in Cassa il codice a barre dell'articolo Padre. L'articolo viene visualizzato col relativo prezzo, sotto vengono visualizzati gli articoli Figli, con prezzo pari a 0.
Nel caso in cui ci siano più versioni (Indici di Modifica diversi) il sistema seleziona automaticamente la versione con indice di modifica più alto.
Sullo scontrino viene stampata solo la descrizione del Padre senza importo e a seguire l'elenco dei Figli con codice a barre, prezzo e descrizione, dove il prezzo è determinato come descritto successivamernte in Determinazione prezzo Articolo Figlio. Ai fini fiscali del registratore di cassa, solamente gli articoli figli vengono inseriti nello scontrino.

## Determinazione prezzo articolo Figlio.
Il prezzo degli articoli Figlio quando venduti come Kit viene calcolato in funzione del peso del Figlio all'interno del Kit stesso. In altre parole il prezzo di vendita del Padre viene ripartito proporzionalmente sui Figli in base alla quantità nel Kit e al prezzo di listino di ogni Figlio.
Consideriamo ad esempio un articolo Kit KP1 composto da 3 articoli figli KF1, KF2, KF3 con i seguenti prezzi di listino e quantità : 
KF1 =5 ¤ x 1 PZ
KF2 = 10 ¤ x 1 PZ
KF3 = 5 ¤ x 3 PZ =15 ¤
Il totale dei componenti del Kit da quindi 30 ¤.
Il kit KP1 invece viene definito a listino con un prezzo di 18 ¤, ovvero con una riduzione del 40% rispetto alla somma dei singoli prezzi (30¤ -40% = 12 ¤)
Il prezzo dei Figli in fase di vendita Kit diventerà il seguente : 
KF1 = 5 ¤ -40% = 3 ¤
KF2 = 10 ¤-40% = 6 ¤
KF3 = 15 ¤- 40% = 9 ¤

