from __future__ import division, print_function
import os
import soundfile as sf
import pyworld as pw


def main():
    x, fs = sf.read('hearme/luogz1np.wav')  #音色的文件
    tx, tfs = sf.read('hearme/sxgz1.wav')  #提取f0的文件
    _f0, t = pw.harvest(x, fs)  #提取歌声的f0
    f0 = pw.stonemask(x, _f0, t, fs)  #原来音色的f0
    sp = pw.cheaptrick(x, f0, t, fs)  #原来音色的频谱
    ap = pw.d4c(x, f0, t, fs)  #原来音色的ap
    y = pw.synthesize(f0, sp, ap, fs, pw.default_frame_period)
    sf.write('original_re_synth.wav', y, fs)
    _f0_h, t_h = pw.harvest(tx, tfs)  #提取出的f0
    f0_h = pw.stonemask(tx, _f0_h, t_h, tfs)  #提取合成用的f0
    #frequencyScale=1.0594630**12 #一个八度
    for i in range(0, len(f0_h)):
        #f0_h[i]*=frequencyScale #升调
        #高音突刺处理
        if f0_h[i] > 550.01:
            f0_h[i] = f0_h[i - 1]  #换用t也就是tuned采样的
    y_h = pw.synthesize(f0_h, sp, ap, fs, pw.default_frame_period)
    sf.write('combined.wav', y_h, fs)
    print('Please check "test" directory for output files')


if __name__ == '__main__':
    main()