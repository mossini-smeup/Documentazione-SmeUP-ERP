# Obiettivo
Gestione dei corsi e dei partecipanti al corso.

## Formato guida
![CQ_PERS_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP21/CQ_PERS_02.png)
## Formato Lista
![CQ_PERS_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP21/CQ_PERS_03.png)
## Formato dettaglio
![CQ_PERS_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP21/CQ_PERS_04.png)
 * _2_Titolo del Corso, è un campo non controllato che permette di specificare il titolo del corso.
 * _2_Edizione del corso, è un campo che è utilizzato per immettere nuove edizioni dei corsi.
 * _2_Data corso, è un campo che richiede caratteri numerici, identifica la data effettiva del corso.
 * _2_Area di riferimento, è un campo tabellato CQ*DL che specifica l'area coinvolta nel tema del corso, ad esempio per un corso di addestramento CAD l'area del software.
 * _2_Subfattore di riferimento, è un campo tabellato CQ*DB che specifica il subfattore dell'area di riferimento, ad esempio per un corso di addestramento CAD l'area del software nell'ambito delle Discipline Tecniche.
 * _2_Ente gestore del Corso, è un campo tabellato *CNTT che identifica l'ente aziendale che gestisce il corso.
 * _2_Luogo del corso, è un campo non controllato che permette di specificare il luogo dove viene tenuto il corso.
 * _2_Docenti del corso, è un campo non controllato che permette di specificare i docenti che tengono il corso.
 * _2_Metodo Didattico, è un campo non controllato che permette di specificare il metodo didattico adottato.
 * _2_Requisiti del corso, è un campo tabellato CRG che permette di specificare i requisiti richiesti al personale per la frequentazione del corso.
 * _2_Durata del corso, gg è un campo che richiede caratteri numerici, identifica la durata in giorni del corso
 * _2_Durata del corso, hh è un campo che richiede caratteri numerici, identifica la durata in ore del corso
 * _2_Data inizio corso, è un campo che richiede caratteri numerici, identifica la data di inizio del corso
 * _2_Data fine corso, è un campo che richiede caratteri numerici, identifica la data di fine del corso
 * _2_Numero partecipanti, è un campo che richiede caratteri numerici, identifica il numero di partecipanti al corso
 * _2_Costo del Corso,  è un campo che richiede caratteri numerici, identifica il costo totale del corso. In base al numero di partecipanti viene addebitata a ciascuno la quota corrispondente. Interrogando quindi la scheda del dipendente, alla voce relativa al corso seguito viene riportato il valore di spesa come frazione del costo totale (è possibile addebitare ulteriori costi aggiuntivi ad ognuno dei partecipanti direttamente nella scheda personale).
 * _2_Note esplicative, è possibile allegare alla scheda del corso delle note di completamento alla spiegazione sugli obiettivi e sugli intenti proposti. Queste note assieme alle principali informazioni sul corso vengono riportate in automatico sul documento del singolo dipendente iscritto al corso; ciò evita di dover consultare ogni volta l'anagrafica dei corsi.
 * _2_Partecipanti al corso, mettendo una 'x' in questo campo, se sono state iscritte delle persone al corso tramite il modulo "Attribuzione Corsi a Dipendente", viene visualizzato l'elenco dei partecipanti

### Formato elenco partecipanti
![CQ_PERS_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP21/CQ_PERS_05.png)