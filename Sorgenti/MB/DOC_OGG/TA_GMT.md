# GMT - Tecniche di gestione
## OBIETTIVO
Impostare i parametri che guidano la modalità di prelievo dei materiali a magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$GMT1 __Modalità di scarico__
È un elemento fisso MOSCA. Definisce se il componente, negli ordini di produzione, va prelevato manualmente, in modo automatico, ecc..
**NOTA1** :  Il valore B impone lo scarico dei componenti al versamento, mentre il valore D prevede lo scarico alla fase.
**NOTA2** :  Queste impostazioni possono essere superate dalla modalità di scarico della tabella P5I.
 :  : FLD T$GMT2 __Escluso da lista di prelievo__
Se impostato, gli articoli con questa tecnica non verranno inclusi nella lista di prelievo per la produzione.
