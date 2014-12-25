waveFile = 'C:\Users\Eric\Desktop\Google ¶³ºÝµwºÐ\Jang\MATLAB-Chroma-Toolbox_2.0\Let_It_Be.wav';
%waveFile = 'C:\Users\Eric\Desktop\Google ¶³ºÝµwºÐ\Jang\MATLAB-Chroma-Toolbox_2.0\Shots.wav';
wObj=waveFile2obj(waveFile);
btOpt=btOptSet;
btOpt.type='constant';		% 'constant' or 'time-varying'
showPlot=0;			% 1 for plotting intermdiate results, 0 for not plotting
cBeat=beatTrack(wObj, btOpt, showPlot);
