# G.SUB.MAT :  Matrice

All'interno di una sezione è possibile definire una matrice di dati.

# Dati

Supporta le funzioni dati relative alle matrici.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.MAT

## ShowTotal :  Mostra totali
Mostra la barra dei totali posta alla fine matrice e alla fine di ogni raggruppamento. I valori possibili sono Yes/No. Il valore di default è No.

## ShowGroup :  Mostra gruppi
Mostra la barra dei raggruppamenti posta sopra la matrice. I valori possibili sono Yes/No. Il valore di default è No.

## ShowFilter :  Mostra filtri
Mostra i pulsanti di filtro sull'intestazioni delle colonne. I valori possibili sono Yes/No. Il valore di default è No.

## DftGroup :  Gruppi
Consente di specificare i campi secondo cui raggruppare la matrice alla sua creazione. Il valore dell'attributo è una stringa contenente i campi in ordine di raggruppamento divisi dal carattere '|' (Fld1|Fld2).

## DftTotal :  Totali
Consente di specificare i campi da totalizzare e la funzione da usare per totalizzare la matrice alla sua creazione. Il valore dell'attributo è una stringa contenente la funzione e i campi da totalizzare divisi dal carattere '|' secondo la seguente sintassi :  Funzione(Campo)|Funzione(Campo)|..

## DftSort :  Ordinamento
Consente di specificare i campi da ordinare (con ordinamento crescente o decrescente) nella matrice alla sua creazione. Il valore dell'attributo è una stringa contenente i campi e il tipo di ordinamento divisi dal carattere '|' secondo la seguente sintassi :  Campo,Ordinamento|Campo,Ordinamento)|.. dove Ordinamento è un carattere che può assumere valore A o D.

## Expanded :  Espansione Iniziale
Mostra la matrice già espansa in caso esistessero dei raggruppamenti. I valori possibili sono Yes/No. Il valore di default è No.

## Columns :  Colonne
Specifica tutte e sole le colonne della matrice che devono essere visualizzate, rendendo "invisibili" tutte le altre. Il valore dell'attributo è una stringa contenente i campi da visualizzare divisi dal carattere '|' secondo la sintassi :  Campo|Campo|..

## Icone :  Mostra Icone
Mostra le icone degli oggetti all'interno della matrice (esclusa la testata). I valori possibili sono Yes/No. Il valore di default è Yes.

## IconeTesta :  Mostra le icone di testata
Mostra le icone degli oggetti nelle intestazioni delle colonne. I valori possibili sono Yes/No. Il valore di default è Yes.

## SelFirst  :  Sel.auto 1° riga
Seleziona automaticamente il primo record della matrice, caricando le relative variabili e facendo scattare i dinamismi legati all'evento change.  I valori possibili sono Yes/No. Il valore di default è No.

## SelectRow :  Sel.auto di una riga
Seleziona automaticamente un record della matrice, caricando le relative variabili e facendo scattare i dinamismi legati all'evento change.  I valori possibili sono valori interi. Il valore di default è 0.

## ToExcel :  Consenti esportazione
Consente l'esportazione in foglio di calcolo dei dati della matrice, abilitando la relativa voce di menù. I valori possibili sono Yes/No. Il valore di default è Yes.

## FontName :  Nome FONT
Specifica quale carattere deve essere utilizzato per visualizzare l'etichetta. Il valore è una stringa di caratteri.

## FontColor :  Colore FONT
Specifica il colore con il quale mostrare il testo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.

## BackColor :  Colore Sfondo
Specifica il colore con in quale mostrare lo sfondo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.

## FontSize :  Dimensione FONT
Specifica la dimensione del carattere usato per visualizzare il testo dell'etichetta. Il valore è espresso con un numero intero.

## ReadOnly :  Non modificabile
Specifica se la matrice è di sola visualizzazione oppure se è possibile aggiornarne i dati contenuti. I valori possibili sono Yes/No. Il valore di default è Yes.

## UpdSvc :  Servizio di aggiornamento
Questo attributo specifica quale servizio AS400 è preposto per l'aggiornamento dei dati della matrice nel caso in cui non sia di sola visualizzazione. Il valore è una stringa del tipo Componente;Servizio;Metodo.

## Context :  Tabella/Contesto
Questo attributo specifica il contesto o la tabella su cui deve operare il servizio AS400 preposto all'aggiornamento dei dati della matrice. Il valore è una stringa.

## AutoFit :  Autofit colonne
Specifica se eseguire automaticamente il ridimensionamento delle colonne in base al contenuto oppure no. I valori possibili sono Yes/No. Il valore di default è Yes.
N.B :  Nel caso la funzione venga disabilitata, la larghezza della colonna verrà impostata al valore presente nell'xml di definizione della tabella. Se un valore valido non è presente per la colonna nell'xml, verrà comunque eseguito l'"Autofit" per quella colonna.

## AlignTotal :  Subtotali incolonnati
Specifica se mostrare i valori delle totalizzazioni incolonnati se sono presenti dei raggruppamenti.  I valori possibili sono Yes/No. Il valore di default è No.

## Styles :  Definizione stili
Definisce gli stili da applicare a colonne, righe e celle della matrice per personalizzarla. Il valore dell'attributo è una stringa del tipo Colonna=(Stile o Espressione)|Colonna=(Stile o Espressione)|.. dove Colonna è il nome del campo (o dei campi usando le macro speciali *ALL etc.) su cui applicare lo stile, Stile rappresenta il nome di uno stile già definito da applicare e Espressione una espressione logica che restituisce uno stile.

es.
Tutto in corsivo
**Styles="*ALL=*ITALIC"**
Colonna X in grassetto, Colonna Y in corsivo
**Styles="X=*BOLD|Y=*ITALIC""**
Colonna X in grassetto solo se Colonna Y diverso da bianco
**Styles="X={Y EQ GT ' ';*BOLD}"**

NB :  i nomi dei campi da utilizzare dove indicato sono quelli assegnati alle colonne della matrice
(primo campo della schiera £JAXSWK), visualizzabili nell'XML della matrice nella sezione <Griglia>,
attributo Cod del tag <Colonna ... />.
