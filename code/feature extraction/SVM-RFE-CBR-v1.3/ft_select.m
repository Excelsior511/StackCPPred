function X_S=ft_select(X, feature_select_index,dim_s)

X_S=[];

n_Features_Selected = size(feature_select_index,2);

for i=1:dim_s
	index_f = feature_select_index(i);
	F = X(:,index_f);
	X_S(:,i) = F;

end