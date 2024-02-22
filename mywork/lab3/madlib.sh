#!/bin/bash


clear
echo "Let's build a mad-lib!"

read -p "1. Please give me a noun: " NOUN1
read -p "2. Please give me a past tense transitive verb: " VERB1
read -p "3. Please give me an adjective: " ADJ1
read -p "4. Please give me another noun: " NOUN2
read -p "5. Please give me a past tense transitive verb: " VERB2
read -p "6. Please give me a part of the body: " POB
read -p "7. Please give me an adverb: " ADV1
read -p "8. Please give me another past tense verb: " VERB3
read -p "9. Please give me one last past tense verb: " VERB4
read -p "11. Please give me another adverb: " ADV2


echo "Once a $NOUN1 $ADV2 $VERB1 the $ADJ1 $NOUN2, and $VERB2 her $POB."
echo "She $ADV1 $VERB3 when she $VERB4."
