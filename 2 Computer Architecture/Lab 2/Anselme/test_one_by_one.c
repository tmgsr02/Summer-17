#include <stdio.h>

// Return the nth bit of x.
// Assume 0 <= n <= 31

#define INTSIZE 31
unsigned get_bit(unsigned x,
                 unsigned n) {
    // YOUR CODE HERE
    unsigned a, b;
    a = x << (31 - n);
    b = a >> 31;
    return b;
}

void set_bit(unsigned * x,
             unsigned n,
             unsigned v) {
    // YOUR CODE HERE
    unsigned a, b, c, d, e, f, g;
    /* Make drawing down. It's a matter of isolating the nth bit. */
    a = * x >> n + 1; 
    b = a << 1;
    c = * x << 31 - (n - 1);
    d = c >> 31 - (n - 1);
    e = b | v;
    f = e << n;
    g  = d | f;
    /* Assigning the final value to the initial memory address */
    * x = g; 
    /* So, apparently, I can't shift a 32-bit int by 32. result: undefined behavior. So, I'm not sure how to make this function work when  n == 0 */
}
void flip_bit(unsigned * x,
              unsigned n) {
    // YOUR CODE HERE
    unsigned a, b, c, d, e, f, g, h, i, j, k, l, m, p, q;
    // save bits on the left of n and insert a zero at the end
    a = * x >> n + 1;
    b = a << 1;
    // save bits on the right of n
    c = * x << INTSIZE - (n - 1);
    d = c >> INTSIZE - (n - 1);
    // shift the bits to the left (back in their positions) & combine all bits
    e = b << n;
    f = d | e;

    // Isolating the nth bit in its position
    g = * x >> n;
    h = g << INTSIZE;
    i = h >> INTSIZE - n;
    // flipping all bits and removing the 1s surrounding the nth bit (0 or 1)
    j = ~i;
    k = j >> n;
    l = k << INTSIZE;
    p = l >> INTSIZE - n;
    printf("%x %x %x\n", k, l, p);
    // combining the value missing nth bit and the one with the flipped one
    q = f | p;
    * x = q;
}


void test_get_bit(unsigned x,
                  unsigned n,
                  unsigned expected) {
    unsigned a = get_bit(x, n);
    if(a!=expected) {
        printf("get_bit(0x%08x,%u): 0x%08x, expected 0x%08x\n",x,n,a,expected);
    } else {
        printf("get_bit(0x%08x,%u): 0x%08x, correct\n",x,n,a);
    }
}

void test_set_bit(unsigned x,
                  unsigned n,
                  unsigned v,
                  unsigned expected) {
    unsigned o = x;
    set_bit(&x, n, v);
    if(x!=expected) {
        printf("set_bit(0x%08x,%u,%u): 0x%08x, expected 0x%08x\n",o,n,v,x,expected);
    } else {
        printf("set_bit(0x%08x,%u,%u): 0x%08x, correct\n",o,n,v,x);
    }
}

void test_flip_bit(unsigned x,
                   unsigned n,
                   unsigned expected) {
    unsigned o = x;
    flip_bit(&x, n);
    if(x!=expected) {
        printf("flip_bit(0x%08x,%u): 0x%08x, expected 0x%08x\n",o,n,x,expected);
    } else {
        printf("flip_bit(0x%08x,%u): 0x%08x, correct\n",o,n,x);
    }
}


int main(int argc,
         const char * argv[]) {
    /* printf("\nTesting get_bit()\n\n");
    test_get_bit(0b1001110,0,0);
    test_get_bit(0b1001110,1,1);
    test_get_bit(0b1001110,5,0);
    test_get_bit(0b11011,3,1);
    test_get_bit(0b11011,2,0);
    test_get_bit(0b11011,9,0);
    printf("\nTesting set_bit()\n\n");
    test_set_bit(0b1001110,2,0,0b1001010);
    test_set_bit(0b1101101,0,0,0b1101100);
    test_set_bit(0b1001110,2,1,0b1001110);
    test_set_bit(0b1101101,0,1,0b1101101);
    test_set_bit(0b1001110,9,0,0b1001110);
    test_set_bit(0b1101101,4,0,0b1101101);
    test_set_bit(0b1001110,9,1,0b1001001110);
    test_set_bit(0b1101101,7,1,0b11101101); */
    printf("\nTesting flip_bit()\n\n");
    test_flip_bit(0b1001110,0,0b1001111);
    test_flip_bit(0b1001110,1,0b1001100);
    test_flip_bit(0b1001110,2,0b1001010);
    test_flip_bit(0b1001110,5,0b1101110);
    test_flip_bit(0b1001110,9,0b1001001110);
    printf("\n");
    return 0;

}
