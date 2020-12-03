echo "Converting ANTLR target from Python to Java"

node "../scripts/py2java.js"


echo "Searching ANTLR files"

alias antlr4='java -Xmx500M -cp "C:\Users\pmhie\Desktop\Assignment1 PPL\antlr-4.8-complete.jar" org.antlr.v4.Tool'

alias grun='java org.antlr.v4.gui.TestRig'

echo "Generating ANTLR to Java Code"

antlr4 BKIT.g4 -o antlr


echo "Generating Java Class files"

javac ./antlr/*.java -d ./


echo "Drawing Parse Tree"

grun BKIT program -f ./test/206.txt -gui

read name