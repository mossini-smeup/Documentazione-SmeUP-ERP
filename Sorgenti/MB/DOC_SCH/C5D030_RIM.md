## Obiettivo
L'obiettivo che si pone la spunta manuale è quello di conciliare i movimenti contabili con i movimenti bancari ricevuti tramite l'importazione del flusso inviato dalla Banca stessa.
Tramite l'utilizzo di questa sezione l'utente potrà manualmente associare i movimenti banca con quelli contabili con gli stessi effetti della spunta automatica.

![C5D030_057](http://localhost:3000/immagini/MBDOC_SCH-C5D030_RIM/C5D030_057.png)
## Parametri di lancio
 * Rapporto Bancario :  specificare quale il rapporto bancario da analizzare.
 * Movimenti :  permette di filtrare : 
 ** i movimenti spuntati (dunque quelli già associati ad una registrazione contabile) ;
 ** tutti, dunque i movimenti già spuntati e quelli ancora da spuntare;
 ** i movimenti annullati e dunque i movimenti su cui è stata precedentemente forzata l'azione di annullamento;
 ** lasciando il campo vuoto otterremo solo i movimenti da spuntare, di prevalente inerenza alla sezione in questione.
 * Forza condizione :  nel caso in cui vengano spuntati movimenti contabili con condizione non attiva (valore della condizione all'interno della registrazione contavìbile diverso da 6) è possibile forzarne l'attivazione in modo che il movimento contabile spuntato venga sempre attivato.
* Ripresa Note :  permette di riprendere all'interno delle note della registrazione contabile la descrizione del movimento che la banca passa all'interno del record di remote banking.
 * Lista Causali Contabili :  consente di filtrare in base al movimento contabile, garantendo maggior efficenza nella selezione di alcuni movimenti piuttosto che altri, risulta particolarmente utile quando i movimenti contabili da associare ai movimenti bancari risultano svariati.
 * Lista Causali ABI :  consente di filtrare in base al codice della causale ABI
 * Tutte le descrizioni :  consente di ottenere l'intera descrizione del movimento bancario con relativa specifica.

## Dettaglio informazioni
All'interno della scheda vengono visualizzati nella metà sinistra i movimenti contabili e nella metà destra i movimenti bancari al fine di rendere immediata la conciliazione.
La matrice relativa ai movimenti contabili presenta : 
* Data Valuta :  viene visualizzata la data valuta inserita sul movimento contabile;
* Data operazione :  è la data operazione impostata sul movimento contabile;
* Importo :  viene visualizzato l'importo dell'operazione
* Causale :  viene visualizzata la causale contabile legata all'operazione
* Descrizione :  viene visualizzata la descrizione riportata sulla riga contabile.

La matrice relativa ai movimenti bancari presenta : 
* Data Valuta :  viene visualizzata la data valuta che è la data di effettiva disponibilità sul conto bancario;
* Data Operazione : indica la data in cui si svolge l'operazione
* Importo : viene visualizzato l'importo dell'operazione, ricevuto dal flusso bancario;
* Causale :  viene visualizzata la causale ABI ricevuta dal flusso Banca : 
* Descrizione : viene visualizzata la descrizione della causale bancaria;

## Opzioni
Movimenti Contabili : 
Forza spunta contabile :  consente di forzare la spunta, "sorvolando" sull'inconciliabilità tra il movimento contabile ed il movimento bancario;
Gestione della registrazione :  consente di modificare,cancellare,interrogare la registrazione contabile.

Movimenti Bancari : 
Forza spunta da banca :  consente di forzare la spunta anche dal punto di vista bancario, "sorvolando" sull'inconciliabiità tra il movimento bancario ed il movimento bancario;
Crea registrazione da Banca :  consente di creare una registrazione partendo dal record di remote banking;
Annulla movimento Banca :  Consente di annullare il movimento dal flusso banca;

## Come Procedere alla Spunta

Al fine di ottenere la conciliazione tra i movimenti contabili ed i movimenti bancari è necessario spuntare i movimenti interessati. Per farlo flaggare il quadratino posto a sinistra del movimento contabile e quello posto a sinistra del movimento bancario : 

![C5D030_058](http://localhost:3000/immagini/MBDOC_SCH-C5D030_RIM/C5D030_058.png)
Confermando con F6 verrà confermata la spunta. La riga del movimento contabile non sarà, quindi, più modificabile e il movimento non comparirà più tra i movimenti da spuntare.

## Come inserire movimenti contabili a partire dal record di remote banking

Per inserire un movimento a partire dal record di remote banking selezionare l'opzione 'Crea registrazione da banca'. A questo punto partirà il data entry della contabilità; nel caso in cui sia stata effettuata l'associazione causale ABI - causale contabile tramite la tabella C5U il sistema proporrà sia la data registrazione (che prenderà dalla data operazione bancaria) che la causale contabile.
Confermando il primo specchietto sarà possibile procedere con il dettaglio della registrazione che potrà essere di due tipologie : 
1- Registrazione di contabilità generale
2- Registrazione di incasso/pagamento
