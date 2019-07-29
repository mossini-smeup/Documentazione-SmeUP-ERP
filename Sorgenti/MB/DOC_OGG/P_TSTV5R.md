# GESTIONE PIANO PROVVIGIONI
## OBIETTIVI
Gestire la scrittura del piano delle provvigioni

## FUNZIONI/METODI

 * - PLA - Gestione piano provvigioni
 ** - INZ - Inizializzazione del piano :  cancella tutti i record del piano corrispondenti ai riferimenti generali passati che non presentano il flag di contabilizzazione.
 ** - INZA - Come INZ ma solo per i record di un'agente.
 ** - AGG - Scrive/aggiornra i record del piano in base ai riferimenti specifici passati.
 ** - FIN - Finalizzazione del piano :  completa i record le piano corrispondenti ai riferimenti generali passati calcolando i contributi relativi agli importi memorizzati sul record tramite la funzione AGG.
 ** - FINA - Come FIN ma solo per i record di un agente.
 * - VER- Verifica
 ** - ENA - Enasarco
