# BRZ - Categoria enti
 :  : DEC T(ST) K(BRZ)
## OBIETTIVO
Stabilire i "valori di default" alla creazione di un ente.
## CONTENUTO DEI CAMPI
 :  : FLD T$BRZA **Livello di nascita**
Livello / Stato.
 :  : FLD T$BRZB **Gruppo flag**
Elemento della B£Y.
 :  : FLD T$BRZC **Categoria parametri**
Elemento della C£E per gestione parametri esterni.
 :  : FLD T$BRZD **Contenitore note**
Elemento della NSC per gestione note.
 :  : FLD T$BRZE **Domande costruzione codice**
Elemento della B£F per costruzione automatica del codice.
 :  : FLD T$BRZF **Parametri impliciti**
Elemento della C£I per gestione parametri interni.
 :  : FLD T$BRZG **Rapporto fiscale assunto**
Elemento della BRX per assunzione rapporto fiscale.
 :  : FLD T$BRZH **Mnemonico automatico**
Permette di impostare il campo nome mnemonico in automatico (copiandolo dal campo ragione sociale) se questo non viene impostato.
 :  : FLD T$BRZI **Suff.pgm Ctr campi**
È il suffisso del pgm che permette di gestire controlli specifici in fase di gestione file. Se si usa il data entry V1 il pgm si dovrà chiamare BREN01D_x, mentre nella V2 si dovrà chiamare
BRBR23_x
 :  : FLD T$BRZJ **Codice nazione di default**
È un elemento della tabella V§N Nazioni da utilizzare per default.
 :  : FLD T$BRZK **Condizione tasse 1 obbligatorio**
Se impostato, per la categoria enti in esame, verrà richiesto obbligatorio il campo "condizione tasse 1" (tab. IVA) nella gestione enti (sezione Dati Fiscali).
 :  : FLD T$BRZL **Codice listino default**
È il codice di listino che viene proposto all'inserimento/copia dell'ente.
