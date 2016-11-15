# 1 "./test/sub.c"
# 1 "<built-in>" 1
# 1 "<built-in>" 3
# 324 "<built-in>" 3
# 1 "<command line>" 1
# 1 "<built-in>" 2
# 1 "./test/sub.c" 2
int printd( int i );

int main() {
  int i,j;
  i = 45000;
  j = -123;
  printd(i-j);
  printd(45000-j);
  printd(i-123);
  printd(45000-123);
  printd(i-(j+0));
  printd((i+0)-j);
  printd((i+0)-(j+0));
  printd((i+0)-123);
  printd(45000-(j+0));
  return 0;
}

