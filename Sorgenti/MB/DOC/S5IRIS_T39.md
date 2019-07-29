# Generalità
La BCD di interrogazione permette di consultare una schedulazione eseguita in precedenza.

# Note tecniche
Questa funzione si attiva impostanto il flag di "memorizza sessione" in tabella B§G.
In questo caso, ad ogni salvataggio della schedulazione vengono salvate tutte le memorie nell'archivio : 
 :  : DEC T(OJ) P(*FILE) K(B£BCDM0F)
Viene creata una nuova sessione (a meno di impostazioni personali che vedremo in seguito) se varia almeno un campo di input (appartenente a S5X). In questo modo, ad ogni salvataggio della schedulazione eseguito senza uscire (successivo al primo) viene mantenuta la sessione, (non essendo variati i campi dalla S5X), e quindi viene ricoperta la memorizzazione precedente.
Il numero di sessione viene memorizzato nell'elemento £BCD della tabella CRN di sottosettore B£.
Vengono mantenute (a meno di impostazioni personali) le sessioni con data maggiore o uguale a quella (ovviamente implicita) impostata in tabella B§G.
In questa tabella va inserito il campo (obbligatorio) "Ambiente" (elemento della tabella *CN/BC) che permette di riclassificare ogni elemento di B§G.
Ogni interrogazione è individuata dai campi :  Ambiente / Elemento B§G / Sessione.

## Modalità di lancio
L'interrogazione si attiva eseguendo il programma B£BCD08.
Lo può essere lanciato in varie modalità, in modo da presentare una lista (completa o filtrata) delle sessioni tra le quali scegliere quella da visualizzare.
Se il filtro individua una sola sessione (o ne è presente una sola), si entra direttamente nell'interrogazione, senza passare dalla lista di scelta (che in questo caso avrebbe un solo elemento).
Se si lancia B£BCD08 senza parametri vengono presentate tutte le sessioni, in questa forma : 
Ambiente / Elemento B§G / SESSIONE / Dati sessione .....
Se lo si lancia con un parametro, lo si può costruire in due modi : 
AMB_xx dove xx è l'abiente. Vengono presentate tutte le sessioni dell'ambiente impostato : 
Elemento B§G / SESSIONE / Dati sessione .....
TAB_yyy dove yyy è l'elemento B§G. Vengono presentate tutte le sessioni della B§G impostata (non viene presentato l'ambiente in quanto e dell'ambiente della B§G) : 
SESSIONE / Dati sessione .....
A sinistra di ogni elemento della lista sono presenti due bottoni :  il primo di scelta per eseguire l'interrogazione, il secondo di eliminazione, per eliminare fisicamente i dati memorizzati della sessione.

## Dati generali
Ogni programma della BCD ha accesso alle seguenti informazioni (contenute nella DS generale £BCDDS1) : 
£BCDNS :  Numero sessione (di 10 caratteri alfanumerico), valorizzato in gestione dopo il primo salvataggio, in interrogazione sempre.
£BCDTS :  Tipo Sessione :  ' ' : gestione, 'I' : interrogazione
Ricordo che ogni programma ha accesso all'ambiente nel campo T$B§GP e all'elemento di B§G nel campo U$NOME.

## Parametrizzazioni
E' possibile eseguire alcune personalizzazioni, contenute nell'exit S5SMX_28x dove x è la posizione 118 dello script dei parametri.
In questo programma è possibile implementare una diversa modalità di mantenimento della sessione, una diversa modalità di individuazione della sessione (ridurre o estendere i campi di S5X), una diversa selezione dei campi presentati nella lista di scelta sessione, e la possibilità di richiamare le exit che contengono delle mongolfiere in memorizzazione (all'atto del salvataggio della sessione) e in ripresa (all'inizio dell'interrogazione).
Si rimanda alla documentazione interna di questo programma per i dettagli implementativi
 :  : DEC T(MB) P(BCDSRC) K(S5SMX_28X) L(1)

 : ; : T02 Descrizione operativa
In interrogazione i risultati della schedulazione si presentano in modo identico alla gestione. Sono attive le medesime navigazioni, mentre, naturalmente sono impedite le azioni di spostamento, congelamento, forzatura, impostazione vincolo, rischedulazione e salvataggio dei risultati.

## Note tecniche
Le memorie sono lette e scritte utilizzando le seguenti procedure : 
a livello di file : 
 :  : DEC T(MB) P(QPROGEN) K(£P007F) L(1)
a livello di prototipo : 
 :  : DEC T(MB) P(QPROGEN) K(£P007D) L(1)
a livello di procedura (consultare il sorgente per gli esempi di chiamata) : 
 :  : DEC T(MB) P(QPROGEN) K(£P007) L(1)

## Tipi record
I tipi record individuano le memorie salvate.
I principali sono
ID - Elemento di individuazione della sessione (senza interventi personali coincide con il contenuto di S5X)
S5B - Tabella scenario
S5X - Tabella Scelte
£BCDD1 - Prima DS delle BCD
£BCDD2 - Seconda DS della BCD
IPR - Istante di inizio schedulazione (la data di lancio è contrenuta nella S5X). L'istante di inizio può variare all'interno della stessa schedulazione in caso di partenza real time. Questo valore, esterno a S5X, non contribuisce alla differenziazione della sessione.
i tipi record delle memorie hanno il loro stesso nome (ad esempio DSIRIS, DSRISO, ecc...)




