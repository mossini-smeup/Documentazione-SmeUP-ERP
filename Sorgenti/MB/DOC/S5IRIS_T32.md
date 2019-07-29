Nel seguente documento elenchiamo in  forma tabellare le impostazioni previste dallo script PAR_SCP.
La colonna numero parametro specifica in quale parametro dello script attivare il set.up e la colonna prototipo indica il nome del programma exit  da copiare  e scrivere nella libreria del cliente


|  Nam="Set.up parametri" |
| 
| .COL Txt="Set.up Parametri Visualizzazione " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Aggiungere / Nascondere Colonne Utente  Visualizzazione Gantt e blocco note|16|S5SMX_06X|Gantt e Matrici| |
| Visualizzazione impegni risorse secondarie s5irse0f |58|| |
| Controllo sovrapposizione/saturazione cdl a capacità infinita|63|| |
| Attivazione possibilità di spostare/congelare/forzare job contigui (Gruppi Temporanei)|85| |
| Identificazione in visualizzazione gantt delle operazioni con istante più presto forzato|93| |
| Attivazione possibilità di forzare Data più presto da Gantt|94| |
| Visualizzazione  Catena Ordini Produzione in zoom cella se impostato parametro 79|112| |
| Analisi  Copertura Impegni Materiali con evidenza criticità |17| |
| Analisi Disponibilità materiali per oggetto rottura|114| |
| Scelta Indice Master Schedulazione|8| |
| Calcolo Indici Utente|96|S5SMX_22X|S5SMES_20| |
| Bottone di modifica Batch|76| |
| Visualizzazione Emulazione|95|S5SMX_20X|S5SMES_DB|Storia Schedulazione |
| Visualizzazione Emulazione|95|S5SMX_20X|S5SMES_30|Presentazione Risultati |
| 



|  Nam="Set.up parametri Scelta Risorsa Specifica" |
| 
| .COL Txt="Set.up Scelta Risorsa Specifica" LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Scelta risorsa specifica solo tra le ammesse dall'operazione(potrebbero essere un sottoinsieme della  risorsa principale)|10| |
| Spostamento inibito su risorsa specifica non appartenente alle risorse secondarie abilitate all'esecuzione dell'operazione|31| |
| Cambio in Spinta del dettaglio da schedulare|15|S5SMX_05X|S5SMES_06|INZ| |
|   |15|S5SMX_05X|S5SMES_11E|PAR/DET/FIN| |
| Esclusione risorse per stato anagrafico|68| |
| Messaggio di Warning o blocco  spostamento operazione tra risorse specifiche|116|S5SMX_25X|SS5SMES_D4 |
| 



|  Nam="Set.up parametri Selezione Operazioni" |
| 
| .COL Txt="Set.up Selezione Operazioni          " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Data limite selezione impegni risorse switch tra  tra data inizio e/o Fine richiesta| 11| |
| Validità Operazioni iniziate|2| |
| Impegni con ore residue a zero sono scartati| 90| |
|  |
| 



|  Nam="Set.up Data Inizio Schedulazione" |
| 
| .COL Txt="Set.up Data inizio schedulazione     " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Impostazione Istante di Partenza|77|S5SMX_16X|S5SMES_T1 |
| Elaborazione in tempo reale della schedulazione integrata con la raccolta dati|88| |
| 



|  Nam="Set.up Appuntamenti tra operazioni" |
| 
| .COL Txt="Set.up Appuntamenti tra operazioni   " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Costruzione Appuntamenti tra i Jobs da distinta base|79| |
| Costruzione Appuntamenti tra Ordini|34|S5SMX_09X|S5SMES_07 |
| Sovrapposizione tra i livelli in modo personale|117|S5SMX_26X|S5SMES_06|INZ |
| |117|S5SMX_26X|S5SMES_07|SOV |
| 




|  Nam="Modifiche  dati  Schedulatore" |
| 
| .COL Txt="Modifiche  Dati Input      " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Modificare/Scartare record di S5IRIS durante la fase iniziale di caricamento memoria|7|S5SMX_02X|S5SMES_01I |
| Modificare Tempi lavoro tra macchine alternative con piccole differenze di tempo|32|S5SMX_07X|S5SMES_01K |
| Inizializzatore Generale. Modifica / Integrazione Aree di memoria BCD|59|S5SMX_11X|S5SMES_06 |
| 





|  Nam="Modifiche  dati  Schedulatore" |
| 
| .COL Txt="Modifiche Dati Processo     " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Sospensione temporanea fase,  revisionabile ad ogni loop di schedulazione|60|S5SMX_12X|S5SMES_11E |
| Scelta di un dettaglio da schedulare |67|S5SMX_14X|S5SMES_06|INZ |
| Scelta di un dettaglio da schedulare |67|S5SMX_14X|S5MES_11E|RIT |
| Forzatura istante al più presto del Job durante il ciclo di schedulazione|78|S5SMX_21X|S5SMES_11E |
| Modifica istante inizio disponibilita risorsa durante ciclo di schedulazione|92|S5SMX_19X|S5SMES_13 |
| Tiro Job successivo a quello schedulato con logiche aziendali|12|S5SMX_03X|S5SMES_15 |
| Matrice Set.up Attrezzaggio|14|S5SMX_04X|S5SMES_13 |
| Ammissibilità cambio Risorsa Generale|95|S5SMX_10X|S5SMES_D4B| |
| Calcolo Data Obiettivo|74|S5SMX_15X|S5SMES_01I |
| 



|  Nam="Modifiche  dati  Schedulatore" |
| 
| .COL Txt="Modifiche Dati Output     " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Aggiustamento dettaglio schedulato|3|S5SMX_01X|S5SMES_13|INZ/PRE/' '/FIN |
| Azioni finali al termine schedulazione|73|S5SMX_13X|S5SMES_19 |
| Aggiornamento Impegni risorse S5IRIS0F|33|S5SMX_08X|S5SMES_25|INZ/PRE/POST/FIN |
| Ritorno Holes Interne |108|S5SMX_23X|S5SMES_72| |
| 






|  Nam="Tempi" |
| 
| .COL Txt="Set.up Tempi" LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Calcolo Data fine attrezzaggio|13| |
| Efficienza tempi job switch tra risorsa specifica e principale|27| |
| Efficienza tempi attrezzaggio switch tra risorsa specifica e principale|27| |
| Switch tra giorni lavorativi/calendario per calcolo giorni anticipo/ritardo|75| |
| 




|  Nam="Risorse Secondarie Vincolo" |
| 
| .COL Txt="Set.up Risorse secondarie vincolo" LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit Prototipo" LunAut="1" |
| 
| .COL Txt="Pgm Lancio Exit" LunAut="1" |
| 
| .COL Txt="Funzioni Exit" LunAut="1" |
| Attivazione Vincolo Risorse secondarie|109| |
| Disponibilità Residua RSV|110|S5SMX_24X|S5SMES_74| |
| Aggiustamenti vincoli RSV|113|S5SMX_27X|S5SMES_13|FIN |
| Aggiustamenti vincoli RSV|113|S5SMX_27X|S5SMES_77|RIT |
| 

