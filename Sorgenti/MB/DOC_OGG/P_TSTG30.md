# OBIETTIVO
Visualizzazione, composizione, scomposizione sequenza campi

# PREREQUISITI
 D*   /COPY £G30E    per definizione schiere

# PARAMETRI
- Funzione :  _campo £G30FU_

- VER        Verifica
- COS       Schiere definite
- COD      Sch.da &&_G30 (Con/Pgm/Fun/Met)
- MDV       Lettura MDV


- Metodo :  _campo £G30ME_

- Se **funzione VER**
-- STD       Standard
-- TRA       Trasf.tipi dinamici in statici

- Se **funzione COS**
-- MOD Modifica
-- VIS Visualizzazione
-- MODF Modifica (in finestra)
-- VISF Visualizzazione (in finestra)

- Se **funzione COD**
-- MOD Modifica
-- VIS Visualizzazione
-- MODF Modifica (in finestra)
-- VISF Visualizzazione (in finestra)

- Se **funzione MDV**
 Non presente un metodo, scegliere la memorizzazione dalla finestra che compare.


- Opzione tasti funzionali :  _campo £G30FI_

-- F06  Abilita tasto F6
-- F11 Abilita tasto F11
-- F06F11 Abilita tasti F06 e F11
-- Se inserisco un testo viene abilitato il tasto F08 associato a quel testo


- Contesto :  _campo £G30MS_

* G30        I dati passati al programma vengono memorizzati nel formato predefinito della G30 (una stringa con i valori concatenati)
* '*Blanks' I dati passati al programma vengono memorizzati nel formato predefinito dalla G11 (una schiera di valori)

- Intestazione :  _campo £G30TI_

Titolo dele finestra di richiesta dati

- Schiera campi G30 :  _campo £G30A_

## METODO DI COSTRUZIONE DELLA SCHIERA £30A

 * Descrizione Posizione 01-30 :  intestazione del campo

**COSTRUZIONE DELL'INTESTAZIONE DINAMICA**
Nella descrizione se si include __Dn viene inclusa la descrizione dell'n.esimo elemento
ES : 'Pippo __D1 Pluto' è la descrizione e nel primo elemento c'è un articolo la cui descriz. è Artic_1.
La descriz.diventerà'Pippo Artic_1 Pluto'

 * TpParametro Posizione 31-50  :  Tipo+Parametro (lungh. 2+18)
Se fisso viene gestito normalmente (es.£DEC), se variabile è tipo dinamico

**COSTRUZIONE DEL TIPO DINAMIC**O
Definizione della schiera con cui va costruita
- __ come primo carattere
- C,D,E,G indicano se deve reperire le informazioni relative rispettivamente dal codice,descriz., TTLIBE o
oggetto di una griglia presente nel TTLIBE dell'n.esimo elem. della schiera d'ingresso
ES :  TA__C1,, indica che a TA concatena il codice del primo elemento

- numero indicante l'indice a cui puntare
- , di separazione (ATTENZIONE : OBBLIGATORIA)
- numero indicante la posizione d'inizio da cui iniziare a prendere l'elemento o nel caso G pos. d'inizio di dove è presente
la griglia di oggetti (TAB£G)
ES :  TA__C1,2,3 e il 1°elem.contiene PIPPO allora il sistema costruirà il tipo dinamico TAIPP

- , di separazione (ATTENZIONE : OBBLIGATORIA)

- numero indicante la lunghezza dell'elemento o nel caso G quale dei 3 oggetti presenti nella
griglia considerare.
Nel tipo dinamico è possibile inserire fino a 3 __ puntando a 3 elementi differenti.

VERIFICA LIMITI/VALORI -

- Tipo = L per controllare i limiti

- Tipo = V per controllare i valori

Parametro = xxxyyy, dove xxx e yyy sono gli
indici della schiera £30A da contare dopo l'elemento intestatario dei limiti/Valori (deve essere il simpolo delle somma (+) )  e rappresentano il range in cui vengono controllati i lim. o valori.

 * Lung. Posizione 51-55  :  rappresenta la lunghezza (se tipo numerico)

 * D Posizione 56-56  :  indica il numero di decimali O Posizione 57-57  :  O= indica l'obbligatorietà
 N= Nè obblig. nè controllo esistenza oggetto
 n= obblig. non controllato
 A= Non obbligatorio, ma accetta **
 a= obblig. ma accetta **
 Blank= Non obblig. con controllo esist. ogg.

 * V Posizione 58-58  :  numero per forzare modalità
  (gestione=2,interrogazione=5,hidden=H)
 nel caso siamo in verifica e è presente 'R' allora il pgm fa apparire una finestra per ricercare il codice R=ricerca

 * Au Posizione 59-60  :  Autorizzazione D

 * Posizione 61-61  :  Se diverso da BLANKS forza nella descrizione della riga X il valore messo in £11D,X
utile per descrivere campi numerici o ** in un loop di immissione
N.B. !! Non valido per righe dinamiche

 * Pos Posizione 62-64  :  Ordinamento
Se diverso da BLANKS forza in visualizzazione la posizione indicata  :  le righe BLANKS si presentano alla fine,
nell'ordine in cui sono nella schiera


# ESEMPIO DI CHIAMATA
>                         MOVEL<Funzione>£G30FU
                         MOVEL<Metodo>  £G30ME
                         MOVEL<Sch.Inp.>£30A
                         MOVEL<Titolo>  £G30TI 50
                         EXSR £G30
                         MOVEL£G30CO    <Str.Risultante>
                         MOVEL£G30MS    <Messaggio>
                         MOVEL£G30FI    <Flle>
                         MOVEL£G30CM    <Comando>
                         MOVEL£G11AM    <Ambiente>
                         MOVEL£G11FR    <Funz.Autoriz>

