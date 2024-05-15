# PVA2 - Programování a vývoj aplikací
## Cvičení 32: GUI Tkinter App

Dokumentace Tk: `https://tk-tutorial.readthedocs.io/en/latest/intro/intro.html`

### 1 Binding
`https://tk-tutorial.readthedocs.io/en/latest/event/event.html?highlight=bind`

Přimějte `button1` spustit funkci `increase_value` BEZ použití parametru `command=`

V předchozích lekcích jste vytvořili funkční tlačítka, ale co když chceme mít klávesové zkratky nebo něco provést pravým tlačítkem myši?

Vázané akce spojují funkci s událostí/vstupem, který se odehrává v okně.

1. Proměnná čítač uchovává aktuální hodnotu proměnné čítač.
2. Funkce increase_value zvyšuje hodnotu proměnné.
3. Poté funkce aktualizuje popisek label1.
4. Před otevřením okna navážeme funkci na tlačítko. Takže když tlačítko obdrží vstupní událost <Button-1>, spustí se funkce increase_value.

Seznam běžně používaných [vstupních událostí](vstupni_udalosti.md) budete ho potřebovat:
