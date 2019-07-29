# A51 - Gestione cespiti
 :  : DEC T(ST) K(A51)
## OBIETTIVO
Definisce i parametri che guidano la gestione dei cespiti ammortizzabili.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È un campo fisso '*'
 :  : FLD T$DESC **Descrizione**
Bianco
 :  : FLD T$A51A **Linea assunta**
È un elemento della tabella A5C, dello stesso sottosettore dell'elemento in manutenzione. Se impostato, la gestione cespiti è 'monolinea' :  la linea non viene mai richiesta, ma viene assunto in automatico il valore qui inserito.
 :  : FLD T$A51B **Linea fiscale**
È un elemento della tabella A5C, dello stesso sottosettore dell'elemento in manutenzione. Se inserita la linea assunta, non è significativa. In caso contrario definisce la linea, tra quelle impostate, che rappresenta l'ammortamento fiscale.
 :  : FLD T$A51C **Linea civilistica**
È un elemento della tabella A5C, dello stesso sottosettore dell'elemento in manutenzione. Se inserita la linea assunta, non è significativa. In caso contrario definisce la linea, tra quelle impostate, che rappresenta l'ammortamento civilistico. Può coincidere con la linea fiscale impostata in precedenza.
 :  : FLD T$A51E **Attivazione flussi**
È un valore V2/SI/NO. Se impostato, all'atto dell'inserimento/variazione/annullamento di un cespite, vengono eseguiti i flussi corrispondenti.
Può essere utile disattivare questo comportamento durante la conversione, per velocizzarne l'esecuzione.
 :  : FLD T$A51F **Tipo periodo**
Definisce il tipo periodo degli elementi della PER utilizzato come riferimento
 :  : FLD T$A51D **Registrazione contabile per cespite**
È un elemento V2 SI/NO. Inserendo il valore '1' si specifica che verrà creata una registrazione contabile per ogni cespite.
 :  : FLD T$A51G **Ammessa contabilizzazione batch**
È un elemento V2 SI/NO. Inserendo il valore '1' si specifica che la funzione di contabilizzazione degli ammortamenti potrà essere eseguita in modalità batch, cioè senza la necessità di confermare le registrazioni create.
 :  : FLD T$A51H **Ricalcolo automatico movimenti di ammortamento**
È un elemento V2 SI/NO. Indicando '1' si richiede l'esecuzione automatica del ricalcolo dei movimenti di ammortamento di un cespite ad ogni immissione/modifica/annullamento dei suoi movimenti di capitale.
 :  : FLD T$A51I **Arrotondamento minimo**
È l'importo minimo arrotondabile nel calcolo della singola quota di ammortamento. Se
non viene indicato alcun numero viene automaticamente assunto 0,99.
 :  : FLD T$A51L **Trattamento Cespiti Immateriali Ammortizzati**
Gestisce nelle elaborazioni che riguardano i cespiti in essere in azienda, il trattamento
cespiti immateriali completamente ammortizzati : 
* Se valorizzato a "1" i cespiti vengono inclusi
* Se valorizzato a " " i cespiti vengono esclusi
 :  : FLD T$A51M **Exit Classificazione Cespite**
Se questo campo viene impostato a '1' (SI), in inserimento dell'anagrafica cespite dalle immissioni
batch, viene richiamata una exit per determinare i valori di classificazione.
Il programma di exit dovrà chiamarsi obbligatoriamente A5CE01D_X
 :  : FLD T$A51N **Stampa Residuo**
Se impostato questo campo ad '1' non verranno stampati i residui dei cespiti da non ammortizzare,
definiti nella tabella A5A (categoria fiscale cespite).
Se non impostato verranno stampati sia i residui dei cespiti da non ammortizzare sia quelli da
ammortizzare
 :  : FLD T$A51P **Note Movimenti Automatici**
Se impostato il programma di calcolo ammortamento scriverà le note per ogni movimento automatico,
con il dettaglio di come è stato fatto il calcolo.
