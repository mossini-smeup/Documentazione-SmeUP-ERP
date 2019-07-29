# V6T - Piano provvigioni
 :  : DEC T(ST) K(V6S)
## OBIETTIVO
Definisce in modo più articolato il calcolo delle provvigioni.
## CONTENUTO DEI CAMPI
 :  : FLD T$V6SA **Tipo Liquidazione 1**
Indica il tipo di liquidazione previsto. Può assumere i seguenti valori : 
 - P = Su pagato ------> la liquidazione avviene in rapporto ai pagamenti effettuati dal cliente nel dato periodo;
 - S = Su saldato -----> la liquidazione avviene in rapporto ai documenti saldati nel dato periodo;
 - F = Su fatturato ---> la liquidazione avviene in rapporto ai documenti fatturati nel dato periodo.
 :  : FLD T$V6SB **% Liquidazione 1**
Indica il valore % delle provvigioni che viene calcolato con il tipo di liquidazione relativo.
 :  : FLD T$V6SC.T$V6SA Tipo Liquidazione 2
 :  : FLD T$V6SD.T$V6SB % Liquidazione 2
 :  : FLD T$V6SE.T$V6SA Tipo Liquidazione 3
 :  : FLD T$V6SF.T$V6SB % Liquidazione 3
