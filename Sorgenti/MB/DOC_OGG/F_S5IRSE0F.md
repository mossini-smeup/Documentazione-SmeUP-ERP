## Contenuto
Questo archivio contiene gli impegni risorse secondari legati ad un impegno risorse primario (IR), contenuto nel seguente archivio
 :  : DEC T(OJ) P(*FILE) K(S5IRIS0F)
e scandendo gli sviluppi operazione di tipo risorse produttive secondarie (RPS) della fase dell'IR, contenuti nel seguente archivio
 :  : DEC T(OJ) P(*FILE) K(BRRIPS0F)
E' costruito automaticamente nella funzione di rifasatura degli impegni primari.
A differenza degli impegni primari, questo è un archivio totalmente ricostruito :  non sono previste riprese di dati precedenti.
E' attivo per gli impegni di produzione, di riga di ciclo esterno, di contenitori FP, di ordini pianificati.
Non è attivo per contenitori PCD.

## Codice Oggetto (in TA/*CNTT)
N.A.

## Chiave primaria
N.A

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
La chiave effettiva è : 
S4SCEN - S4TORI - S4TDOC - S4NDOC - S4NRIG - S4OPER - S4CDRS -  S4TIPA - S4CODI

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRK (Tipo risorsa secondaria) : 
 :  : DEC T(ST) K(BRK)
Altre tabelle interessate
 :  : DEC T(ST) K(BSC)
 :  : DEC T(ST) K(S5B)
 :  : DEC T(ST) K(P5S)

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
N.A.

## /COPY
Scansione risorse produttive secondarie
 :  : DEC T(MB) P(QILEGEN) K(£BRJ) L(1)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
Questo archivio viene costruito se impostato il flag specifico di tabella P5S.
La partenza è dal programma di costruzione impegni risorse, in base all'oggetto intestatario (rispettivamente ordine di produzione o riga di ciclo esterno, ordine pianificato o collo MFP)
 :  : DEC T(OJ) P(*PGM) K(P5FURIT)
 :  : DEC T(OJ) P(*PGM) K(M5FURIT)
 :  : DEC T(OJ) P(*PGM) K(P5MFP02)
Viene eseguito il programma generale di pulizia : 
 :  : DEC T(OJ) P(*PGM) K(S5FUPUL)
E quindi il programma guida di costruzione
 :  : DEC T(OJ) P(*PGM) K(S5FUSEC)
Esso lancia, per ogni elemento di tabella BRK, per la scrittura effettiva del record di risorse secondarie, il programma S5FUSEC_x, se il suffisso x è presente in tabella BRK ed è presente il programma.
A standard sono forniti i seguenti programmi, che partono da quanto impostato in BRRIPS
 :  : DEC T(OJ) P(*PGM) K(S5FUSEC_A)
 :  : DEC T(OJ) P(*PGM) K(S5FUSEC_B)
E' possibile inoltre scrivere programmi specifici che utilizzano altre origini (parametri, ecc...), ma sempre guidati da una BRK, partendo dal prototipo
 :  : DEC T(MB) P(S5SRC) K(S5FUSEC_X)
A tale scopo è fornito l'inizializzatore standard, a cui si passa l'elemento di BRK e il record di S5IRIS
 :  : DEC T(OJ) P(*PGM) K(S5FUINZ).
Al termine del loop di esecuzione dei programmi di BRK, viene eseguito, se presente, il programma S5FUSECU, di cui si fornisce un prototipo
 :  : DEC T(MB) P(S5SRC) K(S5FUSECU)
che riceve il record di S5IRIS.
Questo programma può sia scrivere nuovi record di S5IRIS, sia modificare quelli scritti in precedenza, rileggendoli.

## CONTENUTO DEI CAMPI

 :  : FLD S4SCEN Scenario
Campo ereditato dall'omonimo di IR

 :  : FLD S4TORI Tipo origine
Campo ereditato dall'omonimo di IR

 :  : FLD S4TDOC Tipo documento
Campo ereditato dall'omonimo di IR

 :  : FLD S4NDOC Numero documento
Campo ereditato dall'omonimo di IR

 :  : FLD S4NRIG Numero riga
Campo ereditato dall'omonimo di IR

 :  : FLD S4OPER Fase
Campo ereditato dall'omonimo di IR

 :  : FLD S4CDRS Codice risorsa secondaria
Identifica la natura della risorsa secondaria :  risorsa specifica, risorsa fisica risorsa umana
Campo ereditato dalla natura impostata in tabella BRK

 :  : FLD S4TIPA Tipo / Parametro risorsa secondaria
Identifica iol tipo oggetto intestatario della risorsa secondaria.
Campo ottenuto dall'unione dei campi Tipo codice 3 e Parametro codice 3 impostati in tabella BRK

 :  : FLD S4CODI Oggetto risorsa
