## Contenuto
Questo archivio conitene gli impegni risorse residui di un oggetto intestatario (ordine di produzione, di una riga di ciclo esterno, di un ordine pianiticato, di un contenitore).
E' costruito automanticamente, a partire dal ciclo dell'oggetto intestatario, nettificato dalle attività eseguite.
Per le fasi completate (perchè dichiarata tutta la quantità oppure perchè saldate forzatamente) non viene costruita una riga di impegno.
Viene ricostruito automaticamente ad ogni dichiarazione di attività.
E' inoltre consigliabile attivarne la ricostruzione nel flusso di modifica dell'oggetto intestatario.

## Codice Oggetto (in TA/*CNTT)
 'IR'                               £FUNT1

## Chiave primaria
 S6IDOJ                         £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
La chiave effettiva è : 
S6SCEN - S6TORI - S6TDOC - S6NDOC - S6NRIG -S6OPER - S6FL12

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle P5S (Tipo impegno risorse) : 
 :  : DEC T(ST) K(P5S)
Altre tabelle interessate
 :  : DEC T(ST) K(P5T)
 :  : DEC T(ST) K(P51)
 :  : DEC T(ST) K(P52)
 :  : DEC T(ST) K(V5B)
 :  : DEC T(ST) K(S5B)
 :  : DEC T(ST) K(M5B)

## Autorizzazioni
N.A.

## Note strutturate (Tabella NSC)
N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
E' possibile impostare in tabella P5S il suffisso x di un programma di aggiustamento, che può modificare il contenuto del record prima della scrittura : 
* per gli ordini di produzione non gestiti a MFP, i contenitori PCD, le righe documento e gli ordini pianificati :  S5FURIT_x
* per gli ordini di produzione gestiti a MFP :  S5FURIF_x

E' possibile impostare, sempre in tabella P5S, il suffisso x di un programma di aggiustamento S5FASIR_x, che permette di ripristinare campi del record tra una rifasatura e l'altra.
Riferirsi al programma
 :  : DEC T(OJ) P(*PGM) K(S5FASIR)
per l'elenco dei campi che sono ripristinati in automatico.
NB :  per attivare il ripristino è comunque necessario impostare il flag "Ripresa impegni risorse" in tabella P51.


## /COPY
Interfaccia impegni risorse (£IIR) : 
 :  : DEC T(MB) P(QILEGEN) K(£IIR) L(1)

Situazione avanzamento di un ordine di produzione (£G20) : 
 :  : DEC T(MB) P(QILEGEN) K(£G20) L(1)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
Gli impegni risorse si riferiscono a ordini di produzione, righe documenti, contenitori e ordini pianificati.
Si costruiscono con i seguenti programmi : 
ordini di produzione e righe documento : 
 :  : DEC T(OJ) P(*PGM) K(P5FURIT)
ordini di produzione gestiti a MFP (NB :  programma lanciato dal precedente) : 
 :  : DEC T(OJ) P(*PGM) K(P5MFP02)
contenitori (nella gestione PDC) : 
 :  : DEC T(OJ) P(*PGM) K(P5FUPDC)
ordini pianificati : 
 :  : DEC T(OJ) P(*PGM) K(M5FURIT)


## CONTENUTO DEI CAMPI

 :  : FLD S6SCEN Scenario
Gli impegni risorse sono costruiti sullo scenario ** principale, che deve obbligatoriamente esistere in tabella S5B.
E' possibile costruire altri scenari di simulazione, dipendenti dal principale, su cui effettuare la schedulazione fine.
La loro costruzione avviene contestuamente a quella dello scenario principale, se è impostato, nell'elemento di tabella dello scenario dipendente, il flag di scenario dipendente.

 :  : FLD S6TIRS Tipo impegno risorse
E' ripreso dall'elemento presente : 
- per l'ordine di produzione in tabella P5T
- per la riga documento in tabella V5B
- per il contenitore, in tabella P52
- per l'ordine pianificato, in tabella M5B (scenario di pianficazione)

 :  : FLD S6TSCH Tipo schedulazione
E' un campo ripreso dal campo omonimo di tabella P5S.
E' a disposizione dell'utente per riclassificare diversi elementi di P5S.

 :  : FLD S6TORI Tipo origine
Viene ripreso il valore contenuto nell'elemento di tabella P5S.
Individua l'oggetto intestatario degli impegni (ordine di produzione, riga documento, ecc...).
NB :  Non è esattamente il tipo oggetto, ma un valore ad esso collegato

 :  : FLD S6TDOC Tipo documento
