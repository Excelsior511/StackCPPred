function [bestacc,best_dim]=optem_Dim_mrmr(XX,label,param,alpha)

DD = discretize_mrmr(XX, alpha);

cg_str = ['-c ' num2str(param.rfeC) ' -g ' num2str(param.rfeG) ' -b 1 ' '-v 3'];

feature_dim = size(XX,2);
[Fea] = mrmr_mid_d(DD,label,feature_dim);
acc_list=[];
dim_list=[];

for i=10:2:feature_dim
	sls_fea = Fea(1,1:i);
	X_S=mrmr_select(XX, sls_fea);
	model1=svmtrain(label,X_S,cg_str);
	acc_list = [acc_list,model1];
	dim_list = [dim_list,i];
	str_dd = ['dim: ' num2str(i) ' acc: ' num2str(model1)];
	str_dd
end

hold on
	plot(dim_list,acc_list);
grid on;ll=legend('ACC');
    xlabel('The dimension of feature');ylabel('Accuracy(%)');
    box on;
    grid off;
set(get(gca,'XLabel'),'FontSize',18);
set(get(gca,'YLabel'),'FontSize',18);
set(gca,'FontSize',10);
set(ll,'FontSize',10);

[CC,II]=max(acc_list);
bestacc = CC;
best_dim = dim_list(II);
