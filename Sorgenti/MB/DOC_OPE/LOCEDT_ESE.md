# Esempi

IMG P([IMG : J1;FUN;F(SPC;B£SER_43B;TST.IMG) 1(J1;GRA;SPC) 2(TA;V§R;) P(Typ(FRE))]) R(60)
**In attesa di escluderli solo per latex tolgo  :   :  perchè bloccano la generazione dei manuali**
Ora alcune righe con degli spazi davanti : 
 * riga 1
 * riga 2

Questa parte è precedente al_4_primo titoloe non viene visualizzata se la modalità di richiamo è**HELP** di scheda.
_4_XX

# Alcuni esempi di righe formattate
 :  : R01 Riga di tipo R01
 :  : R02 Riga di tipo R02
 :  : R03 Riga di tipo R03

# Esempi di PARAGRAFI di solo testo
 :  : PAR F(01) T(Paragrafo di tipo 1)
I cipressi che a Bolgheri alti e schietti van da San Guido in duplice filar, quasi in corsa giganti giovinetti mi balzarono incontro e mi guardar...
Parvemi riveder nonna Lucia :  la signora Lucia, da la cui bocca, tra l'ondeggiar de i candidi capelli, la favella toscana, ch' è si sciocca

 :  : PAR T(Paragrafo di tipo 1)
I cipressi che a Bolgheri alti e schietti van da San Guido in duplice filar, quasi in corsa giganti giovinetti mi balzarono incontro e mi guardar...
Parvemi riveder nonna Lucia :  la signora Lucia, da la cui bocca, tra l'ondeggiar de i candidi capelli, la favella toscana, ch' è si sciocca

> T(Paragrafo di tipo 2)
I cipressi che a Bolgheri alti e schietti van da San Guido in duplice filar, quasi in corsa giganti giovinetti mi balzarono incontro e mi guardar...
Parvemi riveder nonna Lucia :  la signora Lucia, da la cui bocca, tra l'ondeggiar de i candidi capelli, la favella toscana, ch'è si sciocca

> T(Paragrafo con allineamento)
Testo                    con                        font               non                 proporzionale
Dovrebbe                 risultare                  allineato          al                  precedente

Altro testo non formattato inserito fra due paragrafi come esempio
 :  : PAR F(03)  T(Paragrafo di tipo 3)
I cipressi         che       a        Bolgheri              alti e schietti van          da San Guido in duplice                     filar, quasi in corsa giganti giovinetti mi balzarono incontro e mi guardar...
Parvemi          riveder nonna Lucia :  la signora Lucia, da la cui bocca, tra l'ondeggiar de i candidi capelli, la favella toscana, ch'è si sciocca

 :  : PAR F(04) T(Paragrafo di tipo 4)
I cipressi                            che a Bolgheri alti e schietti van da San Guido in duplice filar, quasi in corsa giganti giovinetti mi balzarono incontro e mi guardar...
Parvemi riveder nonna Lucia :  la signora Lucia, da la cui bocca, tra l'ondeggiar de i candidi capelli, la favella toscana, ch'è si sciocca

questo è minore <, questo è l'altro <

# Esempi di PARAGRAFI di liste
Lista con cambio formato : 
 * Lista con _5_cambio formato interno

Tipo 1 - numeri : 
 - Riga 1.n
 - Riga 2.n
 - Riga 3.n
 -- Riga 3.1.n
 --- Riga 3.1.1.n
 --- Riga 3.1.2.n
 -- Riga 3.2.n
 - Riga 4.n

Tipo 1 - numeri - CONT : 
 - Riga 1.n
 - Riga 2.n
 - Riga 3.n
 -- Riga 3.1.n
 --- Riga 3.1.1.n
 --- Riga 3.1.2.n
 -- Riga 3.2.n
 - Riga 4.n

Tipo 2 - lettere : 
 - Riga 2.l
 -- Riga 2.l
 --- Riga 2.l
 - Riga 2.l - Riga ancora
 - Riga 2.l
 - Riga 2.l

Tipo 2 - lettere - CONT : 
 - Riga 2.l
 -- Riga 2.l
 --- Riga 2.l
 - Riga 2.l - Riga ancora
 - Riga 2.l
 - Riga 2.l

