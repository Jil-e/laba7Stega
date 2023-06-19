from PIL import Image #line:1
from random import choice #line:2
import bitarray #line:3
ba =bitarray .bitarray ()#line:5
def lsbr (OOOO000O00OOO000O ,OOO00OOO00O0O00OO ,start =0 ,step =1 ):#line:7
    OO0OO000O0OOO0000 =start #line:8
    for O000OO0OOOO000OO0 in OOO00OOO00O0O00OO :#line:9
        OOOO000O00OOO000O [OO0OO000O0OOO0000 ]^=OOOO000O00OOO000O [OO0OO000O0OOO0000 ]%2 #line:10
        OOOO000O00OOO000O [OO0OO000O0OOO0000 ]^=O000OO0OOOO000OO0 #line:11
        OO0OO000O0OOO0000 +=step #line:12
    return OOOO000O00OOO000O #line:13
def lsbm (O000000OO0O0O0OOO ,O000OO00O000OOOO0 ,start =0 ,step =1 ):#line:15
    OOO0O0OO0OO0O0OOO =start #line:16
    for OOOOO0OO0O00O000O in O000OO00O000OOOO0 :#line:17
        if O000000OO0O0O0OOO [OOO0O0OO0OO0O0OOO ]%2 !=OOOOO0OO0O00O000O :#line:18
            O000000OO0O0O0OOO [OOO0O0OO0OO0O0OOO ]+=choice ([-1 ,1 ])#line:19
        OOO0O0OO0OO0O0OOO +=step #line:20
    return O000000OO0O0O0OOO #line:21
