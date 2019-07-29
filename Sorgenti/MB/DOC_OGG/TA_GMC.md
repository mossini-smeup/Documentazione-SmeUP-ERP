# GMC - Causali di movimentazione
## OBIETTIVO
Impostare i parametri che guidano la movimentazione di magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$GMCP __Programma specifico__
Se impostato, viene lanciato all'atto di una transazione che si effettua con questa causale.
Dopo questo programma, se impostato in tabella GM1, si lancia una exit generale.
E' possibile impostando opportunamente il ritorno di questo programma (riferirsi all'esempio)
disattivare, per questo programma, il lancio dell'exit generale.
 :  : FLD T$GMCA __Area giacenza__
È un elemento della tabella GMR :  va impostato obbligatoriamente insieme con il tipo giacenza :  il movimento agirà sull'archivio giacenze sull'area qui definita.
 :  : FLD T$GMCT __Tipo giacenza__
È un elemento della tabella GMQ :  se impostato significa che il movimento deve avere un effetto sull'archivio giacenze, e in particolare sul tipo giacenza qui definito.
 :  : FLD T$GMCQ __Tipo quantità__
Definisce la quantità che verrà usata nell'aggiornamento dell'archivio giacenze (se previsto) :  se si imposta 'A', si userà la quantità in unità di misura alternativa, altrimenti la quantità in unità di misura interna.
 :  : FLD T$GMCM __Tipo movimento__
È un elemento dei valori fissi SMEUP V2/GMTMO :  definisce la natura del movimento. È un campo obbligatorio in quanto le informazioni statistiche sui movimenti di un articolo (ultimo prezzo, ultima data entrata, ecc..) si basano su di esso.
 :  : FLD T$GMC1 __Azione Q.Giac.__
Definisce l'azione ('+' positiva, '-' negativa, ' ' nessuna), sul campo giacenza nell'aggiornamento dell'archivio giacenze (se previsto).
 :  : FLD T$GMC2 __Azione Q.Alloc.__
Definisce l'azione ('+' positiva, '-' negativa, ' ' nessuna), sul campo quantità allocata nell'aggiornamento dell'archivio giacenze (se previsto).
Normalmente, in una gestione dell'allocato tramite richieste di movimentazione, l'azione deve essere '-', in quanto il movimento chiude la richiesta.
In inserimento del movimento, questa azione viene sempre eseguita, mentre in variazione e annullamento solo se impostato il campo esposto successivamente.
 :  : FLD T$GMC3 __Azione Q.Attesa__
Definisce l'azione ('+' positiva, '-' negativa, ' ' nessuna), sul campo quantità attesa nell'aggiornamento dell'archivio giacenze (se previsto).
Valgono le stesse considerazioni fatte per l'azione sulla quantità allocata.
 :  : FLD T$GMCV __Applica anche in variaz/annulamento__
È un elemento fisso V2 SI/NO :  se impostato, le azioni sulla quantità allocata ed attesa sono eseguite anche in variazione e in annullamento.
Nel seguito di questa esposizione, le considerazioni fatte sull'allocato sono estendibili all'atteso.
Normalmente, la transazione di magazzino che riduce l'allocato, è quella che esegue l'applicazione della richiesta di movimentazione che, all'atto della assegnazione, aveva aumentato l'allocato.
Quando si annulla (o si varia) questo movimento, viene riaperto l'allocato, senza che sia riaperta la richiesta di movimentazione; quindi, se si imposta questo flag, si ha l'effetto di una allocazione indebita.
Si deve impostare questo flag se si vuol impostare una gestione particolare, senza passare dallle richieste di movimentazione dell'allocato, con un movimento che lo apre ed un altro che lo chiude. In questo caso, si deve far attenzione a non eseguire la rifasatura dell'allocato, perchè essa parte dalle richieste di movimentazione attive.
 :  : FLD T$GMCR __Applica solo se IDDM__
È un elemento fisso V2 SI/NO :  se impostato, le azioni sulla quantità allocata ed attesa sono eseguite esclusivamente se sul movimento e' presente il numero di richiesta di movimentazione. Questa impostazione permette di non dover avere causali specifiche per l'utilizzo delle richieste movimentazione e specifiche per movimenti extra richieste.
 :  : FLD T$GMCC __Causale collegata__
