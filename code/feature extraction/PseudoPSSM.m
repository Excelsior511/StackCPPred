function [ FEAT ] = PseudoPSSM( P, lg )
%PR: protein sequence
%P:PSSM matrix of the protein PR
%lg=max value of lag

n=size(P,1);%length of the protein
chanles=size(P,2);
for i=1:n
    ME(i)=mean(P(i,:));
    SD(i)=std(P(i,:));
    V(i,:)=(P(i,:)-ME(i))./SD(i);
end

V(find(isinf(V)))=0;
V(find(isnan(V)))=0;

AC=zeros(chanles,lg);
for lag=1:lg
    for i=1:chanles
        for j=1:n-lag
            AC(i,lag)=AC(i,lag)+(V(j,i)-V(j+lag,i))^2;
        end
        AC(i,lag)=AC(i,lag)./(n-lag);
    end
end
AC(find(isinf(AC)))=0;
AC(find(isnan(AC)))=0;
FEAT=[(AC(:)); mean(V)'];
FEAT=(FEAT(:));