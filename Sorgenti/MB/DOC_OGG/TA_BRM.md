# BRM - Gruppo risorsa
 :  : DEC T(ST) K(BRM)
## OBIETTIVO
Definisce una caratterizzazione delle risorse più specifica del tipo risorsa.
_9_Esempio :  se il tipo risorsa è la macchina, si possono raggruppare le frese.
## CONTENUTO DEI CAMPI
 :  : FLD T$BRMM **Categoria parametri**
È un elemento della tabella C£E :  definisce la categoria di parametri associabili alle risorse di questo tipo.
 :  : FLD T$BRMN **Contenitore note**
È un elemento della tabella NSC :  definisce il contenitore delle note legate alle risorse di questo gruppo.
 :  : FLD T$BRMT **Tipo operaz. proposta**
È un elemento della tabella BRD :  se codificato, viene proposto all'atto dell'inserimento di una riga di ciclo, relativa ad una risorsa appartenente a questo gruppo. Tale assunzione viene fatta solo se non è stato inserito il tipo operazione proposto a livello di tipo ciclo e se assenti sia il valore di copia sia quello di derivazione.
 :  : FLD T$BRMA **Tipo/parametro appartenenza**
Permette di definire l'oggetto a cui appartiene la risorsa.
Potremo, ad esempio, dire che un certo gruppo di risorse devono essere associate ad un fornitore.
Se non viene specificato si assume un dipendente da intendersi come responsabile.
 :  : FLD T$BRMB **Tipo/parametro appartenenza**
Vedi T$BRMA.
 :  : FLD T$BRMC **Met.calc. capacità**
Programma di calcolo utente
 :  : FLD T$BRMD **Par.calc. capacità**
Parametro
 :  : FLD T$BRME **Tipo coda**
Definisce il tipo di coda per le risorse di questo gruppo. Se lasciato in bianco si assume il valore impostato in BR1.
 :  : FLD T$BRMF **Tipo schedulazione**
Definisce il modo in cui sono trattati questi codici nella schedulazione fine :  se sono a capacità finita (valore di default), oppure a capacità infinita.
 :  : FLD T$BRMG **Tipo sovarapposizone**
Definisce la sovrapposizione applicata a risorse di questo gruppo.
 :  : FLD T$BRMH **Sovrapposizione in ore dall'inizio**
Se presente, e impostata la sovrapposizione in ore, rappresenta il numero di ore passate le quali può iniziare un'operazione su una risorsa di questo gruppo, dopo l'inizio dell'operazione precedente.
Se si imposta solo questo campo (sovrapposizione dall'inizio) e si lascia vuoto il successivo (sovrapposzione dalla fine), con un valore minore o uguale ad un centsimo di ora (0,01) questo valore viene azzerato, ottenendo la sovrapposizione totale (le operazioni iniziano insieme).
 :  : FLD T$BRMI **Sovrapposizione in ore dalla fine**
Se presente, e impostata la sovrapposizione in ore, rappresenta il numero di ore passate le quali può iniziare un'operazione su una risorsa di questo gruppo, dopo la fine dell'operazione precedente.
 :  : FLD T$BRMJ **Ambito di schedulazione**
Se impostato, permette di costituire un raggruppamento 'logico' di tutte le risorse, il cui gruppo ha lo stesso valore di questo campo.
Tale caratterizzazione viene utilizzata nella schedulazione BCD, nel cui lancio è possibile impostare un ambito. In questo caso verranno trattati solo gli impegni la cui risorsa principale appartiene all'ambito selezionato.
Se si riescono ad individuare gruppi di centri tra di loro indipendenti (su cui non vengono lavorati gli stessi articoli), è possibile definire più ambiti, schedulabili in modo indipendente.
 :  : FLD T$BRMK **Tipo batch**
E' un elemento V2_S5_TB.
Definisce le modalità di elaborazione concorrente di impegni diversi sulla stessa risorsa.
E' a disposizione di estensioni specifiche alla schedulazione fine.
 :  : FLD T$BRML **Classe schedulazione**
E' un elemento TA/*CNS5
E' a disposizione dei programmi specifici di schedulazione BCD per implementare strategie particolari sulle risorse
principali con un valore specifico di questo campo (ad esempio attivare il tiro).
 :  : FLD T$BRMO **Classe batch**
E' un elemento TA/*CNS6
Definisce il batch a cui appartengono le risorse di questo gruppo (presse, forni, ecc..)
Il sistema costriurà i batch in modo omogeeneo, raggruppando impegni che hanno risorse principali il cui gruppo
ha lo stesso valore di questo campo.
 :  : FLD T$BRMP **Parallelismo rigido**
Si imposta se su questa risorsa gli impegni che occupano più di una postazione, lo fanno in modo
contemporaneo (iniziano e finiscono nello stesso istante). Può essere impostato soltanto se le
risorse di questo tipo sono multipostazione.
 :  : FLD T$BRMQ **Multipostazione**
Va impostato se le risorse di questo tipo hanno più di una postazione (tra di loro indistinguibili),
ciascuna delle quali può lavorare (in modo asincrono rispetto alle altre) un impegno diverso.
Il numero di postazioni va impostato a livello della singola risorsa.