In caso di impegno di riga documento è il tipo documento V5D

 :  : FLD S6NDOC Numero documento
- In caso di impegno di riga documento è il numero documento
- In caso di ordine di produzione (non MFP) è il numero ordine
- In caso di ordine MFP o PDC è il  numero di contenitore
- In caso di ordine pianificato è l'indentificativo del consiglio (posizioni 1-3 plant, posizioni 7-15 numero record origine

 :  : FLD S6NRIG Numero riga
In caso di impegno di riga documento è il numero riga

 :  : FLD S6S$OR Stato ordine
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6L$OR Livello ordine
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6MAGC Magazzino
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6COAR Codice Articolo
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6CONF Configurazione
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6TIEN Tipo ente
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
In caso di riga documento è il tipo ente intestatario di tabella V5B

 :  : FLD S6CLIE Codice ente
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
In caso di riga documento è l'ente intestatario

 :  : FLD S6COMS Commessa
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6PRIO Priorità
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6QORD Quantità totale ordine
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6DIRI Data inizio richiesta ordine
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Nel caso di riga documento è la data consegna richiesta
Nel caso di ordine pianificato è la data suggerimento

 :  : FLD S6DFRI Data fine richiesta ordine
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Nel caso di riga documento è la data consegna confermata
Nel caso di ordine pianificato è la data fine pianificata

 :  : FLD S6NORF Numero ordine di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6TORF Tipo oggetto di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6PARF Parametro oggetto di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6OGRF Oggetto di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6TDOR Tipo documento di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6NDOR Numero documento di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6NRIR Numero riga di riferimento
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno
Valorizzato solo in caso di ordine di produzione

 :  : FLD S6NREC Numero record fase
Valore ritornato dalla scansione del ciclo

 :  : FLD S6IDOF Identificativo fase
Campo attualmente non gestito (riservato SMEUP per futura oggettizzazione della riga di ciclo)

 :  : FLD S6OPER Fase
Valore ritornato dalla scansione del ciclo

 :  : FLD S6DEOP Descrizione operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6OPRI Fase principale
Campo attualmente non gestito (riservato SMEUP per futuro collegamento tra fasi per alternative di ciclo)

 :  : FLD S6TIRP Tipo risorsa principale
Se non impostato in tabella P51 il flag di variazione automatica risorse, oppure in caso di ordini pianificati, viene assunto il valore di tabella P5S
Se impostato questo flag ed è stata eseguita una dichiarazione, viene assunto l'ultimo tipo risorsa principale su cui si è dichiarato

 :  : FLD S6CLAV Risorsa principale
Se non impostato in tabella P51 il flag di variazione automatica risorse, oppure in caso di ordini pianificati, viene assunto il valore ritornato dalla scansione del ciclo
Se impostato questo flag ed è stata eseguita una dichiarazione, viene assunto l'ultimo tipo risorsa principale su cui si è dichiarato

 :  : FLD S6TIRF Tipo risorsa specifica
Se impostato in tabella P51 il flag di variazione automatica risorse, sono attive le risorse specifiche (in tabella S5B) ed è stata eseguita una dichiarazione, viene assunto l'ultimo tipo risorsa specifica su cui si è dichiarato.
In tutti gli altri casi viene copiato il tipo risorsa principale

 :  : FLD S6MACC Risorsa specifica
Se impostato in tabella P51 il flag di variazione automatica risorse, sono attive le risorse specifiche (in tabella S5B) ed è stata eseguita una dichiarazione, viene assunto l'ultima risorsa specifica su cui si è dichiarato.
In tutti gli altri casi viene copiata la risorsa principale
NB :  in caso di attivazione risorse specifiche (in tabella S5B tipo risorsa principale e specifica diversi) e non impostato li flag di variazione automatica risorse, questo campo (e il precedente) sono sempre inizializzati come risorsa principale.
L'assegnazione della effettiva risorsa specifica verrà poi eseguita dalla schedulazione FINE.UP, essendo uno dei suoi compiti l'assegnazione della risorsa specifica. La ripresa dei valori memorizzati di una riga di impegno è una fase successiva, durante la rifasatura, rispetto alla presente inizializzazione, cosicchè al termine di questa funzione, in questo campo vi sarà effettivamente una risorsa specifica.
I casi in cui rimarrà una risorsa principale (tipo e codice) sono i seguenti : 
Non sono gestite le risorse specifiche
L'impegno è nuovo :  non è mai stato schedulato nè dichiarato (se attiva la variazione automatica risorse)
La risorsa principale è a capacità infinita :  per gli impegni di queste risorse FINE.UP non sceglie una risorsa specifica.

 :  : FLD S6TPRA Tipo oggetto raggruppamento