È un elemento di questa stessa tabella GMC :  se impostato, dopo aver eseguito la movimentazione (scritto il movimento e aggiornato l'archivio giacenze), viene agganciata questa causale ed eseguito un ulteriore aggiornamento sull'archivio giacenze, secondo le sue impostazioni. Il processo si ripete con l'eventuale ulteriore causale, collegata alla precedente, e si interrompe quando si raggiunge una causale che ha la collegata in bianco.
In questo modo, con un solo movimento di magazzino, si possono aggiornare diverse giacenze.
Va tenuto presente che le causali collegate devono avere tutte lo stesso comportamento nei confronti della giacenza (tutte entrate o tutte uscite). Non servono nel caso in cui si voglia fare un movimento di trasferimento in 'partita doppia', che riduce un'area e ne aumenta un'altra :  in questo caso si devono scrivere due movimenti (infatti è normale aspettarsi che essi abbiano caratteristiche diverse, ad esempio l'ubicazione o l'ente, e quindi il singolo movimento
di magazzino non può che descrivere un'attività elementare di entrata o uscita).
La causale collegata si applica, invece, nei casi in cui la stessa attività elementare ha effetto su più giacenze, ad esempio nel caso in cui si voglia tener conto della giacenza in diverse unità di misura, oppure tenere più livelli di sintesi (giacenza in dettaglio per fornitore e giacenza per tutti i fornitori).
Se si vuole invece eseguire un'attività di trasferimento : 
- se è accompagnata da un DDT, va creato un documento di ciclo esterno di trasferimento (con righe il cui tipo contiene due causali di magazzino).
- se invece è all'interno dell'azienda, può essere svolta impostando, e poi eseguendo, una richiesta di movimentazione di trasferimento, direttamente nella movimentazione, con la funzione di trasferimento tra aree.
 :  : FLD T$GMCF __Forma presentazione__
È un elemento della tabella B£Q :  se impostato, la gestione di questo movimento (inserimento variazione annullamento, con gli eventuali filtri di autorizzazioni) è permessa e guidata dal programma contenuto in questa tabella. Se questo campo è lasciato in bianco è impedita la gestione interattiva del movimento (insermento/variazione/annullamento).
 :  : FLD T$GMCI __Parametri impliciti__
È un elemento della tabella C£I. Definisce la natura dei campi liberi (5 numerici e 5 alfanumerici) del movimento.
 :  : FLD TGMCI1 __Elemento di raggrup.__
È un elemento della tabella IGIMG; indica il che il movimento ha valenza fiscale ed indica il codice di raggruppamento. Se lasciato a blank, il movimento non ha valenza fiscale.
 :  : FLD TGMCI2 __2° Elemento raggrup.__
Esiste la possibilità di indicare un secondo raggruppamento (sempre della tabella IGIMG). Questa viene registrata con quantità invertita. Questo campo viene utilizzato se presente una causale neutra ma che si desidera considerare nei contenitori mensili (IGSTOR0F).
 :  : FLD T$GMCU __Gruppo autorizzazione__
Se valorizzato (deve essere un codice tra 1 e 9, oppure lasciato vuoto), è il gruppo di autorizzazione x a cui appartiene questa causale, con cui si imposta la funzione MOV-MAGx. Essa, insieme con la  classe ABILITA, definisce, per ogni utente, le abilitazioni (di inserimento, variazione e annullamento) alle movimentazioni eseguite con questa causale.
 :  : FLD T$GMCW __Attività collegamento__
È un elemento della tabella GMH. Se impostato, all'atto della scrittura di un movimento con questa causale, verranno eseguite le attività comandate da questa tabella.
 :  : FLD T$GMCZ __Attività inserimento__
È un elemento della tabella GMH. Se impostato, nel programma di monitor, all'atto dell'inserimento di un movimento con questa causale, verranno eseguite le attività comandate da questa tabella.
 :  : FLD T$GMCN __Natura__
Definisce la natura del movimento, in base a come esso aggiorna la situazione della giacenza. È utilizzato dalla navigazione della tracciabilità lotti e dalle statistiche, per individuare i movimenti di entrata, uscita, carico, scarico e trasferimento.
 :  : FLD T$GMCB __Forza ut.__
Se si imposta questo campo, e se in GMTRAN è stato riempito il campo utente di aggiornamento, esso viene copiato nel campo corrispondente del movimento.
