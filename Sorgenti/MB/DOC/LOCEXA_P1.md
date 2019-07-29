# Versione 1.0.h
 1. Se l'Xml ricevuto non contiene le specifiche nell'attribute Fill di Asse e Serie, vengono
    richiesti "on-demand"

# Versione 1.0.i
 2. Aggiunta Possibilità di modificare Assi e Serie anche successivamente
 3. Eliminata gestione nodo Setup

# Versione 1.0.n
 4. Il Componente è stato sostituito da una "Scheda Virtuale"

# Versione 1.8.c
## 5.1 Sono stati aggiunti dei pulsanti che consentono le seguenti operazioni : 

- ordinamento crescente/descescente
- Inversione asse/serie.
- Nascondere la legenda e il pannello condati/serie.
- Visualizzare la serie di media, deviazione standard, interpolazione, cumulativo di ogni serie presente sul grafico.
- Visualizzare le serie di somma, sottrazione, moltiplicazione, divisione delle prime due serie caricate. Sarà disponibile in futuro la possibilità di selezionare a quali serie applicare le operazioni in questione.
- personalizzare le funzioni(cambiare tipo di serie o cambiare il numero di punti utilizzato)

Questi pulsanti sono presenti solo se nel setup si specifica la presenza dei comandi.

## 5.2 Ordinato l'asse se di tipo numerico o di tipo data.

## 5.3 Aggiunte le voci GrpBy GrpOp che consentono di raggruppare serie e di definire un'operazione da applicare.
Se l'asse è temporale posso raggruppare per giorno (GrpBy=Day), per mese (GrpBy=Month), per anno (GrpBy=Year).
Le operazioni disponibili sono per ora limitate alla somma (GrpOp=SUM).

NOTA Questi due attributi non sono stati aggiunti al wizard

# Versione 1.8.d  ANCORA DA RILASCIARE
## 6.1 Aggiunte le voci GrpBy GrpOp al wizard di script
