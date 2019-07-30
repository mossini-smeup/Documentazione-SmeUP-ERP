 :  : HEA RESP(CM) STAT(00) CLAS(A)
# OBIETTIVO
Si occupa della gestione delle configurazioni.

## Nota sui parametri TP20
### manutenzione tabelle
In questo caso il servizio utilizza solo gli oggetti 1 e 2, ad esempio, la modifica della tabella CFQ avviene con la seguente funzione : 
F(G30;CFSER_02;STR.RIV) 2(RE;T-;CFQ) 2(TA;CFQ;BICICLET)
il questionario è l'oggetto RE T- CFQ, la configurazione è l'oggetto TA CFQ BICICLET

### Manutenzione di configurazioni di questionari diversi dai T-
In questo caso la modifica/cancellazione/copia di una configurazione possono avvenire o specificando le chiavi definite dagli oggetti 2,3 e 4 oppure utilizzando l'IDOJ della configurazione nella chiave 5

### Nota questionari con motore statico
Il parametro REBLD può assumere i seguenti tre valori : 
- ALLTIMES :  la creazione del motore delle regole avviene ogni volta che si inizia/modifica una configurazione
- NEVER :  la creazione del motore delle regole non avviene mai. E' compito di chi gestisce il questionario crare il motore e tenerlo aggiornato quando vengono modificate le regole
- DEFAULT :  la creazione del motore avviene se non esiste o se è più vecchio di 1 giorno il motore viene rigenerato

### Nota questionari L-
E' possibile specificare come formati dell'XML di input e di output anche i seguenti due formati : 
1) le risposte sono suddivise per sezioni e la risposta è il valore di un elemento che ha il nome della domanda : 
se ho la sezione sez1 con le domande D1 e D2 e la sezione sez2 con le domande D3 e D4 avrò un XML delle risposte nel seguente formato
<sez1><D1>risposta_x</D1><D2>risposta_y</D2></sez1><sez2><D3>risposta_z</D3><D4>risposta_k</D4></sez2>

## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato
TST.STS|XMLO|TTVER|Non rigenerare mail il motore
TST.STS|XMLO|TTFAULT|Rigenera se più vecchio di un giorno
TST.STS|XMLO|TTS|Risposte/Risposta
TST.STS|XMLO|TTEE|Divise per sezione
TST.STS|XMLO|TTEE_DR|Per sezione con valori nel testo del tag
TST.STS|XMLO|TTEE_DR_CMA|Come sopra, se config. multipla valori negli attributi


 :  : PRO.SER Cod="STR.LET.1" Tit="Struttura. Lettura struttura configuratore" Fun="F(G30;CFSER_02;STR.LET) 1(RE;;-(O;;RE;))"

 :  : PRO.SER Cod="STR.RIS.2" Tit="Struttura. Lettura struttura e risposte senza vinc" Fun="F(G30;CFSER_02;STR.RIS) 1(RE;;-(O;;RE;))"

 :  : PRO.SER Cod="STR.RIV.3" Tit="Struttura. Lettura struttura e risposte con vincol" Fun="F(G30;CFSER_02;STR.RIV)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="STR.RID.4" Tit="Struttura. Lett. str. e risposte con vincolo per c" Fun="F(G30;CFSER_02;STR.RID)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="STR.VLD.5" Tit="Struttura. Lettura valori dinamici" Fun="F(G30;CFSER_02;STR.VLD) 1(RE;;-(O;;RE;)) 2(CS;Q-&OG.K1;-) INPUT(XML RISPOSTE FORMATO Risposte/Risposta)"

 :  : PRO.SER Cod="REC.LET.6" Tit="Record. Lettura risposte senza vincolo" Fun="F(G30;CFSER_02;REC.LET)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.LEV.7" Tit="Record. Lettura risposte con vincolo" Fun="F(G30;CFSER_02;REC.LEV)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.AGG.8" Tit="Record. Aggiorna risposte" Fun="F(G30;CFSER_02;REC.AGG)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.NEW.9" Tit="Record. Aggiungi nuova configurazione/record" Fun="F(G30;CFSER_02;REC.NEW)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.DEL.10" Tit="Record. Elimina configurazione/record" Fun="F(G30;CFSER_02;REC.DEL)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.DEV.11" Tit="Record. Elimina configurazione/record e sblocca" Fun="F(G30;CFSER_02;REC.DEV)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.NXT.12" Tit="Record. Leggi Configurazione/record successiva" Fun="F(G30;CFSER_02;REC.NXT)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.PRV.13" Tit="Record. Leggi Configurazione/record precedente" Fun="F(G30;CFSER_02;REC.PRV)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.BLO.14" Tit="Record. Vincola configurazione/record (blocca)" Fun="F(G30;CFSER_02;REC.BLO)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="REC.SBL.15" Tit="Record. Rilascia configurazione/record (sblocca" Fun="F(G30;CFSER_02;REC.SBL)" Ref="STR.RIS.2"

 :  : PRO.SER Cod="TST.STS.16" Tit="Rilascia configurazione/record (sblocca). Rilascia configurazione/record (sblocca" Fun="F(G30;CFSER_02;TST.STS) 1(RE;;-(O;;RE;)) P( XMLO(-(F;;**;Tipo XML in Output(se non Q-))))"

