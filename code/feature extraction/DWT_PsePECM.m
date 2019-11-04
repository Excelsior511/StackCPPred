

textdata = importdata('./dataset/Uptake-efficiency benchmarking dataset/Uptake-cpp.txt');

rcem=xlsread('rcem.xlsx','Sheet1');

hang=length(textdata);

feature_RCEM_DWT_P = [];
feature_RCEM_DWT = [];
feature_PsePSSM = [];

for i=1:hang
    

    i
    if mod(i,2)==0
        sequence =textdata{i};
        s_length=length(sequence);
        sequence = upper(sequence);
        X = zeros(s_length,20);
        %     S(i)=s_length;
        for si=1:s_length
            if sequence(si)=='A'
                X(si,:) = rcem(1,:);
            end
            if sequence(si)=='C'
                X(si,:) = rcem(2,:);
            end
            if sequence(si)=='D'
                X(si,:) = rcem(3,:);
            end
            if sequence(si)=='E'
                X(si,:) = rcem(4,:);
            end
            if sequence(si)=='F'
                X(si,:) = rcem(5,:);
            end
            if sequence(si)=='G'
                X(si,:) = rcem(6,:);
            end
            if sequence(si)=='H'
                X(si,:) = rcem(7,:);
            end
            if sequence(si)=='I'
                X(si,:) = rcem(8,:);
            end
            if sequence(si)=='K'
                X(si,:) = rcem(9,:);
            end
            if sequence(si)=='L'
                X(si,:) = rcem(10,:);
            end
            if sequence(si)=='M'
                X(si,:) = rcem(11,:);
            end
            if sequence(si)=='N'
                X(si,:) = rcem(12,:);
            end
            if sequence(si)=='P'
                X(si,:) = rcem(13,:);
            end
            if sequence(si)=='Q'
                X(si,:) = rcem(14,:);
            end
            if sequence(si)=='R'
                X(si,:) = rcem(15,:);
            end
            if sequence(si)=='S'
                X(si,:) = rcem(16,:);
            end
            if sequence(si)=='T'
                X(si,:) = rcem(17,:);
            end
            if sequence(si)=='V'
                X(si,:) = rcem(18,:);
            end
            if sequence(si)=='W'
                X(si,:) = rcem(19,:);
            end
            if sequence(si)=='Y'
                X(si,:) = rcem(20,:);
            end
        end
        
        %%%%%%%%%%% DWT %%%%%%%%%%%%%%%%
        FF = GetDWT(X',4);
        feature_RCEM_DWT=[feature_RCEM_DWT;FF];
        %         feature_RCEM_DWT_P(i,:)=FF(:);
        
        %%%%%%%%%%%%%%%%%%%%%%%% DWT %%%%%%%%%%%%%%%%%%%%%%%%%
        
        %%%%%%%%%%%% PsePSSM %%%%%%%%%%%%%%%%
        FPseudo = PseudoPSSM(X, 30);
        feature_PsePSSM=[feature_PsePSSM;FPseudo'];
        
        %%%%%%%%%%%%%%%%%%%%%%%%% PsePSSM %%%%%%%%%%%%%%%%%%%%%%%%%
        
        
    end
    
end


feature_RCEM_DWT_Uptake187=feature_RCEM_DWT;
feature_PsePSSM_Uptake187=feature_PsePSSM;

save feature_RCEM_DWT_Uptake187 feature_RCEM_DWT_Uptake187;
save feature_PsePSSM_Uptake187 feature_PsePSSM_Uptake187;

