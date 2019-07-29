# OBIETTIVO

Gestire la traduzione di frasi in una determinata lingua. Le traduzioni sono sul file A£TRDE0F.

# FUNZIONI E METODI

## TRA - Traduci

Questa funzione prende in input una schiera di frasi da tradurre. Per ogni frase : 
 * In base al formato della schiera (puro testo, schiera di G11, ...) e a considerazioni di normalizzazione (caratteri speciali, prefissi e suffissi, ...) estrae la parte di testo da tradurre effettivamente.
 * Cerca la traduzione per la lingua specificata, in ordine inverso di ambito (ambiti più alti = traduzioni più personalizzate). Esclude le traduzioni di ambiti non consentiti nell'ambiente corrente.
 * Una volta tradotta la frase, la rinormalizza reinserendola nella frase originale (annullando gli effetti della normalizzazione del primo step, ad esempio riaggiungendo prefissi e suffissi).

Nota tecnica :  per motivi di performance questa funzione termina la traduzione dopo avere trovato 5 elementi vuoti nella schiera in input. Qualora fosse necessario forzare di continuare nella traduzione è possibile utilizzare l'apposito flag "Traduci tutto".
