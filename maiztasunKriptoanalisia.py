# Mezua deskriptatzen gai den programa sortu: jatorrizko mezu gaztelerakoa izanik
import string

#freq_sp = {"e":16.78, "a":11.96, "o":8.69, "l":8.37, "s":7.88, "n":7.01, "d":6.87, "r":4.94, "u":4.80, "i":4.15, "t":3.31, "c":2.92, "p":2.776, "m":2.12, "y":1.54, "q":1.53, "b":0.92, "h":0.89, "g":0.73, "f":0.52, "v":0.39, "j":0.30, "ñ":0.29, "z":0.15, "x":0.06, "k":0.00, "w":0.00}
"""
def aldatu(ema):
    karak1= input("Zein da aldatu nahi duzun karakterea?")
    karak2= input("Zein da jarri nahi duzun karakterea?")
    return ema.replace(karak1,karak2)
"""

def main():
    textua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE " \
           "AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE."\
           "AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ" \
           "TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX" \
           "DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936," \
           "PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN" \
           "TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE," \
           "HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK" \
           "HKCZJOI OKEJSZCNHE."

    karakt=list(string.ascii_uppercase) #MAIUSKULAZKO KARAKT GUZTIAK
    print(karakt)
    zenbaketa= {}

    for i in range(len(karakt)): #karaktere bakoitza zenbat aldiz dagoen zenbatu
        print(i)
        print(karakt[i])
        print(textua.count(karakt[i]))
        if (textua.count(karakt[i])!=0):
            zenbaketa[karakt[i]] = textua.count(karakt[i])
    print (zenbaketa)

    zenbaketa_sort=dict(sorted(zenbaketa.items(), key=lambda item:item[1], reverse=True))   #karaktere kop arabera ordenatuta
    print(zenbaketa_sort)
    letrak_ord=list(zenbaketa_sort.keys())  #soilik karaktearekin gelditu, kop ez dugu behar
    print("ORDEZKAPEN FALTA:")
    print(len(letrak_ord))

   # Textuan gehien erabiltzen diren karaktereak, gazteleran gehien erabiltzen diren 2 karakteengandik (e eta a) ordezkatu
    ordezkapenak=list(string.ascii_lowercase)
    gehienOrd=['e','a']
    print("ZENBAT FALTA?")
    print(len(ordezkapenak))
    ema = textua
    print(ema)

    for i in range(len(gehienOrd)):
        ema=ema.replace(letrak_ord[0],gehienOrd[i])
        print(ema)
        letrak_ord.remove(letrak_ord[0])
        ordezkapenak.remove(gehienOrd[i])
        print("ZENBAT FALTA?")
        print(len(ordezkapenak))
        print("ORDEZKAPEN FALTA:")
        print(len(letrak_ord))
    #ema=ema.replace(letrak_ord[1],'a')
    #ordezkapenak.remove('a')


    # 2 eta 3 karaktereez osatutako hitzak l eta s(normalean pl.)-gatik ordezkatuko ditugu
    ema= ema.replace('T','l')
    ordezkapenak.remove('l')
    letrak_ord.remove('T')
    print("ZENBAT FALTA?")
    print(len(ordezkapenak))
    print("ORDEZKAPEN FALTA:")
    print(len(letrak_ord))
    print(ema)

    """
    # oraindik aldatu ez direnetik, gehien errepikatzen dena freeq 3. karakt (o)-rekin aldatzen da
    i=2
    if (letrak_ord[i]=='T'):
        i=3
    ema=ema.replace(letrak_ord[i],'o')
    """

    #Suposaketak
    while len(letrak_ord)!=0:
        print(ema)
        karak1 = input("Zein da aldatu nahi duzun karakterea?")
        karak2 = input("Zein da jarri nahi duzun karakterea?")
        if karak1 in letrak_ord and karak2 in ordezkapenak:
            ema= ema.replace(karak1, karak2)
            ordezkapenak.remove(karak2)
            letrak_ord.remove(karak1)
            print("ORDEZKAPEN FALTA:")
            print(len(letrak_ord))
            print("Aldatzeko falta diren karaktereak:")
            print(list(letrak_ord))

    if len(letrak_ord)==0:
        print("Mezua deszifratuta dago")

    #'A'--> 'd' ,  'N'-->'s',  'J'-->'n','Z'-->'u'
    #Rlase suposatuko dugu: 'R'--> 'c'
    #cIN suposatuko dugu: 'I'--> 'o'
    #coPo suposatuko dugu: 'P'-->'m'
    #maneKa suposatuko dugu: 'K'--> 'r'
    #meGor suposatuko dugu: 'G'--> 'j'
    #dCreccCon: 'C'--> 'i', diriUenHe: U''--> 'g'  'H'-->'t'
    #indeDendencia: 'D'--> 'p', diOerencia: 'O'-->'f'
    # 'S'--> 'q', 'Q'--> 'b', 'V'-->'y', 'M'-->'h', 'L'-->'z'. 'F'-->'x'
    #falta: k,v,w,x, ñ

main()