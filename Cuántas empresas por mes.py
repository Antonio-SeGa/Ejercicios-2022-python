# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
contE = 0;contF = 0;contM = 0;contA = 0;contMa = 0;contJ = 0;contJu = 0; contAg = 0;contS = 0;contO = 0;contN = 0;contD = 0

lista = ['MOH820115NI4','TGJ850121AI3','GAK921218LL2','AAA920127BB1','BGS920206CC5','CJD820305DE6','SLE720111AB5','ABR720525CA4','ANZ930622CC4','DML720525TT2','JEO930622TH3','IXP720525KI9','OOQ930622XD8','LAA720525SA7','MON930622AA2']

for v in lista:
	if (v[5:7]) == "01":
	    contE += 1
	if (v[5:7]) == "02":
	    contF += 1
	if (v[5:7]) == "03":
	    contM += 1
	if (v[5:7]) == "04":
	    contA += 1
	if (v[5:7]) == "05":
	    contMa += 1
	if (v[5:7]) == "06":
	    contJ += 1
	if (v[5:7]) == "07":
	    contJu += 1
	if (v[5:7]) == "08":
	    contAg += 1
	if (v[5:7]) == "09":
	    contS += 1
	if (v[5:7]) == "10":
	    contO += 1
	if (v[5:7]) == "11":
	    contN += 1
	if (v[5:7]) == "12":
	    contD += 1

print("ENERO ", contE)
print("FEBRERO ", contF)
print("MARZO ", contM)
print("ABRIL ", contA)
print("MAYO ", contMa)
print("JUNIO ", contJ)
print("JULIO ", contJu)
print("AGOSTO ", contAg)
print("SEPTIEMBRE ", contS)
print("OCTUMBRE ", contO)
print("NOVIEMBRE ", contN)
print("DICIEMBRE ", contD)
