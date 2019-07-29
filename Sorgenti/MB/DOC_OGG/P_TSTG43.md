## OBIETTIVO
Unificare la composizione e scomposizione di una strinnga che identifica dei campi mediante una separazione con un
carattere. Ad esempio voglio ricavare un file AS/400 a partire da un documento EXCEL.
## FUNZIONI e METODI
- Funzioni
.  COM Riceve una schiera e restituisce una stringa
.  SCO Riceve una stringa e restituisce una schiera
- Metodi
.  INI Nella stringa o nella schiera gestisce i TIPI (come se fosse la prima riga di un foglio EXCEL).
       Se non ho i tipi devo passare la schiera o la stringa bianche
.  INC Rispetto alla funzione precedente, viene aggiornata la variabile £G43NC con il n° di colonne determinate
.  ELB Nella stringa o nella schiera gestisce i DATI
.  ELA Come ELB ma vengono omessi gli assunti descritti di seguito
- Casi particolari
  . I tipi NUMERO e DATA vengono verificati ed elaborati. Ad esempio trasforma le date VARIABILI in date normali

## ESEMPI
Riga per INI -> TACLS;CNCLI;D8*YYMD;
         ELB    010;AAA001;20050102;
         ELB    020;AAA002;20050101;
