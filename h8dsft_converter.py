#Yudha Cipta M. Y.
# Hacktiv8 Batch-01
#NGChalenge 2

        #Temperature converter function
    # abbr. c = celcius, k = kelvin, f = fahrenheit
#function from kelvin to celcius
def k_to_c(temperatur):
    return (float(temperatur - 273.15))
#print(k_to_c(0)) untuk tes value

#function from celcius to kelvin
def c_to_k(temperatur):
    return (float(temperatur + 273.15))
#print(c_to_k(100)) untuk tes value

#function converter celcius and kelvin to fahrenheit
def fconvert(fcelcius,fkelvin):
    celcius=float((9 * fcelcius) / 5 + 32)
    kelvin=float(((fkelvin - 273.15) * 9 / 5)+32)
    return celcius,kelvin #panggil fungsi hasil rumus konversi celcius&kelvin ke fahrenheit
print("T in f from celcius and kelvin= ", fconvert(33,20))

#function fahrenheit to celcius and kelvin
def fconverter (f_temperatur):
     c_temperatur = (f_temperatur - 32) * (5/9) #konversi f ke c
     k_temperatur = c_temperatur + 273.15 #konversi f ke k
     return [f_temperatur, k_temperatur, c_temperatur]
print("fahrenheit" , "kelvin", "celcius")
print(fconverter(72))