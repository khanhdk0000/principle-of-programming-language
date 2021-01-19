echo "Recompiling BKIT.g4"

antlr4 BKIT.g4

echo "Recompiling BKIT*.java"

javac BKIT*.java

echo "Draw AST"

grun BKIT program -f ./test/$1.txt -gui