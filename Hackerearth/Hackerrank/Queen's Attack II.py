#include<stdio.h>
int main()
{
    int r,l,u,d,dlu,dld,dru,drd,n,k,rq,cq,ro,co;
    scanf("%d%d",&n,&k);
    scanf("%d%d",&rq,&cq);
    r=n-cq;
    l=cq-1;
    u=n-rq;
    d=rq-1;
    if(l<u)
    dlu=l;
    else {
    dlu=u;
    }
    if(l<d)
    dld=l;
    else {
    dld=d;
    }
    if(r<u)
    dru=r;
    else {
    dru=u;
    }
    if(r<d)
    drd=r;
    else {
    drd=d;
    }
    for(int i=1;i<=k;i++)
    {
        scanf("%d%d",&ro,&co);
        if(cq>co&&rq==ro)
        {
            if(cq-co-1<l)
            l=cq-co-1;
        }
        else if(cq<co&&rq==ro)
        {
            if(co-cq-1<r)
            r=co-cq-1;
        }
        else if(rq>ro&&cq==co)
        {
            if(rq-ro-1<d)
            d=rq-ro-1;
        }
        else if(rq<ro&&cq==co)
        {
            if(ro-rq-1<u)
            u=ro-rq-1;
        }
        else if(co<cq&&ro>rq)
        {
            if(cq-co==ro-rq)
            {
                if(ro-rq-1<dlu)
                dlu=ro-rq-1;
            }
        }
        else if(co<cq&&ro<rq)
        {
            if(cq-co==rq-ro)
            {
                if(rq-ro-1<dld)
                dld=rq-ro-1;
            }
        }
        else if(co>cq&&rq>ro)
        {
            if(co-cq==rq-ro)
            {
                if(rq-ro-1<drd)
                drd=rq-ro-1;
            }
        }
        else if(ro>rq&&co>cq)
        {
            if(co-cq==ro-rq)
            {
                if(ro-rq-1<dru)
                dru=ro-rq-1;
            }
        }
    }
    printf("%d",r+l+u+d+drd+dld+dru+dlu);
    return 0;
    
}
