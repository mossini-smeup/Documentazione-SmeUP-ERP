# Obiettivo
Interfacciare il programma in esecuzione con l'ANAGRAFICO EVENTI
Eseguire la ricerca alfabetica relativa se richiesto

# Funzioni e metodi

# Input
£IE3FU :  Funzione
£IE3ME :  Metodo
£IE3NK :  Numero chiavi
£IE3AM :  Ambiente
£IE3CO :  Contesto
£IE3PA :  Tipo Evento
£IE3CD :  Numero Evento
£IE3RI :  N.ro Record di input

# Output
£IE3CD :  Numero Evento scelta (se eseguita ricerca)
£IE3DE :  Descrizione evento
£IE3MS :  Codice messaggio ritorno (7)
£IE3FI :  File   messaggio ritorno (10)
£IE3CM :  Ultimo Comando
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
£IE3RO :  N.ro Record di output

# Prerequisiti
D P5EVEN        E DS                  EXTNAME(P5EVEN0F)
# Esempio di chiamata

chiamata ad unico accesso

 C*                  MOVEL     'CHA'         £IE3FU
 C*                  MOVEL     'Metodo'      £IE3ME
 C*                  MOVEL     Ambiente      £IE3AM
 C*                  MOVEL     Contesto      £IE3CO
 C*                  MOVEL     Tp_Event      £IE3PA
 C*                  MOVEL     Evento        £IE3CD
 C*                  EXSR      £IE3
 C*                  MOVEL     £IE3CD        Campo_Evento
 C*                  MOVEL     £IE3DE        Campo_descr

chiamata CON SCANSIONE

 C*                  MOVEL     'RL'          £IE3FU
 C*                  MOVEL     'Metodo'      £IE3ME
 C*                  MOVEL     Ambiente      £IE3AM
 C*                  MOVEL     Contesto      £IE3CO
 C*                  MOVEL     Tp_Event      £IE3PA
 C*                  MOVEL     Evento        £IE3CD
 C*                  EXSR      £IE3
 C
 C                   DO        *HIVAL
 C*                  MOVEL     'RE'          £IE3FU
 C*                  MOVEL     'Metodo'      £IE3ME
 C
 C*                  EXSR      £IE3
 C*                  IF        £IE335=*ON
 C*                  LEAVE
 C*                  ENDIF
 C*                  MOVEL     £IE3CD        Campo_Evento
 C*                  MOVEL     £IE3DE        Campo_descr
 C*
 C*                  ....
 C*                  ENNDO
 C*

# Oggetti collegati


# Note particolari

