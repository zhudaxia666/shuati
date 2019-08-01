'''
给定一个数组arr，和一个数num，请把小于nums的数放在数组的左边，等于nums的数放在数组的中间，大于nums的数放在数组的右边
要求时间空间复杂度为o(1),时间复杂度o（n）
'''
'''
思路和第一个相似。只不过要设置两个指针，前指针less和后指针more，less在从前面开始，more从后面开始，0-less局域表示小于nums的区域，初始值less为-1，more为n
如果当前遍历的元素cur小于nums，将less后一个元素与cur交换，less加1
如果当前元素等于nums，将继续遍历
如果当前遍历的元素cur大于nums，将more-1后与cur交换，然后在判断交换后的cur值与nums的关系

'''
def code(arr,l,r,num):
    less=l-1
    more=r+1
    cur=l
    while cur<more:
        if arr[cur]<num:
            less+=1
            arr[cur],arr[less]=arr[less],arr[cur]
            cur+=1
        elif arr[cur]>num:
            more-=1
            arr[cur],arr[more]=arr[more],arr[cur]
        else:
            cur+=1
    return less+1,more-1#返回的是等于区域的左右边界
