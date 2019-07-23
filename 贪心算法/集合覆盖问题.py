''''
假设举办广播节目，要让全美50个州的听众都收到，决定在哪些广播台播出，力图在尽可能少的广播台播出
思路：
1.选出这样一个广播台，即它覆盖最多的未覆盖州，
2.重复上一步，直到覆盖所有的州
'''
#创建一个列表，包含要覆盖的州
states_needed=set(['mt','wa','or','id','nv','ut','ca','az'])
stations={}
stations['kone']=set(['id','nv','ut'])
stations['ktwo']=set(['wa','id','mt'])
stations['kthree']=set(['or','nv','ca'])
stations['kfour']=set(['nv','ut'])
stations['kfive']=set(['ca','az'])

#存储最终选择的广播台
final_stations=set()
while states_needed:
    best_station=None#存储覆盖最多的未覆盖州的广播台
    states_covered=set()#包含该广播台覆盖的所有未覆盖州
    for station,states_for_station in stations.items():
        covered=states_needed & states_for_station
        if len(covered)>len(states_covered):
            best_station=station
            states_covered=covered
    states_needed-=states_covered
    final_stations.add(best_station)
print(final_stations)
    

