# Opportunità
## Definizione
 :  : I.INC.MBR Fil(DOC_VOC) Mem(REBASE_GLO) Sec( :  : VOC) SAt(008)

## Schema relazioni
![X1MARK06A](http://localhost:3000/immagini/REOPPO_01/X1MARK06A.png)## Dati
* Codice identificativo
* Date apertura / chiusura attesa / scadenza
* Responsabile
* Account
* Referente
* Ricavi stimati per linea prodotto e natura
* Tipo (forecast, account planning)
* Programma di vendita
* Probabilità di chiusura
* Lead origine

![X1MARK0602](http://localhost:3000/immagini/REOPPO_01/X1MARK0602.png)
## Dati New

I dati relativi alle opportunità riesiedono su tre file : 
* BRCOMM0F file primario che definisce l'opportunità, in quanto oggetto CM
* V5TDOC0F estensione del BRCOMM0F per info di testata. Assume come numero documento la commessa M$COMM, Solo se presente il tipo documento nella tabella "RE1".
* V5RDOC0F estensione del BRCOMM0F per info di righe. Prodotti dell'opportunità.

Campi specifici testata
* Codice, è il codice dell'opportunità (M$COMM)
* Descrizione. è la descrizione dell'opportunità (M$DECM)
* Stato, è lo stato in cui si trova l'opportunità (M$STAT, con M$LIVE derivato)
* Data ricezione, è la data in cui è stata ricevuta l'opportunità o data apertura (M$DT01)
* Data accettazione, è la data in cui è stata accettata l'opportunità (M$DT02)
* Data scadenza, è la data in cui scadrà l'opportunità o data chiusura (M$DT03)
* Assegnata a, è la persona a cui  stata assegnata l'opportunità (M$TIRE, M$PARE, M$CDRE, oggetto "TAB£U")
* Tipo, è il tipo opportunutà (M$COD1, oggetto "TAY0001")
* Fase è la fase in cui si trova l'opportunità (M$COD2, oggetto "TAY0002")
* Milestone, indica se è milestone (M$FL10, oggetto "V2SI/NO")
* In appoggio, indica se è un'opportunità segnalata da un esterno (M$FL11, oggetto "V2SI/NO")
* Cliente, è il cliente finale dell'opportunità (M$TIEN, M$COEN e contemporaneamente T§TCCL, T§CDCL, tipo ente "CLI")
* Filiale di, è la filiale del cliente (T§COD1, tipo ente "CLI")  - SIMES T§CODS
* Referent del cliente, è il referente dell'opportunità presso il cliente (M$COD4 oggetto "RN")
* Cantiere, è la sede in cui si sviluppa l'opportunità (T§TCDS, T§CODS tipo ente "IDO"). Ogni opportunità ha il suo cantiere. Il tipo ente è fisso "IDO".  Il codice ente è fisso e costruito come XXYYZZZZZZZZZZ dove XX è l'azienda, YYY il T§TDOC, e ZZZZZZZZZ T§NDOC . La gestione degli indirizzi di spedizione permette di inserire i dati geografici del cantiere. - SIMES M$CD07, e R§TCDS=IDO e R§CODS
* Probabilità di chiusura, è un valore numerico che indica la probabilità di chiusura dell'opportunità (M$NUM1)
* Importo, è un valore che indica l'importo dell'opportunutà (M$NUM2)
* Valuta, è la valuta di riferimento dell'importo. (M$COD3 e T§VALU)
* Agenzia, è l'agenzia che ha segnalato l'opportunità (T§COD2 tipo ente "CLI")
* Agente, è l'agente dell'agenzia che ha segnalato l'opportunità (T§AGE1 oggetto "TAAGE")

Campi specifici riga
* Riga, numero ri riga (R§NRIG)
* Stato, è lo stato della riga (R§STAT). Tra gli stati è importante rilevare lo stato di protezione. Significa che non è possibile creare una nuova opportunià sullo stesso prodotto.
* Fornitore, è il fornitore da cui i acquisterà il prodotto presente nella riga dell'opportunità R§TCED, R§CDED tipo ente "FOR")
* Articolo, è il prodotto di riga dell'opportunità (R§CDOG oggetto "AR")
* Descrizione, è la descrizione del prodotto presente nella riga di opportunità (R§DSOG). All'immissione di un nuovo articolo assume di default la descrizione dell'articolo. E' poi pssibile modificarla.
* Descrizione aggiuntiva. è una descrizione aggiuntiva dell'articolo (R§DSO2). Stesso compprtamento della "Descrizione".
* Unità di misura, è l'unità di misura con cui si vende il prodotto (R§UNMV). Unità di misura esterna. Il sistema in automatico carica anche l'unità di misura interna (R§UNMS) derivata dall'anagrafica articoli.
* Quantità, è la quandità richiesta per il prodotto (R§Q01V). Espressa nell'unità di misura esterna. Il sistema in automatico calcola anche la quantità in unità di misura interna (R§QT01)
* Prezzo, è il prezzo del prodotto presente nella riga (R§VAL1). Il suo valore viene derivato da un listino. Il listino è intestato a :  agenzia, fornitore, articolo.
* Data inizio protezione, è la data in cui inizia la protezione del prodotto (R§DTCR). Se non presente singnifica che è protetto da sempre. In ogni caso è soggetto allo stato di protezione.
* Data fine protezione, è la data in cui finisce la protezione del prodotto(R§DTCC). Se non presente significa che è protetto per sempre.  In ogni caso è soggetta allo stato di protezione.

Ruoli
In aggiunta tutte le persone coinvolte nell'opportunità. Ciascuna con il suo ruolo specifico.
L'associazione opportunità, ruolo, persona viene memorizzata nel parametri.
Categoria "ORA", parametro "R01"
La categoria è intestata agli oggetti :  "CM" opportunità e "TARER" ruolo
Il parametro è intestato all'oggetto "RN" referenti

------------------------------
SIMES

Protezioni

T§CODS Filiale
T§DTRI Data richiesta
T§DT01 Data confermata
T§DTCO Data riconfermata
T§COD1 Tipo contrassegno (MAI USATO)
T§CD07 Cantiere "IDO"
T§NUM1 Spese trasporto ns.car. (MAI USATO)
T§NUM2 Ripartizione % Agente 1 XUVE45 (MAI USATO)
T§NUM3 Ripartizione % Agente 2 XUVE45 (MAI USATO)

R§CODS Cantiere "IDO", ma in testata non è T§CODS ma T§CD07
R§FL15 Prezzo netto in fattura
R§FL17 Tipo scontisitca
R§FL14 Riga ord. particolare (MAI USATO)
R§FL32 Prezzo particolare (MAI USATO)
R§FL43
R§DTCR Data richiesta
R§DT01 Data confermata
R§DTCC Data riconfermata
R§NUM1 Ripartizione % Agente 1 XUVE45 (MAI USATO)
R§NUM2 Ripartizione % Agente 2 XUVE45 (MAI USATO)
R§NUM3 gestito in EDI (MAI USATO)
R§NUM4 Presso listino base XUBB31 CDOG, CDCL
R§NR06
-----------------------------------------------------------------
## Funzioni
### Creazione nuova opportunità ed assegnazione di un responsabile
![X1MARK0601](http://localhost:3000/immagini/REOPPO_01/X1MARK0601.png)
### Scadenzario / promemoria

### Formalizzazione offerta

### Drill down sulle attività di marketing e vendita successive o derivate
 * offerte, ordini, fatture

### Analisi risultati opportunità
* conto economico di commessa (costi propri, margini commesse cliente derivate)


## Implementazione
Le opportunità sono sull'archivio BRCOMM0F ed hanno tipo commessa = 'R04'

### Campi utilizzati
M$COMM as "Opportunità;CM£R4",
M$DECM,
M$STAT,
M$CDRE as "Responsabile;CNCOL",
M$COEN as "Account;CNNOM",
M$DT01 as "Data apertura",
M$DT02 as "Chiusura attesa",
M$DT03 as "Expire Deal Date",
M$QI01 as "Rivendita",
M$QI02 as "SW proprio",
M$QI03 as "Man propria",
M$QI04 as "Noleggi",
M$QI05 as "Canoni",
M$QI06 as "Delivery",
M$QI10 as "Altro",
M$COD1 as "Linea prodotto;TACLR03",
M$COD2 as "Progr. vendita;TAREE",
M$COD3 as "Referente;RN",
M$STCM as "Tipo opportunità;TABSE£4",
M$NUM1  as "Probabilità di ciusura",

