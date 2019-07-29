# Preparazione del Budget
Il budget è uno strumento che determina il bilancio di previsione dell'azienda nel prossimo esercizio. La formulazione del budget è un processo che viene svolto quasi interamente con l'utilizzo di funzioni MPS integrate da un'elaborazione MRP specifica.

## Ingresso al Budget
In MPS l'elaborazione del budget avviene a partire da una vista delle previsioni di vendita a livello articolo / cliente. Questa vista può essere : 
 * creata manualmente
 * provenire da un'elaborazione di previsione statistica in base ai consuntivi degli anni precedenti (es. previsioni con il metodo Holt Winters)
 * importata da un foglio elettronico esterno
 * ecc...
Comunque la definizione della previsione di vendita è un processo a monte e a parte.

## Flusso principale del Budget
Partendo dalla previsione di vendita abbiamo i passi seguenti : 
 * **Valorizzazione delle vendite**, avviene attraverso un'azione di flusso MPS che valorizza le quantità previste attraverso un listino di vendita. I prezzi dal listino vengono reperiti per articolo / cliente, con una data di validità che può essere quella iniziale o finale del periodo, con la valuta tipica del cliente e con un lotto che può essere l'intera quantità del periodo oppure una sua frazione (es. si possono ipotizzare spedizioni settimanali). Se il prezzo è in valuta questo viene convertito nella valuta corrente attraverso la gestione dei cambi di budget.
 * **Elaborazione MRP di budegt**, si lancia una elaborazione MRP in uno scenario di budget, con un gruppo fonti che vede solo la vista piano MPS e che genera dei suggerimenti pianificati di acquisto, conto/lavoro e produzione in funzione delle politiche associate agli articoli. Oltre alla pianificazione dei suggerimenti è consigliabile impostare lo scenario di budget in modo che il programma calcoli anche gli impegni risorse pianificati
 * **Ripresa fabbisogni risorse pianificate**, finita l'elaborazione MRP il flusso crea una vista dei fabbisogni risorse pianificati
 * **Ripresa disponibilità risorse da calendario**, la funzione costruisce una vista di disponibilità risorse presa dal calendario
 * **Confronto tra disponibilità e fabbisogno pianificato**, viene eseguito il confronto tra disponibilità e fabbisgni evidenziando in questa vista i sovrccarichi con delle qtà negative
 * **Ripresa produzione pianificata**, da MRP vengono riprese in questa vista le produzioni pianificate
 * **Valorizzazione produzione pianificata**, la produzione pianificata viene valorizzata con un proprio tipo costo/livello (es. costo standard, costo industriale)
 * **Ripresa acquisti pianificati**, da MRP vengono ripresi in questa vista gli acquisti pianificati, se esiste un fornitore preferenziale questo viene riportato nella vista
 * **Valorizzazione acquisti pianificati**, gli acquisti pianifciati vengono valorizzati con un listino di acquisto, nel listino in questione è possibile inserire dei prezzi con fornitore blank in modo da valorizzare comunque anche gli articoli che non hanno un fornitore preferenziale
 * **Ripresa conto / lavoro pianificato**, come sopra per il conto/lavoro
 * **Valorizzazione conto / lavoro pianificato**, come sopra

![MPBDGT_01](http://localhost:3000/immagini/MPBDGT_01/MPBDGT_01.png)