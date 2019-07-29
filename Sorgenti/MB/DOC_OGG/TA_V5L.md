# V5L - Parametri di c/lavoro att/pass e kit
 :  : DEC T(ST) K(V5L)
## OBIETTIVO
Definire i parametri di conto lavoro (attivo e passivo) e di Kit relativi ad una riga di documento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Identifica il codice del parametro.
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5LA **Tipo Impegno**
È un elemento della tabella P5I :  definisce le modalità con cui verranno costruiti gli impegni di conto lavoro :  il tipo distinta di origine, l'eventuale tipo distinta di memorizzazione, ecc..
 :  : FLD T$V5LB **Modello conto lavoro**
È un elemento fisso V2/MODCL :  definisce la tipologia di conto lavoro che questa tabella descrive. Ha un significato puramente descrittivo.
 :  : FLD T$V5LC **Gruppo fonti disponibilità**
È un elemento di memorizzazione che raggruppa i magazzini (se applicazione multimagazzino), le fonti presenti e/o future che comporranno il valore di disponibilità dei componenti, nelle analisi specifiche.
_9_Esempio :  nella spedizione a bilanciamento, è il gruppo fonti su cui si effettua il bilanciamento stesso; in questo caso devono essere comprese le seguenti fonti : 
-    impegni di conto lavoro da soddisfare;
-    giacenze di materiale presso il terzista.
 :  : FLD T$V5LD **Modalità evasione**
Definisce le modalità di evasione delle righe.
Nel conto lavoro attivo definisce se dovrà essere eseguito un controllo di evadibilità, con eventuale forzatura se si evidenziano mancanti, e passaggio (automatico o con conferma) ad una riga di vendita (per la quantità non coperta o per l'intero documento).
 :  : FLD T$V5LE SSt **Tipo riga alternativa**
È un sottosettore della tabella V5B, che tipizza il campo successivo.
 :  : FLD T$V5LF **Tipo riga alternativa**
È un elemento della tabella V5B, del sottosettore definito nel campo precedente, che definisce il tipo riga che verrà assunto qualora si sia deciso di passare, nel conto lavoro attivo, ad una riga di vendita.
 :  : FLD T$V5LG **Tipo documento alternativo**
È un elemento della tabella V5D :  se impostato, qualora si sia deciso di passare, nel conto lavoro attivo, ad una riga di vendita, tali righe verranno accodate ad un documento separato di questo tipo (e del modello assunto). Se invece è lasciato in bianco, tali righe verranno accodate allo stesso documento.
 :  : FLD T$V5LH **Scarico impegni propri**
Se impostato, vengono scaricati gli impegni di lavorazione, relativi al documento che si sta collegando. Se invece il campo è lasciato vuoto, vengono scaricati gli impegni relativi al documento di origine. Se esso è assente non vengono scaricati gli impegni.
 :  : FLD T$V5LI SSt **Modello documento alternativo**
È un sottosettore della tabella V5A, che tipizza il campo successivo.
 :  : FLD T$V5LJ **Modello documento alternativo**
È un elemento della tabella V5A.
Se è stato impostato il tipo documento alternativo, questo campo non è significativo.
Se impostato, qualora si sia deciso di passare nel conto lavoro attivo ad una riga di vendita, tali righe verranno accodate ad un documento separato di questo modello (nello stesso tipo documento). Se invece è lasciato in bianco, tali righe verranno accodate allo stesso documento.
 :  : FLD T$V5LL **Scarico manuale**
Se impostato, in collegamento a magazzino della riga di conto lavoro non viene eseguito lo scarico automatico dei componenti, anche se è presente la causale nel tipo impegno P5I.
 :  : FLD T$V5LM **Data impegno fissa**
Se impostata, gli impegni di lavorazione vegono datati alla data fine confermata della riga dell'assieme.
Bisogna prestare attenzione a questa impostazione :  può essere usata senza inconvenienti per righe di documenti che non provengono dalla pianificazione (ad esempio gli impegni di una riga di bolla).
La pianificazione comunque, arretra sempre la data degli impegni pianificati e a partire da essi possono venire pianificati nuovi ordini. Se, nel rilascio, gli impegni non vengono più arretrati, gli ordini vengono comunque collocati alla data di fabbisogno degli impegni pianificati, con il risultato che la successiva pianificazione emetterà un suggerimento incongruo di ritardo.
Se lasciata in bianco, gli impegni vengono datati a partire dalla data consegna confermata dell'ordine, arretrando dei tempi di approvvigionamento di lavorazione. Per il calcolo del tempo di approvvigionamento variabile, viene considerata sempre la quantità modificabile della riga e non la quantità residua. Infatti l'eventuale quantità consegnata parzialmente non deve avere effetto sulla datazione degli impegni.
 :  : FLD T$V5LN **Quantità riferimento**
È un elemento fisso V2/V5QRI. Riferirsi ad esso per la documentazione specifica. Definisce da quale quantità si parte per scandire gli impegni di questo tipo.
 :  : FLD T$V5LO **Parametri di pianificazione per riferimento**
Se impostato, e nella tabella generale M51 è stato definito il tipo oggetto intestatario dei parametri, verranno usati, se presenti, i tempi di approvvigionamento specifici per datare gli impegni di lavorazione.
_9_Esempio :  se si è prevista, in M51, la possibilità di definire i parametri di pianificazione a livello di ente, e questo campo è valorizzato, la ricerca dei tempi di approvvigionamento verrà eseguita tenendo conto anche dell'ente.
Questo campo va valorizzato congiuntamente con quello corrispondente, nella politica di pianificazione.
In tal modo gli impegni terranno conto dell'eventuale tempo di approvvigionamento 'corretto' : 
-    in fase di pianificazione (se impostato nella tabella della politica);
-    in fase di costruzione impegni rilasciati (se impostato in questa tabella).
Questa informazione ridondante ha lo scopo di migliorare le prestazioni :  se i tempi di approvvigionamento di lavorazione esterna non sono definiti per riferimento, anche se la politica dell'articolo lo è (ad esempio, per diversificare i lotti a livello di ente), e se nella costruzione degli impegni ci si basasse sull'informazione della politica, verrebbero ricercati inutilmente i parametri di pianificazione per riferimento.
 :  : FLD T$V5LP **Saldo contestuale**
Questo campo è significativo nelle righe di conto lavoro di fase legate ad un ordine di produzione.
Impostandolo, e impostando di eseguire in automatico (nel tipo riga V5B) la dichiarazione di avanzamento dell'ordine di produzione all'atto del ricevimento della riga di conto lavoro, se quest'ultima è a saldo, viene saldata anche la fase corrispondente dell'ordine di produzione.
 :  : FLD T$V5LQ **Solo conto lavoro**
Se questo campo è impostato gli impegni della riga del documento saranno creati se e solo se
il flag di conto lavoro della riga è impostato (R§FL10).
Questo campo risulta comodo ed esempio nel caso di gestione di righe di ordini di vendita di Kit,
in cui in fase di spedizione si scaricano i componenti e non l'assieme stesso. Questo
flag consente di utilizzare lo stesso tipo riga per tutti gli articoli di vendita (il
flag 10 di riga  dovrà essere gestito in questo caso in mofo autonomo, e non dal gruppo
flag di riga).
 :  : FLD T$V5LR **Tipo Kit**
Se impostato, i tipi riga con questa V5L, appartengono ad un kit, secondo quanto specificato nell'elemento di V5K. Le informazioni "di legame" del kit vengono invece assunte dal presente eloemento di V5L.
