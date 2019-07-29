## Abstract
Il componente Dash (DSH) mostra un dato tramite una forma a cruscotto, disponibile in diversi layout.
I layout che si possono scelgiere sono 8 e non possono essere aggiunti dall'utente.
E' possibile scegliere il layout di visualizzazione attraverso l'attributo di setup "SelectLayout".
Tutti gli esempi utilizzabili, sono consultabili nel nostro showcase dei componenti.

Per popolare il componente dash è possibile valorizzarlo anche passando i valori tramite G.SET del componente. utilizzando gli attributi ForceText, ForceUM, ForceValue e ForceIcon.
E' possibile, nel caso si abbia una matrice con più colonne, andare a specificare il nome della colonna da cui prendere i valori. utilizzando gli attributi TextColName, UmColName, ValueColName e IconColName.
In questo componente è anche possibile, specificando il nome della colonna, effettuare delle operazioni matematiche che forniscono un risultato, visualizzato poi all'interno del dash.
Grazie ad un attributo di setup è possibile formattare il valore mostrato.

Le informazioni che il componente può leggere nella griglia XML che rappresenta i suoi dati  sono (in ordine) : 
- Valore
- Unità di misura
- Descrizione
- Icona

Il componente supporta il dinamismo "click".

