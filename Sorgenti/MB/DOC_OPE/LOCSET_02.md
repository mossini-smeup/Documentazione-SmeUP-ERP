# Identificazione delle strutture di setup

I setup esistono in funzione di un componente grafico ed ad esso si associano. L'elenco di tutte le tipologie di setup è definito attraverso l'oggetto V2LOMOD.

 :  : DEC T(OG) P() K(V2LOMOD)
 :  : DEC T(V2) P(LOMOD) K([V2.LOMOD.A.9999999])

# Il contenitore delle definizioni dei setup

La sopracitata classe rappresenta però solo un modo per identicare i setup all'interno della classe di definizione :  infatti i setup appartengono all'insieme più largo delle configurazioni di scheda.
Tali configurazioni sono conservate all'interno dello script SCP_CFG/EDT_SCH. Quando è quindi necessario modificare la struttura di definizione di un setup è necessario intervenire su questo script.
Partendo da un istanza di V2LOMOD per identintificare la corrispondente definizione nello script EDT_SCH è sufficiente aggiungere al codice V2LOMOD un "G." es. "SET.MAT" corrisponde a "G.SET.MAT".

 :  : DEC T(OG) P() K(MBSCP_SCH)

E' inoltre di interesse rilevare che ad ogni setup corrisponde inoltre la definizione di un tipo tracciato RE attraverso cui può essere analizzata in modo preciso la struttura del setup.
(es. l'oggetto corrisponde al tipo tracciato della setup di matrice è RES-EDT_SCH/G.SET.MAT o J5EDT_SCH/G.SET.MAT).
Questa informazione è di particolare interesse perchè da tale struttura vengono eriditate varie caratteristiche, fra cui la modalità di documentazione dei campi del setup.

 :  : DEC T(OG) P() K(RE)

