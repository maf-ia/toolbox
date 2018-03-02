 
#include <stdio.h>

int strcmp(const char *s1, const char *s2)
{
  printf( "CMP: %s - %s\n" );
  return __strcmp(s1,s2);
}