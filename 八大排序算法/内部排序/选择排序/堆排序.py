# 
# def swap(a,b):
#     temp=a
#     a=b
#     b=temp

def sift_dowm(input_list,start,end):
   
    while True:
        left_child=2*start+1#左孩子的节点下标
        if left_child>end:
            break
        #当右孩子存在时，且左孩子小于右孩子
        if left_child+1<=end and input_list[left_child+1]>input_list[left_child]:
            left_child+=1
        if input_list[left_child]>input_list[start]:#左右孩子大于父节点
            input_list[start],input_list[left_child]=input_list[left_child],input_list[start]
            
            start=left_child #交换之后以交换子节点为根的对可能不是大顶锥，需要重新调整
        else:#若父节点大于左右节点，则退出循环
            break
        print(">>",input_list)

def heap_sort(input_list):

    for i in range(len(input_list)//2-1,-1,-1):
        sift_dowm(input_list,i,len(input_list)-1)#从最后一个有孩子的节点开始往上调整
    print("初始化大堆的结果：",input_list)
    #交换堆顶与堆尾
    for head in range(len(input_list)-1,0,-1):
        input_list[head],input_list[0]=input_list[0],input_list[head]
        sift_dowm(input_list,0,head-1) #从上往下调整大椎

'''
最小堆
方法一：
从根节点（index = 0）遍历到最后一个拥有子节点的节点（index = N//2 -1），将父节点与其子节点值作比较
必要时进行交换即可。完成一次上述过程后就能完成最底层节点的归位了。元素个数为N的二叉树层数为ceil(log2n),
因此一共执行floor(log2n)次上述过程就能实现最小堆的建堆了。
'''
import math
def heap(li):
    n=len(li)
    for i in range(0,int(math.log(n,2))):
        for j in range(0,n//2):
            if 2*j+2<n and li[2*j+2]<li[2*j+1]:
                k=2*j+2
            else:
                k=2*j+2
            if li[k]<li[j]:
                li[k],li[j]=li[j],li[k]
    print(li)

#方法二
# 思路还是一样，这次从最后一个拥有子节点的节点向上遍历
# def heap2(li,root):
#     if 2*root+1<len(li):
#         if 2*root+2<len(li) and li[2*root+2]<li[2*root+1]:
#             k=2*root+2
#         else:
#             k=2*root+1
#         if li[k]<li[root]:
#             li[k],li[root]=li[root],li[k]
#             heap2(li,k)
# for i in range(len(li)//2-1,-1,-1):
#     heap2(li,i)


if __name__ == "__main__":
    a=[16,7,3,20,17,8]
    heap(a)
    # print(a)



# public static void heapsort(int[] num){
#         for(int i=num.length/2-1;i>=0;i--){//从第一个非叶子结点开始初始堆
#          adjustHeap(num,i,num.length);
#         }
#         for(int j=num.length-1;j>=0;j--){//从第一个结点开始调整堆
#             swap(num,0,j);
#             adjustHeap(num,0,j);
#         }

# }
# //初始化或者调整堆
# public static void adjustHeap(int []num,int i,int length){
#         int temp = num[i];
#         for(int k=i*2+1;k<length;k=k*2+1){
#             if(k+1<length&&num[k]<num[k+1]){
#                 k++;
#             }
#             if(num[k]>temp){
#                 num[i] = num[k];
#                 i = k;
#             }else{
#                 break;
#             }
#         }
#         num[i] = temp;
# }
# public static void swap(int []num,int a,int b){
#         int temp = num[a];
#         num[a] = num[b];
#         num[b] = temp;
# }
    


