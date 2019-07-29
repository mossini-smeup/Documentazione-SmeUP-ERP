# BRA - Tipi articoli
## OBIETTIVI
Caratterizzare la tipologia degli articoli per poterla utilizzare per impostare comportamenti comuni agli articoli dello stesso tipo
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
Per ogni tipo articolo si possono definire caratterizzazioni che verranno utilizzate per tutti gli articoli dello stesso tipo
 :  : DEC T(ST) K(BRA)
## CONTENUTO DEI CAMPI
 :  : FLD T$BRAD **Domande per configurazione**
Sono gli elementi di un sottosettore della tabella C£D e rappresentano le domande a cui bisogna rispondere per definire la configurazione di un articolo del tipo trattato.
 :  : FLD T$BRAE **Domande costruzione codice**
È un elemento della tabella B£F e rappresenta il flusso di domande che sovrintende alla costruzione del codice (ed eventualmente alle altre caratteristiche) di un articolo di questo tipo.
 :  : FLD T$BRAC **Classe materiale assunta**
È un elemento della tabella CLS. Viene proposta all'atto dell'inserimento degli articoli di questo tipo.
 :  : FLD T$BRAF **Classe programmazione assunta**
È un elemento della tabella BRO. Viene proposta all'atto dell'inserimento degli articoli di questo tipo.
 :  : FLD T$BRAQ **Sviluppo quantità assunto**
È un elemento della tabella C£Q e rappresenta le variazioni in quantità che l'articolo puo subire.
Ad esempio :  si pensi ad un articolo che può essere ordinato in diverse taglie (le scarpe o le camicie) per cui è utile definire diversi sviluppi di quantità per diversi tipi articoli (scarpe e camicie hanno taglie diverse).
 :  : FLD T$BRAP **Criterio Configurazione assunto**
È un elemento della tabella BRC. Viene proposta all'atto dell'inserimento degli articoli di questo tipo.
 :  : FLD T$BRAU **Unità di misura assunta**
È un elemento della tabella UMS. Viene proposta all'atto dell'inserimento degli articoli di questo tipo.
 :  : FLD T$BRAN **Contenitore note**
È un elemento della tabella NSC. Se impostato, è il contenitore delle note degli articoli di questo tipo. Se non impostato, gli articoli di questo tipo useranno il contenitore 'AR'.
 :  : FLD T$BRAM **Categoria parametri esterni**
È un elemento della tabella C£E. Se impostato, è la categoria di parametri che si possono associare agli articoli di questo tipo. Se non impostato, gli articoli di questo tipo non avranno parametri associati.
 :  : FLD T$BRAG **Categoria parametri interni**
È un elemento della tabella C£I. Definisce il come sono gestiti i parametri che descrivono i campi liberi (5 alfanumerici e 5 numerici) contenuti nell'archivio articoli di questo tipologia.
 :  : FLD T$BRAO **Livello di nascita**
È un elemento della tabella B£W00 :  gli articoli di questo tipo nasceranno con il livello qui impostato, e con ilprimo stato di questo livello.
Se è impostato lo stato di nascita il livello viene determinato da questo stato
 :  : FLD T$BRAS **Stato di nascita**
È un elemento della tabella B£WAR :  gli articoli di questo tipo nasceranno con questo stato.
Se è impostato lo stato di nascita il livello viene determinato da questo stato
 :  : FLD T$BRAI **Codice Iva assunta**
È un elemento della tabella IVA. Viene proposta all'atto dell'inserimento degli articoli di questo tipo.
 :  : FLD T$BRAB **Escluso da magazzino**
Se impostato, gli articoli di questo tipo vengono esclusi dalla movimentazione di magazzino.
 :  : FLD T$BRAZ **Codice EAN(Barcode)**.
Se impostato, esegue il controllo del codice EAN secondo le seguenti modalità : 

- '0' o bianco - Nessun controllo.
- '1'          - Controllo sintassi.
- '2'          - Se blank costruzione automatica, controllo sintassi EAN-8.
- '3'          - Se blank costruzione automatica, controllo sintassi EAN-13.
- '4'          - Se blank costruzione automatica, controllo sintassi EAN-8, ammessa forzatura errore.
- '5'          - Se blank costruzione automatica, controllo sintassi EAN-13, ammessa forzatura errore.

>Nota : 
La costruzione automatica è definita tramite la tabella EAN per il codice assegnato dall'autorità nazionale di codifica e la tabella CRN, sottosettore definito nella stessa tabella EAN per l'assegnazione del progressivo.
I numeratori definiti nella tabella CRN dovranno avere come codice elemento rispettivamente il valore EAN8 e EAN13.
Nei casi di costruzione automatica, in immissione o copia articolo, se viene generato un codice duplicato la generazione viene reiterata fino all'ottenimento di un codice univoco.
 :  : FLD T$BRAA **Suffisso Pgm Aggiustamento**
_9_Se utilizzata versione 1 gestione articoli (senza visualizzatore)
È il suffisso del pgm BRAR01D_x :  permette di gestire controlli e impostazioni personalizzate durante la gestione dell'anagrafico articoli (Es BRAR01D_Z).
_9_Se utilizzata versione 2 gestione articoli (con visualizzatore)
È il suffisso del pgm BRAR02C_x :  permette di modificare la tipologia degli oggetti dei campi presenti nel tracciato (per esempio vedi BRAR02C_A).
 :  : FLD T$BRAH **Griglia riclassifica**
Indica l'elemento della B£G che guida alla tipologia dei 3 campi di riclassifica liberi.
 :  : FLD T$BRA1 **Disatt.art. in GrDi**
L'interfaccia articoli assume come default(se non presente) nel gruppo distinta il codice articolo.
Con questo flag è possbile disattivare questa assunzione, in modo che se non valorizzato nell'  ananagrafica il gruppo distinta venga restituito vuoto dall'interfaccia.
 :  : FLD T$BRAK **Tipo date implicite**
Indica il prefisso degli elementi della tabella C£JAR che guidano la gestione delle 5 date implicite
 :  : FLD T$BRAV **Forma presentazione**
È significativo se è stata impostata in tabella BR1 il flag di visualizzatore su articoli.
È un elemento della tabella B£Q, in cui si indica il programma di visualizzazione utilizzato per gli articoli di questo tipo.
 :  : FLD T$BRA2 **Disatt.art. in GrCi**
L'interfaccia articoli assume come default(se non presente) nel gruppo ciclo il codice articolo.
Con questo flag è possbile disattivare questa assunzione, in modo che se non valorizzato nell'  ananagrafica il gruppo ciclo venga restituito vuoto dall'interfaccia.
