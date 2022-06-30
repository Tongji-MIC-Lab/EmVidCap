clear;
clc;

original_split='/data/tpj/tpj/S2VT/videocap-datasets/Youtube_senti/splits/';

split_train=[original_split,'train'];
%split_val=[original_split,'val'];
split_test=[original_split,'test'];

train_folder_list=dir(split_train);
%val_folder_list=dir(split_val);
test_folder_list=dir(split_test);

[mtrain_folder,ntrain_folder]=size(train_folder_list);
%[mval_folder,nval_folder]=size(val_folder_list);
[mtest_folder,ntest_folder]=size(test_folder_list);

fidtrain=fopen([original_split,'train3.txt'],'w');
%fidval=fopen([original_split,'val.txt'],'w');
fidtest=fopen([original_split,'test3.txt'],'w');

for i=3:mtrain_folder
    tmp_path1=[split_train,'/',train_folder_list(i).name];
    video_frame_list=dir(tmp_path1);
    [mframe,nframe]=size(video_frame_list);
    
    k=1;
    for j=3:mframe 
        fprintf('now is disposing the %d/%d th video, %d/%d th frame!\n',i-2,mtrain_folder-2,j-2,mframe-2);
      
        frame_name=video_frame_list(j).name;
        [mname,nname]=size(frame_name);
        t=1;
        x=0;
        while(x~=2 && t<nname)
            if frame_name(t)=='_'
                x=x+1;
            end
            t=t+1;
        end
        name_pre=frame_name(1:t-1);                  
       
        
        fprintf(fidtrain,'%s %d\n',[original_split,'train','/',train_folder_list(i).name,'/',name_pre,num2str(k),'.jpg'],0);
        k=k+1;
    
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%for i=3:mval_folder
%    tmp_path1=[split_val,'/',val_folder_list(i).name];
%    video_frame_list=dir(tmp_path1);
%    [mframe,nframe]=size(video_frame_list);
%    
%    k=1;
%    for j=3:mframe 
%        fprintf('now is disposing the %d/%d th video, %d/%d th frame!\n',i-2,mval_folder-2,j-2,mframe-2);
%      
%        frame_name=video_frame_list(j).name;
%        [mname,nname]=size(frame_name);
%        t=1;
%        x=0;
%        while(x~=2 && t<nname)
%            if frame_name(t)=='_'
%                x=x+1;
%            end
%            t=t+1;
%        end
%        name_pre=frame_name(1:t-1);
%                          
%        fprintf(fidval,'%s %d\n',[original_split,'val','/',val_folder_list(i).name,'/',name_pre,num2str(k),'.jpg'],0);
%        k=k+1;
%    
%    end
%end
        
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for i=3:mtest_folder
    tmp_path1=[split_test,'/',test_folder_list(i).name];
    video_frame_list=dir(tmp_path1);
    [mframe,nframe]=size(video_frame_list);
    
    k=1;
    for j=3:mframe 
        fprintf('now is disposing the %d/%d th video, %d/%d th frame!\n',i-2,mtest_folder-2,j-2,mframe-2);
      
        frame_name=video_frame_list(j).name;
        [mname,nname]=size(frame_name);
        t=1;
        x=0;
        while(x~=2 && t<nname)
            if frame_name(t)=='_'
                x=x+1;
            end
            t=t+1;
        end
        name_pre=frame_name(1:t-1);       
        
        fprintf(fidtest,'%s %d\n',[original_split,'test','/',test_folder_list(i).name,'/',name_pre,num2str(k),'.jpg'],0);
        k=k+1;
    
    end
end
        







