# Struttura numeri documenti

|  Nam="Struttura numeri documenti" |
| 
| .COL Txt="Numero" LunAut="1" |
| ---|----|
| 
| .COL Txt="Uscite" LunAut="1" |
| 
| .COL Txt="Entrate" LunAut="1" |
|  Documento | Interno | Interno |
|  Bolla | Interno | Esterno |
|  Fattura | Interno | Esterno, da "G91" (Riferimento esterno - N. Fattura Fornitori; N. Protocollo contabilità) |
| 


# Struttura numeri documenti in movimenti magazzino
## Ciclo attivo

|  Nam="Struttura numeri documenti in movimenti magazzino - Ciclo attivo" |
| 
| .COL Txt="Numero" LunAut="1" |
| ---|----|
| 
| .COL Txt="Uscita" LunAut="1" |
| 
| .COL Txt="Reso" LunAut="1" |
|  Documento Interno | Riferimento Interno | Riferimento Interno |
|  Documento Esterno | Nostra Bolla | Loro Bolla |
|  Documento Contabile | Nostra Fattura | Nostra Nota Credito |
| 

## Ciclo passivo

|  Nam="Struttura numeri documenti in movimenti magazzino - Ciclo passivo" |
| 
| .COL Txt="Numero" LunAut="1" |
| ---|----|
| 
| .COL Txt="Reso" LunAut="1" |
| 
| .COL Txt="Entrata" LunAut="1" |
|  Documento Interno | Riferimento Interno | Riferimento Interno |
|  Documento Esterno | Nostra Bolla | Loro Bolla |
|  Documento Contabile | Loro Fattura, se Nota d'addebito = Nostra Fattura (oppure documento contabile da "G91") | Nostra Nota Credito (oppure documento contabile da "G91") |
| 

