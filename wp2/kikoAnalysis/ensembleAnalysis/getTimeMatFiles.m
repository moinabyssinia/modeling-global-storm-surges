%to change datenum matlab time to normal time %

%load files 
clear;

dir_in = "G:\\05_era5\\kikoStuff\\ensembleData";
dir_out = "G:\\05_era5\\kikoStuff\\ensDataTimed";
chdir(dir_in);

ensList = dir('*.mat');

for ii = 1:1
  ensName = strsplit(ensList(ii).name, '.mat')(1)
  
  %load file 
  load(ensList(ii).name)
  ensTime = datevec(time);
  clearvars dir_in ensList ii
  
  chdir(dir_out);
  
endfor  
  