# Estrattori da archivi Sme.up
Ogni estrattore è costruito con una logica di calcolo specifica, a seconda del contesto di estrazione.
Per ogni estrazione esistono due programmi specifici, nei quali il prefisso xx cambia a seconda dell'archivio di estrazione.
Per convenzione, i programmi con suffisso numerico sono estrattori da archivi Sme.up, quelli con suffisso con primo carattere una X sono personalizzazioni su archivi del cliente. Il suffisso viene specificato nella tabella D9B e, in base alla scelta, viene contestualizzata l'estrazione.

Ogni estrattore è l'insieme di due programmi : 
 * _2_D9AP_xxP,   caratterizza i parametri origine della tabella D9B, specifica gli oggetti principali dell'estrazione su cui costruire le gerarchie, e specifica le intestazioni dei campi dei valori
 * _2_D9AP_xxC,   scandisce l'archivio e restituisce i codici degli oggetti e i valori da passare al Databeacon

Ogni coppia di programmi di estrazione sarà dunque caratterizzato dall'impostazione di : 
 * _2_Parametri origine,  da compilare nella D9B per caratterizzare ogni singola estrazione. Possono essere degli intervalli di date, degli elementi di tabella, o dei valori interni che influenzano l'estrazione
 * _2_Oggetti origine gerarchizzabili,  sono gli oggetti che verranno estratti dall'archivio in questione, ai quali saranno associate da tabella delle aggregazioni (D9C). Possono essere fissi da programma o possono variare a seconda dei parametri origine
 * _2_Oggetti aggiuntivi piatti,  sono gli oggetti che verranno estratti dall'archivio in questione, sui quali non può essere associata alcuna gerarchia, ma potranno essere utilizzati per aggregare gli oggetti origine principali
 * _2_Valori origine,  sono i valori elementari estratti dall'archivio, ai quali potranno essere affiancati altri valori derivati da questi, impostati da tabella (D9D)

_3_NOTA BENE
_3_Inserendo nelle specifiche HD nel programma estrattore D9AP_xxC una buona spiegazione delle logiche implementate nell'estrattore (anche se cliente), queste sarano fruibili come Help sia da questa documentazione che dall'help della tabella D9B.

# ELENCO ESTRATTORI PRESENTI (numerici = Standard; Xn = Personalizzati)
(_N.B., L'elenco viene presentato solo in emulazione 5250 nativa)
 Per un maggiore dettaglio della specificità degli estrattori utilizzare l'opzione HE in prossimità dell'estrattore (solo via client access). Questa funzione di Help è accessibile anche da help D9B.

 :  : DEC T(OJ) P(*PGM) K(D9AP_[V3.PFC]C) I( Estrattore Cubo >>)

# Modello estrattore da archivio del Cliente
Programmi estrattori da creare :  D9AP_xxP, D9AP_xxC

Il suffisso xx è un contatore che deve assumere i valori da X1 fino a XZ

## PGM parametri :  D9AP_xxP
In questo programma si fanno le seguenti dichiarazioni : 
 * Parametri origine compilabili dalla tabella D9B (schiera e DS)
 * Oggetti su cui associare una gerarchia da tabella D9C
 * Campi piatti da usare come aggregazione
 * Dichiarazione intestazione valori e numero valori

## PGM estrazione D9AP_xxC
In questo programma si scandisce e si riempe il file di estrazione : 
 * Riempire i campi codice oggetti gerarchizzabili dichiarati (schiera £9K)
 * Riempire i campi codice oggetti piatti dichiarati (schiera £9A)
 * Riempire i campi valore dichiarati (schiera £9I)
 * Gestione dei filtri e degli effetti dei parametri origine

# Schedulazione Estrazioni
Per lanciare estrazioni schedulate, basta fare una call al programma _2_D9AP00A (menu D900 "lancio estrazioni) con parametro 1 il nome della memorizzazione video contenente tutti i parametri di lancio selezionati e parametro 2 il nome cubo da estrarre se non già presente nella memorizzazione.

Per schedulare, utilizzare il comando _2_WRKJOBSCDE, e aggiungere il lavoro con il tasto funzione F6.
Compilare i campi necessari e impostarne la cadenza.
In alternativa utilizzare le azioni delle ACG o di qualche altro modulo base.
Importante la call al programma e la descrizione del lavoro.

Esempio sintassi comando aggiunta lavoro : 
Per aggiungerlo : 
>===> ADDJOBSCDE JOB(CUBONC) CMD(CALL PGM(D9AP00A) PARM('TACUB4')) FRQ(*WEEKLY) SCDDATE(*NONE) SCDDAY(*MON *TUE *WED *THU *FRI) SCDTIME(113000) JOBD(SMECUBO) JOBQ(*JOBD) USER(TA) TEXT('Prova schedulazione cubo')


Questo comando aggiungerà un lavoro che estrarrà secondo i parametri della memorizzazione video TACUB4, dal lunedi al venerdi alle 11,30, utilizzando l'utente TA e la descrizione lavoro (JOBD)
 _2_SMECUBO

Per gestirlo successivamente utilizzare : 
_2_WRKJOBSCDE
