# PAG  -  CODICI PAGAMENTO - Rate Fisse
## OBIETTIVO
Definire modalità di pagamento da legare a documenti esterni ed a registrazioni contabili.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC __Descrizione__
Descrive la modalità di pagamento
 :  : FLD T$PAGA __Numero di Rate__
Indica il numero di rate in cui si sviluppa la modalità di pagamento.
**NB** :  si intende rate costanti. In caso contrario bisogna compilare la tabella C5I.
Il campo è obbligatorio.
 :  : FLD T$PAG3 __Gener.Rate Bloccate__
È un elemento della tabella C5*BP ed è un campo facoltativo.
Se viene impostato il programma di generazione rate, queste verranno create _r_BLOCCATE
con la causale specificata nel campo.
 :  : FLD T$PAGL __Tipo Intervallo__
È un valore V2 C5TIR. Indica se l'intervallo tra diverse rate è espresso in giorni (G) o in mesi (M).
Il campo è obbligatorio.
 :  : FLD T$PAGB __Tipo di calendario__
Indica se, per il calcolo degli intervalli, viene utilizzato il calendario solare (anno da 365 giorni) o il calendario
Commerciale (anno da 360 giorni e mesi tutti da 30 giorni). Inserire il valore ' ' per l'anno solare e 'C' per l'anno
commerciale.
 :  : FLD T$PAG2 __Durata Rate__
È un numero ed indica il valore dell'intervallo tra le rate costanti. Possono essere Giorni o Mesi, in funzione dalla scelta fatta nel campo "Tipo intervallo".
 :  : FLD T$PAG1 __Durata 1a RatA__
Si può impostare un intervallo diverso da tutti gli altri per la prima rata. Sono giorni o mesi. Serve per far partire il calcolo delle rate da un intervallo non standard.
 :  : FLD T$PAGC __IVA su 1° rata__
È un elemento V2 SI/NO. Impostando il campo a '1' si vuole inserire tutto il valore dell'imposta (IVA) nella prima rata.
 :  : FLD T$PAGT __IVA su n rata__
Si può inserire tutto il valore dell'imposta in una rata diversa dalla 1, indicando il numero della rata in questo campo.
 :  : FLD T$PAGM __Fine Mese__
Impostando il campo a '1', si sposta indipendentemente dal calcolo delle rate create la scadenza a fine mese.
Impostando il campo a '2', la data inizio pagamento viene spostata al suo fine mese e solo a seguire viene eseguito il calcolo dei gg.
 :  : FLD T$PAGN __Scadenza GG Fissi__
Si può indicare un Giorno fisso per la scadenza delle rate (esempio il 15). In questo caso la data di scadenza della rata viene "portata" automaticamente al giorno scelto.
 :  : FLD T$PAGO __Scadenza MM Fissi__
Vale il discorso fatto per i GG fissi. Si può specificare un mese fisso per la scadenza della/e rate.
 :  : FLD T$PAGP __Forz.gg in mese cor.__
È un elemento V2 SI/NO. Impostando il campo a '1', se è stato impostato anche il GG fisso, la data impostata viene "portata" forzatamente al giorno scelto nel mese della data. Se ad esempio si fissa la scadenza al giorno 20 e si ha una rata con scadenza il 21 febbraio, questa scadenza verrebbe portata al 20 marzo; se la si vuole forzare al 20 febbraio è necessario flaggare questo campo.
 :  : FLD T$PAGQ __Scadenza a vista__
È un elemento V2 SI/NO. Impostando il campo a '1', si specifica che il pagamento è a vista. Di conseguenza non verranno calcolate rate nel tempo.
 :  : FLD T$PAGI __Tipo Pagamento__
È un elemento TA/C5G. Indica il tipo di pagamento generato.
Il campo è obbligatorio.
 :  : FLD T$PAGD __Sconto finanziario__
È un numero espresso in Percentuale e serve per legare al pagamento un eventuale sconto (esempio cassa). Questo campo è collegato alla gestione Spese di Trad.Up ( Vedi tabella V5S).
 :  : FLD T$PAGR __Spese incasso__
Vale il discorso fatto per lo sconto finanziario. Serve per imputare delle spese al pagamento (esempio emissione riba) e può essere gestito nelle spese di TRADE up (tabella V5S).
 :  : FLD T$PAG4 __Sconto pagamento__
È un numero espresso in percentuale e serve per legare al pagamento un eventuale sconto da proporre automaticamente al momento dell'effettivo pagamento in contabilità.
 :  : FLD T$PAG5 __Base sconto pagamento__
Indica se il calcolo dello sconto pagamento deve basarsi sull'importo del documento o al netto dell'imponibile IVA.
 :  : FLD T$PAGF __Codice alternativo__
Permette (se indicato un importo minimo) di sostituire il codice di pagamento con quello indicato in questo campo.
_9_Esempio :  Cod. pagamento con riba. Tuttavia, se l'importo è basso, utilizzo un bonifico o altro
 :  : FLD T$PAGE __Importo minimo__
Permette di definire un importo minimo sotto il quale verrà utilizzato il codice di pagamento del campo codice alternativo.
 :  : FLD T$PAG6 __Classe Sconto__
Se la contabilità è smeup, tramite questo campo può essere specializzato l'elemento della C5U utilizzato per la scrittura delle righe automatiche di sconto (SCFAT/SCPAS).
 :  : FLD T$PAG7 __Durata per sconto pagamento__
Indicare qui il periodo o i giorni in cui si può applicare lo sconto pagamento se eseguito prima della scadenza naturale della fattura (es. Rimessa Diretta a 90 gg d.f.f.m. sconto 3% entro 30 gg d.f.f.m. significa che se la disposizione viene eseguita per valuta entro i 30 gg d.f.f.m. il pgm applicherà lo sconto automatico del 3%)
 :  : FLD T$PAG8 __gg tolleranza per sconto pagamento__
Nella generazione delle proposte e/o pratiche passive la data di pagamento (o valuta) non è definita in sede di selezione ma solo alla conferma della pratica (con i dati di testata) :  completando questo campo viene considerata la data di immissione proposta o pratica più i giorni tolleranza come data pagamento (o valuta) e se rientra nei termini del campo durata per sconto pagamento allora viene calcolato automaticamente lo sconto.
 :  : FLD T$PAGG __SS Tip.Riga Ant.(SV)__
Se il pagamento prevede un acconto sull'ordine e si vuole gestire automaticamente il calcolo dello stesso, bisogna inserire in questo campo il subsettore del tipo riga di acconto che verrà utilizzato nell'immissione di un ordine con questa tipologia di codice pagamento. La compilazione di questo campo permetterà il calcolo automatico dell'acconto.
 :  : FLD T$PAGH __Tipo Riga Ant. (SV)__
Se il pagamento prevede un acconto sull'ordine e si vuole gestire automaticamente il calcolo dello stesso, bisogna inserire in questo campo il tipo riga di acconto che verrà utilizzato nell'immissione di un ordine con questa tipologia di codice pagamento. La compilazione di questo campo permetterà il calcolo automatico dell'acconto.
 :  : FLD T$PAG9 __% Anticipo (SV)__
Se il pagamento prevede un acconto sull'ordine e si vuole gestire automaticamente il calcolo dello stesso, bisogna inserire in questo campo la percentuale di acconto che verrà utilizzata nell'immissione di un ordine con questa tipologia di codice pagamento. La compilazione di questo campo permetterà il calcolo automatico dell'acconto.
