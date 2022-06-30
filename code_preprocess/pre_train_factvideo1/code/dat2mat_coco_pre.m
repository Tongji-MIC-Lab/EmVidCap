
clear;
clc;

type='single';
filename='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits_pre_train/feature_resnet_coco_pre/test/test_pool5_coco_pre.dat';
savedir='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits_pre_train/feature_resnet_coco_pre/test/';

if ~exist('type', 'var') || isempty(type)
   type = 'single';
end
fid = fopen(filename, 'r');
rows = fread(fid, 1, type);
cols = fread(fid, 1, type);
data = fread(fid, rows * cols, type);
fclose(fid);
data = reshape(data, rows, cols);
switch type
  case 'int32'
       data = int32(data);
  case 'single'
       data = single(data); 
        
end

save([savedir,'test_pool5_coco_pre_mat'],'data');
