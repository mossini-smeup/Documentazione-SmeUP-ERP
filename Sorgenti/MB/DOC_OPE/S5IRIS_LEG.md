# Introduzione
Normalmente la prima fase non schedulata di un ordine è considerata 'pronta', e quindi entra subito in competizione nella scelta dell'operazione da schedulare (il suo stato, nell'impegno risorse della memoria BCD è '2').

# Descrizione operativa
La funzione di appuntamenti statici permette di rendere 'pronta' la prima fase di un ordine soltanto quando sono stati completati altri ordini (quando cioè ne è stata schedulata l'ultima operazione).
Il legame tra gli ordini è dichiarato 'statico', in quanto è passato alla schedulazione all'esterno, prima della sua esecuzione.
Il legame tra ordini è tanti a tanti, vale a dire che un ordine puè essere condizionato da più di un ordine, e a sua volta ne può condizionare più di uno.

La fase dell'ordine 'assieme' viene resa non pronta se è la prima in assoluto e non è iniziata. Viene posta in stato '4' (nella memoria BCD) se soddisfa ad entrambe queste condizioni, ed ha un un vincolo di inizio dalla fine di altri ordini. Per la schdulazione, questo stato è equivalente al '3' :  viene differenziato per evidenziare il tipo di 'non pronto'.

Tra livelli diversi
* NON viene calcolata la sovrapposizione
* NON viene applicato l'accostamento (sa standard sia utente)
* Viene applicata all'ultima fase dell'ordine del livello inferiore l'attesa successiva.
Questo perché la fine (data e ora) dell'ordine (nell'elemento di sintesi) è la fine dell'ultima fase a cui si aggiunge l'attesa successiva, ed è questo istante che  costituisce il vincolo per l'ordine assieme.

Si trattano due livelli di ordini 'passanti', vale a dire composti solo di operazioni a capacità infinita.
Ad esempio, se si hanno questi legami tra ordini
     O1 -->  O2 --> O3 --> O4
O2 ed O3 sono composti solo da fasi a capacità infinita :  quando finisce O1 si rende pronto O2.
Le sue fasi a capacità infinita vengono schedulate subito, in sere :  dato che lo sono tutte, l'ordine viene completato e si analizzano i suoi ordini superiori, (in questo caso O3) che a sua volta viene completato e rende pronto l'ordine O4.

# Nota tecnica
Per attivare questa funzione si deve realizzare un programma che comunichi alla schedulazione i legami tra ordini. Riferirsi al prototipo S5SMX_09x per i dettagli implementativi. Si deve quindi impostare, nello script dei parametri, il suffisso 'x' di questo programma.

Il limite di due livell di ordini passanti, è dovuto al fatto che sono state realizzate tre repliche di S5SMES_07 e  S5SMES_13.
I livelli passanti sono dati dal numero di repliche -1. Se si volessero aumentare, basta modificare S5SMES_07 che esegue il lancio del livello opportuno, oltre ad aumentare le repliche.


 :  : REM
*** QUI METTERE UNA FIGURA CON I LEGAMI TRA LE DS DI MEMORIA ****
 :  : REM.END
