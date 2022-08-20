#include "global.h"

typedef struct listNode
{
    ListEntry  entry ; 
    struct listNode * next ; 
}ListNode;


typedef struct list
{
    int size ; 
    ListNode *head ; 
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


