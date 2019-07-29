# GMTMO     -  TIMP MOVIMENTO MAGAZZINO
Definisce la natura del movimento di magazzino in modo noto all'applicazione, che in tal modo può assumere dei
comportamenti specifici in funzione di esso.

## VALORI POSSIBILI

### AC ALTRI CARICHI
Movimenti di carico generici

### AC ALTRI SCARICHI
Movimenti di scarico generici

### DO DOCUMENTIO CICLO ESTERNO
E' un movimento a fronte di una spedizione, un ricevimento o un trasferimento, a fronte di una riga di ciclo esterno
(attivo o passivo).

### MV MOVIMENTO A VALORE
E' un movimento che non prevede carichi/scarichi di giacenza, normalmente usato quando si attribuisce valore a
movimenti neutri.

### PP PRELIEVO DI PRODUZIONE
E' un prelievo a fronte di un impegno interno di produzione, che viene ridotto della quantità del prelievo.

### PE PRELIEVO ESTERNO
E' un prelievo a fronte di un impegno esterno di lavorazione, che viene ridotto della quantità del prelievo.

### PS PRELIEVO PER SCARTO
E' un prelievo a fronte di un impegno interno di produzione, che però non viene ridotto della quantità del prelievo.

### PD PRELIEVO SU DISPONIBILITÀ CHIAMATA
E' un prelievo per la produzione, nell'ambito della gestione a pdc.

### PN PRELIEVO NON PIANIFICATO
E' un prelievo per la produzione, non a fronte di un impegno, che può essere o meno assegnato ad un ordine interno.

### RI RETTIFICA INVENTARIALE
E' un movimento a fronte di uno scostamento rilevato durante una conta inventariale, sia generato manualmente sia
nella correzione dopo l'inventario.

### ST SOLO STATISTICO
E' un movimento che non modifica la giacenza. Per ottenere questo effetto, nella causale si devono lasciare in bianco
area e tipo giacenza.

### TR TRASFERIMENTO TRA AREE
E' un movimento manuale di prelievo o versamento da un'area che, nella transazione, sarà eseguito insieme ad in altro
movimeno manuale di versamento o prelievo.

### VP VERSAMENTO DI PRODUZIONE
E' un versamento a fronte di un ordine di produzione, che viene ridotto della quantità del versamento.

### VE VERSAMENTO ESTERNO
E' un versamento a fronte di un ordine di produzione, indotto dalla dichiarazione di avanzamento di ultima fase
esterna del ciclo.

### VS VERSAMENTO PER SCARTO
E' un versamento a fronte di un ordine di produzione, che però non viene ridotto della quantità del versamento.

### VD VERSAMENTO DISPONIBILITÀ CHIAMATA
E' un versamento da produzione, nell'ambito della gestione a pdc.

### VN VERSAMENTO NON PIANIFICATO
E' un versamento manuale, non a fronte di un ordine di produzione.
