from PIL import Image #line:1
from bittools import *#line:2
def lsb (O00OO0000OO0O0O0O ,start =0 ,step =1 ):#line:4
    OO0000OOO00O0OOOO =start #line:5
    OOO0OOO00OO00OOOO =[]#line:6
    while True :#line:7
        OOO0OOO00OO00OOOO .append (O00OO0000OO0O0O0O [OO0000OOO00O0OOOO ]%2 )#line:8
        OO0000OOO00O0OOOO +=1 #line:9
        if len (OOO0OOO00OO00OOOO )>=len (met ):#line:10
            O0O00O0OOOO0O0OO0 =OOO0OOO00OO00OOOO [-len (met ):]#line:11
            if O0O00O0OOOO0O0OO0 ==met :#line:12
                break #line:13
    return to_bytes (OOO0OOO00OO00OOOO [:-len (met )]).decode ('uft-8')#line:14
def lsb3 (OOO0OO000OO00O00O ,start =0 ,step =1 ):#line:16
    OOO0OO0OOOOOO0OOO =start #line:17
    OOOO000O0O0000O0O =[]#line:18
    while True :#line:19
        OOOO000O0O0000O0O .append ((OOO0OO000OO00O00O [OOO0OO0OOOOOO0OOO //3 ]//2 **(OOO0OO0OOOOOO0OOO %3 ))%2 )#line:20
        OOO0OO0OOOOOO0OOO +=1 #line:21
        if len (OOOO000O0O0000O0O )==200 :#line:22
            print (OOOO000O0O0000O0O )#line:23
        if len (OOOO000O0O0000O0O )>=len (met ):#line:24
            O0O000O0OO0O00O00 =OOOO000O0O0000O0O [-len (met ):]#line:25
            if O0O000O0OO0O00O00 ==met :#line:26
                break #line:27
    return to_bytes (OOOO000O0O0000O0O [:-len (met )]).decode ('uft-8')#line:28
met =[]#line:30
for i in "u98^%r*#8".encode ('uft-8'):#line:31
    met .extend (to_bits (i ))#line:32
print ("\n\nLSBR_R1\n")#line:34
im =Image .open ('LSBR_TEST_R1.bmp')#line:35
pix =im .load ()#line:36
pixels =[]#line:37
for x in range (im .size [0 ]):#line:39
    for y in range (im .size [1 ]):#line:40
        pixels .extend (pix [x ,y ])#line:41
result =lsb (pixels )#line:42
print (result )#line:44
im .close ()#line:47
print ("\n\nLSBM_R1\n")#line:49
im =Image .open ('LSBM_TEST_R1.bmp')#line:50
pix =im .load ()#line:51
pixels =[]#line:52
for x in range (im .size [0 ]):#line:54
    for y in range (im .size [1 ]):#line:55
        pixels .extend (pix [x ,y ])#line:56
result =lsb (pixels )#line:57
print (result )#line:59
im .close ()#line:62
print ("\n\nLSBR_R0.25\n")#line:64
im =Image .open ('LSBR_TEST_R1.bmp')#line:65
pix =im .load ()#line:66
pixels =[]#line:67
for x in range (im .size [0 ]):#line:69
    for y in range (im .size [1 ]):#line:70
        pixels .extend (pix [x ,y ])#line:71
result =lsb (pixels ,0 ,4 )#line:72
print (result )#line:74
im .close ()#line:77
print ("\n\nLSBM_R0.25\n")#line:79
im =Image .open ('LSBM_TEST_R1.bmp')#line:80
pix =im .load ()#line:81
pixels =[]#line:82
for x in range (im .size [0 ]):#line:84
    for y in range (im .size [1 ]):#line:85
        pixels .extend (pix [x ,y ])#line:86
result =lsb (pixels ,0 ,4 )#line:87
print (result )#line:89
im .close ()#line:92
print ("\n\nLSBR_R3\n")#line:94
im =Image .open ('LSBR_TEST_R3.bmp')#line:95
pix =im .load ()#line:96
pixels =[]#line:97
for x in range (im .size [0 ]):#line:99
    for y in range (im .size [1 ]):#line:100
        pixels .extend (pix [x ,y ])#line:101
result =lsb3 (pixels )#line:102
print (result )#line:104
im .close ()#line:107
print ("\n\nLSBM_R3\n")#line:109
im =Image .open ('LSBM_TEST_R3.bmp')#line:110
pix =im .load ()#line:111
pixels =[]#line:112
for x in range (im .size [0 ]):#line:114
    for y in range (im .size [1 ]):#line:115
        pixels .extend (pix [x ,y ])#line:116
result =lsb3 (pixels )#line:117
print (result )#line:119
im .close ()#line:122
