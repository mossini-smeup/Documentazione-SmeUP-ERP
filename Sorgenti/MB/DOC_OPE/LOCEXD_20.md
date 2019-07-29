# Novità dell'interfaccia V4R1


## La nuova interfaccia

![LOCEXD_050](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_050.png)

## Barra del titolo

La nuova barra del titolo occupa meno spazio e contiene **il titolo** e il **sottotitolo** della scheda, **i bottoni**, il **menu UP** e la nuova **command bar**

![LOCEXD_051](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_051.png)
## Command Bar

E' stata introdotta la Command Bar, una **riga di comando sempre visibile**.
_Al momento riceve gli stessi comandi che erano gestiti dall'F21 (Alias)_

![LOCEXD_057](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_057.png)



## Menu Principale

Tutti i menu delle finestra sono stati condensati nel menu UP

![LOCEXD_054](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_054.png)

## Bottoni di Finestra

E' scomparsa la bottoniera principale in basso a destra. Tutte le funzioni sono state spostate o riviste.

![LOCEXD_052](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_052.png)
F1  (Help)                  - Spostato in alto
F3  (Chiudi)               - Dismesso
F4  (Oggetto)            - Spostato - Sostituito da alias 'O' nella Command Bar e dall'F4 sempre dalla Command Bar
F5  (Aggiorna)           - Spostato in alto
F12 (Indietro)            - Spostato in alto
F19 (Preferito)          - Spostato in alto
F21 (Barra comandi) - Dismesso - Ora posiziona il fuoco nella Command Bar
F23 (Esci)                 - Sostituito dalla X della finestra
Bottoni aggiunti dai servizio alla scheda - Spostati in alto




## Bottoni del componente e della sezione

I bottoni specifici **del componente** sono stati spostati nella sezione stessa. E' possibile nasconderli.
I bottoni del **gruppo sezione** sono stati spostati nella sezione stessa. E' possibile nasconderli.

![LOCEXD_056](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_056.png)
### Bottoni associati alla tastiera

I tasti funzione (F1-F24) associati ai bottoni continuano a funzionare.
Nel caso lo stesso tasto F sia definito, nella stessa finestra, in bottoni diversi : 
- al click del mouse, vince quello su cui si è fatto click
- alla pressione del tasto, vince il quello della sezione su cui è presente il fuoco.

Nel caso di sovrascrittura nello stesso gruppo, vince l'ultimo definito (in ordine di caricamento delle sezioni). Si consiglia pertanto di non sovrascirverli.

### Bottoniera di sezione
Il comportamento della bottoniera di sezione può essere definito tramite l'attributo ToolbarState della sottosezione.
- Collassata (Collapsed) :  parte chiusa
- Espansa (Expanded) :  parte aperta
- Invisibile (Invisible) :  non è presente

Esistono dei default : 
- Se la sezione è piccola, parte chiusa
- Se la sezione è una label, un bottone, un gauge, un semaforo, parte invisibile
- Negli altri casi, parte chiusa, a me no che non ci sono bottoni aggiunti o setup multipli


## Bottoni di scheda

I bottoni del **gruppo scheda** sono stati spostati nella barra del titolo

![LOCEXD_055](http://localhost:3000/immagini/MBDOC_OPE-LOCEXD_20/LOCEXD_055.png)