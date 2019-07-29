# C5J - Rapporti bancari
 :  : DEC T(ST) K(C5J)
## OBIETTIVO
Definire i rapporti bancari.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive il rapporto bancario
 :  : FLD T$C5JA **Banca**
È un elemento TA/C5F :  è la banca azienda cui il rapporto fa riferimento
 :  : FLD T$C5JB **Conto Contabile**
È un elemento TA/C5B :  Indica il conto contabile cui la rapporto bancario fa riferimento :  se è attivata la tesoreria, nell'elemento indicato della C5B deve essere a sua volta speficato tale rapporto bancario. I riferimenti devono essere perciò univoci.
 :  : FLD T$C5JC **C/C Bancario**
Viene indicato il codice del c/c bancario cui il rapporto è legato
 :  : FLD T$C5JD **Tipo Rapporto**
E' un elemento V2/C5TRB. Indica il tipo di rapporto intrattenuto con la banca (conto corrente, salvo buon fine, ecc.).
 :  : FLD T$C5JE **Tipo anno per int.credito**
Identifica il tipo di anno (solare, bisestile o commerciale) utilizzato per il calcolo degli interessi dei crediti.
 :  : FLD T$C5JF **Tipo anno per int.debito**
Identifica il tipo di anno (solare, bisestile o commerciale) utilizzato per il calcolo degli interessi dei debiti.
 :  : FLD T$C5JG **Divisore numeri_n
E' possibile definire in questo campo se inserire un divisore dei numeri (per 10 o per 100).
 :  : FLD T$C5JH **Decimali numeri**
Permette di visualizzare anche uno o due numeri decimali.
 :  : FLD T$C5JI **Arrotondamento numeri crediti**
Indica il tipo di arrotondamento applicato al calcolo dei numeri degli interessi attivi

 :  : FLD T$C5JJ **Arrotondamento numeri debiti**
Indica il tipo di arrotondamento applicato al calcolo dei numeri degli interessi passivi

 :  : FLD T$C5JK **Periodo liquidazione interessi**
E' un elemento V2/C5PCI e identifica il periodo per il calcolo degli interessi.
 :  : FLD T$C5JL**Tipo calcolo antergate**

 :  : FLD T$C5JM **Giorni Rischio**
Indica i giorni di rischio specifici del rapporto. Se valorizzato, indica che nell'interrogazione del castelletto (se attivata la tesoreria) per il rapporto, non verranno presi in considerazione i giorni di rischio indicati nella tabella C51, ma quelli qui specificati.
 :  : FLD T$C5JN **Rapporto Bancario collegato**
È un elemento TA/C5J stessa, può assumere significati diversi a seconda del tipo rapporto in cui è indicato : 
- se è un rapporto di c/c il rapporto collegato (generalmente un sbf) indica che tale conto è gestito a conto unico con il c/c per il calcolo degli interessi
- se è un rapporto di anticipo, serve per recuperare il conto utilizzato per la presentazione degli effetti
 :  : FLD T$C5JO **Utilizzo calendario**
Indica se per il rapporto bancario deve essere considerato il calendario indicato nella tabella C55 (il default è SI).
 :  : FLD T$C5JP **Utilizzo % ritenute**
Indica se per il rapporto bancario deve essere considerata la % di ritenute indicata nella tabella C55. (il default è SI).
 :  : FLD T$C5JQ **Data Consolidamento**
Indica la data a cui il rapporto è stato consolidato l'ultima volta.
 :  : FLD T$C5JR **Saldi a 0 da Remote**
Indica se in fase di consolidamento per la determinazione del saldo banca devono essere presi in considerazione anche i movimenti da remote banking che riportano nel campo "saldo contabile" un saldo a zero
 :  : FLD T$C5JS **Accetta CUP**
In fase di creazione distinte di pagamento indica se il rapporto bancario non può accettare CUP/CIG (' '),
accettare solo CUP/CIG ('1') o accettare sia movimenti con CUP/CIG e anche tutti gli altri ('2')
L'impostazione di Grande Opera ('3') identifica un rapporto bancario di grande opera.
Se definito tale in creazione distinta verranno prese in considerazione solo le fatture definite  con il parametro grande opera sulla registrazione contabile (parametro A03 oggetto E4)
 :  : FLD T$C5JT **Periodo Consolidamento**
Definisce la periodicità con la quale viene consolidato il rapporto.
 :  : FLD T$C5JU **Maturazione Effetti**
Per i rapporti utilizzati per la presentazione di effetti, condiziona la modalità di contabilizzazione proposta per la contabilizzazione della maturazione degli effetti.
* Per Valuta :  prende la scadenza o la data valuta se attiva la tesoreria e per ognuna di queste viene fatta un'apposita registrazione
* Per Valuta Adeguata :  prende la scadenza o la data valuta se attiva la tesoreria ed in base a quella calcolata la data valuta adeguata
* Ad una Data :  viene fatta un unica registrazione suddivisa in righe per scadenza o data valuta se attiva la tesoreria
* Per Fine Mese Scadenza :  prende le scadenza le porta a fine mese e viene fatta una registrazione per ogni data ottenuta
* Per Scadenza :  prende la scadenza o se è attiva la tesoreria invece che fare una regitrazione per data valuta, viene fatta una registrazione per ogni combinazione di data valuta/data scadenza
 :  : FLD T$C5JV **Rimargino Castelletto**
Per i rapporti di sbf indica la data che viene presa in considerazione la ricostruzione del castelletto.
* Con valore ' ' viene utilizzata la data scadenza
* Con valore '1' viene utilizzata la data valuta
 :  : FLD T$C5JW **Divisione Calcolo Interessi**
Questo campo ha valenza solo qualora sia stata attivata la gestione della divisione nella tabella C51. In questo caso, non essendo la divisione gestita in tesoreria, ma obbligatoria per la contabilità, risulta necessario attribuire una divisione alle procedure di calcolo automatiche elencate a seguire : 
* Contabilizzazione Operazioni da Spunta Automatica
* Contabilizzazione Interessi
Attraverso il campo in oggetto, sarà quindi possibile attribuire la divisione obbligatoriamente necessaria.
Qualora poi il movimento debba essere attribuito/suddiviso a differenti divisioni, tale attribuzione sarà necessario eseguirla manualmente (se opportuno anche solo a fine mese-trimestre).

