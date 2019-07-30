# Draw Plates - Disegno Pannelli di Cassa

## Draw Plates - Disegno Pannelli di Cassa

Il programma di Cassa di Negoziando è stato pensato per un utilizzo su schermo touch screen, per cui la quasi totalità delle funzioni è attivabile da 'Bottoni' disegnati sullo schermo che compongono un 'Pannello di cassa', in gergo denominato 'Plate'.
Il layout è completamente personalizzabile per ottenere un pannello di cassa più funzionale alle esigenze del punto vendita e/o dell'operatore :  è possibile inserire o togliere Bottoni, raggrupparli in tabSheet, abbinarli a tasti o combinazioni di tasti della tastiera, impostarne l'aspetto, stabilire dei permessi sull'utilizzo.

Dal Menu _Utilità>Personalizzazioni>Disegno Pannelli di Cassa_
Lanciando il programma comparirà una schermata, premendo sul menu a tendina File appariranno le funzionalità disponibili : 

 * Open
 * Save
 * Save As
 * Exit

## Funzione Open

Richiamando la funzione Open è possibile aprire un file .XML contenente un pannello di cassa esistente e caricarlo a video per modificarne il contenuto. Selezionare il percorso contenente il file da modificare e premere Apri.
Si è deciso di partire sempre da un file esistente e di modificarne il contenuto in quanto nell'installazione standard di Negoziando viene sempre distribuito un pannello di default dal quale partire per la personalizzazione.
A questo punto è possibile : 

 * spostare i bottoni posizionandosi sul tasto da cambiare e trascinandolo tenendo sempre premuto il tasto sinistro del mouse.Il cursore assumerà l'aspetto di una croce
 * ridimensionare  i bottoni posizionandosi sui bordi del tasto. Il cursore assumerà l'aspetto di una freccia che indica la possibilità di ridimensionamento
 * spostare il bottone anche in un altro tabsheet tenendo premuto il pulsante Ctrl della tastiera e trascinando lo stesso sulla linguetta relativa all'intestazione del pannello nel quale si vuole che vada a finire
 * cliccare col tasto destro su un bottone per visualizzare il menu a tendina che permette di effettuare alcune operazioni sulle caratteristiche del tasto stesso : 
 ** New Button :  permette di creare un nuovo bottone associando le caratteristiche necessarie
 ** Edit Button :  permette di modificare le caratteriste del bottone
 ** Delete Button :  permette di eliminare un bottone dal pannello di cassa
 ** Duplicate Button :  permette di duplicare un bottone creandone uno nuovo con le stesse caratteristiche
 ** Send to Back :  porta in secondo piano il bottone, nel caso di sovrapposizione di più bottoni
 ** Bring to Front :  porta in primo piano il bottone, nel caso di sovrapposizione di più bottoni
 ** Deselect all Buttons

In caso di inserimento e modifica delle caratteristiche dei bottoni verrà presentata una maschera che permette di modificare i dati e verranno richiesti : 

 * Titolo :  permette di specificare la descrizione da visualizzare sul bottone. E' possibile separare la descrizione con il simbolo | (pipe) per mandare il testo a capo
 * Hint :  permette di specificare un descrizione che verrà visualizzata come una tooltip vicino al bottone
 * KeyCode :  permette di selezionare il tasto funzionale o la combinazione di tasti per attivare la funzione direttamente da tastiera senza l'utilizzo di tasti funzionali.
 * Function Code :  permette di selezionare la funzione da attribuire al bottone. In coda a questo dcoumento l'elenco completo delle funzioni disponibili.
 * Attributi : permette di specificare eventuali attributi facoltativi o obbligatori legati alla funzione.
 * Livello Autorizzazione :  permette di specificare un livello di autorizzazione per la funzione specificata. E' un codice alfanumerico. Alcune funzioni potrebbero essere disabilitate ad alcuni operatori.
 * Stile :  permette di definire lo stile del bottone, ovvero le sue caratteristiche grafiche. E' possibile scegliere il colore di primo piano e della scritta.
 * Posizionamento :  definisce in che TabSheet deve essere posizionato il bottone
 * A Capo Automatico : in automatico, se viene inserita una descrizione che non può essere mostrata su una singola riga, il sistema manderà a capo  adattando il testo alla larghezza del bottone

Esistono altre funzionalità che non riguardano principalmente i bottoni, ma altri elementi dell'interfaccia grafica. Premendo con il tasto destro su un'area vuota del pannello verrà presentato
un menù a tendina : 

 * New Button=Permette di creare un nuovo bottone. E' la stessa funzione del menù a tendina che si presenta sui bottoni.
 * Plate (New, Edit, Delete) =permettono di modificare le caratteristiche di un TabSheet (Plate)
 ** New = Inserimento di un nuovo Plate
 ** Edit = Modifica del Plate
 ** Delete = Cancellazione del Plate
Queste funzionalità richiamano una maschera, che, a sua volta, richiede alcuni valori (consigliamo, di default, di utilizzare i seguenti valori) : 
 ** Titolo
 ** Larghezza : 10
 ** Altezza : 10
 ** Larghezza Bottoni : 15
 ** Altezza Bottoni : 15
 * Manage Style= Permette la gestione degli stili da attribuire ai bottoni.Verrà presentata una griglia in cui sono elencati tutti gli stili disponibili con possibilità di modificare, aggiungere, rimuovere uno stile.
 * Manage Plates=Permette di gestire le caratteristiche del contenitore dei pannelli denominato Plates. E' possibile indicare i tasti per passare da un pannello all'altro direttamente da tastiera senza l'utilizzo del mouse.E' possibile indicare le dimensioni di altezza e larghezza dei tabsheet.

