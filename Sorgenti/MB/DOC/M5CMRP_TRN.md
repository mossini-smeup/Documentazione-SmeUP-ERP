 :  : PRO Cod(PIA) Txt(Pianificazione materiali) STAT(00)
 :  : ATT Cod(TMP) Txt(Tempi di approvvigionamento) STAT(00)
01. Inserire i tempi di approvvigionamento unitari per un articolo, nei dati di pianificazione.
02. Impostare che la sua politica sia di produzione.
03. Inserire il lotto standard nell'anagrafica.
04.Calcolare i tempi di approvvigionamento totali, utilizzando il test della routine £M5T (comando T M5T), inserendo le stesse informazioni (tempi e lotti).
05. Utilizzare l'aiuto di questa routine per comprendere in dettaglio il funzionamento.
 :  : ATT Cod(RIS) Txt(Risalita dati di pianificazione) STAT(00)
01. Impostare la risalita dei dati di pianificazione nella seguente scaletta :  articolo / Classe programmazione / Generico.
02. Impostare la risalita a pettine.
03. Definire le politiche a livello di codice articolo, i lotti a livello di classe e i tempi a livello genrale.
04. Controllare che per l'ariticolo impostato i dati siano reperiti correttamente :  utilizzando il test della routine £M5A (comando T M5A).
 :  : ATT Cod(FON) Txt(Definizione Fonti e Metafonti) STAT(00)
01. Definire un gruppo fonti con fonti sia positive che negative.
02. Definire una metafonte che sia la disponibilità libera di tale gruppo fonti.
03. Definire una fonte di orgine MP che sia fonte guida, con segno negativo.
04. Definire una metafonte che sia la differenza positiva tra la fonte guida ed un gruppo di fonti negative
 :  : ATT Cod(POL) Txt(Definizione politiche di pianificazione) STAT(00)
01. Definire una politica di produzione che utilizzi un gruppo fonti specifica e che non produca suggerimenti se il riordino è inferiore al 10 % del lotto minimo o al 50 % della scorta minima