In caso di impegno appartenente ad un batch, viene impostato a 'IR'
Negli altri casi campo attualmente non gestito

 :  : FLD S6PARA Parametro oggetto raggruppamento
In caso di impegno appartenente ad un batch, viene lasciato bianco
Negli altri casi campo attualmente non gestito

 :  : FLD S6OGRA Oggetto raggruppamento
In caso di impegno appartenente ad un batch, viene impostato con l'IDOJ dell'impegno master del batch
Negli altri casi campo attualmente non gestito

 :  : FLD S6S$OP Stato operazione
Campo attualmente non gestito

 :  : FLD S6L$OP LIvello operazione
Campo attualmente non gestito

 :  : FLD S6TCIC Tipo ciclo
Valore ritornato dalla scansione del ciclo

 :  : FLD S6CICL Ciclo
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TOPE Tipo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6GRAL Gruppo alternativa
Valore ritornato dalla scansione del ciclo

 :  : FLD S6CODC Codice collegato
Valore ritornato dalla scansione del ciclo

 :  : FLD S6CICC Ciclo collegato
Valore ritornato dalla scansione del ciclo

 :  : FLD S6SQCC Sequena ciclo collegato
Valore ritornato dalla scansione del ciclo

 :  : FLD S6UBIP Ubicazione pre
Valore impostato nella gestioe PDC o MFP,

 :  : FLD S6UBID Ubicazione post
Valore impostato nella gestioe PDC o MFP

 :  : FLD S6STOP Stato impegno
Individua se l'operazione è iniziata, pronta, ecc...

 :  : FLD S6UMIS Unità di misura
Valore ripreso dal record dell'oggetto a cui è relativo questo impegno

 :  : FLD S6QTOR Quantità residua dell'operazione
Valore calcolato in base alla quantità richiesta per l'operazione e alla quantità dichiarata
In caso di ordine pianificato è la quantità del suggerimento

 :  : FLD S6QTOT Quantità totale dell'operazione
E' la quantità totale dell'operazione
In caso di ordine pianificato è la quantità del suggerimento

 :  : FLD S6QTSC Quantità schedulata dell'operazione
E' impostata pari alla quantità residua.
A disposizione dell'utente per operare delle variazioni ad hoc.

 :  : FLD S6QTFA Quantità alla fase
E' calcolata durante la rifasatura. Individua la quantità giacente a monte della fase del presente impegno

 :  : FLD S6OPFA Fase dell'operazione
E' la fase a cui è stata rilevata la quantità.

 :  : FLD S6QT01 Quantità
Campo attualmente non gestito

 :  : FLD S6QT02 Quantità
Campo attualmente non gestito

 :  : FLD S6QT03 Quantità
Campo attualmente non gestito

 :  : FLD S6DTUA Data ultima attività
E' la data della dichiarazione più recente su questa fase

 :  : FLD S6HUNI Ore per una unità
E' il componente di carico n.3 diviso per la quantità schedulata

 :  : FLD S6HTOT Ore totali residue
E' il componente di carico n.3

 :  : FLD S6HATR Ore attrezzaggio.
E' il componente di carico n.2. Viene riempito solo se l'operazione non è iniziata, e se deciso di riempirlo (eventualmente con efficienza) in base a quanto impostato in tabella S5B

 :  : FLD S6HR01 Ore
Campo attualmente non gestito

 :  : FLD S6HR02 Ore
Campo attualmente non gestito

 :  : FLD S6HR03 Ore
Campo attualmente non gestito

 :  : FLD S6EF01 Efficienza
Viene riportata l'efficienza della risorsa principale

 :  : FLD S6EF02 Efficienza
Campo attualmente non gestito

 :  : FLD S6EF03 Efficienza
Campo attualmente non gestito

 :  : FLD S6QUET Coda
Viene riportata la coda della risorsa principale

 :  : FLD S6GG01 Giorni della fase
Campo attualmente non gestito

 :  : FLD S6UMTE Unità di misura dei tempi
Valore ritornato dalla scansione del ciclo

 :  : FLD S6CDCA Codice di carico
Viene riportato il codice di carico della risorsa principale

 :  : FLD S6TE01 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE02 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE03 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE04 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE05 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE06 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE07 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE08 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE09 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6TE10 Tempo operazione
Valore ritornato dalla scansione del ciclo

 :  : FLD S6CC01 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC02 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC03 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC04 Componente di carico
