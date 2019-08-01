def core(nums,k):
    # global res
    if not nums:
        return
    res[k].append(nums[0])
    left=[]
    right=[]
    for i in range(1,len(nums)):
        if nums[i]>nums[0]:
            right.append(nums[i])
        else:
            left.append(nums[i])
    core(left,k+1)
    core(right,k+1)

if __name__ == "__main__":
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    n=len(arr)
    res=[[] for _ in range(n)]
    core(arr,0)
    new_res=[]
    for r in res:
        if not r:
            break
        new_res.extend(r)
    # print(res)
    print(' '.join([str(x) for x in new_res]))