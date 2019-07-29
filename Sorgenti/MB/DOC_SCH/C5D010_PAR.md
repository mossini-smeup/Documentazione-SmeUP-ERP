## Obiettivo
Analizzare e pareggiare le scadenze negative aperte per un ente o per una lista di enti.

![C5D010_066](http://localhost:3000/immagini/MBDOC_SCH-C5D010_PAR/C5D010_066.png)
## Parametri di lancio
 * Codice oggetto :  in funzione dell'oggetto scelto all'interno del surf in questo campo sarà necessario indicare il codice cliente, la lista clienti, il codice fornitore, ecc. da analizzare
 * Raggruppa/Includi Soggetti :  nel caso in cui un cliente sia anche fornitore attraverso questo parametro è possibile vederne la posizione netta e, quindi, includere sia le scadenze attive che quelle passive. In questo parametro sarà necessario indicare come effettuare il collegamento cliente/fornitore. Le scelte possibili sono : 
 ** Per codice fiscale / Partita IVA :  il sistema cerca di accoppiare i clienti/fornitori in funzione del codice fiscale/partita iva
 ** Per ente corripondente :  il sistema leggerà l'ente corrispondente impostato sull'anagrafica del cliente/fornitore
 ** Per Nominativo :  il sistema risalirà al nominativo comune tra cliente e fornitore
 ** Per ente di gruppo :  attraverso questo campo è possibile individuare dei gruppi aziendali. Il gruppo a cui appartiene un soggetto è impostabile tramite l'estensione anagrafica £53
 * Cumuli Effetti :  in caso di effetti cumulati permette i visualizzare una scadenza unica o il dettaglio delle scadenze
 * Schema :  permette di impostare uno schema sulle colonne visualizzate
 * Righe per pagina :  permette di aumentare il numero di righe mostrato al lancio della funzione (di default vengono presentate le prime 1000 righe).

## Dettaglio informazioni

Nel caso in cui per il/i soggetto/i analizzato/i siano presenti almeno una scadenza con segno positivo e una scadenza con segno negativo verrà esposto l'elenco di tutte le scadenze aperte per il soggetto stesso.
Selezionando, poi, scadenze di segno opposto sarà possibile pareggiarle digitando il tasto F06 Conferma Pareggio : 

![C5D010_067](http://localhost:3000/immagini/MBDOC_SCH-C5D010_PAR/C5D010_067.png)
Nel caso in cui si sia compilato il parametro "Raggruppa/Includi Soggetti" sarà anche possibile pareggiare partite di clienti diversi e partite di clienti con partite di fornitori.
Se la scheda viene eseguita su una lista di enti sarà anche possibile pareggiare tra loro partite di soggetti diversi (es. fornitore ABC spa con cliente ZZZ srl)