Valore calcolato durante la rifasatura


 :  : FLD S6CC05 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC06 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC07 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC08 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC09 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CC10 Componente di carico
Valore calcolato durante la rifasatura

 :  : FLD S6CROR Criterio ordinamento
Valore calcolato durante la rifasatura, in base a quanto impostato in tabella S5B

 :  : FLD S6TPRG Tipo raggruppamento
In gestione MFP è impostato a '"£MF"
Negli altri casi attualmente  non gestito

 :  : FLD S6CODR Codice raggruppamento
In gestione MFP è impostato con l'ordine di produzione
Negli altri casi attualmente non gestito

 :  : FLD S6NUMR Numero raggruppamenti
Campo attualmente non gestito

 :  : FLD S6CMB1 Composizione statica Batch 1
Campo riempito dalla composizione di un batch, e che individua la compatibilità statica
(famiglia batch) insieme con il campo successivo

 :  : FLD S6CMB2 Composizione statica Batch 2
Campo riempito dalla composizione di un batch, e che individua la compatibilità statica
(famiglia batch) insieme con il campo precedente

 :  : FLD S6TIPF Tipo risorsa forzata
Campo riempito da FINE.UP insieme al codice risorsa forzata

 :  : FLD S6CODF Codice risorsa forzata
Campo riempito da FINE.UP insieme al tipo risorsa forzata
Se attive le risorse specifiche (in tabella S5B) è la risorsa specifica su cui si intende forzare (e congelare, se valorizzato anche il progressivo schedulazione) l'esecuzione di questo impegno
Se non attive le risorse specifiche, è presente solo se è valorizzato il progressivo schedulazione,  e contiene la risorsa principale

 :  : FLD S6PRGS Progressivo schedulazione
Campo riempito da FINE.UP, insieme con la risorsa forzata (tipo e codice)
Individua un impegno congelato, e la sua posizione all'interno della coda nella risorsa forzata (tipo e codice :  campi che sono sempre presenti se questo campo è valorizzato)
E' un numero a passo 10

 :  : FLD S6TRIN Turno inizio schedulazione
Campo attualmente non gestito

 :  : FLD S6DTIN Data inizio schedulazione
E' la data di inizio della schedulazione fine :  impostata da FINE.UP

 :  : FLD S6HRIN Ora inizio schedulazione
E' l'ora  di inizio della schedulazione fine :  impostata da FINE.UP

 :  : FLD S6TRFI Turno fine schedulazione
Campo attualmente non gestito

 :  : FLD S6DTFI Data fine schedulazione
E' la data di fine della schedulazione fine :  impostata da FINE.UP

 :  : FLD S6HRFI Ora fine schedulazione
E' l'ora  di fine della schedulazione fine :  impostata da FINE.UP

 :  : FLD S6DISC Data inizio schedulazione a capacità infinita al più presto
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6HISC Ora inizio schedulazione a capacità infinita al più presto
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6DFSC Data fine schedulazione a capacità infinita al più presto
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6HFSC Ora fine schedulazione a capacità infinita al più presto
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6DIST Data inizio schedulazione a capacità infinita al più tardi
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6HIST Ora inizio schedulazione a capacità infinita al più tardi
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6DFST Data fine schedulazione a capacità infinita al più tardi
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6HFST Ora fine schedulazione a capacità infinita al più tardi
Impostata nella rifasatura, se impostato in S5B (nei due flag per rilasciati e pianificati)

 :  : FLD S6DTPP Data al più presto
Impostata in FINE.UP :  è la data più bassa a cui può iniziare quest impegno (per vincoli di operazioni precedenti, ordini collegati di livelli inferiori, oppure vincoli esterni impostati manualmente)

 :  : FLD S6HRPP Ora al più presto
Impostata in FINE.UP :  è l'ora legata alla data al più presto

 :  : FLD S6DTPT Data al più tardi
Campo attualmente non gestito

 :  : FLD S6HRPT Ora al più tardi
Campo attualmente non gestito

 :  : FLD S6VEIT Vincolo esterno iniziale :  tipo
Campo a disposizione dell'utente per specificare il tipo di vincolo. Può essere inserito nella exit della rifasatura o all'interno di FINE.UP, se prevista la gestione

 :  : FLD S6VEID Vincolo esterno iniziale :  data
Campo a disposizione dell'utente per specificare la data di vincolo. Può essere inserito nella exit della rifasatura o all'interno di FINE.UP, se prevista la gestione

 :  : FLD S6VEIH Vincolo esterno iniziale :  ora
