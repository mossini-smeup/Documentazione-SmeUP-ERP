 :  : HEA RESP(AS) STAT(80)
# OBIETTIVO
Questo servizio consente di costruire l'XML necessario per la compilazione delle schede inerenti l'MPPIAN.

# FUNZIONI/METODI
## Lista oggetti in chiave (LOK)
Costruisce un albero con oggetti diversi in base al metodo richiamato.
Facendo doppio click sull'elemento dell'albero si ottiene il grafico diverso a seconda della tipologia dell'oggetto :  se è un oggetto in chiave1 nella vista si ottiene un grafico riferito a quell'oggetto e dettagliato per periodo e per chiave2 (se la vista ha una sola chiave si ottiene
un grafico vuoto); se è un oggetto in chiave2 nella vista si ottiene un grafico riferito a quell'oggetto e dettagliato per periodo e per chiave1.
Vicino al nome degli oggetti è indicata la quantità totale di tutti i periodi (ovviamente nel caso di viste con due chiavi la quantità viene indicata solo quando è possibile fare riferimento ad entrambe le chiavi)
### Metodo 1E2
Costriusce un albero con 2 livelli i cui nodi sono gli oggetti in chiave ad una coppia piano-vista. I nodi  principali sono dati dagli oggetti in Chiave1, mentre i sottonodi di ogni nodo sono formati da tutti gli oggetti in Chiave2 associati a quel particolare oggetto.
Se la vista ha una sola chiave l'albero non avrà sottonodi e i nodi principali saranno tutti gli oggetti in Chiave1 associati a quella coppia piano-vista.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista.
### Metodo 2E1
Analogo a EOG.1E2, con la differenza che i nodi principali sono formati dagli oggetti in Chiave2 e i sottonodi sono dati dagli oggetti in Chiave1 associati a quegli oggetti. Se la vista ha una sola chiave, i nodi sono tutti gli oggetti in Chiave1 di quela coppia piano-vista.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista.
### Metodo UNO
Costruisce un albero ad un solo livello i cui nodi sono dati da tutti gli oggetti in Chiave1 del Piano-vista specificati.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista.
### Metodo DUE
Costruisce un albero ad un solo livello i cui nodi sono dati da tutti gli oggetti in Chiave2 del piano-vista specificati.
Se la vista ha una sola chiave, l'albero risulta vuoto.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista.
### Metodo 2D1
Costruisce un albero ad un solo livello i cui nodi sono dati dagli oggetti in Chiave2 del piano-vista specificati e associati all'oggetto in Chiave1 in inupt.
Se la vista ha una sola chiave l'albero è vuoto.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista, nell'"Oggetto3" è necessario inserire il codice della chiave1 a cui fare riferimento.
### Metodo 1D2
Costruisce un albero ad un solo livello i cui nodi sono dati dagli oggetti in Chiave1 del piano-vista specificati e associati all'oggetto in Chiave2 in inupt.
Se la vista ha una sola chiave e in input passo *BLANKS come oggetto della Chiave2, l'albero risultante è formato da tutti gli oggetti in Chiave1 associati a quel piano-vista.
Nell'"Oggetto1" è necessario inserire il piano, mentre nell'"Oggetto2" è necessario inserire la vista, nell'"Oggetto3" è necessario inserire il codice della Chiave2 a cui fare riferimento.

