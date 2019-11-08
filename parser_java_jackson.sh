#!/usr/bin/env bash

# Assumes maven on path configured with Java 11+
mvn -f parser-java-jackson/pom.xml clean install -DskipTests

./test_parser.sh "$JAVA_HOME"/bin/java -Xss8400k -jar parser-java-jackson/target/bad-parser-jackson-1.0-SNAPSHOT.jar
