Exemples de boucles bash:

for i in `seq 1 10`; 
do 
    echo "Tentative $i"; 
    ./exploit $i 120; 
done 

for i in $( ls ); do
    echo item: $i
done