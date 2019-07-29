# Componente MAP - Documentazione tecnica
## UIMapModule
Classe che viene istanziata nel momento in cui arriva un evento di tipo MAP_EVENT.
Tramite il costruttore registra se stessa come listener degli eventi a Component e a MouseMotion, crea il parser per lo script e crea il pannello principale.
Lancia il parser dello script ottenendone l'xml che descrive il contenuto della mappa, aggiunge a se stessa le istanze di UIMapPanelBackground (una per ogni sezione definita nello script), setta un'eventuale immagine di sfondo, gestisce la visualizzazione delle coordinate nella barra sottostante riportandole in millesimi, setta le azioni da compiere nell'eventuale refresh automatico della videata, overriding del metodo paint.

### Devo modificare questa classe se : 
 F(02)
- Voglio modificare la disposizione delle sezioni sul pannello
- Voglio aggiungere/eliminare/modificare le azioni iniziali
- Voglio modificare la lettura dello script di definizione mappa
- Voglio modificare le azioni sul refresh automatico


## UIMapPanelBackground
Ogni istanza di UIMapPanelBackground corrisponde ad una sezione.
Svolge la funzione di contenitore; ha come attributi nome, posizione e forme contenute nella sezione. Crea un'istanza di UIMapLabelImage e la aggiunge a se stesso.

## UIMapLabelImage
Corrisponde alla vera e propria sezione :  carica l'immagine di sfondo, contiene un oggetto UIMapGrill che ne gestisce l'insieme di forme contenute, gestisce il repaint della sezione, implementa le azioni collegate agli eventi del mouse, gestisce le proporzioni tra le dimensioni dello schermo e le dimensioni della sezione.

### Devo modificare questa classe se : 
 F(02)
- Voglio modificare una qualsiasi caratteristica grafica della sezione
- Voglio aggiungere/eliminare/modificare le azioni collegate al mouse
- Voglio modificare l'azione di repaint sulla sezione
- Voglio modificare il comportamento della sezione in relazione ad un qualsiasi tag definito nello script di partenza

(Insomma nel 90% dei casi dovete agire qui)

## UIMapGrill
E' il gestore dell'insieme di forme di una sezione. Contiene un array di forme e le coordinate per gestire il rapporto ai millesimi dello schermo.

### Devo modificare questa classe se : 
 F(02)
- Voglio modificare il rapporto alle dimensioni dello schermo
- Voglio modificare le funzionalità di gestione delle aree (Area = Forma attiva e sensibile al mouse)


## UIMapScrReader
E' il generatore di xml dato il contenuto dello script di definizione.

### Devo modificare questa classe se : 
 F(02)
- Ho aggiunto/eliminato/modificato una parte dello script e dunque l'xml dovrà parserizzare una sintassi differente


## UIMapPolyLine
Superclasse di tutte le forme. Contiene le caratteristiche comuni ad ogni forma (Nome, array di coordinate, colore, testo, immagine, tooltips,ecc..)e il metodo per la  loro costruzione partendo dall'xml di definizione.

### Devo modificare questa classe se : 
 F(02)
- Voglio aggiungere/eliminare/modificare una qualsiasi caratteristica comune a tutte le forme


## UIMapPolygon
Classe che implementa la forma poligonale (estende UIMapPolyLine).

## UIMapRectangle
Classe che implementa la forma rettangolare (estende UIMapPolyLine).

## UIMapCircle
Classe che implementa la forma circolare (estende UIMapPolyLine).

## UIMapTimer
Classe per il refresh automatico della mappa
