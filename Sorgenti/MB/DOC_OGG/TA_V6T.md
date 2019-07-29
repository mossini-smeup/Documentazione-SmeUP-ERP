# V6T - Piano Enasarco
 :  : DEC T(ST) K(V6T)
## OBIETTIVO
Definisce i parametri di calcolo dei contributi dell'Enasarco.
## CONTENUTO DEI CAMPI
 :  : FLD T$V6TA **% Enasarco a carico della ditta/agente**
Indicano rispettivamente la percentuale di Enasarco da versare all'Ente dall'azienda e dall'agente a fine trimestre, in rapporto alle provvigioni maturate.
Nella legislatura la % può variare a seconda che l'agente sia o meno monomandatario (cioè lavori per una o più aziende) e che sia un agente di commercio.
 :  : FLD T$V6TB.T$V6TA
 :  : FLD T$V6TC **Massimale annuo**
Indica il massimo importo che l'azienda e l'agente sono obbligati a versare all'Ente, per le provvigioni fatturate e maturate in un anno. Quando la somma dell'Enasarco versata dall'azienda e dall'agente raggiunge tale limite, non sarà più necessario calcolare la percentuale fino all'anno successivo, quando il progressivo annuo si azzererà.
Il valore del massimale dovrà poi essere rapportato in funzione delle date di inizio/fine rapporto avvenute nell'anno.
 :  : FLD T$V6TD **Minimale annuo**
Indica l'importo minimo da versare all'Ente in un anno se sono maturate delle provvigioni.
Se il contributo enasarco calcolato non supera tale importo, dovrà essere l'azienda a integrare il versamento fino al raggiungimento del minimale.
A tale importo è inoltre applicabile il concetto di _frazionamento trimestrale_, che permette di confrontare a fine trimestre l'importo dell'Enasarco sulle provvigioni fatturate nel trimestre, non con l'intero importo del minimale, ma solo con il suo quarto.
È importante ricordare che, nel caso in cui in un trimestre l'azienda sia costretta a versare la differenza con il minimale, se nei trimestri successivi il minimale venisse superato, l'azienda potrebbe rivalersi sull'agente della somma versata in eccedenza.
Il valore del minimale dovrà, poi, essere rapportato in funzione delle date di inizio/fine rapporto avvenute nell'anno.
