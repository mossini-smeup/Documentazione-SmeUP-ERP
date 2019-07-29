# C51 - Impostazioni base keep.up
 :  : DEC T(ST) K(C51)
## OBIETTIVO
Definisce i parametri generali relativi al applicazione Contabilità.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C51D **Passo riga registrazioni contabilità generale**
Se impostato, è il passo che viene assunto nella numerazione delle righe di contabilità generale. Se lasciato in bianco si assume passo 1.
 :  : FLD T$C51F **Passo riga registrazioni contabilità analitica**
Se impostato, è il passo che viene assunto nella numerazione delle righe di contabilità analitica. Se lasciato in bianco si assume passo 1.
 :  : FLD T$C51K **Presentazione data di registrazione**
Definisce la data che viene presentata all'atto dell'immissione della registrazione.
Può assumenre i valori : 
- ' '  - Nessuna data.
- '1'  - Data del giorno.
- '2'  - Ultima data immessa.
 :  : FLD T$C51M **Costo del denaro**
È l'interesse che viene applicato ovunque si richieda di attualizzare un importo situato nel tempo o di calcolare un interesse ad esempio per il ritardo di un pagamento.
 :  : FLD T$C51A **Giorni di rischio**
Identifica la lunghezza del periodo (in giorni) che parte dalla data di scadenza di un pagamento di tipo effetto e all'interno della quale il pagamento stesso è considerato a rischio. Ad esempio, se si considera un pagamento con data scadenza 31/01 e il campo è valorizzato con 10, il pagamento verrà considerato a rischio fino al 10/02. Individua il ritardo con cui l'istituto di credito comunica un insoluto.
 :  : FLD T$C51B **Giorni di scaduto**
Identifica la lunghezza del periodo (in giorni) che parte dalla data di scadenza di un pagamento oltre al quale il pagamento stesso è considerato scaduto. Ad esempio, se si considera un pagamento con data scadenza 31/01 e il campo è valorizzato con 20, il pagamento verrà considerato scaduto a partire dal 20/02. Individua il ritardo con cui vengono eseguite le registrazioni di pagamento dal momento in cui è ricevuta la comunicazione.
 :  : FLD T$C51C **Oscillazione**
Se impostato ad 1, all'interno di una registrazione viene eseguita una riga di oscillazione cambio a livello di ente/valuta/documento, se invece si lascia in bianco, viene eseguita una riga a livello di ente/valuta. La contropartita viene scritta sempre a livello di conto.
Valorizzato a 2 invece disattiva completamente il calcolo delle oscillazioni.
 :  : FLD T$C51E **Abbuono per documento**
Se impostato, all'interno di una registrazione viene eseguita una riga di abbuono a livello di ente/valuta/documento, se invece si lascia in bianco, viene eseguita una riga a livello di ente/valuta. La contropartita viene scritta sempre a livello di conto/valuta.
 :  : FLD T$C51G **Attivazione flussi**
È un valore SI/NO :  se impostato, verranno abilitati i flussi di I/V/A degli oggetti contabili.
 :  : FLD T$C51L **Lunghezza riempimento zero E4**
Se impostata, (con un valore da 01 a 10) il numero registrazione digitato viene automaticamente riempito col carattere zero, partendo da sinistra, fino al raggiungimento del primo carattere inserito dall'utente. Se ad esempio compilo il campo con 8 e digito un numero di registrazione con 5 caratteri il sistema in automatico metterà tre zeri davanti al numero di registrazione.
 :  : FLD T$C51O **Tipo pagamento rate anticipo**
È un valore TA/C5G :  viene assunto all'atto della scrittura di una rata di puro anticipo, nella gestione del saldaconto.
 :  : FLD T$C51P **Soglia IVA versabile**
È un importo espresso nella divisa corrente :  è il valore al di sotto del quale non si esegue il versamento dell'IVA ma lo si somma al mese successivo.
 :  : FLD T$C51Q **Ritenuta per Ente**
Definisce come devono essere scritte le righe automatiche di ritenuta
- ' '  - Unica :  viene generata un'unica riga che comprende tutti i percipienti.
- '1'  - Per Ente :  viene generata una contropartita per ogni ente
- '2'  - Per Ente/Doc :  viene generata una contropartita per ogni ente /documento
 :  : FLD T$C51R **Codice pagamento insoluti**
