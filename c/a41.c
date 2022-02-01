/*Zeiger, struct, dynamische Speicherverwaltung*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct knoten {
    char data[25];
    struct knoten *next;

}knoten;

knoten* addKnoten(char *newData){
    knoten *newKnoten = NULL;
    newKnoten = malloc(sizeof(knoten)); /*Speicher für Knoten freischaufeln*/
    strcpy(newKnoten->data, newData);
    newKnoten->next = newKnoten;

    return newKnoten;
} 


int main(int argc, char *argv[]){
    char help[26]; /*max 25 +1 weil '\0'*/
    knoten *knotpoint = NULL; /*neu allociertes Element*/
    knoten *letztesElement = NULL;
    knoten *before = NULL;
    int anzahlReim = argc-1, i = 0;
    while (fgets(help, 26, stdin) != NULL){
        knotpoint = addKnoten(help);

        if(letztesElement == NULL){
            letztesElement = knotpoint;
        } else {
            knotpoint->next = letztesElement->next;
            letztesElement->next = knotpoint;
            letztesElement = knotpoint;
        }

    }

    /*argc = Worte in Abzählreim.
        knotenliste durch gehen mit argc-Schritten,
        knotenelement löschen und pointer neu setzen*/

    while(knotpoint->next != knotpoint){

        /*abzählen*/
        for(i = anzahlReim; i>0; i--){
            before = knotpoint;
            knotpoint = knotpoint->next;
        }

        /*knoten löschen*/
        printf("wird geloescht: %s \n", knotpoint->data);
        before->next  = knotpoint->next;
        free(knotpoint);
        knotpoint = before->next;
        
    }
    printf("Verlierer: %s \n", knotpoint->data);
    
    free(knotpoint);
    return 0;
}