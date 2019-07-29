# Linux
La release di riferimento è Ubuntu 14.10

## Problemi noti

### Ingrandire il file system

In fase di installazione del sistema operativo occorre gestire  :  : DEC T(J1) P(URL) [https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)
In alternativa non è possibile ingrandire un file system, ma occorre creare e montare un nuovo ramo

### Troppi file aperti

* verificare il numero max con il comando :  ulimit -n
* impostare il numero massimo con il comando :  ulimit -n nnnnn (es 16384)
* per impostare il limite in modo permanente editare il file /etc/security/limits.conf

### Caratteri speciali in copia+incolla cartelle da client Windows
// TODO
