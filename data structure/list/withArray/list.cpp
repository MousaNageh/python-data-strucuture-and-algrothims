#include "list.h"

void CreateList(List *pl){
    pl->size = 0 ; 
}

int ListEmpty(List *pl){
    return !pl->size ; 
}
int ListFull(List * pl ){
    return pl->size == MAXLENGTH ; 
}
int ListSize(List *pl){
    return pl->size ; 
}
void DestoryList(List *pl){
    pl->size = 0 ;
}
/* 0 =< pos <=size */
void InsertList(int pos , ListEntry e ,List *pl){

    for(int i = pl->size - 1 ; i<=pos ; i--){
        pl->entry[i+1] = pl->entry[i] ;
    }
    pl->entry[pos] = e ;
    pl->size++ ;
}
/* 0 <=  pos <= size-1 */
void DeleteList(int pos ,List *pl){
    for(int i = pos+1 ; i<=pl->size-1 ; i ++){
        pl->entry[i-1] = pl->entry[i];
    }
    pl->size--;
}
/* 0 <=  pos <= size-1 */
void RetrieveList(int pos , ListEntry *e  ,List *pl){
    *e = pl->entry[pos] ; 
};
void ReplaceList(int pos , ListEntry e   ,List *pl){
    pl->entry[pos] = e ; 
}

void TraverseList(List *pl,void (*pf) (ListEntry ) ){
    for(int i =0 ; i < pl->size ; i++){
        (*pf)(pl->entry[i]) ;
    }
}