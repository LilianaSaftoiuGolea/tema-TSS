# Raport scurt – laborator 10.05 (L5)

## 1. Cât timp durează pipeline-ul complet?

Pe GitHub Actions, durata exactă se vede după prima rulare în tab-ul **Actions**. În practică, job-ul de teste și coverage durează puțin, iar mutation testing durează mai mult. De aceea, mutation testing a fost pus într-un job separat și marcat opțional.

 
## 2. Ce avantaje aduce această abordare față de rularea manuală a testelor?

Avantajele principale sunt:
- verificare automată la fiecare modificare;
- detectare rapidă a regresiilor;
- raport de coverage disponibil ca artefact;
- mutation testing integrat în procesul de validare;
- trasabilitate: fiecare rulare rămâne salvată în GitHub Actions;
- colaborare mai bună între membrii echipei, pentru că fiecare push este verificat uniform.

## 3. Observație finală

Pentru această rezolvare s-a folosit GitHub Actions. Pipeline-ul include:
- rularea automată a tuturor testelor;
- prag minim de coverage pe codul sursă;
- generarea artefactului HTML pentru coverage;
- mutation testing ca job separat;
- suport pentru badge de status și notificări la eșec.
