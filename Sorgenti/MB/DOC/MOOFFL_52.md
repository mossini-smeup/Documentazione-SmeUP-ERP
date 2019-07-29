# Raccolta ordini
## Sintesi degli obiettivi

App :  Raccolta Ordini (che è la prima sotto-app diciamo)

L'agente entra e sceglie fra i suoi clienti assegnati (agenti diversi possono avere lo stesso cliente per famiglie di prodotto diverso, fresco e secco)
Può scegliere ricercando da una lista, cercando per comune, o tramite geoposizionamento (o altre idee)

Quando ho scelto il cliente il suo dashboard è fatto da : 
- Ultimo ordine e poi da qui può dire, parti da qui per farne uno nuovo
- Estratto conto con quello che deve essere ancora pagato
- Storico ordini (un X numero degli ultimi ordini fatti)
o Oppure i prodotti più comprati dal cliente (per poi dire, aggiungi al carrello)
- Articoli in promozione (che l'agente può proporre)
- Articoli completi
o Ci possono essere alcuni prodotti che non devono essere visibili da un cliente specifico

Mediamente vengono ricevuti 150 - 200 ordini al giorno, mediamente con 20 righe ad ordine

## Fase 1

AGENTE   AZIENDA

ORDINI
Nella maggior parte dei casi l'agente parte dall'ultimo ordine fatto e lo copia identico.
Alcune volte è lo stesso agente che nei magazzini del cliente decide cosa mettere in ordine
1 ordine ha 1 data di consegna. Diverse date di consegna corrispondono a diversi ordini da parte dell'agente (perché gli ordini vengono evasi subito quindi non hanno senso date diverse per un ordine).
A meno di problemi di rotture di stock che eventualmente vengono gestiti internamente.

Dai listini il cliente ha le sue scontistiche approvate su famiglia/prodotti ecc che dipendono dal cliente.
L'agente in fase di ordine può chiedere uno sconto diverso per un prodotto.
Deve quindi essere previsto che l'agente "richiede" per un articolo uno sconto 10+2+2 (invece del 10+2 previsto) oppure un 3x2
L'ordine deve calcolare il totale giusto con lo sconto chiesto dall'agente (perché il cliente vuole sapere il totale dell'ordine quando è con l'agente), anche se poi quest'ordine deve essere approvato dal customer service perché non è standard.

ESTRATTO CONTO
La parte di estratto conto serve perché l'agente riscuote le fatture che il cliente deve pagare.
L'agente deve poter quindi dire : 
- Oggi ho incassato 300 ¤ (scrivendo il totale incassato) che va a saldare le fatture (o eventualmente considerare l'acconto per altre se non è completa la somma)
o Se ho due fatture da 200 ¤, una viene saldata e 100 ¤ vanno come acconto dell'altra.


AZIENDA   AGENTE

Nella fase 2 l'azienda potrebbe voler comunicare alcune cose all'agente : 
Evasione dell'ordine : 
- Un popup/Notifica, oppure un altro bollo per dire :  Questo tuo ordine è stato evaso oggi. Tutto, oppure tutto a parte queste 5 cose.
Questo avviene quando la bolla viene stampata

Nella fase 3 se tutto funziona correttamente si possono aggiungere App oltre alla Raccolta Ordini per informare gli agenti (o la direzione)
Si potrebbe far vedere qualcosa all'agente delle sue statistiche
- Venduto per famiglia
- Venduto per cliente
- Andamento rispetto al suo budget

OSSERVAZIONI-DOMANDE

- Ma c'è anche per il browser normale sul web questa app? perché gli agenti meno "moderni" o se esteso l'uso ai grossisti potrebbero usare il browser (per non avere scheramte diverse se un domani si vuole farla per il web)
- Do per scontato il suo funzionamento su Mobile e sia su iOS che Android

