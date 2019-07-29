# B£I - Deviazione tabella
 :  : DEC T(ST) K(B£V)
## OBIETTIVO
Gestire le tabelle definite in applicazioni diverse come se fossero normali tabelle SMEUP.
Ciò risulta particolarmente rilevante nei casi di tabelle che sono prerequisito al funzionamento di altre applicazioni, come ad esempio nel caso del pagamento per la contabilità.
Il risultato è del tutto simile a quello che si ottiene nella definizione delle interfacce verso articoli o clienti, ecc.
## NOTA IMPORTANTE
La deviazione è attiva se e solo se entrambi i FLAG di attivazione (globale e specifica) sono attivi.
La tabella può essere preparata e consegnata al cliente, completa di tutte le tabelle che potenzialmente possono essere deviate.
L'utente attiva quelle di suo interesse.
## UTILIZZO
_9_Esempi
1.   Gestire i pagamenti nelle tabelle GOLDEN LAKE
2.   Gestire in modo trasparente l'anagrafico agenti delle ACG come se fosse la tabella AGE di SMEUP
3.   Definire un nuovo anagrafico come se fosse una normale tabella SMEUP. In questo caso si definisce una nuova tabella con i campi di interesse e si costruisce l'interfaccia.
## TIPI DI INTERFACCIA
**Mediante file tabelle**
L'interfaccia è gestita da un programma di tipo standard.
Se si tratta di una tabella, il programma si chiama B£ITxx dove xx è il nome dell'ambiente. Se si tratta di un file, si indica in
tabella il nome del programma stesso.
**Ambienti attivi**
SE   Tabelle Seltering/Thera
AC   Tabelle ACG
A2   Tabelle ACG Versione 2
SG   San Giorgio S.T.
**Mediante programma specifico**
## NOTE TECNICHE SUI METODI DI RICHIAMO
**Interfaccia estesa**
L'interfaccia estesa viene attivata quando il programma vuole leggere i dati presenti nella tabella e non la sola descrizione. Tecnicamente ciò si ottiene mediante l'utilizzo della funzione £RITES.
**Dati dell'interfaccia**
Normalmente l'interfaccia fornisce la funzione di selezione e restituisce la decodifica.
Per alcune tabelle può essere attivata una funzione di interfaccia estesa. In questo caso il programma restituisce tutti e solo i dati previsti dalla normale tabella SMEUP come se fossero gestiti nella stessa.
## CONTENUTO DEI CAMPI
 :  : FLD T$FITA **Tipo collegamento**
F    = archivio
Dati collegati
.    Programmi
.    Parametro

T    = tabella
Dati collegati
.    Ambiente
.    Tabella

O    = oggetto
Dati collegati
.    Tipo oggetto
.    Parametro
 :  : FLD T$AMBA **Tipo oggetto**
Qualsiasi ambiente definito nella tabella *CNAA come
.    A2 = ACG versione 2
.    SE = Seltering
.    .. = Ecc.
Qualsiasi tipo definito nella tabella *CNTT come
.    AR = Articolo
.    RI = Risorsa
.    .. = Ecc.
 :  : FLD T$DSET **Tabella/Parametro**
Nome della tabella nell'ambiente d'arrivo/Parametro tipico dell'oggetto
 :  : FLD T$DPGM **Programmi**
-    Manutenzione
-    Interrogazione
-    Ricerca
Specifica il programma che si occupa della gestione dell'archivio richiesto.
Esempi di casi già predisposti : 
Ambiente                      Programma
A2        ACG Versione 2      B£ITA2ANR
 :  : FLD T$DPGI.T$DPGM **Programmi**
 :  : FLD T$DPGR.T$DPGM **Programmi**
 :  : FLD T$DPAM **Parametri**
Specifico del programma.
_9_Esempi di casi già predisposti : 
Parametro
BANCA     Anagrafico banche
AGENTE    Anagrafico agenti
LISTINO   Codice listino
MAGAZZINO Codice magazzino
DEPOSITO  Codice deposito
RAGMAG    Raggruppamento magazzini
 :  : FLD T$DPAI.T$DPAM **Parametri**
 :  : FLD T$DPAR.T$DPAM **Parametri**
 :  : FLD T$B£IA **Attivazione globale**
Definisce la tabella come deviabile. Tecnicamente si modifica la definizione della tabella (TABDS). Vengono inseriti automaticamente i **/*1. In tale modo la tabella sarà trattata dai programmi come "DEVIABILE".
La deviazione con nuovo gruppo di attivazione può rendersi necessaria per risolvere problemi di ricorsione qualora l'oggetto deviato chiami la gestione tabelle.
Il diverso completamento dell'attivazione globale e specifica è rilevante solo in presenza di ambienti con definizione unica e contenuti diversi per le tabelle.
 :  : FLD T$B£IB **Attivazione specifica**
Definisce che per questa tabella devono essere eseguiti i passi di deviazione mediante programma o tabella, come sopra descritti.
