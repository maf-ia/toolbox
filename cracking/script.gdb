set height 0
set width 0
     
file ch20.bin
rwatch *0x80491a0
run
     
b *0x80480d5
set $flag="~~~~~~~~~~~~~~~~~~~~~~~~~"
set $i=0x19-1
     
while $i >= 0
    set $bl = ($al^$dl)&0xff
    set $flag[$i] = ($al^$dl)&0xff
    set $i--
    c
end

print $flag
quit 
