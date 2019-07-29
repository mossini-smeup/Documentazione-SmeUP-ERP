# D9C - Modelli di gerarchia
 :  : DEC T(ST) K(D9C)
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la descrizione dell'elemento della gerarchia per Cube_up. È meglio evitare caratteri accentati e apostrofi.
 :  : FLD T$D9CA **Tipo oggetto**
Contiene il tipo e parametro oggetto dell'elemento della gerarchia.
 :  : FLD T$D9CB **Parametro oggetto**
Contiene il parametro oggetto dell'elemento della gerarchia.
 :  : FLD T$D9CC **Attributo**
Da non compilare per il livello base di aggregazione. Per i livelli inferiori scegliere se puntare ad un attributo dell'oggetto del livello precedente o puntare all'oggetto stesso. Nel primo caso selezionare l'attributo da importare.
Una volta compilato questo campo, compila in automatico il resto della tabella, se precedentemente bianco.
Mettendo un '+' su questo campo si può creare un'aggregazione su un campo piatto aggiuntivo (vedi D9B) specifico di un'estrazione.
 :  : FLD T$D9CD **Inclusione/Esclusione**
In sviluppo. Attualmente non gestiti.
 :  : FLD T$D9CE **Codice lista**
In sviluppo. Attualmente non gestiti.
 :  : FLD T$D9CF **Struttura da registrare**
In base alla scelta da tabella, si decide come portare l'elemento nel Databeacon :  si può portare solo il codice, solo la descrizione, tutti e due scegliendo nell'ordine, oppure non portare l'elemento stesso ma solo la gerarchia che sta sotto di esso.
 :  : FLD T$D9CG **Tipo/par.da pgm ?**
Se impostato, il tipo e parametro dell'oggetto al quale applicare l'OAV non vengono presi dalla tabella, ma vengono utilizzati quelli passati dal programma di estrazione dati o dall'OAV precedente nella gerarchia.
Può essere utile nel caso in cui il tipo oggetto restituito sia variabile.
