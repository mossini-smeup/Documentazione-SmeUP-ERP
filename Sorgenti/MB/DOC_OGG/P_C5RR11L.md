# OPZIONI LISTA
All'interno del saldaconto sono disponibili le seguenti opzioni : 

 * 1 Visualizzazione Testata :  visualizza le funzioni della testata di registrazione della rata
 * 2 Visualizzazione Riga :  visualizza le funzioni della riga di registrazione della rata
 * 3 Visualizzazione Rata :  visualizza le funzioni della rata
 * 4 Visualizzazione Ritenute d'acconto :  nel caso in cui alla rata sia associata una ritenuta d'acconto permette di visualizzarne il dettaglio
 * 5 Visualizza protezioni su rata :  nel caso in cui la rate risulti protetta e non saldabile permette di evidenziare il motivo del blocco
 * 6 Gestione Nota di Rata Dovuto :  permette di entrare in gestione delle note presenti sulla rata aperta
 * 7 Gestione Blocco Rata :  nel caso in cui la rata risulti bloccata e l'utente sia abilitato permette di modificare o cancellare il blocco sulla rata stessa
 * 8 Visualizza CUP/CIG :  nel caso in cui alla rata aperta siano associati un CUP/CIG permette di visualizzarli
 * 9 Visualizza Dettaglio Rata Dovuto :  permette di visualizzare il dettaglio della rata aperta
 * D Elimina importo :  nel caso in cui si sia già compilata la colonna 'Versamento al netto' permette di ripulirla automaticamente
 * R Ripristino residuo iniziale :  nel caso in cui si entri in modifica di una registrazione e si modifichi l'importo saldato sulla rata, questa opzione permette di ripristinare l'importo iniziale
 * S Saldo residuo :  permette di saldare completamente la rata
 * F Saldo residuo e forza sconto :  è utilizzabile solo se il codice pagamento prevede uno sconto e permette di effettuare lo sconto stesso anche se oltre i termini previsti dai parametri della PAG. Quindi se sulla tabella PAG è impostato uno sconto del 5% se il pagamento avviene entro 30gg e il cliente paga dopo 45gg sarà possibile forzare lo sconto indicando l'opzione F.
 * P Saldo residuo con % sconto :  è utilizzabile anche se il codice pagamento della rata non prevede alcun sconto e permette di immettere uno sconto percentuale. Per farlo è necessario indicare nella colonna 'Versam.al netto' il valore percentuale, digitare l'opzione P e dando invio il sistema compilerà la colonna Versam.al netto con l'importo scontato della percentuale indicata e la colonna 'A' con il valore S di sconto.
 * I Saldo residuo con importo sconto :  è utilizzabile anche se il codice pagamento della rata non prevede alcun sconto e permette di immettere uno sconto a valore. Per farlo è necessario indicare nella colonna 'Versam.al netto' il valore da scontare, digitare l'opzione I e dando invio il sistema compilerà la colonna Versam.al netto con l'importo scontato del valore indicato e la colonna 'A' con il valore S di sconto.
 * Z Saldo rate stessa scadenza :  permette di saldare completamente tutte le rate con la stessa scadenza
 * G Saldo rate stessa scadenza e forza :  ha la stessa funzione dell'opzione F ma esegue l'azione su tutte le rate che hanno la stessa scadenza di quella su cui si scrive l'opzione.
 * M Modifica anticipo :  nel caso in cui si sia inserito un anticipo di tipo 4 permette di modificarlo

# OPZIONI ANTICIPO
* 1 :  crea un anticipo con numerazione e tipologia automatica
* 2 :  permette di creare un anticipo riprendendo però i riferimenti di una partita già esistente
* 3 :  con l'importo in più non verrà creato un anticipo, ma verrà creata una seconda contropartita
* 4 :  crea un anticipo per il quale sarà possibile imputare manualmente tutte le caratteristiche dell'anticipo. Solo per questo caso viene un anticipo che viene mantenuto ad ogni richiamo del saldaconto. Nei casi 1 e 2 invece ogni riconferma della schermata del saldaconto comporterà la cancellazione e la ricreazione dell'anticipo. Solo per questo caso inoltre, l'anticipo richiamando il saldaconto, sarà proposto nell'elenco di tutte altre scadenze aperte.

# TASTI FUNZIONALI

* F02 :  seguito da F01 permette di accedere alla documentazione del saldaconto
* F03 :  permette di uscire dalla funzione
* F05 :  permette di aggiornare la videata
* F06 :  permette di confermare la selezione effettuata
* F07 :  permette di confermare il saldaconto sull'ente attuale e inserirne uno nuovo
* F08 :  permette di distribuire l'importo indicato nello specchietto precedente o nella casella 'Importo' in alto a sinistra sulle rate aperte partendo da quelle con scadenza minore
* F09 :  permette di saldare tutte le rate aperte presenti
* F13 :  permette di accedere alle parzializzazioni
## F17 Impostazioni


- Importo Rata :  Determina il tipo di importo visualizzato nella colonna "Importo Rata"; è possibile scegliere tra Importo Rata e Residuo Lordo
- Gestione Rate :  Deterima se riportare nella visualizzare anche le rate che per un qualche motivo non sono saldabili. Nel caso si scelga di visualizzarle tramite l'opzione di lista 5 è possibile vedere il motivo del blocco.
- Aggiornam.Contropartita :  Permette di indicare (compatibilmente anche alle impostazioni del tipo di registrazione) se si vuole che alla conferma del saldaconto la contropartita venga aggiornata
nel suo importo.
- Disattiva Blocco pagamento :  Permette di disattivare il controllo sul blocco pagamento e,quindi, di saldare anche le rate bloccate
- Contabilizzazione effetti :  Permette saldare anche effetti attivi da saldaconto,  questa opzione dovrebbe essere attivata solo se la contropartita è il conto del portafoglio effetti.
- Seconda Contropartita :  è la contropartita che viene utilizzata se c'è un differenza fra l'importo selezionato sulle singole rate e l'importo previsto per la riga, qualora per tale differenza venga attribuito il valore 3 nel campo anticipo. Questo significa che con questa impostazione l'importo in più non genererà un anticipo sul soggetto ma solo una riga di contropartita aggiuntiva. Ad esempio se la banca mi comunica un bonifico di 98 a fronte di una scadenza di 100 compilando il Versamento al netto con 100, il campo 'Anticipo' con 3 e indicando in questo conto il conto delle spese bancarie il sistema mi presenterà la scrittura già completa.
- Ordinamento :  indica l'ordinamento delle scadenze nella lista
- Riferimenti :  indica se nel colonna "N° Documento" voglio vedere il n° fattura originale o il n° di protocollo
- % Sconto 1 :  permette di applicare uno sconto finanziaro sul saldo anche quando questo non è previsto dal codice pagamento
- % Sconto 1 :  permette di applicare un secondo sconto finanziaro sull'importo al netto del primo 1° sconto.

