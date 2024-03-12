import math

def calc_log(lista):
    log = []
    for x in lista:
        log.append(round(20 * math.log10(x), 2))
    return log

VsA = 2
VsB = 14
VsC = 400
VsD = 8

#wartości w mv
V0A = [24.6, 44.8, 65, 122, 208, 278, 308, 344, 346, 337, 300, 237, 226, 82, 58, 41, 28]
V0B = [50, 86, 120, 195, 255, 278, 285, 289, 289, 288, 285, 274, 237, 182, 142, 106, 74]
V0C = [90, 148, 195, 288, 344, 362, 367, 368, 367, 367, 367, 368, 368, 368, 365, 360, 346]
V0D = [1.2, 1.4, 1.7, 2.8, 5.8, 9.8, 14, 54, 90, 124, 250, 271, 277, 280, 268, 238, 205, 166, 122]

KuA = [v/VsA for v in V0A]
KuB = [round(v/VsB, 2) for v in V0B]
KuC = [round(v/VsC, 2) for v in V0C]
KuD = [round(v/VsD, 2) for v in V0D]

#print("KuA:", KuA)
#print("KuB:", KuB)
#print("KuC:", KuC)
#print("KuD:", KuD)

logA = calc_log(KuA)
logB = calc_log(KuB)
logC = calc_log(KuC)
logD = calc_log(KuD)
print(logA)

