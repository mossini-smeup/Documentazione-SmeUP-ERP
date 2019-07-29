Talvolta vi è la necessità che vi siano più enti che eseguano separatamente la schedulazione, su risorse diverse.
Ciò è realizzabile solo se è possibile dividere le risorse dell'azienda in più sottoinsiemi, e tutte le operazioni del ciclo di ogni articolo si eseguono in un solo sottoinsieme.
Definiamo questo sottoinsieme 'ambito' (elemento della tabella S5C), e lo attribuiamo al gruppo risorse (tabella BRM) e quindi indirettamente alla risorsa principale).
Questa informazione viene assegnata ad ogni impegno risorse, e quindi può costituire un filtro per l'insieme degli impegni che vengono sottoposti alla schedulazione.
In tal modo si ottiene l'effetto di suddividere l'azienda in più sottoaziende parallele, che non interagiscono tra di loro.

Se vi sono risorse a capacità infinita comuni a più ambiti, occorre prestare particolare attenzione all'attribuzione dell'ambito stesso. Da un punto di vista della datazione, ciò non costituisce un problema, essendo tali risorse schedulate in serie alle operazioni a capacità finita.
Si devono estrarre però soltanto le operazioni appartenenti all'ambito che si sta schedulando.
Un modo per risolvere questo problema è attribuire l'ambito in base ad una caratteristica (oav) dell'oggetto della schedulazione. Si imposta il codice di tale oav nella tabella dello scenario.
Ad esempio, se gli ordini di produzione che operano nei vari ambiti si distingono per il primo carattere del codice dell'ordine, si definisce un oav di tipo U che ritorna questo carattere, utilizzando, ad esempio, il programma B£OA_SST, e lo si memorizza nello scenario.


 :  : REM
SV - Autorizzazione generale e agli ambiti
SV - Contemporaneità tra accessi
 :  : REM.END