È un elemento TA/PAG :  se impostato, verrà utilizzato nella generazione insoluti come codice pagamento della registrazione.
 :  : FLD T$C51S **Presentazione esercizio**
È un elemento C5PRD e dichiara se ad ogni registrazione devo presentare l'ultimo esercizio utilizzato o meno.
 :  : FLD T$C51I **Minuscolo in descrizioni**
È un valore SI/NO :  se impostato, permette anche l'inserimento di caratteri "minuscoli" nelle descrizioni base ed estesa delle righe di registrazione contabile.
 :  : FLD T$C51H **Contenitore note**
È un valore TA/NSC :  se impostato, indica il contenitore delle note relative ai record dei file della contabilità.
Un prerequisito per il suo corretto funzionamento è che nel relativo campo Tipo Note deve essere indicato un elemento della tabella NSI che abbia impostato il campo "Let.Note Liv.Super.".
 :  : FLD T$C51N **Collegamento automatico a cespiti**
Se impostato, innesca l'alimentazione automatica di dati derivanti dalle righe contabili, il cui conto ha rilevanza cespiti (campo definito sulla tabella C5B), nell'ingresso batch del modulo cespiti. Questo evento viene innescato dal programma di immissione movimenti contabili, alla conferma della registrazione. In particolare è possibile gestire immediatamente l'anagrafica dei cespiti oppure effettuare una ripresa dei movimenti in un secondo momento.
Il campo può assumere i seguenti valori : 
- " "-->Non esegue alcun collegamento.
- "1"-->Viene creato il collegamento tramite la creazione cieca dei record del file A5BATC0F. Con questa modalità nel momento in cui verrà inserita una fattura di acquisto cespite il dato verrà memorizzato per essere eleborato in un secondo momento tramite l'esecuzione delle azioni periodiche dei cespiti.
- "2"-->Viene creato il collegamento tramite la creazione cieca dei record del file A5BATC0F proponendone a video l'applicazione. Con questa modalità al termine dell'inserimento di una fattura di acquisto cespite verrà immediatamente proposta la schermata per l'immissione dei dati anagrafici del cespite stesso.
 :  : FLD T$C51V **Controllo collegamento stanziamenti interattivo**
È un valore SI/NO :  se impostato, alla conferma di ogni registrazione contabile verrà controllata la presenza di conti con rilevanza stanziamenti che non sono stati collegati. In caso affermativo verrà proposta la lista degli stanziamenti aperti collegabili, in modo similare a ciò che può avvenire nell'analitica. L'unica  differenza consiste nel non comportare alcun obbligo. Naturalmente la sua impostazione comporta un'ulteriore appesantimento del data entry contabile. Per questo dovrebbe essere impostato solo se gli utenti che inseriscono le registrazioni hanno l'onere di dover gestire tale collegamento.
 :  : FLD T$C51X **Calendario per inserimento registrazioni**
È un valore TA/TRG :  se impostato, durante la gestione registrazioni contabili, viene controllato che la data registrazione non ricada tra le date di chiusura.
 :  : FLD T$C51Y **Contenitore note lettere (SV)**
È un valore TA/NSC :  se impostato, indica il contenitore delle note relativo alle lettere gestite dalla £G69 per il modulo C5. Un prerequisito è il fatto di impostare nel campo "Capitolo / Tipo Note"  un elemento che abbia impostato la vista a 132.
 :  : FLD T$C51W **Scol.Aut.Docum.Orig.**
Se impostato, indica che al momento della cancellazione di una registrazione vengono scollegati automaticamente i documenti origine collegati.
L'esempio classico è rappresentato dalle fatture attive :  alla cancellazione della registrazione le testate bolle che la compongono vengono riportate allo stato "Fatture da contabilizzare" (flag 19 = 'B').
 :  : FLD T$C51J **Coll. autom. intra**
Se impostato, innesca l'alimentazione automatica di dati derivanti dalle righe contabili. Questo evento viene innescato dal programma di immissione dei movimenti contabili, alla conferma della registrazione.
 :  : FLD T$C512 **Emissione msg.esito positivo**
Il campo gestisce i messaggi di esito alla conferma della registrazione contabile
" "  :  Viene emmesso il messaggio di assegnazione protocollo
"1"  :  Viene emmesso sia il messaggio di esito positivo che il messaggio di assegnazione protocollo
"2"  :  Non vengono emmessi messaggi di esito
 :  : FLD T$C513 **Azienda Aggregato**
