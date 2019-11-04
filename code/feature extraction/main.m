

path('E:/SVM-RFE-CBR-v1.3',path);
path('E:/360files/libsvm-3.18/matlab',path);




load feature_PsePSSM_GT427
load feature_RCEM_DWT_GT427
load pss_com_gt427


load feature_PsePSSM_ID311
load feature_RCEM_DWT_ID311
load pss_com_ID311

X=[feature_PsePSSM_GT427,feature_RCEM_DWT_GT427,pss_com_gt427];

[Train_matrix,PS] = mapminmax(X');
train_data = Train_matrix';


param.kerType = 2;
param.rfeC = 16;
param.rfeG = 0.0078;
param.useCBR = true;
param.Rth = 0.9;
[bestacc,best_dim,ftRank,ftScore]=optem_Dim(train_data,label,param);
aftRank=ftRank';

mappedX=ft_select(train_data, ftRank,best_dim);

[bestacc,bestc,bestg]=SVMcg(label,mappedX,-5,5,-5,5,5,1,1,1,2 )

label_mappedX=[label,mappedX];

save all_3_optemDim label_mappedX


 
 
 


