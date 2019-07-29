# Introduzione
Tramite questa scheda è possibile eseguire le azioni necessarie per : 
* Ricerca
* Selezione
* Creazione
di un nominativo.

# Struttura della scheda

## Sezione Richiesta Parametri
In questa sezione è possibile inserire il valore dei campi tramite i quali poter identificare il nominativo. Tutti i campi eccetto quelli oggettizzati applicano, un filtro in scansione :  quindi posso scrivere anche solo una parte della parola che mi interessa e questa verrà confrontata con i dati verificando se essa è contenuta nella riga di confronto. Posso scrivere anche più parole e ognuna di esse verrà cercata all'interno delle righe. Es. se nel campo ragione sociale scrivo "ROSSI" mi verranno ritornati tutti i nominativi che nella ragione sociale riportano la parola "ROSSI" come ad esempio "ROSSIGNOLO SRL", "MARCO ROSSI", "MAROSSI ROBERTO" ecc..
In tale scansione non viene inoltre controllata la differenza fra caratteri minuscoli (scrivendo ROSSI troverei quindi anche una ragione sociale scritta come "Rossi Mario").

![BRENTI_21](http://localhost:3000/immagini/MBDOC_SCH-CN_RNOM/BRENTI_21.png)
## Sezione Elenco Nominativi
In questa sezione ho l'elenco dei nominativi che risultano corrispondere alle domande poste nella sezione di richiesta parametri. L'operatività di tale sezione cambia a questo punto a seconda che sia entrato : 
* In ricerca di un qualsiasi nominativo
* In ricerca di un nomativo corrispondente ad un altro contatto (es. Cliente o Fornitore)

Nel primo caso mi viene riportato l'elenco di tutti i nominativi corrispondenti alle domande poste in ricerca e posso fare queste azioni : 
* Selezionare il nominativo che mi interessa in quanto sono riuscito ad identificarlo
* Ripetere la ricerca
* Se opportuno premere F07 per inserire un nuovo nominativo, in quanto quello interessato non risulta inserito
* Abbandonare

Nel secondo caso ho comunque tutti i nominativi corrispondenti alle domande poste ma ho in più l'indicazione anche del fatto che il nominativo corrisponda o meno ad un contatto pre-esistente in azienda.

Di seguito viene riportato l'esempio del risultato della ricerca, del primo caso e del secondo caso.

![BRENTI_22](http://localhost:3000/immagini/MBDOC_SCH-CN_RNOM/BRENTI_22.png)
![BRENTI_23](http://localhost:3000/immagini/MBDOC_SCH-CN_RNOM/BRENTI_23.png)

