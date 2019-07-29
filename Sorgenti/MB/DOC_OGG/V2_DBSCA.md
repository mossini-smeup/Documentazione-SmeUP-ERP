# DBSCA     -  TRATTAMENTO SCARTI IN DISTINTA BASE
Definisce il modo in cui gli scarti contribuiscono alla determinazione della quantità del componente nell'esplosione
di distinta base.
Gli scarti possono essere : 
-    di assieme :  si inseriscono nei parametri logistici d'ordine.
     Perchè siano effettivamente considerati deve inoltre essere impostato in tabella P51 che si intendono trattare gli
     scarti di assieme (è valorizzato il campo 'Modo calcolo scarti').
     Sono trattati nelle esplosioni di produzione, (dal tipo esplosione '3' in poi), e se l'assieme è un articolo.
     Essi aumentano la quantità dell'assieme da esplodere, prima di applicare il coefficiente di impiego, secondo la
     modalità specificata in tabella P51 (scarti sulla quantità buona o sulla quantità ordinata). La quantità
     dell'assieme così calcolata viene poi arrotondata in funzione di quanto impostato nella tabella dell'unità di
     misura dell'assieme.
-    di legame :  si inseriscono nel legame di distinta.
     Essi si intendono sempre come una percentuale di aumento del coefficiente di impiego.
     La quantità risultante del componente (eventualmente aumentata della quantità per lotto), viene poi arrotondata in
     funzione di quanto impostato nella tabella dell'unità di misura del componente.

## VALORI POSSIBILI

### ' ' NESSUNO
Non vengono considerati gli scarti.

### 'A' DI ASSIEME
Vengono considerati solo gli scarti di assieme.
Se questa opzione non è sceglibile, significa che in tabella P51 non è attiva la gestione scarti.

### 'B' DI LEGAME
Vengono considerati solo gli scarti di legame.

### '*' ENTRAMBI
Vengono considerati entrambi gli scarti.
Ricordo che in questo caso l'eventuale arrotondamento dell'unità di misura viene applicato separatamente per lo scarto
di assieme e per quello di legame.
Se questa opzione non è sceglibile, significa che in tabella P51 non è stata attivata la gestione scarti.
