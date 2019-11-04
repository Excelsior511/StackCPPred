function [ACC,SN,Spec,PE,NPV,F_score,MCC] = roc( predict_label,test_data_label )
%ROC Summary of this function goes here
%   Detailed explanation goes here
l=length(predict_label);
TruePositive = 0;
TrueNegative = 0;
FalsePositive = 0;
FalseNegative = 0;
max_label = max(test_data_label);
min_label = min(test_data_label);
for k=1:l
    if test_data_label(k)==max_label & predict_label(k)==max_label  %真阳性
        TruePositive = TruePositive +1;
    end
    if test_data_label(k)==min_label & predict_label(k)==min_label %真阴性
        TrueNegative = TrueNegative +1;
    end 
    if test_data_label(k)==min_label & predict_label(k)==max_label  %假阳性
        FalsePositive = FalsePositive +1;
    end

    if test_data_label(k)==max_label & predict_label(k)==min_label  %假阴性
        FalseNegative = FalseNegative +1;
    end
end
%TruePositive
%TrueNegative
%FalsePositive
%FalseNegative
ACC = (TruePositive+TrueNegative)./(TruePositive+TrueNegative+FalsePositive+FalseNegative);
SN = TruePositive./(TruePositive+FalseNegative);

Spec = TrueNegative./(TrueNegative+FalsePositive);%

PE=TruePositive./(TruePositive+FalsePositive);

NPV = TrueNegative./(TrueNegative+FalseNegative);

F_score = 2*(SN*PE)./(SN+PE);

MCC= (TruePositive*TrueNegative-FalsePositive*FalseNegative)./sqrt(  (TruePositive+FalseNegative)...
    *(TrueNegative+FalsePositive)*(TruePositive+FalsePositive)*(TrueNegative+FalseNegative));
end