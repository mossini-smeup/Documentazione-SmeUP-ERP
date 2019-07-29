# Obiettivo
 Interfacciare il programma con l'archivio impegni risorse

# Input

£IIRNR - N.record Impegno risorse (I/O)
£DECR4 - Se diverso da blanks esegue solo la
         presentazione delle funzioni

# Output

DS P5IRIS valorizzata

# Prerequisiti
IS5IRIS         E DS                  EXTNAME(S5IRIS0F)

# Esempio di chiamata

C*                  MOVEL     Funzione      £IIRFU
C*                  MOVEL     Metodo        £IIRME
C*                  MOVEL     Ambiente      £IIRAM
C*                  MOVEL     Contesto      £IIRCO
C*                  MOVEL     N_Record      £IIRNR
C*                  EXSR      £IIR

# Note particolari
è preferibile eseguire un clear della DS P5IRIS prima di ogni richiamo
