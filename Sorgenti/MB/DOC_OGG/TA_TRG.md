# TRG - Tipo risorsa gestita
 :  : DEC T(ST) K(TRG)
## OBIETTIVO
Permettere di catalogare le risorse per le quali si vuole definire la disponibilità. Tipicamente avremo, come tipo di risorsa, il centro di lavoro ma potremo anche definire la risorsa macchina oppure i dipendenti. Ciò consente di generalizzare la funzione di definizione della disponibilità risorse.
## UTILIZZO
Utilizzata in tutte le funzioni del calendario. Deve essere specificato l'elemento ogni volta che si richiama l'analisi disponibilità.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$CODR __Tipo oggetto risorsa__
Il tipo e il parametro oggetto risorsa definiscono l'oggetto intestatario (del calendario base e delle eccezioni) dei calendari di questo tipo risorsa.
 :  : FLD T$PATO.T$CODR __Parametro oggetto risorsa__
 :  : FLD T$CORS __Tipo risorsa superiore__
Se manca il calendario annuale per il tipo risorsa di base, viene letto il calendario annuale di questo tipo risorsa.
 :  : FLD T$TRGA __Tipo risorsa deviata__
Va compilato insieme all'OAV di deviazione.
Se presente, viene usato nella risalita per il reperimento dei dati settimanali e delle eccezioni.
Si deve fare attenzione che il tipo oggetto definito in questo tipo risorsa sia congruente con l'oggetto dell'OAV.
 :  : FLD T$TRGB __OAV di deviazione__
Va compilato insieme al tipo risorsa deviata.
Se presente, viene usato nella risalita per il reperimento dei dati settimanali e delle eccezioni.
Deve essere un OAV dell'oggetto di questo tipo risorsa :  è un oggetto di tipo 'OA' e di parametro =  "tipo + parametro risorsa".
 :  : FLD T$TRGC __Eccezioni di default__
Impostando questo flag, nella risalita eccezioni, si considerano anche le eccezioni dell'anno 3000, con questa sequenza (NB :  ogni elemento successivo, se presente, sostituisce il precedente, nei campi non blanks del primo).
Un utilizzo dell'eccezione di default è la possibilità di definire che, nel calendario collegato ai pagamenti, un cliente è sempre chiuso per tutto il mese di agosto.
Si possono impostare due criteri di risalita : 
>**Risalita '1'**
    __Risorsa__        __Anno__
    "**"           3000
    Collegata      3000
    Deviata        3000
    Risorsa        3000
    "**"           Anno
    Collegata      Anno
    Deviata        Anno
    Risorsa        Anno


>**Risalita '2'**
    __Risorsa__        __Anno__
    "**"           3000
    "**"           Anno
    Collegata      3000
    Collegata      Anno
    Deviata        3000
    Deviata        Anno
    Risorsa        3000
    Risorsa        Anno


 :  : FLD T$TRGD __Calendario base__
Se si imposta il flag di calendario base, viene assunto il seguente comportamento :  nella creazione cieca e nell'inserimento di un nuovo anno, esso non viene creato vuoto, ma prendendo le informazioni dal calendario base dell'anno 3000, se presente (del tipo risorsa definito nel campo 'Tipo risorsa calendario base', oppure, se a blanks, del tipo risorsa che si sta trattando).
In questo modo si può costruire un calendario con impostate le chiusure comuni a tutti gli anni (festività civili e religiose fisse).
 :  : FLD T$TRGE.T$TRGD __Tipo risorsa calendario base__
 :  : FLD T$TRGF __Sviluppo squadre__
Se si imposta questo campo, le risorse di questo tipo sono "squadre", con la possibilità di caratterizzarle con un numero di risorse, variabile anche all'interno dello stesso giorno.