Identifica l'azienda utilizzata per la gestione dei dati aggregati di bilancio. La sua indicazione va perciò effettuata solo per l'ambiente di tale azienda.
 :  : FLD T$C514 **Gestione competenza**
Se valorizzato attivato viene assunto il valore "3" per il campo competenza di tutti i tipi di registrazione (tabella C5D) fiscali. La differenza fra i valori 1 e 2 consiste nel fatto che nel caso in cui la competenza sia costituita da un range di date, con il valore 1 viene applicata la distribuzione esclusivamente in funzione del mese di appartenenza, mentre con il valore 2 la distribuzione viene applicata tenendo conto dei giorni di competenza effettivi di ogni mese (es. con il valore 1 che abbia le date 01/03/08-31/12/08 o 16/03/08-15/12/08,
non fa differenza, al primo e l'ultimo mese viene sempre applicata la quota intera di un mese, mentre con con il valore 2
nel secondo caso al primo e l'ultimo mese verrà applicata una quota corrispondente alla metà di un mese intero).
Con i valori 3 e 4 si ottengono gli stessi risultati se non che la competenza verrà applicata solo se rilevante ai fini fiscali.
NOTA BENE :  se vengono valorizzati i campi fiscali, la rilevanza "gestionale" anche se indicata sul conto non viene presa in considerazione.
 :  : FLD T$C515 **Enasarco sempre contabilizzato**
Se impostato considera sempre l'enasarco come contabilizzato, ed utilizza perciò per le righe automatiche
sempre l'elemento ENACO della C5U.
 :  : FLD T$C516 **Aliquota Indetraibile**
Se impostato valorizzato permette di attivare la gestione utente del campo relativo all'aliquota indetrabile iva. Diversamente il campo è bloccato e l'aliquota è valorizzata sempre in base al relativo campo previsto dall' assoggettamento iva utilizzato.
 :  : FLD T$C517 **Storno Competenza**
Se impostato permette di forzare il fatto, che nel caso in cui sia attivata la competenza, se questa è relativa a più periodi, venga stornata anche la quota di competenza del periodo stesso, considerandola come rateo.
 :  : FLD T$C518 **Presentazione Competenza**
Se impostato, alla conferma della registrazione in presenza di movimenti con data compenteza rilevante, viene emessa una finestra che li riepiloga.
 :  : FLD T$C519 **Divisione**
Valorizzando questo campo, si attiva la gestione della divisione in contabilità.
Le divisioni sono codificate attraverso la tabella C5Q ed attraverso tali elementi possono essere identificati differenti unità organizzative di un'impresa.
Questo tipo di gestione risulta idonea rispetto all'impiego della struttura dell'analitica qualora le unità possano a tutti gli effetti considerate quasi come entità a sè stanti (es. è possibile redarne verosimilmente un bilancio separato).
Attivandola si otterranno questi effetti : 
1. Ogni registrazione dovrà essere obbligatoriamente attribuita ad una divisione. Tale attribuzione potrà essere fissata a livello di tipo registrazione oppure decisa al momento momento dell'immissione della registrazione. Andrà posta quindi particolare attenzione in merito alla configurazione di contabilizzazioni batch (fatturazione attiva in primis).
2. I crediti/debiti saranno gestiti in modo separato (nel saldaconto vedrò solo i crediti/debiti della divisione prevista per la registrazione, nelle distinte non potrò mescolare crediti/debiti di differenti divisioni).
3. Nelle principali interrogazioni contabili sarà possibile filtrare il risultato per divisione.
Il campo può essere impostato con : 
-'1' Si :  viene attivata la gestione della divisione e ogni registrazione potrà avere una ed una
sola divisione
-'2' Multidivisione :  viene attivata la gestione della divisione e ogni registrazione potrà avere
più divisioni ma l'utente dovrà verificare che ci sia sempre quadratura sulla singola divisione
 :  : FLD T$C510 **Presentazione Divisione**
Definisce quale divisione viene presentata all'atto dell'immissione della registrazione.
Può assumenre i valori : 
- ' '  - Default :  la divisione viene ripresa dai parametri aziendali
- '1'  - Campo Bianco.
- '2'  - Ultima :  Ultima divisione utilizzata.

4. Se viene attivata la multidivisione nelle registrazione di incasso e contabilità generale
sarà possibile attribuire più divisioni.
