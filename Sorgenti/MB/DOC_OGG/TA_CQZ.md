# CQZ - Tipo richiesta intervento
 :  : DEC T(ST) K(CQZ)
## OBIETTIVO
Classificare le tipologie delle richieste di intervento.
Associare ad ogni tipologia di richiesta il profilo di posizione ottimale, a cui il responsabile per l'assegnazione delle richieste dovrebbe riferirsi nella scelta della persona responsabile per l'evasione.
Personalizzare le descrizioni dei campi in funzione della tipologia delle richieste di intervento.
Definire il contenitore delle note strutturate da utilizzare per il tipo di richiesta specifico
## CONTENUTO DEI CAMPI
 :  : FLD T$LIST **Tipo lista distribuzione**
Lista di distribuzione da utilizzare. Questo campo è controllato nella tabella NSL. Viene utilizzato nella gestione della distribuzione delle richieste attraverso il videoterminale.
 :  : FLD T$PRPO **Profilo Posizione**
Campo controllato dalla tabella 'CQ*DA' (Personale - Profilo posizione). Se tale campo è diverso da 'blank' allora, nella fase di assegnazione del RESPONSABILE PER L'EVASIONE, ponendo 'DI' e la richiesta '/', il programma evidenzia tutti i dipendenti che hanno una valutazione per tale profilo.
 :  : FLD T$TIEN **Tipo Ente Designato**
Campo controllato dalla tabella '*CNTT' (Codici oggetti applicativi). Se tale campo è diverso da 'blank' allora, nella fase di assegnazione dell'ENTE DESIGNATO, il programma propone tale valore.
 :  : FLD T$COEN **Codice Ente Designato**
Campo non controllato. Se tale campo è diverso da 'blank' allora, nella fase di assegnazione del secondo campo dell'ENTE DESIGNATO, il programma propone tale valore.
 :  : FLD T$RAPD **Definiz.Campo Z§RAPP**
Campo controllato dalla tabella 'CQ*QZ' (Descrizione valori richieste). Tale campo assegna il significato del contenuto del campo Z§RAPP del file della gestione richieste di intervento.
 :  : FLD T$AOBD **Definiz.Campo Z§AOBB**
Campo controllato dalla tabella 'CQ*QZ' (Descrizione valori richieste). Tale campo assegna il significato del contenuto del campo Z§AOBB del file della gestione richieste di intervento.
 :  : FLD T$FDBD **Definiz.Campo Z§FDBK**
Campo controllato dalla tabella 'CQ*QZ' (Descrizione valori richieste). Tale campo assegna il significato del contenuto del campo Z§FDBK del file della gestione richieste di intervento.
 :  : FLD T$NOTS **Contenitore note**
Campo controllato dalla tabella 'NSC' (Contenitori note strutturate). Tale campo definisce il contenitore utilizzato per il tipo di richiesta specifico. Se questo campo non viene compilato verrà utilizzato per default il contenitore 'RIN'.
 :  : FLD T$CQZA **Giorni a scadere**
Campo numerico che indica il numero di giorni antecedenti alla data di scadenza durante i quali
verrà evidenziata l'azione correttiva.
