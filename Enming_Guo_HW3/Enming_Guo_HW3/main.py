def find(i):
    if Used[i]==0:
        return;
    else:
        find(i-weight[Used[i]]);
        Item.append(Used[i]);

if __name__ == '__main__':

    f = open("KP_input_1.txt")
    lines = f.readline();
    weight=[0];
    value=[0];
    W=int(lines);
    cnt=0;
    while True:
        lines=f.readline();
        if not lines:
            break;
        else:
            cnt=cnt+1;
            temp=lines.split(" ");
            weight.append(int(temp[1]));
            temp[2]=temp[2].replace("\n","");
            value.append(int(temp[2]));
    global Opt
    Opt=[0]*(W+1);
    global Used
    Used=[0]*(W+1);
    global Item
    Item=[];
    for i in range(W+1):
        if i==0:
            continue;
        else:
            Maxx=0;
            id=0;
            for j in range(1,cnt+1):
                if(weight[j]<=i):
                    if(Opt[i-weight[j]]+value[j]>Maxx):
                        Maxx=max(Maxx,Opt[i-weight[j]]+value[j]);
                        id=j;
            Opt[i]=Maxx;
            Used[i]=id;
    print(Opt[W]);
    find(W);
    for i in range(len(Item)):
        if(i!=0):
            print(" ",end="");
        print(Item[i],end="");
    f.close()
    
