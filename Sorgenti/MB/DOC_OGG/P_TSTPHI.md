
# Obiettivo
Gestire le funzioni di apertura/chiusura eventi della raccolta dati di campo macchina.
Gestire le funzione di informative del stato avanzamento raccolta dati.

## Funzione CHG
Dato input obbligatorio la macchina, contatori buoni/scarti e stato macchina.
E' la funzione chiamata dalla exit del LOA37 che esegue le chiamate alla £G95 per chiudere evento
ed aprire nuovo evento al cambio di : 
- Stato macchina
- Turno lavoro

## Funzione DIC
Dato input obbligatorio la macchina, contatori buoni/scarti e stato macchina.
E' la funzione chiamata dalla exit del LOA37 quando è chiamata in letura pezzi(non cambio stato)
e serve per capire se necessario forzare cambio evento(esempio cambio turno).

## Funzione EOT  Event  on Time
Dato input obbligatorio la macchina.
Restituisce data una macchina le seguenti inmformazioni : 
-Stato Macchina
-Ordine Produzione
-Fase Lavoro
E' in grado di leggere 'n' ordini di produzione se la macchina è attrezzata con batch di produzione
Restituisce 'FIN' quando finisce di leggere

## Funzione LET  Lettura dati macchina
Dato input obbligatorio la macchina.
Restituisce data una macchina le informazioni della macchina collegata con LOA37.
Le informazioni ad oggi gestite sono : 
- Stato macchina  :  Lavoro, Non Lavoro.
- Conta Pezzi Scarti
- Conta Pezzi Buoni

## Funzione LET  Metodo QUA.
Dato input obbligatori la macchina, ordine e fase.
Restituisce le quantità buone,scarte della raccolta eventi non ancora applicati.

## Funzione LET  Metodo QTO.
Dato input obbligatori la macchina, ordine e fase.
Restituisce le quantità buone,scarte dell'ordine di produzione totalizzando sia i dati
già consuntivati sul P5ATTI0F che i dati non ancora applicati della raccolta dati presenti
sul P5EVEN0F


## Funzione STOP metodo bianco
Dato input obbligatori la macchina. Ordine opzionale se passato fa STOP solo su ordine passato
Chiude evento di livello '0' in corso sulla macchina ed apre un vento su ordine di Fermo Gestionale

## Funzione STOP metodo SAL
Come STOP metodo bianco con il saldo della fase dell'ordine di produzione in macchina.

## Funzione WRI
Dato input obbligatori la macchina, ordine,fase, Causale evento e Dipendente.
E' una funzione utilizzata per scrivere eventi a macchina ferma di questa tipologia : 
- Dichiarazioni attrezzaggio, smontaggio
- Causalizzazione Fermi

