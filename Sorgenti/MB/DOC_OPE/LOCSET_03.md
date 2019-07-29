# L'Utilizzo dei setup da parte dello sviluppatore

Vengono qui di seguito descritte le possibilità a disposizione dello sviluppatore per l'utilizzo dei setup.

# Le risalite
Prima di descrivere i punti in cui lo sviluppatore può fissare lo specifico setup da applicare da una particolare funzione applicativa, vengono qui descritti i livelli di risalita attraverso cui vengono determinati i valori del setup. E' importante infatti notare che i valori dei setup non sono sempre indicati in modo esplicito.

* Il default del client. Se non viene specificato nulla il client recupera i suoi valori default ed applica quelli. Il valore di defautl è indicato nell'help del campo.
* Il parent. Fra i campi dei setup è sempre previsto un particolare campo chiamato "Parent" :  in questo campo può essere specificato un oggetto J3, attraverso cui lo standard fornisce alcuni modelli pre-configurati di setup. Quando si usa questo campo (utilizzo che viene consigliato) tutti gli eventuali attributi indicati in modo specifico nel setup e presenti anche nel modello vincono rispetto a quelli previsti dal modello. E' quindi possibile indicare un modello per riprenderne la configurazione e specificare poi in esplicito i soli campi che si ha interesse di indicare in modo specifico.
* Il setup da scheda o da programma. All'ultimo livello di dettaglio di determinazione dei valori di setup stanno i setup definiti a livello di programma.
**





Le sopracitate caratteristiche sono comuni a tutti i componenti grafici, ma esistono poi alcune specificità legate a particolari componenti : 
* Per i setup FRM.REP e SET.EXC è prevista una risalita a pettine per tutti questi livelli :  [...]


Per il componente SET.EXC esiste inoltre un altro livello di risalita, che è per questo il primo preso in considerazione dopo i defautl del client.
[...]


# Dove possono essere fissati i setup