Identifica l'oggetto intestatario della risorsa secondaria.
Campo ereditato dall'oggetto 3 dell'archivio BRRIPS0F del livello individuato

 :  : FLD S4TBRK Tipo risorsa secondaria
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4TTRG Tipo reperimento calendario
Campo ereditato dall'omonimo di tabella BRK

 :  : FLD S4MAGC Codice magazzino
Campo ereditato dall'omonimo di IR

 :  : FLD S4COMS Codice commessa
Campo ereditato dall'omonimo di IR

 :  : FLD S4CODA Codice A
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4CODB Codice B
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4CODC Codice C
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4NUMA Numero A
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4NUMB Numero B
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4NUMC Numero C
Campo ereditato dall'omonimo di BRRIPS0F

 :  : FLD S4NOTA Nota aggiuntiva
Campo derivato dall'omonimo di BRRIPS0F

 :  : FLD S4HRCI Ore a capacità infinita
Campo derivato dalle ore presenti in S5IRIS0F, in base alla durata utilizzo (impostata in BRK e riportata nel flag 4 del presente archivio)
se tempo totale = ore totali + ore attrezzaggio
se solo attrezzaggio = ore attrezzaggio
se solo lavoro = ore totali
Le ore di attrezzaggio sono teoriche in quanto non dipendenti dalla sequenza di esecuzione sulla risorsa, essendo questa informazione di capacità infinita.
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero.
ll motivo è che gli impegni di risorse specifiche non sono ulteriori impegni che si devono soddisfare (oltre all'impegno primario), ma costituiscono un elenco di possibili risorse dove esso può essere eseguito. Se fossero valorizzato il presente campo, le ore della risorsa specifica verrebbero contate due volte (sia nell'impegno primario, dove la risorsa specifica viene memorizzata, sia nell'impegno secondario).

 :  : FLD S4HRCF Ore a capacità finita
Campo derivato dalle ore presenti in S5IRIS0F, in base alla durata utilizzo (impostata in BRK e riportata nel flag 4 del presente archivio)
se tempo totale = ore totali + ore attrezzaggio
se solo attrezzaggio = ore attrezzaggio
se solo lavoro = ore totali
Le ore di attrezzaggio sono effettive (campo S6HL01) in quanto dipendenti dalla sequenza di esecuzione sulla risorsa, essendo questa informazione di capacità finita.
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DTIN Data inizio a capacità finita
Campo derivato dall'omonimo di S5IRIS0F
Se solo carico e presenti ore di attrezzaggio viene ottenuta dalla data fine a capacità finita arretrata delle ore di carico.
Questo impegno è infatti è occupato dalla fine dell'attrezzaggio (che è più alta dell'inizio schedulazione) alla fine del carico.
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HRIN Ora inizio a capacità finita
Campo costruito insieme alla data inizio a capacità finita
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DTFI Data fine a capacità finita
Campo derivato dall'omonimo di S5IRIS0F
Se solo attrezzaggio e  presenti ore di attrezzaggio viene ottenuta dalla data inizio a capacità finita avanzata delle ore di attrezzaggio.
Questo impegno è infatti è occupato dall'inizio della schedulazione alla fine dell'attrezzaggio (che è più bassa della fine schedulazione).
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HRFI Ora fine a capacità finita
Campo costruito insieme alla data fine a capacità finita
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DISC Data inizio a capacità infinita al più presto
Campo derivato dall'omonimo di S5IRIS0F
Se solo carico e presenti ore di attrezzaggio viene ottenuta dalla data fine a capacità infinita al più presto arretrata delle ore di carico.
Questo impegno è infatti è occupato dalla fine dell'attrezzaggio (che è più alta dell'inizio schedulazione) alla fine del carico.
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HISC Ora inizio a capacità infinita al più presto
Campo costruito insieme alla data inizio a capacità infinita al più presto
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DFSC Data fine a capacità infinita al più presto
Campo derivato dall'omonimo di S5IRIS0F
Se solo attrezzaggio e  presenti ore di attrezzaggio viene ottenuta dalla data inizio a capacità infinita al più presto avanzata delle ore di attrezzaggio.
Questo impegno è infatti è occupato dall'inizio della schedulazione alla fine dell'attrezzaggio (che è più bassa della fine schedulazione).
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HFSC Ora fine a capacità infinita al più presto
Campo costruito insieme alla data fine a capacità infinita al più presto
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DIST Data inizio a capacità infinita al più tardi
Campo derivato dall'omonimo di S5IRIS0F
Se solo carico e presenti ore di attrezzaggio viene ottenuta dalla data fine a capacità infinita al più tardi arretrata delle ore di carico.
Questo impegno è infatti è occupato dalla fine dell'attrezzaggio (che è più alta dell'inizio schedulazione) alla fine del carico.
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HIST Ora inizio a capacità infinita al più tardi
Campo costruito insieme alla data inizio a capacità infinita al più tardi
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DFST Data fine a capacità infinita al più tardi
Campo derivato dall'omonimo di S5IRIS0F
Se solo attrezzaggio e  presenti ore di attrezzaggio viene ottenuta dalla data inizio a capacità infinita al più tardi avanzata delle ore di attrezzaggio.
Questo impegno è infatti è occupato dall'inizio della schedulazione alla fine dell'attrezzaggio (che è più bassa della fine schedulazione).
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4HFST Ora fine a capacità infinita al più tardi
Campo costruito insieme alla data fine a capacità infinita al più tardi
Se risorsa specifica (campo S4CDRS='RISP') questo campo viene lasciato a zero. Riferirsi al campo "Ore a capacità infinita" per la spiegazione.

 :  : FLD S4DT01 Data libera 1