Tipo 3 - puntato : 
 * Riga 3.p
 * Riga 3.p
 ** Nested 1
 ** Nested 2
 * Riga 3.p
 * Riga 3.p

# Esempi di titoli
# - Titolo di livello 1  1
## - Titolo di livello 2  1.A
 :  : NPG
### - Titolo di livello 3  1.A.1
### - Titolo di livello 3  1.A.2
## - Titolo di livello 2  1.B
### - Titolo di livello 3  1.B.1

# Link ad altri file di documentazione
- [Esempi di compilazione (senza tabelle X LATEX](Sorgenti/MB/DOC_OPE/LOCEDT_ESE)

# Esempi di tutti i font trattati
<table border="1" cellspacing="0" cellpadding="0" align="center">
<tr><td>**Valore**</td><td>**Versione Loocup**</td><td>**Versione AS**</td></tr>
<tr><td>n  </td><td>  Normale            </td><td>Normale    </td></tr>
<tr><td>1  </td><td>_1_  Rosso   Grande    </td><td>Rosso Reverse</td></tr>
<tr><td>2  </td><td>_2_  Blu     Grande    </td><td>Blu Reverse</td></tr>
<tr><td>3  </td><td>_3_  Verde scuro    Grande    </td><td>Rosa Reverse</td></tr>
<tr><td>4  </td><td>_4_  Rosa  Grande    </td><td>Giallo Reverse</td></tr>
<tr><td>5  </td><td>_5_  Verde chiaro Reverse    </td><td>Azzurro Reverse</td></tr>
<tr><td>7  </td><td>_7_  Rosso              </td><td>Rosso</td></tr>
<tr><td>8  </td><td>>  Blu                </td><td>Blu</td></tr>
<tr><td>9  </td><td>_9_  Verde scuro      </td><td>Rosa</td></tr>
<tr><td>B  </td><td>_B_  Rosa   </td><td>Blu sottolineato</td></tr>
<tr><td>R  </td><td>_R_  Verde chiaro</td><td>Rosso sottolineato</td></tr>
<tr><td>u  </td><td>__  Sottolineato       __</td><td>Sottolineato</td></tr>
<tr><td>h  </td><td>** Alta intensità    **</td><td>Alta intensità</td></tr>
<tr><td>i  </td><td>_  Italic             _</td><td>_Non corrispondente_</td></tr>
<tr><td>r  </td><td>_r_  Rosso sottolineato</td><td>Inversione di fondo</td></tr>
</table>

# Esempi di riferimento ad oggetti
 :  : DEC T(CN) P(CLI) K(000001) I(Cliente) O(GKIJ)
 :  : DEC T(AR) P() K(A01) I(Articolo) D(XXX) O(I)
 :  : DEC T(TA) P(CLS) K(010) I(Classe materiale) O(GKI)

# Esempio di riferimento a file sul server
 :  : DEC T(J1) P(PATHFILE) K([AZI.HOM.01]\Programmi\Loocup_test\LOOCUP_ICO\AR\default.gif) O(GKJ)
[http://www.smeup.com](http://www.smeup.com)

# Esempi di funzioni
 :  : DEC T(AR) P() K(A01) D(G) I(Link a programma) X({M(EMU;ESE;AZI) 1(TA;MEABR;0101) P() G() SP() SG() NOTIFY()}) O(I)

# Esempi di inclusione di immagini
## Definite direttamente


Testo come prefisso <img src="file : [AZI.HOM.01]\Programmi\Loocup_test\LOOCUP_ICO\AR\default.gif" width="25" height="25">

Testo come suffisso con _&_ anche in tag _7_inline _&_





<img src="file : [AZI.HOM.01]\Programmi\Loocup_test\LOOCUP_IMG\CN\CLI\000001.jpg" width="80" height="80"> Testo affiancato all'immagine

## IMG con percorso esplicito
IMG P([AZI.IMG]\CN\CLI\000001.PNG) A(C)
 :  : IMG P([AZI.IMG]\CN\CLI\000001.PNG) R(60)

### IMG con immagine oggetto
IMG P([IMG : AR;;A01]) R(60)
 :  : IMG P([IMG : AR;;A01]) R(60)



# Tabella con font non proporzionale
>TpParametro Codice                        Ava  ISm ISu      Persona            Funzione
OG          AR articolo                   20       A
OG          AZ azienda                    30       A        Rossi              Analisi
OG


# Elenchi puntati/numerati stile WIKI
Per iniziare un elenco basta  inserire a inizio riga la seguente serie di caratteri : 
' * '  (spazio-asterisco-spazio) e nome del valore del punto elenco (nel caso di elenchi puntati)
' - ' (spazio-diesis-spazio) e nome del valore del punto elenco (nel caso di elenchi numerati)
e man mano incrementare il numero di simboli se si vuole cambiare livelli. Per concludere l'elenco aggiungo uno spazio bianco.

Esempio elenco puntato : 
 ' * ' Primo punto
 ' ** ' Secondo punto con un testo molto lungo per testare i ritorni a capo ed eventuali problemi di
 ' *** ' Terzo punto

Diventa : 
 * Primo punto
 ** Secondo punto con un testo molto lungo per testare i ritorni a capo ed eventuali problemi di
 *** Terzo punto

Esempio elenco numerato : 
 ' - ' Primo punto elenco numerato
 ' -- ' Secondo punto elenco numerato
 ' - ' Terzo punto di nuovo di primo livello

Diventa : 
 - Primo punto elenco numerato
 -- Secondo punto elenco numerato
 - Terzo punto di nuovo di primo livello

# Titoli stile WIKI
I titoli hanno lo stesso comportamento degli elenchi con la differenza che si usa il simbolo di ! : 
' ! '  (spazio-punto esclamativo-spazio) e nome del titolo

Esempio : 
' ! ' Titolo livello 1
' !! ' Titolo livello 2
' !!! ' Titolo  livello 3

Diventa : 
 ! Titolo livello 1
!! Titolo livello 2
!!! Titolo  livello 3

# Esempio di trattamento di un documento (test)
## OBIETTIVO
Avere uno strumento di gestione della documentazione aziendale. Per documentazione aziendale intendiamo la documentazione tecnica, le schede tecniche, i cataloghi, i disegni, le
specifiche e qualsiasi altro tipo di documento che la realtà aziendale necessita. L'applicazione realizzata consente di effettuare tutte le operazioni di gestione della documentazione attraverso un
unico formato video che presenta una serie di opzioni disponibili all'utente, consentendo a diversi utenti di effettuare solo le operazioni per cui sono abilitati.

## Formato video guida
![CQDOCU_02](http://localhost:3000/immagini/MBDOC_OPE-LOCEDT_ESE/CQDOCU_02.png)
Le opzioni disponibili sono : 
 * 01 Aggiunta :  per immettere un nuovo documento;
 * 02 Modifica :  per modificare, approvare, rilasciare e distribuire un documento;
 * 03 Copia :  per creare un nuovo documento con caratteristiche simili ad uno già creato;
 * 04 Annullamento :  per eliminare un documento;
 * 05 Interrogazione :  per visualizzare un documento.

## Tipo documento
Per poter accedere in modo corretto alle funzioni si deve precisare quale è il TIPO DOCUMENTO che si vuole gestire; il TIPO DOCUMENTO è codificato nella tabella CQ0 (si veda eventualmente la descrizione della tabella CQ0).
Il tipo documento suddetto può anche essere precisato prima ancora di entrare nell'applicazione e, in questo caso, deve essere passato all'applicazione come parametro (CALL CQQM10G PARM('tipo docum.')).
Con questa possibilità la gestione sarà personalizzata in funzione di quel tipo di documento senza però poter modificarne il tipo fino al termine dell'applicazione.

## Formato video dettaglio
![CQDOCU_03](http://localhost:3000/immagini/MBDOC_OPE-LOCEDT_ESE/CQDOCU_03.png)
### Note particolari
L'opzione di modifica permette di effettuare una molteplicità di operazioni : 
 * modificare la parte relativa all'immissione
 * approvare il documento una volta immesso
 * rilasciare il documento una volta approvato
 * distribuire il documento

Tutte queste operazioni sono assoggettate alle autorizzazioni che ogni singolo utente può avere o non avere.
Gli utenti che non possono ne approvare ne rilasciare un documento non vedranno nella prima videata del DETTAGLIO il tasto funzionale F15 che permette di passare alla seconda videata che gestisce l'approvazione, il rilascio e la distribuzione.
