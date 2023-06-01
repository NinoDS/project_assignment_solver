#import "template.typ": *

#show: project.with(
  title: "Optimale Projektzuweisung für die Projektwoche",
  authors: (
    "Friedrich Darius",
  ),
)


= Einleitung
Ein essenzieller Bestandteil einer gelungenen Projektwoche ist eine gute Projektzuweisung. Die Schüler haben die Möglichkeit, ihre Präferenzen anzugeben, indem sie einen Erstwunsch, Zweitwunsch, Drittwunsch und einen Nichtwunsch angeben. Gleichzeitig können die verschiedenen Projekte eine unterschiedliche Anzahl an Teilnehmern aufnehmen. Das Ziel ist es, unter den Einschränkungen der Projektplätze und Präferenzen der Schüler eine ideale Projektzuweisung zu finden, welche die Gesamtzufriedenheit der Schüler zu optimiert.

= Mathematische Modellierung
Um das Problem mathematisch zu modellieren, definieren wir folgende Variablen:

- $s$ : Die Gesamtanzahl an Schülern 
- $p$ : Die Anzahl aller Projekte
- $c_(i j) in RR^(s times p)$ : Die Präferenzmatrix mit der Präferenz von Schüler $i$ für Projekt $j$. Hier wählen wir $3$ für den Erstwunsch, $2$ für den Zweitwusch, $1$ für den Drittwunsch, $-10$ für den Nichtwunsch und $0$ bei keiner Angabe.
- $x_(i j) in {0,1}^(s times p)$ : Der binäre Entscheidungsmatrix. Wenn $x_(i j) = 1$, besucht Schüler $i$ Projekt $j$, wenn $x_(i j) = 0$, dann nicht.
- $bold(t)_j$ : Die maximale Anzahl an Teilnehmern, die Project $j$ aufnehmen kann 

Wir möchten die Variablen $x_(i j)$ so wählen, dass die Gesamtpräferenzen maximiert werden. Dies kann als lineares Optimierungsproblem formuliert werden:

$ "maximiere"             &sum_(i=1)^s sum_(j=1)^p x_(i j) c_(i j) \
  "u.d.N.:" \
                          &sum_(j=1)^p x_(i j) = 1 space forall i = 1,...,s "(jeder Schüler besucht genau ein Projekt)" \
                          &sum_(i=1)^s x_(i j) <= bold(t)_j space forall j = 1,...,p "(Projekte nehmen nicht mehr Teilnehmer auf als erlaubt)" \
                          &x_(i j) in {0,1} space forall i = 1,...,s, space j = 1,...,p
                          $
  

== Implementierung
Für die praktische Implementierung zur Lösung des Problems der optimalen Projektzuweisung wurde die OR-Tools-Bibliothek von Google verwendet. Die Implementierung erfolgte in Python. 

Der Code nutzt die GLOP-Bibliothek des OR-Tools-Pakets @ortools, um das lineare Optimierungsproblem zu lösen. Zunächst werden Entscheidungsvariablen erstellt, die die Zuweisung der Schüler zu den Projekten repräsentieren. Anschließend werden die Projektbeschränkungen und Präferenzmatrix berücksichtigt, um die Zielfunktion und die Nebenbedingungen zu formulieren. 

Der Solver sucht nach der optimalen Lösung des Problems, wobei sicherstellt wird, dass jeder Schüler genau einem Projekt zugewiesen wird und dass die Kapazität jedes Projekts eingehalten wird. Es wird erwartet, dass der Solver eine optimale Zuweisung findet, die die Gesamtpräferenzen maximiert.

Der Code ist auf GitHub unter #link("https://github.com/NinoDS/project_assignment_solver") verfügbar.

#bibliography("works.bib")