Campo a disposizione dell'utente per specificare l'ora di vincolo. Può essere inserito nella exit della rifasatura o all'interno di FINE.UP, se prevista la gestione

 :  : FLD S6VEFT Vincolo esterno finiale :  tipo
Campo attualmente non gestito

 :  : FLD S6VEFD Vincolo esterno finale :  data
Campo attualmente non gestito

 :  : FLD S6VEFH Vincolo esterno finale :  ora
Campo attualmente non gestito

 :  : FLD S6CAUS Causale transazione
Campo attualmente non gestito

 :  : FLD S6ID01 Data fine attrezzaggio
Calcolato da FINE.UP :  se non è impostato il calcolo di questa data, coincide con la data inizio schedulazione

 :  : FLD S6IH01 Ora fine attrezzaggio
Calcolato da FINE.UP :  se non è impostato il calcolo di questa data, coincide con l'ora inizio schedulazione

 :  : FLD S6ID02 Data istante 2
Campo attualmente non gestito

 :  : FLD S6IH02 Ora istante 2
Campo attualmente non gestito

 :  : FLD S6ID03 Data istante 3
Campo attualmente non gestito

 :  : FLD S6IH03 Ora istante 3
Campo attualmente non gestito

 :  : FLD S6ID04 Data istante 4
Campo attualmente non gestito

 :  : FLD S6IH04 Ora istante 4
Campo attualmente non gestito

 :  : FLD S6DT01 Data libera 1
Campo a disposizione utente

 :  : FLD S6DT02 Data libera 2
Campo a disposizione utente

 :  : FLD S6DT03 Data libera 3
Campo a disposizione utente

 :  : FLD S6DT04 Data libera 4
Campo a disposizione utente

 :  : FLD S6DT05 Data libera 5
Campo a disposizione utente

 :  : FLD S6HL01 Ora libera (durata) 1
Nella schedulazione fine vengono riportate le ore effettive di attrezzaggio.
Se questo campo è diverso dalle ore di attrezzaggio previste, significa che è stata apportata una correzione per comunanze tra due attrezzaggi successivi sulla stessa risorsa.

 :  : FLD S6HL02 Ora libera (durata) 2
Campo a disposizione utente

 :  : FLD S6HL03 Ora libera (durata) 3
Campo a disposizione utente

 :  : FLD S6HL04 Ora libera (durata) 4
Campo a disposizione utente

 :  : FLD S6HL05 Ora libera (durata) 5
Campo a disposizione utente

 :  : FLD S6AA01 Codice libero 1
Campo a disposizione utente

 :  : FLD S6AA02 Codice libero 2
Campo a disposizione utente

 :  : FLD S6AA03 Codice libero 3
Campo a disposizione utente

 :  : FLD S6AA04 Codice libero 4
Se impegno appartenente ad un batch è la prima parte del campo che definisce la famiglia batch. Impostato nella exit di definizione della famiglia batch.
Negli altri casi campo a disposizione utente

 :  : FLD S6AA05 Codice libero 5
Se impegno appartenente ad un batch è la seconda parte del campo che definisce la famiglia batch. Impostato nella exit di definizione della famiglia batch.
Negli altri casi campo a disposizione utente

 :  : FLD S6NU01 Numero libero 1
Campo a disposizione utente

 :  : FLD S6NU02 Numero libero 2
Campo a disposizione utente

 :  : FLD S6NU03 Numero libero 3
Campo a disposizione utente

 :  : FLD S6NU04 Numero libero 4
Campo a disposizione utente

 :  : FLD S6NU05 Numero libero 5
Campo a disposizione utente

 :  : FLD S6NOTA Nota
Valore ritornato dalla scansione del ciclo

 :  : FLD S6IDOJ Identificativo oggetto
Viene determinato col numeratore degli impegni risorse presente in tabella P51.
E' un identificativo univoco che, al ripresentarsi della stessa combinazione di chiavi, ritorna lo stesso valore.
L'accoppiata "identificativo - chiave estesa" viene memorizzata nell'archivio
 :  : DEC T(OJ) P(*FILE) K(S5IDIR0F)

 :  : FLD S6DTCR Data creazione
Impostato alla data di rifasatura

 :  : FLD S6HRCR Ora creazione
Impostato all'ora di rifasatura

 :  : FLD S6USIN Utente creazione
Impostato con l'utente che ha lanciato la rifasatura

 :  : FLD S6DTAG Data aggiornamento
Impostato alla data di rifasatura

 :  : FLD S6HRAG Ora aggiornamento
Impostato all'ora di rifasatura

 :  : FLD S6USAG Utente aggiornamento
Impostato con l'utente che ha lanciato la rifasatura
