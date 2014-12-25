%function hit_rate=humming(file,onset_detection,melody_matching)
b=cputime;
file='filenames_20';
onset_detection = 'Proposed Onset Detection 2';
melody_matching = 'Hidden Markov Model Method';
t1=cputime-b;

%% best parameter setting
% clc;clear all;close all;
filenames=load(strcat(file,'.mat')); % filenames_15.mat
% filenames=filenames.filenames_20;
eval(['filenames=filenames.',file,';']);
length_file=length(filenames);
num_hitting=0;
MRR_number=0;
%%
tic
%filename_single=strcat(filenames{num_file},'.wav');

filename_single = 'Let_It_Be.wav';
%filename_single = 'Shots.wav';
% function [y t0 x0]=test(x,f,Fs)
[audioarray,Fs,bits] = wavread(filename_single); % 用"lugo_擁抱"作最佳切割; lugo_用心良苦 是個挑戰
audioarray = audioarray(:,1); % extract only one channel
x=audioarray';
%% cut the input into 10 pieces, in case different parts have different volume
interval = floor(length(x)/10);
XX = x(1:interval*10);
Time_Slot=[];
Onsets=[];
for i = 1:10
    x = XX(interval*(i-1)+1:interval*i);
    x=x-mean(x); % 為了使聲音訊號在振幅0的地方上下震動

    %% create a gaussian function to smooth signal
    gau = [1 5 10 15 25 15 10 5 1];   % create a gaussian function
    X = conv(x,gau/(sum(gau)));       % in order to smooth the waveform
    X = X(length(gau):end);           % extract the valid signal ; X: x after smoothing
    X = abs(X);              % where amplitude increases dramatically is attacking time

    %% Proposed Method 2
    ws=round(Fs*0.01); % window size = 80
    L=ceil(length(x)/ws); % how many windows, 2000
    amp = zeros(1,L);
    n1=1;
    for n = 1:ws:length(x)-ws % length(x) = 16000
        if n==L % won't happen??
            amp(n1)=max(X(n:end)); % sum(x(n:end))/(length(x)-n+1);
        else
            amp(n1) = max(X(n:n+ws-1)); % sum(x(n:n+ws-1))/ws;
        end
        n1=n1+1;
    end
    fil=[3,4,5,-1,-1,-1,-2,-2,-2,-3];
    lm1=7;lm2=2; % head and tail buffer
    amp=[0.01*ones(1,lm1),amp,0.01*ones(1,lm2)]; % add buffer in head and tail
    amp=amp/mean(amp)*0.2;
    amp=amp.^0.85;
    a1=conv(amp,fil); % filter
    threshold=1.5;
    a2=find(a1(lm1+1:lm1+n1-6)>threshold); % a2 records the index 
    onset_index=[a2(1)];
    ref=a2(1);
    
    for n=2:length(a2)
        if a2(n)-ref >= 15 % 15*80=1200點的距離以內不會有兩個onset time
            ref=a2(n);
            onset_index=[onset_index ref];
        end
    end    
    
onsets=(onset_index-1).*ws+1; % 還原成真正 onset 的 time index
time_slot=zeros(1,length(x));
time_slot(onsets)=max(x)+0.01;
%time_slot(onsets)=1;
Onsets = [Onsets (onsets+interval*(i-1))/Fs];
Time_Slot = [Time_Slot time_slot];
end

%% show the time segmentation result
figure;
time=(0:length(XX)-1)/Fs;
% plot(time,XX,time,Time_Slot,'r');
xlabel('Time (sec)');
ylabel('Magnitude');
dlmwrite('onsets.txt',Onsets');