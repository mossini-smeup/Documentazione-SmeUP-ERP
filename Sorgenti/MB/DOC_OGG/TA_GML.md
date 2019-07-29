# GML - Lotto di conta inventariale
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$DESC Descrizione
È la descrizione del lotto di conta.
 :  : FLD T$GMLA __Codice inventario__
È il codice dell'inventario corrispondente.
 :  : FLD T$GMLB __Numero iniziale__
Numero iniziale cartellino
 :  : FLD T$GMLC __Numero finale__
Numero finale cartellino
 :  : FLD T$GMLQ __Compl.Numero con 0__
Inserendo il valore '1', il numero cartellino inserito viene completato con '0' iniziale (es. se si inserisce il valore '1' diventa automaticamente '0000000001')
 :  : FLD T$GMLD __1° numero non utilizzato__

 :  : FLD T$GMLE __Responsabile__

 :  : FLD T$GMLF __Area giacenza assunta__
Area giacenza assunta in creazione cartellino
 :  : FLD T$GMLG __Tipo giacenza assunta__
Tipo giacenza assunta in creazione cartellino
 :  : FLD T$GMLH __Numeratore cartellini__
Numeratore da CRN
 :  : FLD T$GMLI __Area protetta__
Se valorizzato, protegge in gestione il campo Area giacenza e, nella generazione cartellini da estrazione inventario, riprende solo quelli che hanno l'area giacenza corrispondente a quella scelta sopra.
 :  : FLD T$GMLJ __Tipo protetto__
Se valorizzato, protegge, in gestione, il campo tipo giacenza e, nella generazione cartellini da estrazione inventario, riprende solo quelli che hanno il tipo giacenza corrispondente a quello scelto sopra.
 :  : FLD T$GMLM __Visualizza quantità prevista in gestione lista__
Se valorizzato, visualizza la quantità prevista nella gestione in lista dei cartellini di conta.
 :  : FLD T$GMLN __Modalità numerazione cartellini__
La numerazione dei cartellini viene eseguita secondo tre possibili modalità : 
1= Generazione manuale.
Controlla i limiti iniziale e finale, se impostati. Non è possibile utilizzare le funzioni ripresa di massa.
2= Generazione automatica da limite iniziale a finale.
Controlla limiti iniziale e finale. In generazione di massa carica i cartellini numerandoli dal valore inziale e controllando che non superino il valore finale. In tal caso viene emesso un messaggio di operazione non completata regolarmente ed è possibile incrementare il limite finale per caricare i rimanenti cartellini.
I valori dei limiti devono essere numerici, della stessa lunghezza, e inseriti da destra verso sinistra.
_9_Esempio : 
'00001     '  SI.
'     00001'  NO.
Se fosse necessario incrementare il numero finale è possibile aumentare anche la lunghezza dei caratteri usati per i limiti.
_9_Esempio : 
Limite iniziale  da '001            ' a  '0001           '.
Limite finale    da '999            ' a  '9999           '.
3= Generazione automatica da numeratore.
Non controlla i limiti iniziale e finale. In generazione di massa numera i cartellini in funzione del valore del numeratore.
