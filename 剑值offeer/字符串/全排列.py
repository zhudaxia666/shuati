'''
将指针指向第一个元素时，它可以使其本身a，也可以和b,c进行交换故有三种可能，当第一个元素a确定以后，指针移向第二个位置，第二个位置可以
和其本身b以及其后的c进行交换，又可以形成两种排列，当指针指向第三个元素c的时候，这个时候其后没有元素了，此时，则确定一组排列，输出。但是
后要把数组恢复为原来的样子
也可以使用itertools模板，
import itertools
list(itertools.permutations(arr))
'''
def permutations(arr,position,end):
    if position==end:
        print(arr)
    else:
        for index in range(position,end):
            arr[index],arr[position]=arr[position],arr[index]
            permutations(arr,position+1,end)
            arr[index],arr[position]=arr[position],arr[index]
arr=[1,2,3]
permutations(arr,0,len(arr))