## Visualizzazione dati contenuti nel piano-vista (DAT)
Costruisce le tabelle contenenti i dati del piano, cumulando rispetto ad una chiave o dettagliando per periodi o per chiavi.
### Metodo KY1
Costruisce la tabella (visualizabile poi in grafico o in matrice) dettagliando gli oggetti in Chiave1, ossia mettendo un oggetto per riga. Nel caso di visulizzazione con grafico tali oggetti vanno in ascissa, nel caso di visualizzazione a matrice visualizzo una riga per ognuno di tali oggetti.I dati sono tutti riferiti ad un periodo specificato.
Se nell'Oggetto4 inserisco un oggetto in chiave2 allora le quantita dei vari oggetti sulle righe sono riferiti a quel particolare valore presente in Chiave2, altrimenti le quantità sono cumulate.
Nell'Oggetto1 devo specificare il piano, nell'Oggetto2 la vista. Il periodo lo inserisco nei parametri usando il tag PER (inserendo il numero del periodo con tre cifre). Nell'Oggetto4 posso specificare un oggetto in Chiave2.
### Metodo KY2
Costruisce la tabella mettendo su ogni riga gli oggetti in Chiave2. I dati sono (anche in questo caso) tutti riferiti ad un periodo specificato.
Se nell'Ogetto3 inserisco un oggetto in chiave1 allora le quantita dei vari oggetti sulle righe sono riferiti a quel particolare valore presente in Chiave1, altrimenti le quantità sono cumulate.
Nell'Oggetto1 devo specificare il piano, nell'Oggetto2 la vista. Il periodo lo inserisco nei parametri usando il tag PER (inserendo il numero del periodo con tre cifre). Nell'Oggetto3 posso specificare un oggetto in Chiave1.
### Metodo PER
Costruisce la tabella mettendo su ogni riga i vari periodi. Se specifico un oggetto in Chiave1 allora le quantità sono riferite a quell'oggetto (cumulando tutte le quantità della Chiave2 in caso di vista con due chiavi). Se invece specifico un oggetto in Chiave2 allora le quantità sono riferite a quell'oggetto cumulando rispetto a tutti gli oggetti in Chiave1 associati. Se specifico entrambi gli oggetti le quantità sono riferite a quella particolare coppia di chiavi.
Nell'Oggetto1 devo specificare il piano, nell'Oggetto2 la vista. L'eventuale oggetto in Chiave1 lo specifico nell'oggetto3, mentre quello in Chiave2 nell'Ogegtto4.
### Metodo AK1
Costruisce la tabella dettagliando per la Chiave1, questo significa che in ogni riga ho un oggetto specificato nella chiave1 della vista (dettagliato per periodo).
Se specifico un oggetto del tipo della chiave2 allora sulle righe ottengo tutti gli oggetti chiave1 associati a quella particolare chiave2 (ovviamente solo nel caso di vista con due chiavi).
Nell'Oggetto1 devo specificare il piano, nell'Oggetto2 la vista. Se nell'Oggetto3 inserisco un oggetto di tipo chiave2 allora, come detto, nelle righe ho solo gli oggetti in chiave1 associati a quella particolare chiave2, se invece lascio vuoto l'Oggetto3, allora sulle righe ho tutti gli
gli oggetti in chiave1 con una quantità pari alla somma di tutte le quantità riferite ai vari oggetti in chiave2. Questo servizio genera un XML potenzialmente molto grande e questo può determinare lunghi tempi computazionali.
### Metodo AK2
Costruisce la tabella dettagliando per la Chiave2, questo significa che in ogni riga ho un oggetto specificato nella chiave2 della vista (dettagliato per periodo).
Se specifico un oggetto del tipo della chiave1 allora sulle righe ottengo tutti gli oggetti chiave2 associati a quella particolare chiave1 (ovviamente solo nel caso di vista con due chiavi).
Nell'Oggetto1 devo specificare il piano, nell'Oggetto2 la vista. Se nell'Oggetto3 inserisco un oggetto di tipo chiave1 allora, come detto, nelle righe ho solo gli oggetti in chiave2 associati a quella particolare chiave1, se invece lascio vuoto l'Oggetto3, allora sulle righe ho tutti gli
gli oggetti in chiave2 con una quantità pari alla somma di tutte le quantità riferite ai vari oggetti in chiave1. Questo servizio genera un XML potenzialmente molto grande e questo può determinare lunghi tempi computazionali.

## Caratteristiche dei piani e delle viste corrispondenti ai criteri specificati (MPV)
Recupera i dati dei piani e delle viste inseriti nel file MPPIAN0F.
Vengono forniti anche i dati relativi alla famiglia di appartenenza del piano, i tipi oggetto delle chiavi delle viste, la periodicità e la data di inizio.
E' possibile effettuare delle parzializzazioni. In particolare posso impostare il codice del piano, il codice della vista e il codice della famiglia. Questi filtri vengono gestiti in AND :  se imposto un codice piano e un codice vista vengono cercati tutti i record associati a quel piano E quella vista.
E' inoltre possibile impostare le chiave1 o la chiave2 (tipo, tipo-parametro, codice o tipo-parametro-codice); questi filtri vengono gestiti tra loro in OR ma in AND con i filtri su piano, vista e famiglia.
Cioè se imposto il codice della chiave1 e il codice della chiave2 cerco tutti i record aventi quelcodice1 O quel codice2. Se imposto il tipo chiave1, il tipo chiave2, il codice piano e il codice vista cerco tutti i record aventi quel codice piano E il codice vista E il tipo chiave1 OPPURE quel codice piano E quel codice vista E il tipo chiave2.
Se imposto un oggetto in una chiave, cerco tutti i record che contengono quell'oggetto.
In particolare se imposto tipo-parametro e codice, individuo anche i record che contengono quell'oggetto e quelli che contengono quel tipo, quel codice e parametro BLANKS. Se invece imposto tipo e codice, individuo i record che contengono quel tipo e quel codice, indipendentemente dal parametro.
Nell'Oggetto1 è possibile specificare un piano, nell'Oggetto2 una vista, nell'Oggetto3 tipo e parametro e/o codice della chiave1, enll'Oggetto4 tipo e parametro e/o codice della chiave2 e nell'Oggetto5 una famiglia.
### Componente EXB
Genero l'XML di una matrice contenente tutti i dati gestiti (piano, vista, famiglia tipo chiave1, tipo chiave2, periodicità e data di inizio).
### Componente TRE
Genero l'XML di un albero contenente i codici relativi ad un solo dato.
E' possibile generare un albero con tutti i codici piano relativi ai filtri impostati, oppure l'albero delle viste, o dellefamiglie o dei tipo-parametro della chiave1 o dei tipo-parametro della chiave2.
Il tipo di dato nell'albero viene selezionato tramite il parametro CDLST :  PIA per i piani, VIS per le viste, FAM per le famiglie e TPKY per i tipi-parametri in chiave.

