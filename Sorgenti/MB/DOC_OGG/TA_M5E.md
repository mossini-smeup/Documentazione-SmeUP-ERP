# M5E - Fonti esistenti di impegno/disponibilità
## OBIETTIVO
Definisce le caratteristiche delle fonti esistenti (giacenze, scorte) nelle analisi di pianificazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Codice__
Indica il codice della fonte.
 :  : FLD T$DESC __Descrizione__
 :  : FLD T$M5EA __Origine Fonte__
È un elemento V2/M5OFP che definisce la natura della fonte.
 :  : FLD T$M5EB __Parametro 1/2/3/4 Fonte__

I parametri 1/2/3/4 della fonte assumono un significato diverso in funzione dell'origine fonte : 

- [&-x2a; M5E - AP - Altra applicazione](Sorgenti/MB/DOC_OGG/TA_M5E_AP)
- [&-x2a; M5E - GC - Giacenza](Sorgenti/MB/DOC_OGG/TA_M5E_GC)
- [&-x2a; M5E - GF - Giacenza alla fase](Sorgenti/MB/DOC_OGG/TA_M5E_GF)
- [&-x2a; M5E - MP - MPS](Sorgenti/MB/DOC_OGG/TA_M5E_MP)
- [&-x2a; M5E - PM - Parametri](Sorgenti/MB/DOC_OGG/TA_M5E_PM)
- [&-x2a; M5E - PR - Punto di riordino](Sorgenti/MB/DOC_OGG/TA_M5E_PR)
- [&-x2a; M5E - QE - Quantità eccedente](Sorgenti/MB/DOC_OGG/TA_M5E_QE)
- [&-x2a; M5E - SC - Scorta minima](Sorgenti/MB/DOC_OGG/TA_M5E_SC)
- [&-x2a; M5E - UT - Fonte Utente](Sorgenti/MB/DOC_OGG/TA_M5E_UT)
 :  : FLD T$M5EC __Azione fonte (+/-/N)__
Definisce se il contributo della fonte è positivo, negativo oppure neutro per la disponibilità.
Una fonte neutra viene riportata in un campo separato dell'analisi disponibilità :  un esempio di utilizzo è una giacenza in collaudo, che non è disponibile ma che si vuole comunque visualizzare.
 :  : FLD T$M5EJ __Segno fonte neutra__
Significatico solo se Azione Fonte = N.
Definisce il segno della quantità neutra e consente di suddividere la stessa in Entrate/Uscita. Se impostato al valore '-' la quantità neutra verrà presentata con il segno invertito. L'impostazione di questo campo NON condizionerà in alcun modo la disponibilità dell'articolo, in quanto la quantità neutra NON verrà considerata in nessun modo nel calcolo della quantità disponibile.
 :  : FLD T$M5ED __Ordinamento fonte__
È un carattere che stabilisce, nell'ambito delle fonti esistenti, la posizione in cui verrà esposta questa fonte.
**Attenzione !!!**
Se più fonti hanno lo stesso carattere di ordinamento, vengono sommate in una sola riga di disponibilità, con la descrizione della prima fonte, in ordine di codice. In questo modo si possono raggruppare in modo libero le varie aree/tipi giacenze.
 :  : FLD T$M5EE.T$M5EB
 :  : FLD T$M5EF __Presenta anche se 0__
Se impostato, mostra la riga della fonte anche se con quantità zero. Nel caso di fonti sommate, vale il comportamento della prima, in ordine di codice.
 :  : FLD T$M5EG __Descrizione ridotta__
È la descrizione che viene usata nei casi di rappresentazioni compatte (ad esempio nelle visualizzazioni e stampe JMRP).
 :  : FLD T$M5EH __Classe fonte JMRP__
È un elemento V2/CFIM, che serve a JMRP per riconoscere le fonti di questa classe.
 :  : FLD T$M5EI __Suffisso programma aggiustamento__
Se impostato, è il suffisso x del programma M5M5D0G_x, che viene lanciato all'atto della scrittura delle fonti di questo tipo, per modificarne il comportamento.
 :  : FLD T$M5EL __Riclassifica__
È un elemento della tabella 'M5*RF' :  viene usato nell'analisi pianificazione e disponibilità riepilogate. Se impostato, le fonti verranno raggruppate per questo campo. Se non impostato verrà assunta come riclassifica l'azione fonte, in questa stessa tabella.
 :  : FLD T$M5EM __Ordinamento riclassifica__
È usato nelle analisi pianificazione e disponibilità riepilogate :  all'interno della riclassifica impostata nel campo precedente, le fonti verranno presentate ordinate per questo campo.
Se non impostato, verrà assunto come ordinamento il codice della fonte.
 :  : FLD T$M5EN.T$M5EB
 :  : FLD T$M5EO.T$M5EB
 :  : FLD T$M5EK __Filtro plant di competenza__
Questo campo è utilizzato solo in ambienti multiplant.
Se vale 1, questa fonte verrà ritornata solo in scansione del plant di competenza.
Se vale 2, verrà invece ritornata in scansione degli altri plant.
Se la si lascia vuota, verrà sempre ritornata.
 :  : FLD T$M5EU __Origine se fonte utente__
È un elemento V2/M5OFF che, se impostato, viene ritornato nel campo "origine fonte", nel caso di fonte utente.
Può essere utile se la fonte utente è in realtà una fonte "standard" ma elaborata con programmi utente (ad esempio la giacenza sia dell'articolo in esame sia dei suoi alternativi), nel qual caso i camp della fonte sono di giaceza, e quindi, impostando l'origine fonte GC si ottengono i vantaggi di caratterizzazione della fonte.
E' cura di chi implementa il programma di ritorno della fonte utente, garantire la congruenza dei campi di caratterizzazione, con il valore inserito in questo campo.

