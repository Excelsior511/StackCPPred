
function F=EstraggoConDWT(I,Nscale)

F=[];
CA=I;
for i=1:Nscale
    [CA,CD] = dwt(CA,'bior3.3');
    CC=dct(CA);
    F=[F CC(1:5) min(CA) max(CA) mean(CA) std(CA) min(CD) max(CD) mean(CD) std(CD)];
end