## Funzione Save, Save As

Richiamando la funzione Save è possibile salvare il file XML di cui si sta modificando il contenuto. Richiamando la funzione Save as è possibile salvare il file XML di cui si sta modificando il contenuto, attribuendo un nuovo nome.

## Funzione Exit

Permette di uscire dal software. Nel caso fossero state effettuate modifiche al pannello l'operatore verrà avvisato richiedendo la conferma di uscita.


## Funzioni Disponibili


| 
| .COL Txt="Codice Funzione" Lun="70" |
| ---|----|
| 
| .COL Txt="Descrizione"  A="L" |
| BOARDINGPASS|Richiesta Boarding Pass |
| BOOKING|Emissione Prenotazione Cliente |
| CASHMOVEMENTS|Registrazione Entrate Uscite di Cassa |
| CHANGEOPPWD|Cambia Password Operatore |
| CLEAR|Pulisci testo digitato |
| CORR|Correzione (Cancella Riga) |
| CUSTFISCCODE|Richiesta Codice Fiscale |
| DELETESELECTED|Cancella Riga Selezionata |
| DEPARTMENT|Vendite a Reparto |
| DIGIT|per Indicare singole cifre o lettere |
| DISCLINEAMOUNT|Sconto di Riga (Importo) |
| DISCLINEPERC|Sconto di Riga (Percentuale) |
| DISCSUBTAMOUNT|Sconto SubTotale (Importo) |
| DISCSUBTFIDELY|Sconto SubTotale Clienti Fidelity |
| DISCSUBTPERC|Sconto  SubTotale (in Percentuale) |
| DISPLAYPRICE|Visualizza Prezzo |
| DSPCSHCLOSE|Imposta/Toglie Display Cassa Chiusa |
| DSPFIDPOINTS|Visualizza Punti Tessere Fidelity |
| DSPGIFTINFORM|Visualizzazione Informazioni Gift Card |
| DSPPRODUCTSHEET|Visualizzazione Scheda Prodotto |
| DSPSUSPENDED|Visualizzazione Scontrini Sospesi |
| DSPTOTCURRENCY|Visualizza Importo in Valuta |
| EXTFUN|Esecuzione di una Funzione Esterna |
| FIDELITYCARD|Indicazione di un Codice Fidelity |
| FIDELITYSEARCH|Ricerca Nominativi Fidelity |
| GETADVANCE|Ritiro Acconto |
| GETPAYMENT|Pagamento |
| GETPLVOUCHER|Utilizzo Voucher Pasti Prepagati |
| GETREPAIR|Merce da Riparare |
| GETVOUCHER|Ritiro Buono |
| GIFTPAYMENT|Pagamento con Tessera Regalo |
| GIFTRECEIPT|Gestione Stampa Scontrino Regalo |
| INTFUN|Esecuzione di una Funzione Interna |
| LOCKPLATES|Blocca Tastiera |
| OC_SELECT||Selezione Ordine Cliente |
| OPENDRAWER|Apertura Cassetto |
| PDQ|Incasso tramite POS collegato |
| PLU|Codice |
| PLULIST|Plu da Elenco |
| PRICE|Imposta Prezzo |
| PUTADVANCE|Storno Acconto |
| PUTPAYMENT|Storno Pagamento |
| PUTPROMOVOUCHER|Emissione Buoni per Promozioni |
| PUTREPAIR|Consegna Merce Riparata |
| PUTVOUCHER|Emissione Buono |
| QUANTITY|Imposta Quantità |
| RELOADPLATES|Ricarica Pannello di Cassa |
| REPRINTPDQ|Ristampa Scontrino POS |
| REPRINTRECEIPT|Ristampa Ricevuta |
| RESETOPERATOR|Cancella Operatore |
| RETURN|Imposta Reso |
| SCROLLDISP|Scroll Righe Display Cassa |
| SEARCHBOOKING|Ritiro Prenotazione Cliente |
| SERVICE|Associazione Servizi |
| SERVICEFUNCTIONS|Funzioni di Servizio |
| SETDISCOUNT|Imposta Sconto sulla Riga Selezionata |
| SETNOTAX|Disabilita Tasse su Scontrino |
| SETOPERATOR|Imposta Operatore |
| SETPRODFORSALE|Impostazione Prodotto in Vendita |
| SETTARE|Impostazione Tara |
| SETVAR|Imposta Documento / TaxFree / Listino |
| SHIFTCLOSURE|Chiusura Turno Operatori |
| SHOWPOPUP|Popup Plates |
| SHUTDOWN|Riavvio/Spegnimento PC |
| SUBTOTAL|Subtotale |
| TICKETRETURN|Reso con Scontrino |
| TOTAL|Incasso |
| USEDCOLLECTION|Ritiro Prodotti Usati |
| VATEXEMPTION|Imposta Iva specifica |
| VOID|Pulisci Scontrino |
| WITHDRAWFORSAFE|Registrazione Prelievi per Cassaforte |
| WRITEVOUCHER|Scrittura/Attivazione Buoni di Cassa |
| XREPORT|Stampa Rapporto X |
| ZREPORT|Stampa Rapporto Zeta |
| 


Sme.UP
Last Rev 16/03/215