## Lista periodi associati ad un piano (PER)
Costruisce un lista con tutti i periodi presenti nel piano specificato.
Nell'Oggetto1 devo specificare il piano.

## Dati riferiti ad un preciso oggetto in chiave(OGG)
### Metodo MPP
Costruisce un albero a due livelli con tutti i piani e le viste in cui è presente l'oggetto in esame. Nel primo livello sono presenti i piani, mentre nel secondo le viste. E' posibile filtrare impostando la periodicità e/o la famiglia del piano e/o il tipo oggetto associato
alla vista (oltre al tipo dell'oggetto in esame).
Nell'oggetto 1 è necessario specificare l'oggetto in esame, nell'oggetto 2 è possibile specificare l'eventuale filtro sulla periodicità, nell'oggetto 3 è possibile specificare la famiglia di piani e nell'oggetto 6 è possibile specificare il tipo oggetto associato.
Il filtro su periodicità, famiglia e tipo è gestito in AND.

### Metodo MPC
Analogo a MPP, con la differenza che nel primo livello sono presenti le viste e nel secondo livello i piani.

### Metodo FEP
Costruisce un albero a due livelli con tutte le famiglie di piani e le periodicità associate all'oggetto in esame. Nel primo livello sono presenti le famiglie e nel secondo le periodicità.
Nell'oggetto 1 è necessario specificare l'oggetto in esame.

### Metodo OGA
Costruisce un albero con tutti i tipi oggetto associati all'oggetto in esame (ossia con tutti i tipi oggetto dell'altra chiave nei piani in cui è presente l'oggetto in esame.
Nell'oggetto 1 è necessario specificare l'oggetto in esame.

### Metodo MAT
Costruisce una matrice con i dati di tutti i piani e le viste associati all'oggetto in esame. Sono presenti la famiglia di piani, la periodicità, il piano, la vista, gli oggetti associati e le date di inizio.
Nell'oggetto 1 è necessario specificare l'oggetto in esame.

### Metodo DAT
Costruisce i grafici (o le matrici) riferiti all'oggetto in esame.
In particolare posso specificare sia il piano che la vista o entrambi. Se li specifico entrambi produco un grafico (o una matrice) con il dettaglio di tutti gli oggetti associati all'oggetto in esame (nel caso di vista con due chiavi), nel caso di vista con una chiave inserisco i dati del solo oggetto in esame. Se specifico solo il piano produco un grafico (o una matrice) con il riepilogo dei dati delle viste associate; in questo caso posso specificare un certo tipo oggetto associato da usare come filtro. Se specifico solo la vista produco un grafico (o una matrice) con il riepilogo dei dati dei piani associati; in questo caso posso specificare come filtro la periodicità e la famiglia di appartenenza dei piani. In caso non specifico un filtro e siano associati alla vista più piani con differenti periodicità (e quindi non confrontabili) viene visualizzato un messaggio di avvertimento e vengono caricati i dati dei soli piani confrontabili.
Nell'oggetto1 è necessario specificare l'oggetto in esame, nell'oggetto2 è possibile specificare la periodicità, nell'oggetto3 la famiglia, nell'oggetto4 il piano, nell'oggetto5 la vista e nell'oggetto6 l'oggetto associato.

Con tutti i metodi di questa funzione è possibile passare il parametro MSGFUP che abilita la visualizzazione di messaggi in caso di caricamenti parziali o errati dovuti al riempimento di alcune schiere in memoria. Il parametro deve valere 'SI' per abilitare l'emissione del messaggio e qualunque alra cosa (anche BLANKS) per disabilitarla.

>.         Descrizione                                  Para Comp Tipi
MPV       Caratteristiche piani e viste                PA20 CO10 TP90
PER       Lista periodi associati ad un piano               CO20 TP10
LOK       Lista oggetti associati al piano-vista            CO20 TP20
.1E2       nodo principale MPCD01 nodo figlio MPCD02
.2E1       nodo principale MPCD02 nodo figlio MPCD01
.UNO       tutti e solo MPCD01
.DUE       tutti e solo MPCD02
.2D1       solo MPCD02 associati all'MPCD01 in input             TP30
.1D2       solo MPCD01 associati all'MPCD02 in input             TP40
DAT       Dati del piano-vista                              CO30
.KY1       dettaglio oggetti in K1, un periodo         PA10      TP60
.KY2       dettaglio oggetti in K2, un periodo         PA10      TP50
.PER       dettaglio i periodi                                   TP70
.AK1       dettaglio oggetti in K1, tutti i periodi              TP60
.AK2       dettaglio oggetti in K2, tutti i periodi              TP50
.AKX       dettaglio ogg. in K1 o K2, tuttti i per.              TP95
OGG       Funzioni su oggetto                          PA30
.MPP       piani e viste associati                          CO20 TP96
.MPC       viste e piani associati                          CO20 TP96
.FEP       famiglie e periodicità associate                 CO20 TP97
.OGA       oggetti associati                                CO20 TP97
.MAT       matrice riepilogativa                            CO40 TP97
.DAT       dati associati                                   CO30 TP98

>.                                  TpParametro         Lung.DOVAuD         Tag
PA10 Periodo                       NR                  00003 O             PER
PA20 Codice colonna                                          F             CDLST
PA30 Visual mess schiere piene                         00002 F             MSGFUP

>.              2         3         4         5         6         7
CO10 EXB       TRE
CO20 TRE
CO30 EXA       EXB
CO40 EXB

>.          TpPa1       TpPa2       TpPa3       TpPa4       TpPa5       Descrizione
TP05 1 FFF
TP10 1 OOO TAMPP                                                       Piano
TP20 1 OOO TAMPP                                                       Piano
TP20 2 OOO TAMPC                                                       Vista
TP30 1 OOO TAMPP                                                       Piano
TP30 2 OOO TAMPC                                                       Vista
TP30 3 OFO                                                             Ogg. in chiave1
TP40 1 OOO TAMPP                                                       Piano
TP40 2 OOO TAMPC                                                       Vista
TP40 4 OFO                                                             Ogg. in chiave2
TP50 1 OOO TAMPP                                                       Piano
TP50 2 OOO TAMPC                                                       Vista
TP50 3 FFF                                                             Ogg. in chiave1
TP60 1 OOO TAMPP                                                       Piano
TP60 2 OOO TAMPC                                                       Vista
TP60 4 FFF                                                             Ogg. in chiave2
TP70 1 OOO TAMPP                                                       Piano
TP70 2 OOO TAMPC                                                       Vista
TP70 3 FFF                                                             Ogg. in chiave1
TP70 4 FFF                                                             Ogg. in chiave2
TP90 1 FFF TAMPP                                                       Piano
TP90 2 FFF TAMPC                                                       Vista
TP90 3 FFF                                                             Ogg. in chiave1
TP90 4 FFF                                                             Ogg. in chiave2
TP90 5 FFF TAMP*TP                                                     Famiglia
TP95 1 OOO TAMPP                                                       Piano
TP95 2 OOO TAMPC                                                       Vista
TP95 3 OFO                                                             Ogg. in chiave
TP96 1 OOO                                                             Ogg. in esame
TP96 2 FFF TAA£Q                                                       Periodicità
TP96 3 FFF TAMP*TP                                                     Famiglia
TP96 6 FFF OG                                                          Ogg. associato
TP97 1 OOO                                                             Ogg. in esame
TP98 1 OOO                                                             Ogg. in esame
TP98 2 FFF TAA£Q                                                       Periodicità
TP98 3 FFF TAMP*TP                                                     Famiglia
TP98 4 FFF TAMPP                                                       Piano
TP98 5 FFF TAMPC                                                       Vista
TP98 6 FFF OG                                                          Ogg. associato

