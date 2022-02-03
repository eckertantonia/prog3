#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAXOUTPUT 100
    
void schwabify(char *input, char output[]);



/*****************************************************************
 * Bitte nachfolgend basteln
 *****************************************************************/

void schwabify(char *input, char output[]) {
    /* Bitte hier ergaenzen */
    
}





/*****************************************************************
 * Hier kommen die einzelnen Tests
 *****************************************************************/

static void test1(void) {
    char output[MAXOUTPUT];
    char input[] = "Das ist interessant.";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Das isch interessant, woisch?", output));
}

static void test2(void) {
    char output[MAXOUTPUT];
    char input[] = "Dort, ein Auto. Das hat da geparkt.";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Dort, ein Auto, woisch? Das hat da geparkt, woisch?", output));
}

static void test3(void) {
    char output[MAXOUTPUT];
    char input[] = "Mit     diesem Kleber     sollte es halten, oder?";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Mit     diesem Kleber     sollte es heben, oder?", output));
}

static void test4(void) {
    char output[MAXOUTPUT];
    char input[] = "Oh, da steht ein    Anhalter.";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Oh, da steht ein    Anheber, woisch?", output));
}

static void test5(void) {
    char output[MAXOUTPUT];
    char input[] = "Der Griff ist zum Aufhalten der Tuere.";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Der Griff isch zum Aufheben der Tuere, woisch?", output));
}

static void test6(void) {
    char output[MAXOUTPUT];
    char input[] = "Das ist Mister Dingdong... von dem ist nichts zu halten.";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("Das isch Mischer Dingdong, woisch?, woisch?, woisch? von dem isch nichts zu heben, woisch?", output));
}

static void test7(void) {
    char output[MAXOUTPUT];
    char input[] = ".";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp(", woisch?", output));
}

static void test8(void) {
    char output[MAXOUTPUT];
    char input[] = "haltisthalt. isthaltist...";
    schwabify(input,output);
    printf("[%s] --> [%s]\n", input, output);
    assert(!strcmp("hebischheb, woisch? ischhebisch, woisch?, woisch?, woisch?", output));
}

int main(void) {
    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();
    printf("** fertig **\n");
    return 0;
}
