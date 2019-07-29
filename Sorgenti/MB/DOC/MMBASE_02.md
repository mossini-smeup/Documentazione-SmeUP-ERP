# Pianificazione
Gli interventi di manutenzione devono essere pianificati in modo da poter consentire la sistematica esecuzione degli interventi previsti per assicurare il mantenimento di una elevata affidabilità dell'impianto per tutta la durata del suo ciclo di vita dall'installazione alla dismissione.

Gli interventi vengono generati per associazione ad un "raggruppamento" di risorse che saranno responsabili dell'esecuzione.

Il raggruppamento è la classificazione degli interventi estratti (pianificati). Serve nei casi in cui la manutenzione impianti è affidata a gruppi di manutentori diversi per capacità o per responsabilità di impianti o per altri criteri esplicitabili con le parzializzazioni indicate nella schermata di estrazione.
Per esempio possono essere estratti solo gli interventi di tipo elettrico o elettronico ed essere messi nel raggruppamento "ELETTR". Gli interventi di tipo idraulico possono essere raggruppati come "MECCAN", e cosi via. La codifica di tali raggruppamente si suddivide in due operazioni :  l'implementazione della tabella MMG e le creazione di un membro del file MMPRES0F con codice corrispondente alla tabella MMG.


![MMEC10G](http://localhost:3000/immagini/MMBASE_02/MMEC10G.png)
Gli interventi sono pianificati per un certo periodo e per un certo Raggruppamento, il programma di estrazione individua gli interventi che , a partire dalla data dell'ultimo intervento dichiarato , e secondo le politiche di pianificazione indicate per ogni intervento, cadono nel periodo indicato.

Gli interventi che cadrebbero prima dell'inizio del periodo sono considerati "scaduti".

Quindi, mettendo la 'X' nel campo "Ometti Scaduto" non vengono registrati nel raggruppamento  gli interventi che cadrebbero prima del periodo.

Mettendo la 'X' nel campo "Pulizia non eseguiti", gli interventi pianificati precedentemente nel raggruppamento in questione vengono cancellati, altrimenti restano nel raggruppamento.

## Gestione degli interventi pianificati
L'obiettivo di questa funzione è quello di organizzare gli interventi, rispettando i vincoli per ottenere : 

- efficienza degli interventi (economicità del piano)
- efficacia degli interventi (adeguatezza del piano rispetto alle esigenze del sistema)

Una volta creato e popolato (tramite estrazione) il raggruppamento, può essere gestito modificando gli interventi contenuti, aggiungendone altri manualmente o cancellandoli.

La gestione interventi estratti consente di modificare gli interventi pianificati e/o di pianificare "manualmente" degli interventi aggiuntivi, si seleziona un raggruppamento : 


![MMM23G](http://localhost:3000/immagini/MMBASE_02/MMM23G.png)
Viene presentata la lista degli interventi pianificati attribuiti al raggruppamento scelto : 


![MMM23L](http://localhost:3000/immagini/MMBASE_02/MMM23L.png)
Ogni intervento può essere modificato, oppure si possono creare manualmente nuovi interventi o anche eliminarne.

## Scheda interventi pianificati

Gli interventi pianificati possono anche essere rappresentati graficamente sotto forma di scheda : 


![MMBASE_007](http://localhost:3000/immagini/MMBASE_02/MMBASE_007.png)