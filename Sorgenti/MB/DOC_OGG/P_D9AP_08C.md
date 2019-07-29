# 08   D9AP_08C - Estrattore da IGREPT0F
Estrae dall'archivio ÌGREPT0F, relativo a report da documenuti


_2_Parametri origine

- Sintesi o aggregazione :  1 (gli oggetti origine saranno i 3 della tabella ÌGS dei livelli di sintesi); 2 (gli oggetti origine saranno i primi 9 oggetti della tabella ÌGG dei livelli di aggregazione); 3 (gli oggetti origine saranno i tre della ÌGS + i primi 6 della ÌGG)
- Tabella ÌGA, determina la chiave e il contesto su come leggere il file ÌGREPT
- Tabella ÌGS dei livelli di sintesi :  determina fino a tre oggetti origine per l'estrazione e serve come chave per la scansione.
- Tabella ÌGT del tema :  determina i valori origine da estrarre e associa le intestazioni
- Tabella ÌGG del livello di aggregazione :  determina fino a nove oggetti origine per l'estrazione e serve come chave per la scansione.
- Tabella PER dei periodi :  determina il periodo iniziale su cui si vuole fare l'estrazione
- Tabella PER dei periodi :  determina il periodo finale su cui si vuole fare l'estrazione

_2_Oggetti origine

- Oggetto 1 :  è il periodo. È fisso e caratterizza il periodo di riferimenuto
- Oggetto 2,3,4,5,6,7,8,9,10 :  sono determinati dai parametri origine del livello di sintesi e del livello di aggregazione

_2_Valori origine
Sono determinati dal parametro origine della ÌGT, nella quale sono indicati e caratterizzati i valori che sono relativi agli oggetti e al contesto dell'estrazione


_2_Parametri dinamici
Se compilato il campo nella D9B relativo ai parametri dinamici prima del lancio si potranno compilare dei filtri sugli oggetti origine. Compilando il campo l'estrazione viene fatta tenendo conto solo dei record che hanno quel particolare valore dell'oggetto origine, se non compilati vengono accettati

_2_ATTENZÌONE
Se si sceglie sintesi + aggregazione si rischia di raddoppiare alcuni campi

Estrae dal logico ÌGREPT3L creato ad hoc. Controllare che sia presente, e se manca compilarlo nella libreria dati, il sorgente è presente nella smeup_dev/srcdb