Campo a disposizione utente

 :  : FLD S4DT02 Data libera 2
Campo a disposizione utente

 :  : FLD S4DT03 Data libera 3
Campo a disposizione utente

 :  : FLD S4DT04 Data libera 4
Campo a disposizione utente

 :  : FLD S4DT05 Data libera 5
Campo a disposizione utente

 :  : FLD S4TP01 Tipo e parametro libero 1
Campo a disposizione utente

 :  : FLD S4AA01 Codice libero 1
Campo a disposizione utente

 :  : FLD S4TP02 Tipo e parametro libero 2
Campo a disposizione utente

 :  : FLD S4AA03 Codice libero 3
Campo a disposizione utente

 :  : FLD S4TP04 Tipo e parametro libero 4
Campo a disposizione utente

 :  : FLD S4AA04 Codice libero 4
Campo a disposizione utente

 :  : FLD S4TP05 Tipo e parametro libero 5
Campo a disposizione utente

 :  : FLD S4AA05 Codice libero 5
Campo a disposizione utente

 :  : FLD S4TP06 Tipo e parametro libero 6
Campo a disposizione utente

 :  : FLD S4AA06 Codice libero 6
Campo a disposizione utente

 :  : FLD S4TP07 Tipo e parametro libero 7
Campo a disposizione utente

 :  : FLD S4AA07 Codice libero 7
Campo a disposizione utente

 :  : FLD S4TP08 Tipo e parametro libero 8
Campo a disposizione utente

 :  : FLD S4AA08 Codice libero 8
Campo a disposizione utente

 :  : FLD S4TP09 Tipo e parametro libero 9
Campo a disposizione utente

 :  : FLD S4AA09 Codice libero 9
Campo a disposizione utente

 :  : FLD S4TP10 Tipo e parametro libero 10
Campo a disposizione utente

 :  : FLD S4AA10 Codice libero 10
Campo a disposizione utente
In caso di collo MFP viene riportato il campo S6CODR (codice raggruppamento, che contiene l'ordine di produzione)

 :  : FLD S4NU01 Numero libero 1
Campo a disposizione utente

 :  : FLD S4NU02 Numero libero 2
Campo a disposizione utente

 :  : FLD S4NU03 Numero libero 3
Campo a disposizione utente

 :  : FLD S4NU04 Numero libero 4
Campo a disposizione utente

 :  : FLD S4NU05 Numero libero 5
Campo a disposizione utente

 :  : FLD S4NU06 Numero libero 6
Campo a disposizione utente

 :  : FLD S4NU07 Numero libero 7
Campo a disposizione utente

 :  : FLD S4NU08 Numero libero 8
Campo a disposizione utente

 :  : FLD S4NU09 Numero libero 9
Campo a disposizione utente

 :  : FLD S4NU10 Numero libero 10
Campo a disposizione utente

 :  : FLD S4LVRI Livello di risalita
Identifica il livello a cui è stato trovato l'archivio delle risorse secondarie BRRIPS
Viene impostato in modo specifico dai vari programmi di sviluppo risorse secondarie (S5FUSEC_x)

 :  : FLD S4TPOR Tipo / parametro origine
E' il tipo dell'oggetto origine

 :  : FLD S4CDOR Oggetto origine
E' l'oggetto intestatario del record a cui è stato trovato l'archivio delle risorse secondarie BRRIPS

 :  : FLD S4DTCR Data creazione
Campo ereditato dall'omonimo di IR

 :  : FLD S4HRCR Ora creazione
Campo ereditato dall'omonimo di IR

 :  : FLD S4USIN Utente creazione
Campo ereditato dall'omonimo di IR

 :  : FLD S4DTAG Data aggiornamento
Campo ereditato dall'omonimo di IR

 :  : FLD S4HRAG Ora aggiornamento
Campo ereditato dall'omonimo di IR

 :  : FLD S4USAG Utente aggiornamento
Campo ereditato dall'omonimo di IR



