function [bestacc,best_dim,ftRank,ftScore]=optem_Dim(XX,label,param)

[ftRank,ftScore] = ftSel_SVMRFECBR(XX,label,param);

cg_str = ['-c ' num2str(param.rfeC) ' -g ' num2str(param.rfeG) ' -b 1 ' '-v 5'];

feature_dim = size(XX,2);

acc_list=[];
dim_list=[];

for i=10:1:feature_dim
	X_S=ft_select(XX, ftRank,i);
	model1=svmtrain(label,X_S,cg_str);
	acc_list = [acc_list,model1];
	dim_list = [dim_list,i];
	str_dd = ['dim: ' num2str(i) ' acc: ' num2str(model1)];
	str_dd
end
max_y = max(acc_list);
max_x = dim_list(find(acc_list==max_y));


hold on
	plot(dim_list,acc_list,'b','LineWidth',1.5);
	
%	plot([max_x max_x],[0 max_y],'r:','LineWidth',1.5);
%	plot([0 max_x],[max_y max_y],'r:','LineWidth',1.5);

grid on;ll=legend('ACC');
    xlabel('The dimensions of feature');ylabel('Accuracy(%)');
    box on;
    grid off;
set(get(gca,'XLabel'),'FontSize',18);
set(get(gca,'YLabel'),'FontSize',18);
set(gca,'FontSize',10);
set(ll,'FontSize',10);

[CC,II]=max(acc_list);
bestacc = CC;
best_dim = dim_list(II);
