## Cos'è l'ATP
L'ATP è un modulo che permette di determinare la data di consegna di una certa quantità di articolo, e quindi per esempio viene usato negli ordini di vendita per determinare la data di consegna confermata.
## ATP :  avviamento veloce
Per far partire velocemente l'ATP bisogna seguire il seguente procedimento.

Leggere la parte relativa nel documento di visione.

Poi bisogna eseguire i seguenti passi : 

 - definire la fonte Impegno Provvisorio in tabella M5F
    Tipo impegno considerato
    ' '  tutti gli impegni (sia '1' sia '2')
    '1'  consumi su disponibilità esistente
    '2'  nuovi impegni
     Tipo provvisorio
        ' '  Impegno provvisorio "confermato"
        '1'  Impegno provvisorio "provvisorio"
     NB :  Gli impegni provvisori del primo tipo sono quelli che vengono confermati dopo l'esecuzione dell'ATP, mentre i secondi sono gli impegni che vengono creati durante l'esecuzione
     dell'ATP.
 - definire la fonte disponibilità provvisoria in tabella M5F
 - definire un gruppo fonti che le comprende e che comprende anche le fonti normalmente incluse nell' MRP, ad esclusione delle fonti negative utilizzate per creare scorta di magazzino, perchè     l'ATP permette di ottenere una data anticipata rispetto al leadtime cumulato utilizzando le scorte di magazzino !
 - Creare una fonte che sia la disponibilità libera di questo gruppo fonti
 - Creare un gruppo fonti che includa solo questa fonte
 - A questo punto puo' essere creato il modello di ATP nella tabella M5H, seguendo l'Help della tabella M5H
 - Testare l'ATP


## Tabelle di ATP
Leggere attentamente l'help della tabella M5H
 :  : DEC T(ST) K(M5H)
Deve esser compilato un elemento che rappresenti un modello di ATP e create due fonti specifiche, di origine IR (impegni provvisori) per gli impegni e le disponibilità provvisorie.
 :  : DEC T(ST) K(M5F)
## Come agganciare il calcolo ATP alle righe di ordini V5
Per agganciare il calcolo ATP alla riga d'ordine bisogna impostare le seguenti parametrizzazioni : 
- Tabella V5D, tipo documento :  impostare il flag "ATP abilitato" a 1= sì
- Tabella V5B, tipo riga :  impostare il modello ATP (elemento M5H) nel campo "modello ATP"
- Flusso di creazione della riga di ordine di vendita  (B£H, elemento I-DRxxx) :  tra le azioni del flusso bisogna impostare il programma V5FUATPA che offre le seguenti parametrizzazioni : 

Funzione               		CAL                  Calcolo
Tipo esecuzione        		I                    Interattiva
Signif. Dt.Conf manual                     Data libera
Mem.Dt.conf.precedente                 Non memorizzata
Mem.Data Atp in conf.  1                 Memorizzata in data confermata
Mem.Data Atp in altre                      Non memorizzata in altra data
Modo tracciamento ATP  1              Grafico  ATP (se interattivo)
Suff.pgm.agg. modello











