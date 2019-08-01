''''
使用数组表示的堆，第index个索引的左子树是2*index+1，右子树是2*index+2，接下来是是建最大堆得过程
'''
def heapsort(arr):
    if not arr or len(arr)<2:
        return
    for i in range(1,len(arr)):
        heapInsert(arr,i)    #这是建堆得过程
    #下面是排序的过程，需要将最大堆中堆顶元素与最后一个节点互换，然后堆长度减1
    size=len(arr)
    arr[0],arr[size-1]=arr[size-1],arr[0]
    size-=1
    while size>0:
        heapify(arr,0,size-1)




def heapInsert(arr,index):
    while arr[index]>arr[(index-1)//2]:
        arr[index],arr[(index-1)//2]=arr[(index-1)//2],arr[index]
        index=(index-1)//2
