#include "global.h" 
typedef struct list
{
    int size ; 
    ListEntry entry[] ;
}List;

void CreateList(List *);
int ListEmpty(List *);
int ListFull(List *);
int ListSize(List *);
void DestoryList(List *);
void InsertList(int , ListEntry ,List *);
void DeleteList(int ,List *);
void RetrieveList(int , ListEntry *  ,List *);
void ReplaceList(int , ListEntry   ,List *);
void TraverseList(List *,void (*) (ListEntry) );


