# GMI - Codice inventario
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$GMIA Descrizione
È la descrizione dell'inventario.
 :  : FLD T$GMID __Data esecuzione__
In formato YYMD indica la data di esecuzione dell'inventario (Le rettifiche di magazzino avranno questa data).
 :  : FLD T$GMIS __Tabelle di sintesi__
Sintesi che verrà utilizzata nella costruzione dell'inventario :  in fase di scrittura dell'archivio GMDAIN0F, è possibile memorizzare per ciascuna riga anche il valore di una delle classificazioni dell'articolo (CLR, CLS, BRA, BRO, .....) in questo campo si deve mettere il nome della tabella desiderato.
Per gestire riclassifiche che non sono comprese nello standard, è possibile gestirle tramite la exit utente GMIN03A_U.
Successivamente l'inventario potrà essere riclassificato secondo questa sintesi..
 :  : FLD T$GMIM __Magazzino assunto__
Si può impostare il magazzino di default.
 :  : FLD T$GMIN __Estrazione Inventario.__
Costruisce un inventario da una giacenza secondo uno dei metodi seguenti : 
1. Partendo dall'anagrafico articoli viene utilizzata la giacenza calcolata alla data di inventario (Campo DATA ESECUZIONE).
_7_ATTENZIONE :  Il calcolo alla data viene eseguito tramite la £GMC per ogni singolo articolo. Verrà pertanto ritornato un valore per articolo, totalizzato in funzione delle parzializzazioni scelte sui codici di giacenza. Per ogni estrazione è obbligatorio indicare area e tipo giacenza.
2. Partendo dall'anagrafico articoli viene utilizzata la giacenza della Foto (Campo FOTO PARTENZA) e alla data inventario (Campo DATA ESECUZIONE).
3. Partendo dall'anagrafico articoli viene utilizzata la giacenza al momento dell'elaborazione.
4. Viene utilizzata la giacenza di una Foto partendo direttamente dall'anagrafico delle FOTO (Campo FOTO DI PARTENZA) e alla data inventario (Campo DATA ESECUZIONE).
5. Viene utilizzata la giacenza al momento dell'elaborazione partendo direttamente dall'anagrafico giacenze.
6. Viene lanciato il programma di estrazione utente.
Le estrazioni Standard permettono di eseguire una stampa di LOG oppure di effettuare una simulazione (senza scrivere l'archivio).
La simulazione genera sempre e solo la stampa di LOG anche se questa non è richiesta.
Per attivare tale opzione, vedere la tabella "PGM" con elemento nome = nome programma (STD SMEUP).
I programmi sono rispettivamente :  GMIN10 (Per opzioni 1. 2. 3.), GMIN11 (Per ozioni 4. 5.).
 :  : FLD T$GMIO __Tipo 1=Eff. 2=Sint__
Sv
 :  : FLD T$GMIP __Codice inven. di sintesi__
Codice in cui verrà costruito l'inventario di sintesi.Sv
 :  : FLD T$GMIF __Foto di partenza.__
Foto di giacenza utilizzata se richiesta elaborazione per FOTO.
 :  : FLD T$GMIB __Rifasatura quantità inventario.__
Aggiorna la quantità prevista sull'inventario.
1. Ripresa quantità giacenza alla data.
2. Ripresa quantità giacenza da Foto(Campo FOTO-RIFASAT.INVENTARIO) ALLA DATA(CAMPO DATA-RIFASAT.INVENTARIO).
3. Ripresa quantità giacenza attuale.
_7_ATTENZIONE :  La rifasatura ripercorre il file degli inventari, pertanto aggiorna la quantità prevista solo degli elementi presenti in questo archivio. Se dovessero esistere ulteriori giacenze, questa operazione non le riprende.
 :  : FLD T$GMIH __Programma estrazione utente.__
Programma che esegue l'estrazione inventario secondo modalità e regole definite dall'utente. Viene lanciato dalla modalità 6 del Campo (ESTRAZIONE INVENTARIO).
