# CS1 - Personalizzazione costi std
 :  : DEC T(ST) K(CS1)
## OBIETTIVO
Contenere tutte le condizioni specifiche dell'impostazione iniziale dell'applicazione.
## UTILIZZO
Viene letta all'inizio dei programmi per condizionarne il comportamento
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$CNA0 **Contenitore note assieme**
Specifica quale fra i contenitori di note, definiti nella tabella NSC, contiene le eventuali note relative all'assieme per un tipo costo. Tali note potranno essere stampate se richiesto dalla stampa dei costi.
 :  : FLD T$INA0 **Informazione note assieme**
Specifica con che codice informazione (Tabella NSI) sono immesse le note aggiuntive relative agli assiemi.
__Struttura : __
- Contenitore
- Assieme
- Tipo costo (facoltativo)
- Tipo informazione
 :  : FLD T$CNC0 **Contenitore e informazioni per componente**
Significato come sopra
Le note sul componente si intendono relative ad un tipo costo ma indipendenti dall'assieme cui questo appartiene.
_9_Esempio : 
Se per i costi standard 1993, il costo di un cuscinetto ha qualche specificità, caricandolo in queste note apparirà se richiesto su tutti gli assiemi che contengono tale cuscinetto.
__Struttura : __
- Contenitore
- Componente
- Tipo costo (facoltativo)
- Tipo informazione
 :  : FLD T$CNL0 **Contenitore e informazioni per legame**
Significato come sopra
Le note sul legame si intendono relative ad un componente e tipo costo ma dipendenti dall'assieme cui questo appartiene.
__Struttura : __
- Contenitore
- Assieme
 :  : FLD T$DSCA **Disattivazione del calcolo dell'attrezzaggio**
Tramite l'utilizzo di questo Flag si piloterà il calcolo dei costi di attrezzaggio nel programma di calcolo costi.
I suoi valori saranno  : 
- Blanks = Il calcolo è attivo
- 1      = Il calcolo è disattivo
 :  : FLD T$DSCS **Disattivazione del calcolo degli scarti**
Tramite l'utilizzo di questo Flag si piloterà il calcolo dei costi relativi agli scarti nel programma di calcolo costi.
I suoi valori saranno  : 
- Blanks = Il calcolo è attivo
- 1      = Il calcolo è disattivo
 :  : FLD T$DSAG **Disattivazione aggiornamento ARCHIVI**
Tramite l'utilizzo di questo Flag si piloterà l'aggiornamento degli archivi dell'applicazione interfacciata. In questo modo si permetterà la manipolazione dei dati sfruttando un ambiente reale e conservando comunque la sicurezza sugli stessi.
I suoi valori saranno  : 
- Blanks = L'aggiornamento è attivo
- 1      = L'aggiornamento è disattivo
 :  : FLD T$TCO1 **Tipo Costo assunto 1 / 2 / 3**
Permette di definire quale tipo costo deve essere considerato dall'applicazione gestionale presente come corrispondente dei costi dell'applicazione stessa. Abbiamo in particolare : 
A.   GIPROS
1 = corrispondenza del costo 1
2 = corrispondenza del costo 2
3 = corrispondenza del costo 3
B.   MAPICS DB
1 = Corrispondenza del costo STANDARD
2 = Corrispondenza del costo CURRENT
Questa corrispondenza viene usata per modificare facilmente le applicazioni di base quando queste fanno riferimento ad uno dei 2 o 3 costi presenti.
(_9_Esempio  :  nell'attribuzione del costo alle righe ordine per la valorizzazione del WIP)
