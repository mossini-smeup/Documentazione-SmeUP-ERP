# MPC - Viste piano
## OBIETTIVI
Permettere di costruire in modo parametrico una vista di un piano. La tabella descrive le entità collegate alla vista piano.
## SOTTOSETTORI
Non gestiti.
## INTRODUZIONE
**Definizioni**
_Vista piano_ :  è una matrice costituita da colonne, che rappresentano i periodi, e da righe, che rappresentano le quantità per periodo delle entità caratteristiche della vista piano.
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 __Codice / parametro 1__
Identifica il tipo della prima entità che caratterizza la vista.
Il tipo può essere un elemento della tabella *CNTT, oppure essere una tabella specifica.
 :  : FLD T$PAR1 __Parametro 1__
Identifica il parametro della prima entità che caratterizza la vista.
 :  : FLD T$KYC2 Codice / parametro 2
Identifica il tipo della seconda entità che carratterizza la vista.
Il tipo può essere un elemento della tabella *CNTT, oppure essere una tabella specifica.
 :  : FLD T$PAR2 __Parametro 2__
Identifica il parametro della seconda entità che caratterizza la vista.
 :  : FLD T$TRG __Tipo risorsa__
È un elemento della tabella TRG, che  viene utilizzato per recuperare dal calendario la disponibilità risorse nella vista specifica e verificare, quindi, il carico sui centri di lavoro.
 :  : FLD T$GRAC __Gruppo azioni__
Identifica il flusso di azioni che possono essere collegate alla vista piano (tabella B£H).
 :  : FLD T$GDEC __Gestione decimali__
Se questo campo è diverso da blank, nella stampa della vista vengono utilizzati i decimali.
 :  : FLD T$MPCG __Gruppo viste__
È un carattere che permette di riaggregare, secondo criteri liberi, le varie viste. In particolare, nell'interrogazione di confronto fra viste (Azioni su riga) si può usare quella della tabella come valore assunto.
 :  : FLD T$MPCU __Unità misura quantità__
Indica in quale unità di misura sono espressi i numeri (120) che sono gestiti nella vista.
 :  : FLD T$MPCV __Inversione segno__
Valido solo per interrogazioni in matrice Loocup : 
Definisce se la natura della vista contiene dei valori che devono essere considerati negativi.
Ad esempio se creo un piano MPS con due viste, una relativa alle quantità acquistate, l'altra relativa
alle quantità vendute, se interrogo le viste tramite la scheda standard le totalizzazioni delle colonne
devono considerate la quantità acquistata come positiva e la quantità venduta come negativa.
Tramite questo flag è possibile creare le due viste utilizzando per entrambe quantità positive (come è
sarebbe naturale), ma l'interogazione tramite scheda considererà la quantità venduta come negativa.
