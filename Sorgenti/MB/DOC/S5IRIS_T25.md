
# Generalità


Esposizione della strategia di ottimizzazione del richiamo della exit di avanzamento IPP del dettaglio (S5SMX_21x) nel programma di selezione dettaglio da schedulare (S5SMES_112E).

Supponiamo di avere, in un loop di selezione, questa situazione

S :  disponibilità standard
X :  avanzamento con exit S5SMX_21x

Primo dettaglio :  viene sempre considerato (XXX potrebbe essere anche zero)
SSSSXXXXXXX

Secondo dettaglio :  di suo è già maggiore e viene trascurato
SSSSSSSSSSSSSSSSSSSS

Terzo dettaglio :  è minore e viene considerato
SSSSSSSXXX                          in questo caso diventa il dettaglio da considerare
SSSSSSSXXXXXXXX            in questo caso viene trascurato

Quarto dettaglio di suo è già maggiore e viene trascurato (paradossalmente XXX per lui potrebbe essere anche zero, ma non farebbe arretrare S)
SSSSSSSSSSSSS

Quinto dettaglio (stessi ragionamenti del terzo)
SSSXXXX                              in questo caso diventa il dettaglio da considerare
SSSSSXXXXXXX                  in questo caso viene trascurato.

Non può verificarsi il caso di un dettaglio trascurato "di suo" che con la exit potrebbe rientrare in gioco :  infatti se è stato trascurato vuol dire che c'era un dettaglio precedente inferiore (exit compresa), e quindi il richiamo della exit è inutile. In questo modo viene richiamata la exit solo per i dettagli potenzialmente selezionabili (se in quel momento della schedulazione lo erano).

Va tenuto presente che questa exit viene lanciata solo per il miglior dettaglio dell'impegno, e quindi può trattare solo vincoli derivanti da oggetti (e da loro attributi) dell'impegno, e non dei suoi dettagli (ad esempio l'articolo, l'ordine, la risorsa principale, ma non la risorsa specifica).

Queste considerazioni valgono anche per l'avanzamento dell'IPP in presenza di RSV, che viene eseguita prima di questa exit, ma che sostanzialmente esegue la stessa funzione di avanzamento (ovviamente con criteri diversi), e ne condivide l'impossibilità di trattare vincoli dipendenti dal dettaglio.