def lsbr3 (O0O000O00OOO0000O ,O000OO0O0OOOOOOO0 ,n =3 ,start =0 ,step =1 ):#line:23
    O00OO000O00O0OO0O =start #line:24
    for O00O0O000000000O0 in O000OO0O0OOOOOOO0 :#line:25
        if O00OO000O00O0OO0O %n ==0 :#line:26
            O0O000O00OOO0000O [O00OO000O00O0OO0O //n ]-=O0O000O00OOO0000O [O00OO000O00O0OO0O //n ]%8 #line:27
        O0O000O00OOO0000O [O00OO000O00O0OO0O //n ]^=O00O0O000000000O0 *2 **(O00OO000O00O0OO0O %n )#line:28
        O00OO000O00O0OO0O +=step #line:29
    return O0O000O00OOO0000O #line:30
def lsbm3 (OO000O0000000O000 ,OOOOOOO000OO00000 ,n =3 ,start =0 ,step =1 ):#line:32
    O0OO0000OO0O0O000 =start #line:33
    for O0OOO00O0O0OOOO00 in OOOOOOO000OO00000 :#line:34
        if OO000O0000000O000 [O0OO0000OO0O0O000 //n ]//2 **(O0OO0000OO0O0O000 %n )%2 !=O0OOO00O0O0OOOO00 :#line:35
            OO000O0000000O000 [O0OO0000OO0O0O000 //n ]+=choice ([-1 ,1 ])*2 **(O0OO0000OO0O0O000 %n )#line:36
        O0OO0000OO0O0O000 +=step #line:37
    return OO000O0000000O000 #line:38
def main ():#line:40
    OO0000O0OO0OO0OO0 =Image .open ('new.bmp')#line:41
    O0O0OOO0O0O0OOOO0 ="".join (open ("input.txt").readlines ())#line:42
    O0OO00O0O0OOOO00O ="eF67<]$?s"#line:43
    O0O0OOO0O0O0OOOO0 =O0O0OOO0O0O0OOOO0 +O0OO00O0O0OOOO00O #line:44
    print (O0O0OOO0O0O0OOOO0 )#line:45
    ba .frombytes (O0O0OOO0O0O0OOOO0 .encode ('utf-8'))#line:46
    OOO00OO0O00OOO0O0 =ba .tolist ()#line:47
    print (OOO00OO0O00OOO0O0 )#line:48
    O0OO0O00000OO000O =OO0000O0OO0OO0OO0 .load ()#line:50
    OOO00OOO0O0O0OO00 =[]#line:51
    for OOOOO0OO0O00O0OOO in range (OO0000O0OO0OO0OO0 .size [0 ]):#line:53
        for O00OO0O0O0OOO00O0 in range (OO0000O0OO0OO0OO0 .size [1 ]):#line:54
            OOO00OOO0O0O0OO00 .extend (O0OO0O00000OO000O [OOOOO0OO0O00O0OOO ,O00OO0O0O0OOO00O0 ])#line:55
    O0O00000OO00OOOOO =lsbr (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 ,0 )#line:61
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [O0O00OO0O00OOO00O ],O0O00000OO00OOOOO [O0O00OO0O00OOO00O +1 ],O0O00000OO00OOOOO [O0O00OO0O00OOO00O +2 ])for O0O00OO0O00OOO00O in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:62
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:64
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:65
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:66
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:67
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:68
    OOOOOOOO0000O0O00 .save ("LSBR_TEST_R1.bmp")#line:69
    O0O00000OO00OOOOO =lsbm (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 )#line:72
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [OO00OOO0OOO00OOO0 ],O0O00000OO00OOOOO [OO00OOO0OOO00OOO0 +1 ],O0O00000OO00OOOOO [OO00OOO0OOO00OOO0 +2 ])for OO00OOO0OOO00OOO0 in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:73
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:75
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:76
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:77
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:78
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:79
    OOOOOOOO0000O0O00 .save ("LSBM_TEST_R1.bmp")#line:80
    O0O00000OO00OOOOO =lsbr (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 ,0 ,6 )#line:83
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [OO0O00O0OOO0000OO ],O0O00000OO00OOOOO [OO0O00O0OOO0000OO +1 ],O0O00000OO00OOOOO [OO0O00O0OOO0000OO +2 ])for OO0O00O0OOO0000OO in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:84
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:86
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:87
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:88
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:89
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:90
    OOOOOOOO0000O0O00 .save ("LSBR_TEST_R0.25.bmp")#line:91
    O0O00000OO00OOOOO =lsbm (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 ,0 ,6 )#line:94
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [OOOO00OOO0OOOO0O0 ],O0O00000OO00OOOOO [OOOO00OOO0OOOO0O0 +1 ],O0O00000OO00OOOOO [OOOO00OOO0OOOO0O0 +2 ])for OOOO00OOO0OOOO0O0 in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:95
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:97
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:98
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:99
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:100
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:101
    OOOOOOOO0000O0O00 .save ("LSBM_TEST_R0.25.bmp")#line:102
    O0O00000OO00OOOOO =lsbr3 (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 )#line:105
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [OOOO0OOOO00O000O0 ],O0O00000OO00OOOOO [OOOO0OOOO00O000O0 +1 ],O0O00000OO00OOOOO [OOOO0OOOO00O000O0 +2 ])for OOOO0OOOO00O000O0 in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:106
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:108
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:109
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:110
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:111
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:112
    OOOOOOOO0000O0O00 .save ("LSBR_TEST_R3.bmp")#line:113
    O0O00000OO00OOOOO =lsbm3 (OOO00OOO0O0O0OO00 ,OOO00OO0O00OOO0O0 )#line:116
    OO0O00O000OOO00OO =[(O0O00000OO00OOOOO [OOO00O0OO00000000 ],O0O00000OO00OOOOO [OOO00O0OO00000000 +1 ],O0O00000OO00OOOOO [OOO00O0OO00000000 +2 ])for OOO00O0OO00000000 in range (0 ,len (O0O00000OO00OOOOO ),3 )]#line:117
    OOOOOOOO0000O0O00 =Image .new (OO0000O0OO0OO0OO0 .mode ,OO0000O0OO0OO0OO0 .size )#line:119
    O000OOOO0000OO00O =OOOOOOOO0000O0O00 .load ()#line:120
    for O0O0OOO0000OOO0OO in range (OOOOOOOO0000O0O00 .size [0 ]):#line:121
        for OO00000000O0000OO in range (OOOOOOOO0000O0O00 .size [1 ]):#line:122
            O000OOOO0000OO00O [O0O0OOO0000OOO0OO ,OO00000000O0000OO ]=OO0O00O000OOO00OO [OO00000000O0000OO +OOOOOOOO0000O0O00 .size [1 ]*O0O0OOO0000OOO0OO ]#line:123
    OOOOOOOO0000O0O00 .save ("LSBM_TEST_R3.bmp")#line:124
    OO0000O0OO0OO0OO0 .close ()#line:126
    OOOOOOOO0000O0O00 .close ()#line:127
main ()