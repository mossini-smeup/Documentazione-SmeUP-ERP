# Costruzione statistica del contabilizzato

## Quadratura con contabilità
La statistica del contabilizzato ha come requisito la quadratura con la contabilità. L'importo a livello di conto contabile della statistica deve corrispondere con i rispettivi valori della registrazione contabile. Per ottenere questo obiettivo, una volta estratti i valori della fattura dai documenti V5, con una scansione della relativa registrazione contabile, vengono scritti sulla statistica dei record di integrazione e di quadratura.
I record di integrazione della registrazione contabile sono intestati all'oggetto E4 (D6TPOG='E4') e quindi il codice oggetto corrisponderà al numero di registrazione. I record di quadratura sono intestati ad un oggetto generico ** (D6TPOG='**'). Nel codice oggetto sarà riportata la dicitura "Quadratura Conto".

**Esempio**
Nel caso riportato la fattura 001618 è stata registrata in contabilità cambiando il conto contabile per la riga relativa all'articolo S302 :  il fatturato dell'articolo è stato imputato non più sul conto 7002001, ma sul conto 7003003.
Le prime 3 righe della statistica sono derivate dal documento V5 :  il tipo oggetto intestatario è AR.
 Il 4° record della statistica è  intestato all'oggetto E4, codice oggetto è il numero di registrazione contabile e rappresenta l'integrazione da contabilità del valore del conto 7003003.
Poiché il totale della fattura in statistica deve essere congruente, viene scritto un'ulteriore riga di quadratura, intestata all'oggetto generico **, di segno negativo, che riporta il totale al valore corretto.

![V5STAT_010](http://localhost:3000/immagini/V5STAT_09/V5STAT_010.png)E' possibile configurare il modulo statistiche in modo da non effettuare il controllo con i valori contenuti in contabilità, evitando quindi di scrivere record di integrazione e quadratura (vedi il paragrafo CONFIGURAZIONE della presente documentazione)

## Aggiustamento periodi di competenza
Per ogni registrazione contabile di ciclo attivo, i programmi di ripresa della statistica eseguono la verifica se è necessario un'aggiustamento per quanto riguarda la data di competenza dei valori registrati, cioè se è necessario cambiare l'esercizio e il periodo di competenza.

In contabilità viene verificato se ci sono registrazioni collegate di cambio competenza : 
T5FL20='C' , riattribuzione competenza
T5FL01>'2' , competenza gestionale

Se necessario, viene operata la redistribuzione dei valori scrivendo 2 record : 
 * uno negativo per togliere l'importo dalla competenza originale
 * uno positivo per ridistribuirlo su quello di destinazione.

Nell'esempio riportato è stata spostata la competenza della fattura dal mese di marzo 2003 (Periodo 200303) al mese di febbraio (Periodo 200302).
Sui record scritti dal programma, sulla descrizione dell'oggetto compare la dicitura "RETTIFICA per COMPETENZA".

![V5STAT_011](http://localhost:3000/immagini/V5STAT_09/V5STAT_011.png)