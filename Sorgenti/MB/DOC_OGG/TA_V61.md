# V61 - Parametri modulo Rich.offerta
 :  : DEC T(ST) K(V61)

## OBIETTIVO
IN questa tabella vengono inseriti i parametri per la gestione delle gare e offerte di acquisto.
Vengono richiesti i parametri base per la gestione.
per la documentazione dei campi vi rimandiamo alla documentazione specifica di campo.

## SOTTOSETTORI
Non gestiti

## CONTENUTO DEI CAMPI
 :  : FLD T$V61A **Tipo Doc. Rda      **
E' un elemento della tabella V5D ed identifica il tipo documento in cui sono gestite le richieste
di acquisto
 :  : FLD T$V61B **Tipo Doc. Gare e Off**
E' un elemento della tabella V5D ed identifica il tipo documento in cui sono gestite le gare e le
richieste di offerta (di acquisto)
 :  : FLD T$V61C **Modello Gara       **
E' un elemento della tabella V5Axx (xx definito nella tabella del tipo documento delle gare e delle
richieste di offerta) ed indica il modello che viene utilizzato per la gestione delle
gare.
 :  : FLD T$V61D **Modello Offerte    **
E' un elemento della tabella V5Axx (xx definito nella tabella del tipo documento delle gare e delle
richieste di offerta) ed indica il modello che viene utilizzato per la gestione delle richieste di
offerta.
 :  : FLD T$V61E **Stato minimo  input**
Campo facoltativo. E' possibile, tramite questo campo, impostare un limite inferiore, durante la
estrazione delle richieste di acquisto, sullo stato della riga di RDA
 :  : FLD T$V61F **Stato Massimo input**
Campo facoltativo. E' possibile, tramite questo campo, impostare un limite superiore, durante la
estrazione delle richieste di acquisto, sullo stato della riga di RDA
 :  : FLD T$V61G **Stato Output Riga  **
E' lo stato in cui viene impostata la riga della richiesta di acquisto dall'aggiudicazione della
gara (normalmente la chiusura della riga RDA, dopo la quale la riga è pronta per essere trasformata
in ordine)
 :  : FLD T$V61H **Exit Programmi     **
E' un suffiso del programma V5GO01_x (dove x è il contenuto del campo), Con il quale è possibile
impostare delle modifiche nelle varie fasi dell'applicazione
 :  : FLD T$V61I **OAV AR ric. Rda    **
E' un OAV di articolo ed è utilizzato per specificare un oggetto di raggruppamento. Normalmente
l'oggetto con cui vengono raggruppati gli articoli dall'ufficio acquisti
 :  : FLD T$V61L **Flusso Gestione off.**
E' un elemento della tabella B£H con il quale si può impostare un flusso e quindi delle azioni da
legare alla gestione delle offerte (modifica, impostazione prezzi, invio mail ecc.)
 :  : FLD T$V61M **Stato Output Testata**
E' lo stato in cui viene impostata la testata della richiesta di acquisto quando tutte le righe
(RDA) sono almeno allo stato di aggiudicazione GARA
