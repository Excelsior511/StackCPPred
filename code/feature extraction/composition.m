
rcem=xlsread('rcem.xlsx','Sheet1');

textdata = importdata('./dataset/ID-cpp.txt')

num=length(textdata);

aa='ACDEFGHIKLMNPQRSTVWY'
output1=[];
for i=1:num
    i

    
    if mod(i,2)==0
%         seq = textdata.textdata{i};
        seq = textdata{i};
        len=length(seq);
        output = [];
        seqmatrix = zeros(len,20);
        for ii=1:len
            pos=strfind(aa,seq(ii));
            if length(pos)==1
            seqmatrix(ii,:)=rcem(pos,:);
            end
        end
        
        for j=1:20
            pos=strfind(seq,aa(j));
            %     if isempty(pos)==0
            posdata=seqmatrix(pos,:);
            if length(pos)==1
                d(1:20)=0;
                posdata=[posdata;d];
            end
            t=sum(posdata);
            if length(pos)==0
                t(1:20)=0;
            end
            
            output=[output,t];
            %     end
        end
        
        output1=[output1;output/len];
    end
end

pss_com_ID311=output1;
save pss_com_ID311 pss_com_ID311

% save com_400dim output1

