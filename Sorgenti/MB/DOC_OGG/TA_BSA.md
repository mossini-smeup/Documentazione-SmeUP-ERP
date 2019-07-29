# BSA - Tipo commessa
 :  : DEC T(ST) K(BSA)
## OBIETTIVI
-    Caratterizzare la tipologia delle commesse in modo da poterla utilizzare per impostare comportamenti e classificazioni comuni a commesse dello stesso tipo
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
Per ogni tipo commessa si possono definire caratterizzazioni che verranno utilizzate per tutte le commesse dello stesso tipo
## CONTENUTO DEI CAMPI
 :  : FLD T$BSAA **Natura commessa**
È un elemento fisso V2/NACOM e definisce in modo univoco la natura della commessa :  se è produttiva, se è ausiliaria alla produzione, se è di servizi generali.
 :  : FLD T$BSAB **Tipo ente**
È un elemento della tabella BRE. Definisce il tipo ente a cui si assegneranno le commesse di questo tipo.
 :  : FLD T$BSAC **Tipo/parametro oggetto di riferimento**
Individuano il tipo di oggetto a cui si intesteranno le commesse di questo tipo.
 :  : FLD T$BSAE **Tipo/parametro oggetto di riferimento**
Individuano il tipo di oggetto che individua il responsabile per le commesse di questo tipo.
 :  : FLD T$BSAG **Tipo/parametro oggetto per controllo di gestione**
Individuano il tipo di oggetto che costituisce l'aggregazione nel controllo di gestione per le commesse di questo tipo.
 :  : FLD T$BSAI **Livello di nascita**
Se, in inserimento della commessa, non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$BSAJ **Gruppo flag**
È un elemento della tabella B£Y. Se valorizzato, all'atto dell'inserimento della commessa, vengono assegnati i flag di questo elemento.
 :  : FLD T$BSAK **Priorità assunta**
È un elemento della tabella B§A che viene proposto all'atto dell'inserimento della commessa.
 :  : FLD T$BSAL **Categoria parametri**
È un elemento della tabella C£E che definisce i parametri esterni collegabili alla commessa.
 :  : FLD T$BSAM **Parametri impliciti**
È un elemento della tabella C£I che definisce i parametri collegabili alla commessa, contenuti all'interno dell'archivio.
 :  : FLD T$BSAN **Contenitore note**
È l'elemento della tabella NSC che contiene le note delle commesse di questo tipo.
 :  : FLD T$BSAO **Numeratore commesse**
È l'elemento della tabella CRN (sottosettore CM) che viene usato per assegnare il numero alla commessa.
 :  : FLD T$BSAP **Suff.Pgm Aggiustam.**
È il suffisso del pgm BRCM01D_x
 :  : FLD T$BSAQ **Domande costruzione codice**
È un elemento della tabella B£F e rappresenta il flusso di domande che sovrintende alla costruzione del codice e della descrione di commesse di questo tipo.
