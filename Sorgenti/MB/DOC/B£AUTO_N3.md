# AUTORIZZAZIONI PER OGGETTO - NOTE TECNICHE

L'archivio su cui si basa questa funzione è AUTOOG0F
AO£CLA     Classe autorizzazione
AO£TIP     Tipo oggetto
AO£PAR     Parametro oggetto
AO£COD     Codice oggetto
AO£ATT     Attributo
AO£VAL     Valore attributo
AO£GRA     Funzione

Il logico 0L coincide con l'archivio
Il logico 1L ha come primo campo il codice oggetto, ed i rimanenti uguali a 0L.


**Prerequisiti**
- Nuovo logico AUTOOG1L
- Replica R di B£OAV0



# UTILIZZO

Le autorizzazioni per oggetto possono essere utilizzate attraverso la /COPY £AUO, la quale si rimanda alla corrispondete documentazione.

- [TST Copy autorizazioni](Sorgenti/MB/DOC_OGG/P_TSTAUO)

A seguire si riporta la documentazione tecnica che programma che sottostà alla £AUO.

# DESCRIZIONE FUNZIONAMENTO
Il programma che ritorna l'autorizzazione è B£AUA6F (Funizzato)

**Nomenclatura**
- Classe - Elemento della B£P (Tabella classe di autorizzazione)
- Oggetto - Classe dell'oggetto da autorizzare (Es :  CNCLI, AR, mentre ARTIP e CN non sono validi :  il parametro è obbligatorio se lo è per la classe, e obbligatoriamente nullo se facoltatico).
- Istanza - Istanza dell'oggetto da autorizzare
- OAV  codice dell'OAV da autorizzare (I/01, J/02)
-- Implicito - se non è presente il valore (AO£VAL),  l'OAV deve restituire la funzione su cui testare il le autorizzazioni (il campo AO£GRA deve essere valorizzato con '**')
-- Esplicito - se è presente il valore (AO£VAL), in base alla corrispondenza tra l'OAV e il valore indicato utilizza la funzione indicata sul campo AO£GRA
- Valore - valore dell'OAV
- Gruppo - gruppo per protezione (in base alla classe)

**Riceve**
£FUNT1/£FUNP1/£FUNK1
(obbligatori) oggetto da autorizzare
£FUNK2 (Classe) facoltativa
£FUNK3 (Utente) facoltativo (se assente assume utente del lavoro) :  serve per simulazioni

**Ritorna**
£FUNK4  :  i valori £AU1(x) definiti dalla classe, gruppo e utente.
I valori £AU1(x) sono di tipo V2AUTOG.
Se impostato un numero da 1 a 3 in £FUNNR ritorna £AU1(£FUNNR).
Altrimenti ritorna, consecutivamente :  £AU1(1); £AU1(2); £AU1(3), ciascuno per due posizioni.

£FUNP2  :  ritorna la classe utilizzata per eseguire la £AUAC1
£FUNK5  :  ritorna l'origine del reperimento (V2AUTOO)
£FUNPS  :  ritorna la funzione usata per eseguire la £AUAC1
£FUNW2  :  ritorna la classe, la funzione e l'utente restituiti dalla £AUAC1 (£AUAOR/OA/OU)

**Procedimento**
Se l'oggetto non è gestito (in AUTOOG0F) torna subito blanks.

Se NON riceve la classe assume la prima (in ordine alfabetico) presente nel file per l'oggetto ricevuto.
Se viene ricevuta la classe e questa non c'è, torna subito blanks.

A questo punto la classe è fissata, e si deve determinare la funzione.

Le successive condizioni vengono verificate in cascata :  alla prima soddisfatta esce.

Se l'istanza ricevuta è presente, la funzione è quello impostata sul record dell'istanza.

Se trova OAV espliciti (con AO£VAL valorizzato), assume la funzione del primo valore che se soddisfa la condizione :  in pratica tratta questi OAV in OR.

Se trova OAV impliciti  (con AO£VAL uguale blanks)  se AO£GRA  è uguale a '**' assume come funzione il valore dell'OAV  del primo che trova. E' quindi inutile codificare più di un OAV implicito.

Sia nel caso di OAV impliciti che espliciti, se AO£GRA  contiene '**', '**' viene sostituito con il valore dell'OAV.

Se non è riuscito a determinare una funzione, assume quella definito nel record con la sola classe (se presente), altrimenti assume funzione blanks.

A questo punto ha la classe, la funzione e l'utente e quindi ricava l'autorizzazione, con la routine £AUAC1.










