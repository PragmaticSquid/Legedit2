I am no java expert (so far from it), but I made these notes to document how I attempted to compile ...

(cd src; find . -type f -name "*.java" > sources.txt)
(cd src; javac -d ./out/ @sources.txt)
(cd src/out; jar cfm ../../legedit2.jar ../../src/META-INF/MANIFEST.MF legedit2 opensource)
java -jar legedit2.jar
