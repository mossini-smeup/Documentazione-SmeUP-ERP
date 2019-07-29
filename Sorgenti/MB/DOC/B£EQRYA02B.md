# Avvio della ricerca tramite combo-box
A fianco della funzionalità di ricerca in finestra se ne affianca un'altra molto importante, per la semplicità d'uso, che si avvia tramite lo strumento grafico delle combo-box.

La combo-box è uno strumento grafico che permette di effettuare scrivendola o selezionandola da un elenco in cui vengono presentate le istanze selezionabili con la propria descrizione.

Quando è attivata la possibilità di ricercare tramite combo-box, a fianco del campo di imputazione viene aggiunto un bottone, attraverso il quale potrà essere avviata la funzione di ricerca.

Possono essere attivate due tipologie di combo-box : 
* combo-box su elenco completo
* combo-box su funzione di ricerca

# Combo-box su elenco completo

La prima identificabile dall'icona riportata a seguire permette di ricercare il codice all'interno dell'elenco completo delle istanze della classe stanziata. Quindi quando ricerco viene sempre presentato l'elenco completo per codice.

![B£EQRY_05](http://localhost:3000/immagini/B£EQRYA02B/BXEQRY_05.png)
# Combo-box su funzione di ricerca

La seconda identificabile dall'icona riportata nell'immagine a seguire, riguarda normalmente classi per le quali le istanze sono molto numerose (al di sopra del migliaio, come può avvenire per i codici clienti o gli articoli). Non essendo per tali classi possibile presentare l'intero elenco delle istanze si è aiutati a ricercare sull'elenco tramite l'applicazione di filtro. Tale filtro è costituito dal valore contenuto nel campo nel momento in cui si sta cercando. Tale valore può essere applicato alla ricerca secondo tre modalità : 
* Se viene apposto un " : " verrà eseguita la funzione di ricerca per codice, verrà effettuata una ricerca ordinata per codice in cui verranno presentati i risultati che presentano nel codice o nella descrizione i caratteri indicati nei caratteri successivi al carattere " : "
* Se viene apposto un "!" verrà eseguita la funzione di ricerca per codice, con posizionamento al codice uguale/successivo ai caratteri indicati dopo il carattere "!"
* Se viene apposto un "?" verrà eseguita la funzione di ricerca per codice, con posizionamento alla descrizione uguale/successivo ai caratteri indicati dopo il carattere "?"
* Se non viene apposto nessuno dei suddetti caratteri speciali verrà effettuata una ricerca ordinate per codice in cui verranno presentati i risultati che presentano nel codice o nella descrizione i caratteri indicati nel campo.

![B£EQRY_06](http://localhost:3000/immagini/B£EQRYA02B/BXEQRY_06.png)
NOTA BENE :  quando è attiva la funzionalità del combo-box, il tasto funzione F04 invece che lanciare la funzione di ricerca principale esegue la funzione di ricerca collegata alla combo box.

