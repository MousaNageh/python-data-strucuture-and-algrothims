#include <stdlib.h>
#include <stdio.h>
#include "list.h"

void CreateList(List *pl){
    pl->size = 0 ; 
    pl->head=NULL ;
}

int ListEmpty(List *pl){
    return !pl->size ; 
}
int ListFull(List * pl ){
    return 0 ; 
}
int ListSize(List *pl){
    return pl->size ; 
}
void DestoryList(List *pl){
    ListNode *ph ;
    while (pl->head)
    {
        ph = pl->head->next ;
        free(pl->head) ;
        pl->head = ph ; 
    }
    pl->size = 0 ; 
    
}
/* 0 =< pos <=size */
void InsertList(int pos , ListEntry e ,List *pl){
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    node->entry =e ; 
    node->next = NULL ; 
    if(pos == 0){
        node->next = pl->head ;
        pl->head = node ;   
    }
    else{
        ListNode *ph = pl->head ;
        for(int i = 0 ; i<=pos-1 ; i++){
            ph = pl->head->next ;
        }
        node->next = ph->next ;
        ph->next = node ;
    }
    pl->size++ ;
}
/* 0 <=  pos <= size-1 */
void DeleteList(int pos ,List *pl){
    ListNode * ph = pl->head ;
    if(pos==0){
        pl->head = ph->next ;
        free(ph);
    }
    else{
        for(int i = 0 ; i<=pos-1 ; i ++){
            ph = pl->head->next ;
        }
        ListNode * node = ph->next ; 
        ph->next = node->next ;
        free(node);
    }
    pl->size--;
}
/* 0 <=  pos <= size-1 */
void RetrieveList(int pos , ListEntry *e  ,List *pl){
    ListNode *ph = pl->head ;  
    for(int i = 0 ; i<=pos ; i ++){
        ph = pl->head->next ;
    }
    *e = ph->entry ;
};
void ReplaceList(int pos , ListEntry e   ,List *pl){
    ListNode *ph = pl->head ;  
    for(int i = 0 ; i<=pos ; i ++){
        ph = pl->head->next ;
    }
    ph->entry= e ; 
}

void TraverseList(List *pl,void (*pf) (ListEntry ) ){
    ListNode *ph = pl->head ;
    while (ph)
    {
        (*pf)(ph->entry) ;
        ph = ph->next ;
    }
    
    
}