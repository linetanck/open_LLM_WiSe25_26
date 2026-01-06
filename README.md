# Open LLMs in der Praxis: Liebeslieder
Projekt für das Seminar Open LLMs in der Praxis. Karoline Tanck 7449219 
![Taylor_Swift_The_Eras_Tour_Lover_Set_(53108816372)](https://github.com/user-attachments/assets/3cf8eaa4-dac0-4498-8f6f-2b7730ca2cc6)  
_Bild von Paolo Villanueva - Taylor Swift The Eras Tour: Lover Set, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=135971014._


## Aufgabenstellung
In diesem Projekt sollen open LLMs auf ihre Fähigkeit Texte zu interpretieren, getestet werden. Dabei wird sich fokussiert auf Songtexte eines bestimmten Artist (tbd.) und auf einen Bestimmten Aspekt: die Einstellung von dem lyrischen Ich zu dem lyrischen Du. Es soll um die Art des Liebesliedes gehen.

Dabei bekommt das Modell folgende Promts:
```
 You are a classifier.

            Allowed labels (choose exactly ONE):

            happily in love
            - the singer is in a mutual, positive relationship

            broken up
            - the relationship has ended or is ending

            yearning
            - the singer wants someone they are NOT with (distance, unrequited love, waiting)

            revenge empowerment
            - anger, revenge, or self-empowerment after hurt

            forbidden love
            - love that must be hidden or is socially blocked

            unrelated to love
            - love is not the main theme

            Rules:
            - Output exactly ONE label
            - No explanation
            - No punctuation
            Lyrics: {lyrics}
```
Die Kategorien, die vergeben werden sind: 
* "happily in love",
* "broken up",
* "yearning",
* "revenge empowerment",
* "forbidden love",
* "unrelated to love"

Grundsätzlich lassen sich Ergebnisse dieses Projektes auch auf andere Formen von Lyrik übertragen, zum Beispiel Gedichte. Sollten das genutzte offene LLM gut performen in diesem Projekt, dann ermöglichen LLMs das schnelle Analysieren solcher kurzen künstlerischen Texte.
## Daten:
Bei der Auswahl eines Datensatzes wird darauf geachtet, dass genug Lieder eines Artist im Datensatz sind. Zusätzlich aufgrund der Notwendigkeit einer manuellen Einteilung der Songs in die Kategorien ist es auch wichtig, dass alle Lieder gerne einmal gehört werden. 

Es wurden alle Songs vom Album Red (2012) und Lover (2019) genutzt. Die Songlyrics stammen aus einem Kaggle Datensatz von Ishika Johari  
https://www.kaggle.com/datasets/ishikajohari/taylor-swift-all-lyrics-30-albums  
Die Zielkategorien wurden manuell hinzugefügt.

## Modell
Für die Bearbeitung des Projekts wurden erste Experimente mit dem Modell [llama3.2:3b](https://ollama.com/library/llama3.2:3b) via Ollama gemacht. In der Entscheidungsfindung welches Modell genutzt wird, wurde neben der Offenheit hauptsächlich auf die Größe des Modells in Relation zur Leistungsfähigkeit geachtet. Das Projekt soll auf einem Laptop mit 8GB Arbeitsspeicher laufen, da dies auch ein zukünftiges Anwendungsszenario sein könnte. Laut Ollama übertrifft llama3.2:3b viele der anderen offenen Modelle und ist besonders gut darin, Zusammenfassungen zu erstellen.

## Projektverlauf
### Erste Tests
