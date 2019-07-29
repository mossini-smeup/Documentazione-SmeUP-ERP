# V5G - Tipo attività
 :  : DEC T(ST) K(V5G)
## OBIETTIVO
Definire le modalità con cui si effettuano i passaggi interattivi da un tipo documento all'altro (ad esempio, da ordini clienti a bolle, da previsioni a ordini, ecc..)
## OBBLIGATORIETÀ CAMPI
Il tipo documento d'arrivo è sempre obbligatorio.
Il tipo documento di partenza è obbligatorio nel caso in cui si esegua un'estrazione da documento.
L'area ed il tipo giacenza sono obbligatori nel caso in cui si esegua un'estrazione da magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Identifica il codice del tipo attività.
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5GA __Tipo Doc.Partenza__
È un elemento della tabella V5D. Identifica il tipo documento da cui verranno estratti i documenti.
 :  : FLD T$V5GJ __Modello Doc.Partenza__
Opzionale. È un elemento della tabella V5A. Identifica il modello del documento da cui verranno estratti i documenti.
Se impostato, funge da parzializzatore/limitatore dei documenti di partenza.
 :  : FLD T$V5GK __Tipo Riga Partenza__
Opzionale. È a cura del compilatore impostare un elemento significativo (infatti il sottosettore non è, a priori, individuabile).
Se impostato, funge da parzializzatore/limitatore delle righe di partenza (è presentato ma non è modificabile nella scelta di dettaglio dell'estrazione).
 :  : FLD T$V5GB __Tipo Doc.Arrivo__
È un elemento della tabella V5D. Identifica il tipo documento con cui verranno scritti i documenti.
 :  : FLD T$V5GG __Modello Doc.Arrivo__
È un elemento della tabella V5A. Identifica il modello del documento con cui verranno scritti i documenti.(N.B. l'impostazione del modello di destinazione dipende anche dall'impostazione dei parametri del flusso)
 :  : FLD T$V5GC __Flusso Azioni__
È un elemento della tabella B£H. Identifica la sequenza di azioni (flusso) con cui verrà eseguita questa transazione.
 :  : FLD T$V5GE __Area Giacenza__
È un elemento della tabella GMR. Qualora l'origine della transazione sia un'area di magazzino, lo si definisce in questo campo.
 :  : FLD T$V5GF __Tipo Giacenza__
È un elemento della tabella GMQ. Insieme con l'area giacenza, definsice l'origine della transazione, qualora sia un'area di magazzino.
 :  : FLD T$V5GM __Eredità tipo riga__
- ' '  :  Il tipo riga del documento di arrivo sarà quello definito nel tipo riga destinazione del documento origine;
- '1'  :  Il tipo riga del documento di arrivo sarà quello definito dal tipo riga assunto nel modello di destinazione;
- '2'  :  Il tipo riga del documento di arrivo sarà quello definito nel tipo riga destinazione del documento origine se specificata, altrimenti sarà quello definito dal tipo riga assunto nel modello di destinazione.
 :  : FLD T$V5GN __Esegui 1 Solo flusso__
Se inserito '1' nel campo, viene eseguito il flusso UNA sola volta, dopodiché il programma viene chiuso.
 :  : FLD T$V5GH __Gruppo Fonti__
È un elemento di memorizzazione che raggrruppa i magazzini (se applicazione multimagazzino), le fonti presenti e/o future, che forniranno un valore di giacenza/disponibilità degli articoli in esame, a cui potranno accedere le funzioni di estrazioni (ciascuna secondo le proprie modalità).
 :  : FLD T$V5GI __Tipo ente/Ente__
Se specificati entrambi. Il flusso viene eseguito unicamente per l'ente indicato.
 :  : FLD T$V5GL.T$V5GI Ente
