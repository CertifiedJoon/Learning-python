#include "calc.h"
#define BUFSIZE 1

static char buf[BUFSIZE];  // buffer for ungetch
static int bufp;           /*next free psition in buffer */

int getch(void){
  return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c){
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters \n");
  else
    buf[bufp++] = c;
}
