# Descrizione
Nel processo di schedulazione vine controllata una serie di errori.

Essi si dividono in due tipi : 
* Errori bloccanti (livello 99)
La presenza di almeno uno di essi fa sì che la schedulazione non possa essere eseguita :  viene presentata, al posto della scheda dei risultati, una matrice contenente tutti gli errori riscontrati (sia bloccanti sia non bloccanti).
* Errori non bloccanti (livello minore di 99)
Questi errori vengono corretti automaticamente (con assunti, esposti nel seguito di questo documento)  :  la schedulazione giunge al termine e, anche se il risultato non è del tutto esatto, il completamento fa sì che siano rilevati tutti gli errori non bloccantii.
In presenza di errori, nella scheda master viene proposto il pulsante "Errori presenti :  controlla", che fa passare alla presentazione della matrice con il dettaglio degli errori.

In questa matrice gli oggetti coinvolti sono "oggettizzati", è quindi possibile, avendone l'autorizzazione, correggere gli errori rimanendo all'interno di questa applicazione.

Nel seguente esempio, gli errori sono dovuti ad un filtro errato sulle risorse secondarie dell'ordine di produzione, Cliccando sul codice dell'ordine, si può passare alla sua scheda, e da essa alla gestione delle risorse secondarie. Dopo aver eseguite le modifiche, si torna a questa scheda, e da essa alla scheda base,  dalla quale è possibile lanciare una nuova schedulazione con i dati corretti.

![FIG_058](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_ERR/FIG_058.png)
Gli errori bloccanti controllati sono i seguenti : 
* riempimento delle memorie (numero massimo di impegni risorse, di alternative, di dettagli)
* assenza della risorsa principale definita nel ciclo, oppure di una risorsa specifica definita nel filtro delle risorse secondarie
* esiste almeno un record con l'IDOJ vuoto.
Viene registrato un solo errore, indipendentemente dal fatto che ci sia uno o più IDOJ mancanti,  in quanto presumibilmente questa situazione è presente per un gran numero di record (potenzialmente  tutti). Per questo stesso motivo, non vengono riportati gli estermi del record anomalo. La scheduiazione non viene eseguita in quanto, pur essendo corretta, potrebbe dar luogo ad errori imprevedibili nelle successive attività manuali. Si deve rimuovere la causa dell'errore (presumibilmente mancanza del numeratore in tabella P51), rigenerare gli impegni risorse e rieseguire la schedulazione.
Attenzione :  verificare se l'archivio S5IDIR0F (di corrispondenza tra chiave estesa e IDOJ) contiene dei record con IDOJ vuoto, nel qual caso essi vanno elminati fisicamente.

Gli errori non bloccanti controllati sono i seguenti : 
* controllo deadlock
se una fase viene eseguita sulla stessa risorsa principale di una fase precedente, può verificarsi un deadlock tra le due quando, dopo aver congelato la situazione, si modifica dall'esterno il filtro risorse della precedente. Si evidenzia la situazione, e si elimina il congelamento sulla fase successiva
* errato filtro su risorse specifiche
se per una fase viene impostato il filtro sulle risorse specifiche, e nessuna di esse appartiene alla risorsa principale, esso viene trascurato, e si assume che la fase possa essere eseguita su tutte le risorse specifiche appartenenti alla risorsa principale della fase stessa.
* errata definizione calendario
se il sistema non riesce a calcolare l'istante di fine, a partire da un istante di partenza, un intervallo di tempo e una risorsa, si assume la fine coincidente con l'inizio
* la risorsa specifica forzata o congelata non appartiene alla risorsa generale nel ciclo.
Viene eliminata la forzatura e l'eventuale congelamento.
Questo errore si può verificare se, dall'interno della schedulazione, si modifica la risorsa generale nel ciclo dell'ordine di una fase che è stata forzata durante quella sessione di schedulazione. L'incongruenza non può essere controllata all'atto della modifica della risorsa, in quanto la forzatura è nota soltanto alla schedulazione.
* in un'operazione iniziata non c'è la risorsa specifica.
L'operazione viene declassata a pronta. -

# Nota tecnica
Gli errori vengono registrati nella DS multipla DSERRO.
Il programma che elabora questa DS è S5SMES_DE, che viene lanciato in più punti dello script, con funzioni diverse.
* dopo il caricamento della memoria, quando cioè sono stati rilevati tutti gli errori bloccanti, e prima di iniziare l'effettivo processo di schedulazione, lo si lanciacon funzione 'CEB' (controllo errori bloccanti).
** Se ve ne sono, viene presentata la matrice degli errori, e viene ritornato il messaggio 'FIN', che fa terminare l'esecuzione dello script.
** Se non ve ne sono, viene semplicemente ritornato il messaggio blanks.
* nella presentazione della scheda master, se vi sono errori (tutti non bloccanti, altrimenti non si sarebbe arrivati a questo punto), viene presentato il pulsante "Errori presenti :  controlla" (vi sono errori se il campo £T12, riempimento della DSERRO, è maggiore di zero).
La pressione di questo pulsante fa eseguire il programma con funzione blanks, con effetto di presentare la matrice degli errori.
