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

if __name__ == "__main__":
    a=[16,7,3,20,17,8]
    heap_sort(a)
    print(a)


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
    


