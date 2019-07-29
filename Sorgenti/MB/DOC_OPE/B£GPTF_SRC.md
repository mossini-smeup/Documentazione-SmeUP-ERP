# Obiettivo

Facilitare l'allineamento dei sorgenti di una PTF, evidenziando le criticità rispetto alla situazione dell'ambiente in cui si opera.

# Struttura

La scheda è divisa in due sezioni : 
* Nella prima è riportata una matrice, con l'elenco dei sorgenti della libreria della PTF, ordinati in funzione della loro criticità definita in ordine : 
** % Utilizzo del pgm nell'ambiente di lavoro (in quanto al di là delle specifiche differenti sul sorgente la % di utilizzo evidenzia la criticità del programma che si andrà a modificare)
** Il totale del n° di differenze riscontrate fra i due sorgenti
** Il n° di righe cancellate o aggiunte nei due sorgenti (rispetto al precedente vengono contate solo le specifiche in più o in meno e non quelle solo modificate)
* Nella seconda sono riportate le azioni che si riferiscono al sorgente selezionato nella prima selezione

La prima sezione si basa su un file di report prodotto dal costruttore LOA15. Per poter far si che il contenuto del report sia riferito alla libreria di PTF interessata è necessario creare/ricreare il report dopo aver indicato nella configurazione tale libreria.

_1_NOTA BENE :  alla data odierna in un ambiente può esistere un solo file di report, per cui più utenti non possono analizzare differenti analisi.

# Colonne della prima sezione

* Libreria PTF :  Nome della libreria della PTF in cui si trova il file del membro
* File Origine PTF :  Nome del file della PTF in cui si trova il membro
* Membro Origine PTF :  Nome del membro della PTF
* Tipo Membro Origine PTF :  Tipo di sorgente del membro della PTF
* Libreria Origine Ambiente :  Nome della libreria dell'ambiente di lavoro in cui si trova il corrispondente al membro della PTF
* File Origine Ambiente :  Nome del file dell'ambiente di lavoro in cui si trova il corrispondente al membro della PTF
* Membro Origine Ambiente :  Nome del membro corrispondente al membro della PTF nell'ambiente di lavoro
* Libreria Oggetto Ambiente :  Libreria dell'ambiente di lavoro in cui si trova l'oggetto del sorgente corrispondente al membro della PTF
* % Utilizzo Ambiente :  % di utilizzo rapportata a giorni e data di creazione dell'oggetto corrispondente al sorgente della PTF nell'ambiente di lavoro
* gg Utilizzo Ambiente :  gg di utilizzo dell'oggetto
* Totale Differenze :  n° totale delle specifiche differenti riscontrate fra i membri della PTF e quello dell'ambiente reale
* Delta Righe :  rispetto al precedente vengono contate solo le specifiche in più o in meno e non quelle solo modificate
* Righe Aggiunte nella PTF :  n° di righe presente solo nel sorgente della PTF
* Righe Cancellate dall'Ambiente :  n° di righe presenti solo nel sorgente dell'ambiente di lavoro (e non più nella PTF)
* Righe Modificate :  n° di righe corrispondenti ma modificate fra i due sorgenti
* Righe PTF :  n° di righe totali del sorgente della PTF
* Righe Ambiente :  n° di righe totali del sorgente dell'ambiente di lavoro

# Azioni della seconda sezione

* Esegui comparazione :  lancia una scheda che permette di analizzare le differenze fra i due sorgenti
* Copia Sorgente Ptf in ambiente SV : emette finestra per confermare/modificare i valori
* Compila Sorgente ambiente SV : emette finestra per confermare/modificare i parametri di compilazione

# Tasti funzione

* F06 Permette di lanciare la rigenerazione del file di report
* F16 Pulisce il file di report
* F18 Configura i parametri di generazione del file di report

T01 Lancio comendi presenti nella PTF
a) Se il comando è preceduto da un ? staccato di un blank :  esce la prompt completa del comando (es. ? SNDMSG)
b) Se nel comando viene inserito ?? per ciascun parametro si ottiene il prompt di quel parametro (es.SNDMSG ??MSG(*N) TOUSR(*SYSOPR) )
c) Se nel comando viene inserito ?* per ciascun parametro si ottiene il prompt non modificabile di quel  parametro (es. SNDMSG ??MSG(*N) ?*TOUSR(*SYSOPR) )

# Codifica delle PTF
I membri sono strutturati nel seguente modo : 
 * Nome del membro :  Applicazione (Tabella TAB£A) di appartenenza + anno di rilascio della ptf (solo ultima cifra) + mese di rilascio + giorno di rilascio + lettera progressiva delle ptf lasciate nello stesso giorno
 * Tipo membro :  viene indicata la release corrente al momento del rilascio

Le sopraddette regole hanno un'eccezione per quelle PTF che hanno una valenza generale e persistente nel tempo. In questo caso il nome del membro inizia per XX99999 + lettera progressiva ed il tipo membro riporta V999.

I pgm modificati/creati in funzione della ptf dovrebbero riportare nelle specifiche di intervento non la data ma il nome del membro della ptf di riferimento.

Se la PTF deve richiamare un programma di fasatura di un archivio, e questo programma viene usato solo in occasione dell'applicazione della PTF allora il nome di questo programma deve essere composto in questo modo :  _2_xxUTXnn dove xx=modulo Sme.up e nn=progressivo
Ad esempio, se la PTF lancia un programma che valorizza un campo del C5RATE0F, questo pgm si chiamerà C5UTXnn (es. C5UTX01, C5UTX02 ...). Questo pgm verrà messo in SMEDEV/C5SRC.
