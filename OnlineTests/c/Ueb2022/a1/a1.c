#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

typedef struct lst {  char name[20];  int alter; struct lst *next; } ListEle;

ListEle *einfuegen(ListEle *lst, const char *n, int a); 
int dopple(ListEle *lst, const char *n, int a);
void befreie(ListEle *lst);


/**********************************************************
 * bitte die nachfolgenden drei Funktionen bebasteln 
 **********************************************************/

ListEle *einfuegen(ListEle *lst, const char *n, const int a) {
    /* bitte ergaenzen */

}

int dopple(ListEle *lst, const char *n, const int a) {
    /* bitte ergaenzen */

}

void befreie(ListEle *lst) {
    /* bitte ergaenzen */

}






/**********************************************************
 * Testkram und main()
 **********************************************************/

static void printList(ListEle *lst) {
    ListEle *p = lst;
    while (p) {
        printf("[%s,%d] >", p->name? p->name : "(NULL)", p->alter);
	p = p->next;
    }
    printf("NULL\n");
}

/* main() - wie man sieht... */

int main(int argc, char *argv[]) {

    /* Platz fuer eigenen Testcode */

    ListEle *lst=NULL, *erster = NULL;
    int rc;

    erster = lst = einfuegen(lst, "Joghurta", 21);
    printList(lst);
    assert(!strcmp("Joghurta", erster->name));
    assert(erster->alter == 21);
    assert(erster->next == NULL);

    /* Wubbo Ockels war der erste Niederlaender im Weltall */
    lst = einfuegen(lst, "Wubbo", 75);
    printList(lst);
    assert(!strcmp("Wubbo", erster->next->name));
    assert(erster->next->alter == 75);
    assert(erster->next->next == NULL);
    assert(erster == lst);

    lst = einfuegen(lst, "Glogomir", 12);
    printList(lst);
    assert(!strcmp("Glogomir", erster->next->next->name));
    assert(erster->next->next->alter == 12);
    assert(erster->next->next->next == NULL);

    rc = dopple(lst, "Wubbo",75);
    printList(lst);
    printf("rc=%d\n",rc);
    assert(rc == 1);
    assert(!strcmp("Wubbo", erster->next->name));
    assert(erster->next->alter == 75);
    assert(!strcmp("Wubbo", erster->next->next->name));
    assert(erster->next->next->alter == 75);
    assert(!strcmp("Glogomir", erster->next->next->next->name));
    assert(erster->next->next->next->alter == 12);
    assert(erster->next->next->next->next == NULL);

    rc = dopple(lst, "Wubbo",100);
    printList(lst);
    printf("rc=%d\n",rc);
    assert(rc == 0);
    assert(!strcmp("Glogomir", erster->next->next->next->name));
    assert(erster->next->next->next->next == NULL);

    rc = dopple(lst, "Glogomir",12);
    printList(lst);
    printf("rc=%d\n",rc);
    assert(rc == 1);
    assert(!strcmp("Glogomir", erster->next->next->next->name));
    assert(erster->next->next->next->alter == 12);
    assert(!strcmp("Glogomir", erster->next->next->next->next->name));
    assert(erster->next->next->next->next->alter == 12);
    assert(erster->next->next->next->next->next == NULL);
    

    rc = dopple(lst, "Joghurta",21);
    printList(lst);
    printf("rc=%d\n",rc);
    assert(rc == 1);
    assert(!strcmp("Joghurta", erster->name));
    assert(!strcmp("Joghurta", erster->next->name));
    assert(!strcmp("Wubbo", erster->next->next->name));
    assert(!strcmp("Wubbo", erster->next->next->next->name));
    assert(!strcmp("Glogomir", erster->next->next->next->next->name));
    assert(!strcmp("Glogomir", erster->next->next->next->next->next->name));
    assert(erster->next->next->next->next->next->next == NULL);

    befreie(lst);

    return 0;
}


