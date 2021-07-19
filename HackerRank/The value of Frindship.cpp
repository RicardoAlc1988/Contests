#include <bits/stdc++.h>
using namespace std;

#define intt long long int

class Disjoint_set{
    public:
    vector<intt> mydset;
    vector<intt> size;
    void Union(intt s,intt d){
        if(Find(s)!=Find(d)){
        size[Find(d)]+=size[Find(s)];
        mydset[Find(s)]=Find(d);
        }
    }
    intt Find(intt s){
        if(mydset[s]==s) return s;
        intt p=Find(mydset[s]);
        mydset[s]=p;
        return p;
    }
    vector<intt> get_parent(){
        vector<intt> ans;
        for(intt a=1;a<mydset.size();a++) if(mydset[a]==a) ans.push_back(size[a]);
        return ans;
    }
    Disjoint_set(intt n):mydset(n+1),size(n+1,1){
        for(intt a=1;a<=n;a++) mydset[a]=a;
    }
};

intt value(intt n){
    intt t1=n*(n+1)*(2*n+1);
    t1/=6;
    intt t2=n*(n+1);
    t2/=2;
    return t1-t2;
}

int main(){
    intt t;
    cin>>t;
    while(t--){
        intt s,d,n,m,ans=0,tmoves;
        cin>>n>>m;
        tmoves=m;
        Disjoint_set dset(n);
        while(m--){
            cin>>s>>d;
            dset.Union(s,d);
        }
        intt total=0,used=0;
        vector<intt> parent=dset.get_parent();
        sort(parent.begin(),parent.end(),greater<intt>());
        for(auto a:parent) {
            used+=(a-1);
            ans+=value(a)+total*(a-1);
            total+=(a*(a-1));
        }
        ans+=(tmoves-used)*total;
        cout<<ans<<endl;
    }
    return 0;
}