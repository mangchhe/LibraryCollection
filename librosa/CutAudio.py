import librosa
import os
import numpy as np
import matplotlib.pyplot as plt

#mp3 = r'C:\Users\mangc\Desktop\Test 4_Part2.mp3'

wav = r'C:\Users\mangc\Desktop\Test 4_Part2 (online-audio-converter.com).wav'

file_dir, file_id = os.path.split(wav)

print('file_dir : ', file_dir)
print('file_id : ', file_id)

y, sr = librosa.load(wav)
y = y[:round(len(y)/2)]
time = np.linspace(0, len(y)/sr, len(y))

fig, ax1 = plt.subplots()
ax1.plot(time, y, color = 'b', label = 'speech waveform')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time [s]')
plt.title(file_id)
plt.savefig(file_id+'.png')
librosa.output.write_wav('half_file.wav',y,sr)
plt.show()