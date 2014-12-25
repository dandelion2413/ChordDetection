tempWaveFile=[tempname, '.wav'];
tickAdd(wObj, cBeat, tempWaveFile);
%tickAdd(wObj, Onsets, tempWaveFile);
dos(['start ', tempWaveFile]);
