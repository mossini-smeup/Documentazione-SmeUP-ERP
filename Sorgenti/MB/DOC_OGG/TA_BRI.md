# BRI - Tipi estensioni contatti
 :  : DEC T(ST) K(BRI)
## OBIETTIVI
Definisce le caratteristiche dei tipi estensione (archivio BRESCO0F).
## ELEMENTI STANDARD

Alcuni elementi sono predefiniti a standard, di seguito ne viene riportato l'elenco. La configurazione di tali elementi è disponibile dal file modello delle tabelle.

 - _2_£01 Indirizzi di spedizione. Permette di estendere gli indirizzi di spedizione (è direttamente collegato ai campi dell'anagrafica E§TSPE/E§CSPE). Rappresenta i soggetti a cui spedire la merce.
 - _2_£02 Indirizzi di contabilizzazione. Permette di estendere gli indirizzi di contabilizzazione (è direttamente collegato ai campi dell'anagrafica E§TCON/E§CCON). Rappresentano i soggetti a cui fatturare (es. l'azienda intestataria della bolla fa parte di un gruppo aziendale, ed il pagamento viene effettuato dalla holding del gruppo).
 - _2_£03 Indirizzi di conferma. Permette di estendere gli indirizzi di conferma (è direttamente collegato ai campi dell'anagrafica E§TCIN/E§CINC). E' legato agli ordini, un soggetto fa l'ordine, ma un'altro lo devo confermare (un esempio è il sopracitato caso del gruppo aziendale).
 - _2_£04 Indirizzi di tratt. prezzo. Permette di estendere gli indirizzi di tratt.prezzo (è direttamente collegato ai campi dell'anagrafica E§TPRZ/E§CPRZ).
 - _2_£05 Indirizzi di corrispondenza. Permette di estendere gli indirizzi di corrispondenza (è direttamente collegato ai campi dell'anagrafica E§TCRR/E§CCRR).
 - _2_£06 Indirizzi di vettore. Permette di estendere gli indirizzi di vettore (è direttamente collegato ai campi dell'anagrafica E§TVET/E§CVET). Rappresentano i soggetti che possono eseguire il trasporto.
 - _2_£07 Modelli ammessi. Ha lo scopo definire i vari modelli disponibili o non disponibili per un tipo documento su un ente.
 - _2_£08 Param. fatturazione. Ha lo scopo di indicare il calendario fatturazione e n° copie della fattura.
 - _2_£09 Partite IVA. Per chi non attiva la gestione dei data-effective direttamente sull'anagrafico permette di definire le modifiche per partita IVA sulla data.
 - _2_£10 Home page internet. Definisce le pagine internet collegate all'ente.
 - _2_£11 Documenti/Allegati specifici. Elenco dei documenti accompagnatori (TAV5C).
 - _2_£12 Percorsi validi. Elenco dei percorsi validi (TAV5W).
 - _2_£13 Lettere di esenzione.
 - _2_£14 Dati specifici per modello. Elenco per TAV5A per i quali posso inserire dati specifici del modello (es. codice pagamento spese assoggettamento ecc.).
 - _2_£15 Vettori e Agenti Aggiuntivi.
 - _2_£16 Indirizzi E-MAIL. Definisce gli indirizzi mail collegati all'ente.
 - _2_£17 Contropartite contabili. Definisce le contropartite usuali di un fornitore (se non è previsto il controllo bolle fatture passivo).
 - _2_£18 Numero R.I.D.. Definisce il numero di R.I.D. se previsto.
 - _2_£19 Indirizzo Alternativo Riba. Definisce l'indirizzo da indicare nella trasmissione delle riba attive.
 - _2_£20 Calendario alternativo. Definisce una fonte di calendario alternativa rispetto a quella prevista dal tipo contatto.
 - _2_£21 Coordinate bancarie. Permette di estendere le coordinate bancarie utilizzabili sull'ente.
 - _2_£22 Piano campionamento forzato.
 - _2_£23 Livello camp. forzato.
 - _2_£24 C.F.It.per non resid. mod. 770. Codice fiscale interno per non residenti utilizzato in 770.
 - _2_£25 MSN messenger.
 - _2_£26 S.I.P..
 - _2_£27 Indirizzo IP.
 - _2_£28 Skype.
 - _2_£29 Matricola Enasarco. Per un soggetto che è un'agente permente di indicarne il n° matricola Enasarco.
 - _2_£30 Azienda Intercompany.
 - _2_£31 Tipo Ente Cessione. Definisce il soggetto a cui vengono ceduti i crediti intestati all'ente. I bonifici bancari verranno intestati perciò a questo ente.
 - _2_£32 Codice Agente (per fornitore).
 - _2_£33 Società.
 - _2_£34 Parametri spedizione/consegna.
 - _2_£35 Sede Amministrativa.
 - _2_£40 Dati Persona Fisica. Definisce i dati specifici della persona fisica.
 - _2_£41 Dati Percipiente. Definisce i dati specifici di percipiente.


## CONTENUTO DEI CAMPI
 :  : FLD T$BRIA **Estens. a Elem.fisso**
Indica (se inserito il carattere 1) che il codice di accesso è '*' ed è fisso, questo tipo di estensione è singolo.
 :  : FLD T$BRIT **Tipo codice**
Se il campo precedente è lasciato bianco identifica l'oggetto da inserire nell'estensione.
 :  : FLD T$BRIP **Parametro codice**
È il parametro aggiuntivo dell'oggetto specificato nel campo precedente.
Se valorizzato propone la tipologia di contatto in immissione dell'estensione.
 :  : FLD T$BRIS **Significato codice**
È la descrizione del tipo oggetto specificato precedentemente.
 :  : FLD T$BRIN **Nome programma**
C'è la possibilità di indicare un programma per la gestione specifica dell'estensione (per un esempio, vedi BRESXXX).
 :  : FLD T$BRIB **Tipo chiave ricerca**
È un campo di due posizioni :  la prima posizione definisce il contenuto delle chiavi dei parametri; la seconda posizione identifica la modalità di risalita nella ricerca delle informazioni. Le composizioni e le risalite numeriche hanno significati definiti e sono fornite da SMEUP; esiste la possibilità di creare delle composizioni e delle risalite personalizzate utilizzando delle lettere; in questo caso le chiavi vengono composte da un programma esterno che si chiamerà BRBRR_XY, dove XY è la modalità personale del cliente.
_Modalità standard_
- 1° posizione :  Composizione
- 2° posizione :  Risalita

_Risalita_
Key1     Key2
' '  :  Nessuna risalita
'1'  :  Generalizza Key1                   **
'2'  :  Generalizza Key2                            **
'3'  :  Generalizza Key1+Key2              **       **
Composizione   key1            key2
' '  :           Articolo        Tipo ciclo+ciclo+fase+val.iniz.
'1'  :            ""                 ""        ""       ""
'2'  :           Articolo        Risorsa
'3'  :           Articolo        Operazione
 :  : FLD T$BRIC.T$BRIB
 :  : FLD T$BRIE **Obbl.codice Ricerca**
Se impostato (e presente tipo chiave ricerca) rende obbligatorio la chiave ricerca.
 :  : FLD T$BRIF **Stato Non Significativo**
Se valorizzato, da indicazione del fatto che i campi livello/stato non sono significativi per l'estensione
