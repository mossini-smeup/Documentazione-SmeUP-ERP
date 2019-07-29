## Previsioni con Holt Winters
### Introduzione
Questo passo calcola, a partire da una vista di input**(vista storica)**la previsione futura con il metodo di Holt Winters (nel seguito HW) e ne memorizza il risultato nella vista di output**(vista previsioni)**. NB; nella vista di output oltre alle previsioni nei periodi futuri vengono calcolate anche le previsioni HW relative alla storia (in questo modo è possibile ad esempio l'applicazione dell'autofit senza arretramento e per il calcolo del coefficiente di bontà della previsione).
Per una esposizione dettagliata del metodo HW : 
- [Previsioni con Holt Winters](Sorgenti/MB/DOC/B£MATE_01)
 :  : I.INC.MBR Fil(DOC_OPE) Mem(MP_INC002)
### Periodicità
E' un campo obbligatorio. Si imposta il numero di periodi dopo i quali la serie assume, approssimativamente, lo stesso valore. Ad esempio, una periodicità di 12 mesi indica che la forma della serie si ripete (con picchi e valli) dopo questo intervallo.
 :  : I.INC.MBR Fil(DOC_OPE) Mem(MP_INC003)
Non può essere minore della periodicità aumentata di 1, in HW additivo, e di due volte la periodicità, in HW moltiplicativo. Una storia più estesa (e quindi almeno di due periodicità) smorza gli effetti della stagionalità.
### Numero periodi iniziali
E' un campo facoltativo :  se non impostato, si assume pari alla periodicità. Deve essere maggiore di 1 e minore o uguale alla storia. Indica il numero di periodi su cui si esegue l'interpolazione per determinare i valori iniziali  di livello e trend, necessari per il calcolo. Un valore vicino ad 1 rafforza i periodi iniziali, un valore vicino alla storia considera tutti i periodi in modo più uniforme.
 :  : I.INC.MBR Fil(DOC_OPE) Mem(MP_INC004)
### Fattori di smorzamento
**Alfa, Beta, Gamma**
Indicano il peso, all'interno della storia, dei periodi più recenti rispetto a quelli  più remoti, rispettivamente per il livello, il trend e la stagionalità. Il loro valore va da 0 (conta solo il primo periodo) ad 1 (conta solo l'ultimo periodo). Per ognuno di essi si può, in modo indipendente dagli altri due : 
* impostare il campo di autofit (in modo che il sistema calcoli il valore ottimo)
* lasciare in bianco l'autofit e impostare un valore tra 0 (il che corrisponde a utilizzare solo il periodo iniziale) e 1 (il che corrisponde a utilizzare solo il periodo finale). Il default se il campo non è impostato è 0.
Un valore sufficientemente adeguato per i tre coefficienti si è rivelato essere 0,2, senza ricorrere all'autofit (che comporta tempi di elaborazione estremamente più lunghi).
__Nota Bene__; il campo autofit e il valore sono alternativi :  se il valore è impostato l'autofit deve essere blank.
A seconda delle versioni installate, se impostato il campo autofit può assumere valori : 
* 1 = attivo autofit, il sistema itera il calcolo con valori di incremento del fattore di smorzamento a passo 0,2 :  valori 0 - 0,2 - 0,4 - 0,6 - 0,8 - 1
* da 2 a 9 = autofit con passo variabile, il passo di incremento del fattore di smorzamento viene calcolato dividendo l'intervallo tra 0 e 1 in un numero pari a quello inserito nel campo, il calcolo viene iterato incrementando di volta in volta il fattore di smorzamento con un valore pari al passo calcolato

### Autofit senza arretramento
Se si imposta di calcolare almeno uno dei tre fattori di smorzamento, e la storia non vale almeno tre periodicità, deve essere impostato questo campo, e quindi eseguire  il test direttamente sul periodo di previsione. In assenza di questa impostazione si devono poter ritagliare due periodicità di training ed una di test. A rigore, per l'HW additivo, sarebbero sufficienti due periodicità più uno, ma si è preferito  avere un periodo di training più robusto.
### HW Moltiplicativo
Se impostato, la previsione verrà eseguita con il metodo moltiplicativo, (più sensibile alla variazioni stagionali). Se invece si lascia in bianco, verrà utilizzato il metodo additivo (impostazione consigliata).
 :  : I.INC.MBR Fil(DOC_OPE) Mem(MP_INC005)
