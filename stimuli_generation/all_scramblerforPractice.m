cd('C:\Users\stweis\Dropbox\Penn Post Doc\Arrows_VVA\Extra_Stimuli\');
mkdir('scrambled');
files = dir('*jpg*');
temp = struct2cell(files);
names = temp(1,:)';


cd('scrambled');


for i=1:length(names)
    name = mat2str(cell2mat(names(i)));
    name = name(2:end-1);
    phase_scrambler('C:\Users\stweis\Dropbox\Penn Post Doc\Arrows_VVA\Extra_Stimuli\',name);
end