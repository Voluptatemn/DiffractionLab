import numpy as np

gn1_2 = [0.5, 0.6]
gn2_2 = [0.9, 1.0]
gn3_2 = [1.4, 1.6]
gn4_2 = [2.0, 2.0]
rn1_2 = [0.6, 0.6]
rn2_2 = [1.2, 1.1]
rn3_2 = [1.9, 1.7]
rn4_2 = [2.5, 2.5]


def average(n): # output error and mean
    std3r = np.std(n)
    mean = np.mean(n)
    return (std3r, mean)
 
sz = 1000
d = 198.6
d_err = 0.1
dnormal = np.random.normal(d, d_err, sz)

def nullangle(n): # return the null angle
    std = average(n)[0]
    mean = average(n)[1]
    nnormal = np.random.normal(mean, std, sz)
    theta = np.arctan(nnormal/dnormal)
    return theta
    

def wavelength_ratio(gn, rn): # compare the wavelength
    gnull = nullangle(gn)
    rnull = nullangle(rn)
    ratio = np.sin(gnull)/np.sin(rnull)
    return ratio

def wavelength(n): # finding the wavelength; needs to divide by the any nulls 
    a = 0.013716 # thickness of the tape
    a_err = 0.000001 # thickness error of the tape
    anormal = np.random.normal(a, a_err, sz)    
    p = 0.0075 # thickness of the paper
    p_err = 0.0003 # thickness error of the paper
    pnormal = np.random.normal(p, p_err, sz)
    wave = (anormal + pnormal) * np.sin(nullangle(n)) 
    return wave

wavelength_ratio_final = (wavelength_ratio(gn1_2, rn1_2) + wavelength_ratio(gn2_2, rn2_2) + wavelength_ratio(gn3_2, rn3_2) + wavelength_ratio(gn4_2, rn4_2)) / 4

print(average(wavelength_ratio_final))

greenWavelength = average((wavelength(gn1_2) + wavelength(gn2_2) / 2 + wavelength(gn3_2) / 3 + wavelength(gn4_2) / 4) / 4)
RedWaveLength = average((wavelength(rn1_2) + wavelength(rn2_2) / 2 + wavelength(rn3_2) / 3 + wavelength(rn4_2) / 4) / 4)

print(greenWavelength)
print(RedWaveLength)


# -- accepted value of wavelength ratio
g_real = 0.0000526
g_err = 0.0000006
r_real = 0.000065
r_err = 0.000002
gnormal = np.random.normal(g_real, g_err, sz)
rnormal = np.random.normal(r_real, r_err, sz)
w_real = gnormal / rnormal

# Percent error
perr = np.abs(average(wavelength_ratio_final)[1] - average(w_real)[1]) / average(w_real)[1] * 100
print('Measurement of wavelength ratio is accurate to %.2f%%'%perr)

# z-score
from scipy.special import erf, erfc

z = np.abs(average(wavelength_ratio_final)[1] - average(w_real)[1]) / average(wavelength_ratio_final)[0]
# Can reject the hypothesis (that the measurement is consistent with
# the accepted value) with calculated confidence (2-sided)
pval = erfc(z/np.sqrt(2))

confidence = erf(z/np.sqrt(2)) * 100
print('Measurement of wavelength ratio is inconsistent with accepted value with confidence of %.2f%%'%confidence)

perrGreen = np.abs(greenWavelength[1] - average(gnormal)[1]) / average(gnormal)[1] * 100
print('Measurement of the absolute green wavelength is accurate to %.2f%%'%perrGreen)

zGreen = np.abs(greenWavelength[1] - average(gnormal)[1]) / greenWavelength[0]
pvalGreen = erfc(zGreen/np.sqrt(2))
confidenceGreen = erf(zGreen/np.sqrt(2)) * 100
print('Measurement of the absolute green wavelength is inconsistent with accepted value with confidence of %.2f%%'%confidenceGreen)

perrRed = np.abs(RedWaveLength[1] - average(rnormal)[1]) / average(rnormal)[1] * 100
print('Measurement of the absolute red wavelength is accurate to %.2f%%'%perrRed)

zRed = np.abs(RedWaveLength[1] - average(rnormal)[1]) / RedWaveLength[0]
pvalGreen = erfc(zRed/np.sqrt(2))
confidenceRed = erf(zRed/np.sqrt(2)) * 100
print('Measurement of the absolute red wavelength is inconsistent with accepted value with confidence of %.2f%%'%confidenceRed)





    
    
    