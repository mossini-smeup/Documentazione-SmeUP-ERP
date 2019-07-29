# Obiettivo
Permettere l'inserimento dei Profili di Posizione.

## Formato guida
![CQ_PERS_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP10/CQ_PERS_06.png)
Si immette : 
 * _2_Profilo di Posizione,  è un campo tabellato CQ*DA che identifica il codice del profilo. Utilizzando la barra (/), si può consultare l'archivio in cui sono contenuti tutti i profili che sono già stati inseriti fino a quel momento, come è riportato qui di seguito (sono attivi come sempre i soliti strumenti di ricerca e di parzializzazione)
 * _2_Subfattore, è un campo tabellato CQ*DB che identifica il codice del subfattore.
 * _2_Dettaglio Competenza, è un campo tabellato CRH che identifica il codice del dettaglio.

Supponiamo di non scegliere un profilo già esistente ma di crearne un nuovo riguardo alla posizione di "EDP-Manager" :  si desidera ad esempio stabilire, nella sfera delle competenze relazionali  (subfattore  "Relazioni"), un livello di valutazione di riferimento per quanto concerne lo "sviluppo dei collaboratori". Quando si andrà a definire lo skill del manager "A", sarà richiesto di inserire un giudizio sulla conoscenza delle tecniche in oggetto per vedere se supera gli standard minimi.

## Formato dettaglio
![CQ_PERS_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQGP10/CQ_PERS_07.png)
 * _2_Importanza Dettaglio, è un campo tabellato CRE che permette di specificare, il peso che si ritiene che abbia un particolare aspetto del profilo di posizione in oggetto nella sua valutazione complessiva. Si può ritenere che nell'ambito della figura professionale dell'EDP Manager, la padronanza delle tecniche di relazione è una caratteristica rilevante. Il valore dell'importanza attribuito alla specifica competenza, viene moltiplicato per la valutazione assegnata, e di tutte le competenze viene fatta una media pesata che definisce il livello del profilo :  questo discorso vale sia per il profilo ideale sia per lo specifico dipendente.
 * _2_Valutazione Minima Richiesta, è un campo tabellato CRF che specifica il valore minimo accettabile che deve avere un dipendente la cui posizione coincide con il profilo indicato. È una soglia di riferimento che viene confrontata con la valutazione attribuita al dipendente; se dal confronto emerge che il livello del dipendente è inferiore a quello di soglia si può decidere di assumere provvedimenti volti all'addestramento e alla formazione al fine di colmare le lacune riscontrate.

Esempi di valutazioni sono le seguenti : 
 * SCARSO :           non raggiunge gli standard;
 * SUFFICIENTE :  raggiunge gli standard;
 * DISCRETO :       supera gli standard;
 * OTTIMO :           supera largamente gli standard;
 * ...

Il nuovo profilo così creato va ad aggiungersi a quelli già presenti nell'archivio dedicato alla posizione di "EDP Manager".
