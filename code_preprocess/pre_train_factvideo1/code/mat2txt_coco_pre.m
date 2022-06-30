
clear;
clc;

matfile='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits_pre_train/feature_resnet_coco_pre/test/test_pool5_coco_pre_mat.mat';

listfile='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits_pre_train/feature_resnet_coco_pre/test/test.txt';

fid=fopen('/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits_pre_train/feature_resnet_coco_pre/test/test_pool5_coco_pre_txt.txt','w');

load(matfile);
[pathlist,label]=textread(listfile,'%s %d\n');

[m,n]=size(data);

frame_path=pathlist{1};

for i=1:n
    fprintf('now is disposing the %d/%d th record!\n',i,n);
    frame_path=pathlist{i};
    t=0;
    k=1;
    while(t<10)
        if(frame_path(k)=='/')
            t=t+1;
        end
        k=k+1;
    end
    
    frame_name=frame_path(k:length(frame_path)-4);
    
    for j =1:m+1
        if(j==1)
            fprintf(fid,'%s,',frame_name);
        elseif(j==m+1)
            fprintf(fid,'%d\n',data(j-1,i));
        else
            fprintf(fid,'%d,',data(j-1,i));
        end
    end
end

fid(close);
    
