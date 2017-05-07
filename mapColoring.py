#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-

'''
variables
'''
provinces = ['Beijing','Shanghai','Tianjing','Chongqing','Taiwan',
            'Xinjiang','Xizang','Ningxia','Inner Mongol','Guangxi',
            'Shaanxi','Gansu','Qinghai','Sichuan','Yunnan','Guizhou',
            'Hunan','Hubei','Shanxi','Shandong','Henan','Hebei',
            'Jiangsu','Anhui','Zhejiang','Jiangxi','Fujian','Guangdong',
            'Hainan','Heilongjiang','Jilin','Liaoning','Macau','HongKong']
neighbors = {
        'Beijing' : ['Tianjing','Hebei'],                                                                       #0
        'Shanghai': ['Jiangsu','Zhejiang'],                                                                     #1
        'Tianjing': ['Beijing','Hebei'],                                                                        #2
        'Chongqing':['Sichuan','Guizhou','Hunan','Hubei','Shaanxi'],                                            #3
        'Taiwan'  : ['Fujian'],                                                                                 #4
        'Xinjiang':['Gansu','Qinghai','Xizang'],                                                                #5
        'Xizang'   : ['Xinjiang','Qinghai','Sichuan','Yunnan'],                                                 #6
        'Ningxia' : ['Inner Mongol','Gansu','Shaanxi'],                                                         #7
        'Inner Mongol':['Gansu','Ningxia','Shaanxi','Shanxi','Hebei','Liaoning','Jilin','Heilongjiang'],        #8
        'Guangxi' : ['Yunnan','Guizhou','Hunan','Guangdong'],                                                   #9
        'Shaanxi' : ['Inner Mongol','Ningxia','Gansu','Sichuan','Chongqing','Hubei','Henan','Shanxi'],          #10
        'Gansu'   : ['Xinjiang','Qinghai','Sichuan','Ningxia','Shaanxi','Inner Mongol'],                        #11
        'Qinghai' : ['Xinjiang','Xizang','Gansu','Sichuan'],                                                    #12
        'Sichuan' : ['Qinghai','Xizang','Yunnan','Guizhou','Chongqing','Shaanxi','Gansu'],                      #13
        'Yunnan'  : ['Xizang','Sichuan','Guizhou','Guangxi'],                                                   #14
        'Guizhou' : ['Sichuan','Chongqing','Hunan','Guangxi','Yunnan'],                                         #15
        'Hunan'   : ['Guizhou','Chongqing','Hubei','Jiangxi','Guangdong','Guangxi'],                            #16
        'Hubei'   : ['Hunan','Chongqing','Shaanxi','Henan','Anhui','Jiangxi'],                                  #17
        'Shanxi'  : ['Inner Mongol','Shaanxi','Henan','Hebei'],                                                 #18
        'Shandong': ['Hebei','Henan','Anhui','Jiangsu'],                                                        #19
        'Henan'   : ['Hebei','Shanxi','Shaanxi','Hubei','Anhui','Shandong'],                                    #20
        'Hebei'   : ['Inner Mongol','Shanxi','Henan','Shandong','Beijing','Tianjing','Liaoning'],               #21
        'Jiangsu' : ['Shandong','Anhui','Zhejiang','Shanghai'],                                                 #22
        'Anhui'   : ['Shandong','Henan','Hubei','Jiangxi','Zhejiang','Jiangsu'],                                #23
        'Zhejiang': ['Shanghai','Jiangsu','Anhui','Jiangxi','Fujian'],                                          #24
        'Jiangxi' : ['Anhui','Hubei','Hunan','Guangdong','Fujian','Zhejiang'],                                  #25
        'Fujian'  : ['Zhejiang','Jiangxi','Guangdong','Taiwan'],                                                #26
        'Guangdong':['Fujian','Jiangxi','Hunan','Guangxi','Macau','HongKong'],                                  #27
        'Hainan'  : ['Guangdong'],                                                                              #28
        'Heilongjiang':['Inner Mongol','Jilin'],                                                                #29
        'Jilin'   : ['Heilongjiang','Inner Mongol','Liaoning'],                                                 #30
        'Liaoning': ['Jilin','Inner Mongol','Hebei'],                                                           #31
        'Macau'   : ['Guangdong'],                                                                              #32
        'HongKong': ['Guangdong']                                                                               #33    
}

colors = ['red', 'blue', 'green','yellow'] # 0 1 2 3
records = [[0,1,2,3] for i in range(34)]
N = 34
total = 0

'''
functions
'''
def checkLeastConstraintLeft():
    temp = [-1,4]
    for i in range(34):
        if isinstance(records[i],int):
            continue

        if len(records[i])<temp[1]:
            temp[0] = i
            temp[1] = len(records[i])
        elif len(records[i])==temp[1] and temp[0]==-1:
            temp[0] = i
    return temp

def outputResult():
    global total
    total+=1
    for i in range(N):
        if records[i]==0:
            print('R', end=' ')
        elif records[i]==1:
            print('G', end=' ')
        elif records[i]==2:
            print('B', end=' ')
        else:
            print('Y', end=' ')
    print()
    return

def csp():
    x = checkLeastConstraintLeft()
    if x[0]==-1:
        outputResult()
        return

    xName = provinces[x[0]]
    currentColors = records[x[0]][:]

    # color current province by the remaining color
    for i in range(x[1]):
        records[x[0]] = currentColors[i]

        recoverTemp = []

        # forward checking: remove the conflict color from neighbor
        for neighbor in neighbors[xName]:
            nIndex = provinces.index(neighbor)
            if isinstance(records[nIndex],int):  # if province has already be colored
                if records[nIndex]==records[x[0]]: # can remove this condition
                    return
                else:
                    continue

            if records[x[0]] in records[nIndex]:
                recoverTemp.append(nIndex)
                records[nIndex].remove(records[x[0]])
            
            # when one neighbor color list become empty then return
            if ~isinstance(records[nIndex],int) and len(records[nIndex])==0:
                for i in recoverTemp:
                    records[i].append(records[x[0]])
                return
        
        # recursive
        csp()

        # recover data when backtarcking
        for i in recoverTemp:
            records[i].append(records[x[0]])
        
    records[x[0]] = currentColors[:]
    return



def main():
    csp()

if __name__ == "__main__":
    main()

