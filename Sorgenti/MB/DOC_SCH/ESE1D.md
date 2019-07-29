# Esempi di layout dinamico
Cliccando nella sezione 1A della scheda ESE1D si chiama, nella sezione 1B, una sottoscheda (per
 comodità definita in questo stesso membro) passandogli nei parametri il valore dell'attributo della
 riga cliccata.
Così facendo la variabile dinamica [£OAVOV] della scheda ESE1D diventa una variabile statica nella
 scheda ESE1D-sottoscheda GR1 (perchè è passata nei parametri) e può essere usata per condizionare
 la struttura della sottoscheda.
Notare come avviene il passaggio :  la variabile viene passata nei parametri della chiamata
 (ad es. P(PAR(A01)) ) e referenziata nella sottoscheda come &PA.PAR, dove PAR è l'espressione che
 precede le parentesi con il valore.