### Indice autofit
Se impostato il calcolo dei fattori di smorzamento tramite autofit, in questo campo si seleziona l'indice di confronto per stabilire la migliore previsione, tra i tre valori calcolati e memorizzati nei numeri dell'MPS : 
* % di errore (default)
* Mape
* Sigma
### Memorizzazione numeri
E' possibile memorizzare, sia i numeri di dettaglio sia i numeri di riepilogo, su appositi record di D5COSO.
Con questo campo si può impostare di : 
* ' ' Memorizzare sia i numeri di dettaglio sia i numeri di riepilogo
* '1' Memorizzare solo i numeri di dettaglio
* '2' Memorizzare solo i numeri d riepilogo
* '3' Non memorizzare i numeri
E' consigliato il popolamento delle tabelle relative a questi numeri con il programma D5FS01A (contesti AR e MP)
### Numeri di dettaglio
Sono memorizzati dopo aver calcolato le previsioni di ogni articolo. Per la loro memorizzazione, devono verificarsi le seguenti condizioni : 
* Le viste devono avere il codice 1 di tipo AR e il codice 2 o vuoto o di tipo TAMAG.
* Se l'applicazione è multiplant, nel codice piano deve essere impostato il plant (A), oppure il plant è il codice 2 della vista (B).
Il contesto è AR (articolo) ed il tema £P1 (del sottosettore AR). Il codice 1 è il plant (anche se applicazione monoplant), ripreso dal plant fisso in applicazione monoplant, dal plant del piano nel caso (A) e dal plant del record nel caso (B). Il campo data/periodo viene riempito con la data iniziale del periodo successivo alla frontiera.
### Numeri di riepilogo generali
Sono memorizzati al termine del calcolo delle previsoni di tutti gli articoli. Il contesto è TAMPC (codice vista) ed il tema £P2 (del sottosettore MP). Il codice 1 è il piano. Il campo data / periodo è lasciato vuoto, in quanto la coppia vista / piano è univoca.
### Numeri di riepilogo per plant.
Sono memorizzati al termine del calcolo delle previsoni di tutti gli articoli se l'applicazione è multiplant. Il contesto è TAMPC (codice vista) ed il tema £P3 (del sottosettore MP). Il codice 1 è il piano. Il codice 2 è il plant, ripreso dal plant del piano nel caso (A) e dal plant del record nel caso (B). Il campo data / periodo è lasciato vuoto, in quanto la coppia vista / piano è univoca.
### Vista di statistica Hotelling
Per ogni record di previsione viene scritta una vista che riporta la statistica Hotelling, allo scopo di analizzare la prevedibilità della serie. Il piano è lo stesso delle previsioni. La vista, di codice fisso £P1 (elementi del settore MPC che viene costruito automaticamente al primo richiamo), ha la stessa tipizzazione delle viste di storia e di previsioni (primo codice fisso "AR" e secondo codice o bianco o "TAMAG"). Essa riporta il valore della statistica per ogni elemento della storia. Ad esempio, con una frontiera al periodo 36, ed una storia di 24 periodi, sono valorizzati gli elementi dal 13 al 36 della vista £P1. Vengono inoltre valorizzati i primi quattro numeri del record della vista : 
 - Nel primo numero, il numero di elementi che superano il limite. E' sufficiente che il limite sia superato una sola volta, perchè la serie non sia prevedibile.
 - Nel secondo numero, il valore limite (che dipende dal numero di periodi della storia)
 - Nel terzo numero, il primo periodo della storia (primo periodo siginificativo della vista MPS di Hotelling).
 - Nel quarto numero, l'ultimo periodo della storia (ultimo periodo siginificativo della vista MPS di Hotelling).
