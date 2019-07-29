# NUMERI DELLA VISTA x RISORSE DELL'ORDINE DI PRODUZIONE
## OBIETTIVO
Contiene i numeri legati all'avanzamento di un ordine di produzione
Prerequisiti  :  impegni su S5IRIS e, per alcuni campi, la schdulazione a capacità infinita in avanti e finita
Viene aggiornato alla rifasatura degli impegni risorse
Dato che alcuni campi sono sensibili al passare del tempo, è opportuno lanciare la rifasatura totale ogni notte.
Alcuni campi (relativi alla schedulazione a capacità finita) sono aggiornati al momento della memorizzazione della
schedulazione stessa.
Vengono calcolati se impostato il flag in tabella S5B.
Il contesto (TAD5S) è "OR"
Il tema (TAD5O sottosettore "OR") è "£I1"
## CONTENUTO DEI CAMPI
 :  : FLD 02 Numero di operazioni totali
 :  : FLD 03 Numero di operazioni eseguite
 :  : FLD 04 Numero di operazioni in corso
 :  : FLD 05 Numero di operazioni non iniziate
 :  : FLD 12 Ore di carico totali
 :  : FLD 13 Ore di carico eseguite
 :  : FLD 14 Ore di carico residue di operazioni in corso
 :  : FLD 15 Ore di carico residue di operazioni non iniziate
Si definisce least remaining work
 :  : FLD 16 Ore di carico residue totali
 :  : FLD 22 Data di calcolo
 :  : FLD 23 Data fine richiesta
 :  : FLD 24 Data fine schedulata a capacità infinita in avanti
 :  : FLD 25 Data fine schedulata a capacità finita

 :  : FLD 31 Indici
Le differenze sono in giorni lavorativi del calendario impostato in tabella MAG.

 :  : FLD 32 Data fine richiesta - Data calcolo
= (Indice 23 - Indice 22). Se negativo indica un ordine scaduto

 :  : FLD 33 Slack time
 = (Indice 23 - Indice 24)

Se è < 0 (ordine in ritardo) vi sono due casi : 

Se ordine scaduto (Indice 32 negativo) è scomponibile nei seguenti valori (entrambi negativi o nulli)
- giorni di scaduto (data richiesta - oggi)
- giorni di lavoro da eseguire (oggi - data fine schedulata a capacità infinita ). Quest'ultimo valore non può essere
  mai inferiore ad oggi, in quanto la schedulazione a capacità infinita in avanti parte dalla data più alta tra l'inizio
  richiesto e oggi.
Sull'asse dei tempi, si ha quindi : 
    (1) ---------- (2) ---------- (3)
    >>>>>>>>>>> slack >>>>>>>>>>>>>>>
dove (1) è la fine richiesta
     (2) è oggi
     (3) è la data fine schedulata
L'andamento  delle frecce (>> o <<) è dalla data di arrivo a quella di partenza

Se ordine non scaduto (Indice 32 positivo) si ha la seguente situazione, sull'asse dei tempi
    (2) ---------- (3) ---------- (1)
                   >>>>> slack >>>>>>

Se è > 0 l'ordine è in anticipo.
Sull'asse dei tempi, si ha quindi : 
    (2) ---------- (1) ---------- (2)
                   <<<<< slack <<<<<<

Una caratteristica di questo indice di priortità è che non è detto che gli ordini scaduti vengano prima degli altri :  un
ordine non scaduto ma drammaticamente in ritardo può essere più urgente di un ordine scaduto ma con poco lavoro rimanente
Ad esempio : 
Ordine scaduto
    (1) ------ (2) - (3)
    >>>>>> slack A >>>>>
Ordine non scaduto
               (2) ---- (3) ----------------- (1)
                        >>>>> slack B >>>>>>>>>>>>
Come si vede :  slack B > slack A

 :  : FLD 34 Data fine schedulata a capacità finita - Data calcolo
= (Indice 25 - Indice 22).

 :  : FLD 35 Data fine schedulata a capacità finita - Data fine schedulata a capacità infinita.
= (Indice 25 - Indice 24).

 :  : FLD 36 Slack time per operazione
= (Indice 24 / Indice 05)

 :  : FLD 37 Critical ratio
Se l'Indice 32 è negativo coincide col lo slack time (indice 33)
Se invece l'Indice 32 è positivo è = (Indice 33 / Indice 32)
Assume i seguenti valori
Se < 0 ordine scaduto
Se < 1 ordine in ritardo
Se = 1 ordine puntuale
Se > 1 ordine in anticipo
Questo indice, a differenza dello slack, mette in prima posizione gli ordini scaduti.
Esso non può mai valere zero :  se scaduto
