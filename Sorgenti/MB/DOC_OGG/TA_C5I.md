# C5I - Codici Pagamento - Rate variabili
 :  : DEC T(ST) K(C5I)
## OBIETTIVO
Definire le singole rate dei codici pagamento definiti nella tabella PAG. I codici degli elementi di questa tabella sono formati dal codice dell'elemento della PAG e da un numero progressivo (lungo 3) che rappresenta la rata del pagamento separati da un punto.
Ad esempio : 
Codice PAG = B10
Codici C5I = B10.001, B10.002, B10.003 ecc.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive la rata di pagamento.
 :  : FLD T$C5IA Tipo Intervallo
Identifica il tipo di intervallo tra due rate (G= giorni M=mesi).
 :  : FLD T$C5IB Durata Intervallo
Definisce la lunghezza dell'intervallo tra due rate. Tale lunghezza assumerà come unità di misura quella definita nel campo precedente :  se ad esempio viene definito come tipo intervallo 'Mesi' e in questo campo viene inserito 1, l'intervallo tra due rate sarà di un mese.
 :  : FLD T$C5IC Importo % rata
Definisce la quota percentuale della rata relativamente all'importo totale del pagamento.
 :  : FLD T$C5ID Importo % IVA
Identifica la parcentuale IVA da versare nella rata. Se ad esempio il campo viene compilato con 100, in questa rata verrà versata l'intera quota dell'imposta.
Se in questa e in nessuna altra rata viene indicata la % IVA questa verrà automaticamente attribuita per relativa quota di importo rata.
 :  : FLD T$C5IT Tipo IVA
Identifica se la rata è di sola IVA oppure no.
 :  : FLD T$C5IO Tipo pagamento
E' un elemento TA/C5G e identifica il tipo di pagamento utilizzato per la rata.
 :  : FLD T$C5IP Scadenza GG Fissi
In questo campo è possibile indicare un giorno fisso per la scadenza delle rate (esempio il 15). In questo caso la data di scadenza della rata viene portata automaticamente al giorno scelto.
 :  : FLD T$C5IQ Scadenza MM Fissi
In questo campo è possibile indicare un mese fisso per la scadenza delle rate. In questo caso il mese di scadenza della rata viene portato automaticamente al mese scelto.
 :  : FLD T$C5II Forz.giorno nel mese
È un elemento V2 SI/NO. Impostando il campo a '1', se è stato impostato anche il GG fisso, la data impostata viene portata forzatamente al giorno scelto nel mese della data. Se ad esempio viene impostato come giorno fisso il 20 del mese e si ha una fattura con scadenza 30 gennaio la scadenza della rata verrebbe automaticamente portata al 20 febbraio. Se si vuole forzare il pagamento al 20 gennaio è necessario impostare il campo 'Forzatura giorni in mese corrente'.
 :  : FLD T$C5IE Scadenza fine mese
Attraverso questo campo è possibile imporre la scadenza della rata all'ultimo giorno del mese.
 :  : FLD T$C5IF Listini sconti

 :  : FLD T$C5IG Sezione sconti

 :  : FLD T$C5IL Scadenza fissa
E' possibile fissare una data fissa per la scadenza.

