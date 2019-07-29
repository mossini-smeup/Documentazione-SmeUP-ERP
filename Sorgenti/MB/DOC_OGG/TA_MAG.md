# MAG - Magazzino
## OBIETTIVO
Raggruppare le informazioni specifiche di un magazzino.
Ricordiamo che in SME_UP, per magazzino si intende un 'plant', vale a dire una sede dell'azienda identificata da un numero civico.
All'interno del magazzino, l'ulteriore suddivisione delle giacenze viene descritta tramite le singole aree.
Per materiale all'interno del magazzino, si intende il materiale di competenza del magazzino, quindi anche il materiale presso terzi. È una caratterizzazione dell'area il fatto che essa sia localizzata fisicamente all'interno o all'esterno del magazzino.
Nella tabella generale B£1 si definisce se l'applicazione è monomagazzino :  anche in questo caso è necessario codificare il magazzino in questa tabella, per definirene la caratteristiche.
## CONTENUTO DEI CAMPI
 :  : FLD T$MAGF __Magazzino fiscale__
È un elemento della tabella MAF :  definisce il magazzino fiscale a cui appartiene il magazzino. In questo modo è possibile raggruppare in più magazzini fiscali i singoli magazzini fisici. Ciò può essere utile in caso di valorizzazione fiscale a livello di divisione, oppure di più aziende presenti nello stesso sistema informativo.
 :  : FLD T$MAG1 __Area/Prefisso aree 1/2/3__
Sono elementi della tabella GMR :  si possono impostare anche radici dell'area (il primo carattere impostato ed il secondo lasciati in bianco).
Vengono utilizzati nella costruzione del modello dinamico del magazzino : 
-    se si impostano delle aree valide, o delle radici di aree, si collegano al magazzino solo le aree che soddisfano le impostazioni.
-    se invece sono tutte e tre in bianco, si collegano al magazzino tutte le aree.
 :  : FLD T$MAG2.T$MAG1 __Area/Prefisso aree 1/2/3__
 :  : FLD T$MAG3.T$MAG1 __Area/Prefisso aree 1/2/3__
 :  : FLD T$UESG __Ultimo esercizio chiuso__
È un elemento della tabella PER :  indica l'ultimo periodo di chiusura del magazzino fiscale. Viene aggiornato automaticamente dalla funzione di chiusura mensile.
 :  : FLD T$MAG4 __Tipo / Codice risorsa calendario__
Identificano il calendario di apertura del magazzino :  vengono usati, ad esempio, nella determinazione delle date di inizio/fine pianificazione a partire dai tempi di approvvigionamento, nel caso si sia impostato, nella tabella M51, che debbano essere calcolate secondo i giorni lavorativi.
 :  : FLD T$MAG5.T$MAG4 __Tipo / Codice risorsa calendario__
 :  : FLD T$MAGA __Tipo / Codice Ente__
Definiscono l'ente interno che corrisponde a questo plant.
**NB** :  I due campi devono essere entrambi compilati.
In pianificazione multiplant completa, quando il sistema pianifica un ordine di trasferimento, esso verrà assegnato a questo ente.
