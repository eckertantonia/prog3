/*Zeiger struct, dynamische Speicherverwaltung*/
#include <stdio.h>
#include <stdlib.h>

struct n{
    void *ndata;
    struct n *before;
    struct n *next;
};
typedef struct n *nodep; /*namensersetzung für struct-pointer auf n*/

void printList(nodep lst){
    while(lst != NULL){
        printf("%p \n", lst);
        lst = lst->next;
    }
    printf("\n");
}

nodep insertAt(nodep lst, int pos, void *data){
    int i = 0;
    nodep newKnot = NULL;
    newKnot = malloc(sizeof(nodep)); /*Speicherplatz sichern*/
    newKnot->ndata = data;
    
    
    if(pos == -1){
        /*als letzten Knoten in Liste einfuegen*/
        while(lst->next != NULL){
            lst = lst->next;
        }
        newKnot->before = lst;
        lst->next = newKnot;

    } else if(pos == 0){
        /*als ersten Knoten in Liste einfuegen*/
        newKnot->before = NULL;

        if(lst == NULL){
            newKnot->next = NULL;
            lst = newKnot;
        } else {
            lst->before = newKnot;
            newKnot->next = lst;
        }
        
    } else {

        for(i = 1; i<pos; i++ ){
            lst = lst->next;
        }

        newKnot->next = lst->next;

        if(lst->next != NULL){
            (lst->next)->before = newKnot; /* wenn position vorher das erste element gibts segmentation fault*/
        }    

        newKnot->before = lst;
        lst->next = newKnot;
    }

    /*Zurück an Listenkopf navigieren*/
    while(lst->before != NULL){
        lst = lst->before;
    }

    free(newKnot);
    return lst;
}

nodep deleteAt(nodep lst, int pos){

    int i = 0;
    for(i = 0; i<pos; i++){
        lst = lst->next;
    }
    (lst->before)->next = lst->next;
    (lst->next)->before = lst->before;

    lst = lst->next;

    /*Zurück an Listenkopf navigieren*/
    while(lst->before != NULL){
        lst = lst->before;
    }
    return lst;
}

int main(int argc, char *argv[]){
    
    /*small change for git*/
    nodep liste = NULL;
    int a = 1, b = 2, c = 3;
    void *vp = NULL, *vp1 = &b, *vp2 = &c;
    vp = &a;

    liste = insertAt(liste, 0, vp); 
    printList(liste);
    liste = insertAt(liste, 1, vp1);
    printList(liste);
    liste = insertAt(liste, 1, vp2);
    printList(liste);
    liste = insertAt(liste, 2, vp);
    printList(liste);
    liste = insertAt(liste, -1, vp);
    printList(liste);

    liste = deleteAt(liste, 2);
    printList(liste);

    free(liste);
    return 0;
}

