def suslu_metin(metin):
    return f"\033[1;94;40m{metin}\033[0m"

def suslu_metin2(metin):
    return f"\033[1;30;47m{metin}\033[0m"

def suslu_metin3(metin):
    return f"\033[1;31;40m{metin}\033[0m"

def musteri_bilgileri_okuma():
    with open("22100011932.txt", "r", encoding="utf-8") as musteri_dosyasi:
        try:
            bilgiler = musteri_dosyasi.readlines()
            bilgiler = bilgiler[1:]
            musteri_bilgileri = {}
            for satir in bilgiler:
                satir = satir.split()
                musteri_bilgileri[satir[0]] = satir[1:]
            return musteri_bilgileri
        except FileNotFoundError:
            print(suslu_metin3("Müşteri bilgilerine ait dosya bulunamadı!!"))
            return {}
        except Exception as e:
            print(suslu_metin3(f"Dosya okunurken bir hata oluştu: {e}"))
            return {}

def ucak_koltuk_gorunumu(*koltuklar):
    satir = 15
    sutun = 6
    for i in range(satir):
        for j in range(sutun):
            koltuk_numarasi = ((i * 6) + j + 1)
            if j == sutun // 2:
                print("\t", end="")
            if j < satir and koltuk_numarasi < 10:
                if str(koltuk_numarasi) in koltuklar:
                    print("| " + suslu_metin3(str(koltuk_numarasi)) + "| ", end="")
                else:
                    print("| " + str(koltuk_numarasi) + "| ", end="")
            elif j < satir and koltuk_numarasi >= 10:
                if str(koltuk_numarasi) in koltuklar:
                    print("|" + suslu_metin3(str(koltuk_numarasi)) + "| ", end="")
                else:
                    print("|" + str(koltuk_numarasi) + "| ", end="")
        if i == sutun:
            print("\n")
        print()

def bagaj_menu():
    print(suslu_metin2("--------- EK BAGAJ İŞLEMLERİ---------"))
    print(suslu_metin2("| İŞLEM NO | EK BAGAJ YÜKÜ | ÜCRET  |"))
    print(suslu_metin2("| 1        | 10 KG         | 500TL  |"))
    print(suslu_metin2("| 2        | 20 KG         | 900TL  |"))
    print(suslu_metin2("| 3        | 30 KG         | 1200TL |"))
    print(suslu_metin2("| 4        | 40 KG         | 1600TL |"))
    print(suslu_metin2("| 5        | >40 KG        | 2500TL |"))
    print(suslu_metin2("-------------------------------------"))
    secim = input("Yapmak istediğiniz işlemi giriniz:")
    return secim

def ek_hizmet_menu():
    print(suslu_metin2("------EK HİZMET İŞLEMLERİ-------"))
    print(suslu_metin2("|İŞLEM NO | EK HİZMET | ÜCRET  |"))
    print(suslu_metin2("| 1       | BATTANİYE | 200TL  |"))
    print(suslu_metin2("| 2       | YEMEK     | 250TL  |"))
    print(suslu_metin2("| 3       | YASTIK    | 100TL  |"))
    print(suslu_metin2("--------------------------------"))
    secim = input("Almak istediğiniz ek hizmeti giriniz:(1-3)")
    return secim

def sefer_gosterim():
    ucus_bilgisi = [
        ["ADANA", "HAKKARİ", "10:00", "11:30", "2000 TL"],
        ["İSTANBUL", "ANKARA", "15:00", "16:00", "500 TL"],
        ["VAN", "ANTALYA", "07:00", "09:00", "1500 TL"],
        ["ANKARA", "SİİRT", "22:00", "23:10", "1000 TL"]
    ]

    baslik = (f"| {'SEFER NUMARASI':<15} | {'NEREDEN':<10} | {'NEREYE':<10} | "
              f"{'KALKIŞ SAATİ':<15} | {'VARIŞ SAATİ':<15} | {'BİLET FİYATI':<10} |"
              )

    print("-" * len(baslik))
    print("|" + " " * ((len(baslik) // 2) - 4) + "SEFERLER" + " " * ((len(baslik) // 2) - 6) + "|")
    print("-" * len(baslik))
    print(baslik)
    print("-" * len(baslik))

    for i in range(len(ucus_bilgisi)):
        print("|" + str(i + 1) + " " * (16) + "| " + ucus_bilgisi[i][0] + " " * (11 - len(ucus_bilgisi[i][0])) + "| " +
              ucus_bilgisi[i][1] + " " * (11 - len(ucus_bilgisi[i][1])) + "| " + ucus_bilgisi[i][2] + " " * (
                      16 - len(ucus_bilgisi[i][2])) + "| " + ucus_bilgisi[i][3] + " " * (
                      16 - len(ucus_bilgisi[i][3])) + "| " + ucus_bilgisi[i][4] + " " * (
                      13 - len(ucus_bilgisi[i][4])) + "|")
        print("-" * len(baslik))

def musteri_ekle(musteri_sayisi):
    for i in range(musteri_sayisi):
        musteri_bilgileri = musteri_bilgileri_okuma()
        with open("22100011932.txt", "a", encoding="utf-8") as musteri_dosyasi:
            print()
            print(suslu_metin2("|---------------------------|"))
            print(suslu_metin2("|        İNDİRİMLER         |"))
            print(suslu_metin2("|---------------------------|"))
            print(suslu_metin2("|1)18 yaş altına %50 indirim|"))
            print(suslu_metin2("|---------------------------|"))
            print(suslu_metin2("|2)Öğrenciye %30 indirim    |"))
            print(suslu_metin2("|---------------------------|"))
            print()
            sefer_gosterim()
            while True:
                sefer_secim = input("\nLütfen bir sefer seçimi yapınız(1-4):")
                print("-------------------------------")
                if sefer_secim == "1":
                    sefer_ismi = "ADANA-HAKKARİ"
                    sefer_saati = "10:00-11:30"
                    bilet_ucreti = "2000TL"
                    break
                elif sefer_secim == "2":
                    sefer_ismi = "İSTANBUL-ANKARA"
                    sefer_saati = "15:00-16:00"
                    bilet_ucreti = "500TL"
                    break
                elif sefer_secim == "3":
                    sefer_ismi = "VAN-ANTALYA"
                    sefer_saati = "07:00-09:00"
                    bilet_ucreti = "1500TL"
                    break
                elif sefer_secim == "4":
                    sefer_ismi = "ANKARA-SİİRT"
                    sefer_saati = "22:00-23:10"
                    bilet_ucreti = "1000TL"
                    break
                else:
                    print(suslu_metin3("Lütfen geçerli bir sefer seçimi yapınız!"))
                    continue
            isim = input("Lütfen isminizi giriniz:")
            soyisim = input("Lütfen soyisminizi giriniz:")
            while True:
                yas = input("Lütfen yaşınızı giriniz:")
                if yas.isdigit():  # Burada sadece sayıgirilmesini sağlıyorum
                    break
                else:
                    print(suslu_metin3("Lütfen geçerli bir giriş yapınız!!"))
                    continue
            bagaj_ucreti = "0TL"
            bagaj_tut = bagaj_ucreti.split("TL")
            if int(yas) < 18:
                yas_indirim_orani = 0.5
                tut = bilet_ucreti.split("TL")
                yas_indirim = int(int(tut[0]) * yas_indirim_orani)
                bilet_ucreti = str(int(tut[0]) - yas_indirim) + "TL"
            else:
                yas_indirim = 0
            while True:
                ogrenci = input("Öğrenci misiniz?(E/H):").upper()
                if ogrenci == "E":
                    ogrenci_indirim_orani = 0.3
                    ogrenci = "EVET"
                    tut2 = bilet_ucreti.split("TL")
                    ogrenci_indirim = int(int(tut2[0]) * ogrenci_indirim_orani)
                    bilet_ucreti = str(int(tut2[0]) - ogrenci_indirim) + "TL"
                    break
                elif ogrenci == "H":
                    ogrenci = "HAYIR"
                    ogrenci_indirim = 0
                    break
                else:
                    print(suslu_metin3("Lütfen geçerli bir seçim yapınız!!"))
                    continue
            bilet_tut = bilet_ucreti.split("TL")
            toplam_ucret = str(int(bagaj_tut[0]) + int(bilet_tut[0])) + "TL"
            koltuk_tutucu1 = []
            koltuk_tutucu2 = []
            koltuk_tutucu3 = []
            koltuk_tutucu4 = []
            for anahtar in musteri_bilgileri:
                basamak = int(anahtar) // 1000
                if basamak == 1:
                    koltuk_tutucu1.append(musteri_bilgileri[anahtar][6])
                elif basamak == 2:
                    koltuk_tutucu2.append(musteri_bilgileri[anahtar][6])
                elif basamak == 3:
                    koltuk_tutucu3.append(musteri_bilgileri[anahtar][6])
                elif basamak == 4:
                    koltuk_tutucu4.append(musteri_bilgileri[anahtar][6])
            # print("-------------------------------")
            print("---------UÇAK GÖRÜNÜMÜ---------\n")
            if sefer_secim == "1":
                ucak_koltuk_gorunumu(*koltuk_tutucu1)
                print("-------------------------------")
                while True:
                    koltuk_numarasi = input("Lütfen bir koltuk seçimi yapınız:")
                    if int(koltuk_numarasi) < 1 or int(koltuk_numarasi) > 90:
                        print(suslu_metin3("Girmiş olduğunuz koltuk numarası bulunmamaktadır!"))
                        print(suslu_metin3("Lütfen tekrar koltuk numarası seçiniz:"))
                        continue
                    if koltuk_numarasi in koltuk_tutucu1:
                        print(suslu_metin("Bu koltuk doludur"))
                        print(suslu_metin("Lütfen başka bir koltuk seçimi yapın!"))
                        continue
                    else:
                        break
                bilet_numarasi = str(int(sefer_secim) * 1000 + int(koltuk_numarasi))
            elif sefer_secim == "2":
                ucak_koltuk_gorunumu(*koltuk_tutucu2)
                print("-------------------------------")
                while True:
                    koltuk_numarasi = input("Lütfen bir koltuk seçimi yapınız:")
                    if int(koltuk_numarasi) < 1 or int(koltuk_numarasi) > 90:
                        print(suslu_metin3("Girmiş olduğunuz koltuk numarası bulunmamaktadır!"))
                        print(suslu_metin3("Lütfen tekrar koltuk numarası seçiniz:"))
                        continue
                    if koltuk_numarasi in koltuk_tutucu2:
                        print(suslu_metin("Bu koltuk doludur"))
                        print(suslu_metin("Lütfen başka bir koltuk seçimi yapın!"))
                        continue
                    else:
                        break
                bilet_numarasi = str(int(sefer_secim) * 1000 + int(koltuk_numarasi))
            elif sefer_secim == "3":
                ucak_koltuk_gorunumu(*koltuk_tutucu3)
                print("-------------------------------")
                while True:
                    koltuk_numarasi = input("Lütfen bir koltuk seçimi yapınız:")
                    if int(koltuk_numarasi) < 1 or int(koltuk_numarasi) > 90:
                        print(suslu_metin3("Girmiş olduğunuz koltuk numarası bulunmamaktadır!"))
                        print(suslu_metin3("Lütfen tekrar koltuk numarası seçiniz:"))
                        continue
                    if koltuk_numarasi in koltuk_tutucu3:
                        print(suslu_metin("Bu koltuk doludur"))
                        print(suslu_metin("Lütfen başka bir koltuk seçimi yapın!"))
                        continue
                    else:
                        break
                bilet_numarasi = str(int(sefer_secim) * 1000 + int(koltuk_numarasi))
            elif sefer_secim == "4":
                ucak_koltuk_gorunumu(*koltuk_tutucu4)
                print("-------------------------------")
                while True:
                    koltuk_numarasi = input("Lütfen bir koltuk seçimi yapınız:")
                    if int(koltuk_numarasi) < 1 or int(koltuk_numarasi) > 90:
                        print(suslu_metin3("Girmiş olduğunuz koltuk numarası bulunmamaktadır!"))
                        print(suslu_metin3("Lütfen tekrar koltuk numarası seçiniz:"))
                        continue
                    if koltuk_numarasi in koltuk_tutucu4:
                        print(suslu_metin("Bu koltuk doludur"))
                        print(suslu_metin("Lütfen başka bir koltuk seçimi yapın!"))
                        continue
                    else:
                        break
                bilet_numarasi = str(int(sefer_secim) * 1000 + int(koltuk_numarasi))
            bagaj_yuku = "15"
            ek_hizmet = "YOK"
            musteri_dosyasi.write("\n"f"{bilet_numarasi:<18} {isim:<14} {soyisim:<14} "
                                  f"{yas:<8} {ogrenci:<15} {sefer_ismi:<19} {sefer_saati:<19} "
                                  f"{koltuk_numarasi:<17} {bagaj_yuku:<12} {ek_hizmet:<18} "
                                  f"{bilet_ucreti:<14} {bagaj_ucreti:<14} "
                                  f"{toplam_ucret:<12}")
            print("-------------------------------")
            print(suslu_metin("Bagaj yükünüz 15 KG'dır."))
            print("-------------------------------")
            print(suslu_metin(
                "{}-->{} seferi için ödeyeceğiniz ücret: {} , Yapılan indirim: {}".format(sefer_ismi, sefer_saati,
                                                                                          toplam_ucret, (
                                                                                                      str(yas_indirim + ogrenci_indirim) + "TL"))))
            print("-------------------------------")
            print(suslu_metin(
                "{} numaralı bilet satın alma işleminiz başarılı bir şekilde gerçekleşmiştir!!".format(bilet_numarasi)))
            print("-------------------------------")
            print(suslu_metin("CNG UÇAK FİRMASINI TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ."))
    secim_kontrol()

def musteri_bilgileri_yaz(**musteriler):
    with open("22100011932.txt", "w", encoding="utf-8") as musteri_dosyasi:
        baslik = (f"{'BİLET NUMARASI':<17}| {'İSMİ':<13}| {'SOYADI':<12} | "
                  f"{'YAŞI':<7}| {'ÖĞRENCİ':<14}| {'SEFER İSMİ':<18}| {'SEFER SAATLERİ':<18}| "
                  f"{'KOLTUK NUMARASI':<16}| {'BAGAJ YÜKÜ':<11}| {'EK HİZMET':<17}| {'BİLET ÜCRETİ':<13}| "
                  f"{'BAGAJ UCRETİ':<13}| {'TOPLAM UCRET':<11}|"
                  )
        musteri_dosyasi.write(baslik)

        for bilet_no, bilgiler in musteriler.items():
            musteri_dosyasi.write("\n"f"{bilet_no:<18} {bilgiler[0]:<14} {bilgiler[1]:<14} "
                                  f"{bilgiler[2]:<8} {bilgiler[3]:<15} {bilgiler[4]:<19} {bilgiler[5]:<19} "
                                  f"{bilgiler[6]:<17} {bilgiler[7]:<12} {bilgiler[8]:<18} "
                                  f"{bilgiler[9]:<14} {bilgiler[10]:<14} "
                                  f"{bilgiler[11]:<12} ")

def musteri_bilet_iptal(iptal_numarasi):
    musteri_bilgileri = musteri_bilgileri_okuma()
    for bilet_no in musteri_bilgileri:
        if iptal_numarasi == bilet_no:
            del musteri_bilgileri[bilet_no]
            print(suslu_metin("{} No'lu biletiniz iptal edilmiştir.").format(bilet_no))
            break
    else:
        print(suslu_metin3("{} No'lu Bilet bulunamadı!!".format(iptal_numarasi)))

    musteri_bilgileri_yaz(**musteri_bilgileri)
    secim_kontrol()

def bilgi_guncelleme(guncel_bilet_no):
    musteri_bilgileri = musteri_bilgileri_okuma()

    for bilet_no in musteri_bilgileri:
        basamak = int(guncel_bilet_no) // 1000
        if basamak == "1":
            musteri_bilgileri[bilet_no][9] = "2000TL"
        elif basamak == "2":
            musteri_bilgileri[bilet_no][9] = "500TL"
        elif basamak == "3":
            musteri_bilgileri[bilet_no][9] = "1500TL"
        elif basamak == "4":
            musteri_bilgileri[bilet_no][9] = "1000TL"

        if guncel_bilet_no == bilet_no:
            musteri_bilgileri[bilet_no][0] = input("Lütfen isminizi giriniz:")
            musteri_bilgileri[bilet_no][1] = input("Lütfen soyisminizi giriniz:")
            while True:
                musteri_bilgileri[bilet_no][2] = input("Lütfen yaşınızı giriniz:")
                if musteri_bilgileri[bilet_no][2].isdigit():
                    break
                else:
                    print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                    continue
            if int(musteri_bilgileri[bilet_no][2]) < 18:
                yas_indirim = 0.5
                tut = musteri_bilgileri[bilet_no][9].split("TL")
                bilet_ucreti = int(int(tut[0]) * yas_indirim)
                musteri_bilgileri[bilet_no][9] = str(int(tut[0]) - bilet_ucreti) + "TL"
            while True:
                musteri_bilgileri[bilet_no][3] = input("Öğrenci misiniz?(E/H)").upper()
                if musteri_bilgileri[bilet_no][3] == "E":
                    musteri_bilgileri[bilet_no][3] = "EVET"
                    ogr_indirim = 0.3
                    tut2 = musteri_bilgileri[bilet_no][9].split("TL")
                    bilet_ucreti = int(int(tut2[0]) * ogr_indirim)
                    musteri_bilgileri[bilet_no][9] = str(int(tut2[0]) - bilet_ucreti) + "TL"
                    break
                elif musteri_bilgileri[bilet_no][3] == "H":
                    musteri_bilgileri[bilet_no][3] = "HAYIR"
                    break
                else:
                    print(suslu_metin3("Lütfen geçerli bir seçim yapınız!!"))
                    continue
            musteri_bilgileri[bilet_no][11] = str(
                int(musteri_bilgileri[bilet_no][9][:-2]) + int(musteri_bilgileri[bilet_no][10][:-2])) + "TL"
            print(suslu_metin("Biletiniz güncellenmiştir!!"))
            break
    else:
        print(suslu_metin3("{} No'lu bilet bulunamadı!!".format(guncel_bilet_no)))

    musteri_bilgileri_yaz(**musteri_bilgileri)
    secim_kontrol()

def bilet_arama(aranacak_bilet_no):
    musteri_bilgileri = musteri_bilgileri_okuma()

    baslik = (f"{'BİLET NUMARASI':<17}| {'İSMİ':<13}| {'SOYADI':<12} | "
              f"{'YAŞI':<7}| {'ÖĞRENCİ':<14}| {'SEFER İSMİ':<18}| {'SEFER SAATLERİ':<18}| "
              f"{'KOLTUK NUMARASI':<16}| {'BAGAJ YÜKÜ':<11}| {'EK HİZMET':<17}| {'BİLET ÜCRETİ':<13}| "
              f"{'BAGAJ UCRETİ':<13}| {'TOPLAM UCRET':<11}|"
              )

    for bilet_no in musteri_bilgileri:
        if aranacak_bilet_no == bilet_no:
            print(suslu_metin("{} No'lu aranan bilet bulunmuştur.").format(bilet_no))
            gosterme = input("{} No'lu bilet bilgilerini görmek için 1'e basınız:".format(bilet_no))
            if gosterme == "1":
                print(suslu_metin(baslik))
                print((f"{bilet_no:<18} {musteri_bilgileri[bilet_no][0]:<14} {musteri_bilgileri[bilet_no][1]:<14} "
                       f"{musteri_bilgileri[bilet_no][2]:<8} {musteri_bilgileri[bilet_no][3]:<15} {musteri_bilgileri[bilet_no][4]:<19} {musteri_bilgileri[bilet_no][5]:<19} "
                       f"{musteri_bilgileri[bilet_no][6]:<17} {musteri_bilgileri[bilet_no][7]:<12} {musteri_bilgileri[bilet_no][8]:<18} "
                       f"{musteri_bilgileri[bilet_no][9]:<14} {musteri_bilgileri[bilet_no][10]:<14} "
                       f"{musteri_bilgileri[bilet_no][11]:<12}"))
            break
    else:
        print(suslu_metin3("{} No'lu bilet bulunamadı!!").format(aranacak_bilet_no))
    secim_kontrol()

def bagaj_hesabi(bagaj_bilet_no):
    musteri_bilgileri = musteri_bilgileri_okuma()
    for bilet_no in musteri_bilgileri:
        if bagaj_bilet_no == bilet_no:
            print(suslu_metin("{} No'lu bilet bulunmuştur").format(bilet_no))
            secim = bagaj_menu()
            if secim == "1":
                ek_bagaj = "10KG"
                tut = ek_bagaj.split("KG")
                tut2 = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][7] = str(int(musteri_bilgileri[bilet_no][6]) + int(tut[0]))
                musteri_bilgileri[bilet_no][10] = str(int(tut[0]) * 50) + "TL"
                musteri_bilgileri[bilet_no][11] = str(int(tut2[0]) + (int(tut[0]) * 50)) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek bagaj eklenmiştir.").format(bilet_no, ek_bagaj))
                break
            elif secim == "2":
                ek_bagaj = "20KG"
                tut = ek_bagaj.split("KG")
                tut2 = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][7] = str(int(musteri_bilgileri[bilet_no][6]) + int(tut[0]))
                musteri_bilgileri[bilet_no][10] = str(int(tut[0]) * 45) + "TL"
                musteri_bilgileri[bilet_no][11] = str(int(tut2[0]) + (int(tut[0]) * 45)) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek bagaj eklenmiştir.").format(bilet_no, ek_bagaj))
                break
            elif secim == "3":
                ek_bagaj = "30KG"
                tut = ek_bagaj.split("KG")
                tut2 = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][7] = str(int(musteri_bilgileri[bilet_no][6]) + int(tut[0]))
                musteri_bilgileri[bilet_no][10] = str(int(tut[0]) * 40) + "TL"
                musteri_bilgileri[bilet_no][11] = str(int(tut2[0]) + (int(tut[0]) * 40)) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek bagaj eklenmiştir.").format(bilet_no, ek_bagaj))
                break
            elif secim == "4":
                ek_bagaj = "40KG"
                tut = ek_bagaj.split("KG")
                tut2 = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][7] = str(int(musteri_bilgileri[bilet_no][6]) + int(tut[0]))
                musteri_bilgileri[bilet_no][10] = str(int(tut[0]) * 40) + "TL"
                musteri_bilgileri[bilet_no][11] = str(int(tut2[0]) + (int(tut[0]) * 40)) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek bagaj eklenmiştir.").format(bilet_no, ek_bagaj))
                break
            elif secim == "5":
                ek_bagaj = ">40KG"
                tut = ek_bagaj.split(">")
                tut2 = tut[1].split("KG")
                tut2 = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][7] = ek_bagaj
                musteri_bilgileri[bilet_no][10] = str(2500) + "TL"
                musteri_bilgileri[bilet_no][11] = str(int(tut2[0]) + 2500) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek bagaj eklenmiştir.").format(bilet_no, ek_bagaj))
                break
            else:
                print(suslu_metin3("Yanlış bir seçim yaptınız!!"))
                break
    else:
        print(suslu_metin("{} No'lu bilet bulunmamıştır").format(bagaj_bilet_no))

    musteri_bilgileri_yaz(**musteri_bilgileri)
    secim_kontrol()

def ek_hizmet(ek_bilet_no):
    musteri_bilgileri = musteri_bilgileri_okuma()
    for bilet_no in musteri_bilgileri:
        if ek_bilet_no == bilet_no:
            secim = ek_hizmet_menu()
            if secim == "1":
                musteri_bilgileri[bilet_no][8] = "BATTANİYE(200TL)"
                ek_ucret = 200
                tut = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][11] = str(int(tut[0]) + ek_ucret) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek hizmeti eklenmiştir").format(bilet_no,
                                                                                           musteri_bilgileri[bilet_no][
                                                                                               8]))
                break
            elif secim == "2":
                musteri_bilgileri[bilet_no][8] = "YEMEK(250TL)"
                ek_ucret = 250
                tut = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][11] = str(int(tut[0]) + ek_ucret) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek hizmeti eklenmiştir").format(bilet_no,
                                                                                           musteri_bilgileri[bilet_no][
                                                                                               8]))
                break
            elif secim == "3":
                musteri_bilgileri[bilet_no][8] = "YASTIK(100TL)"
                ek_ucret = 100
                tut = musteri_bilgileri[bilet_no][11].split("TL")
                musteri_bilgileri[bilet_no][11] = str(int(tut[0]) + ek_ucret) + "TL"
                print(suslu_metin2("{} No'lu biletinize {} ek hizmeti eklenmiştir").format(bilet_no,
                                                                                           musteri_bilgileri[bilet_no][
                                                                                               8]))
                break
            else:
                print(suslu_metin3("Lütfen geçerli bir seçim yapın!!"))
                break
    else:
        print(suslu_metin3("{} No'lu bilet bulunamadı!!".format(ek_bilet_no)))

    musteri_bilgileri_yaz(**musteri_bilgileri)
    secim_kontrol()

def menu():
    print(suslu_metin("--------------------------------"))
    print(suslu_metin("|CNG UÇUŞ FİRMASINA HOŞGELDİNİZ|"))
    print(suslu_metin("--------------------------------"))
    print("\n")
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|                  MENÜ                   |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|1.UÇAK BİLETİ SATIN ALMA                 |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|2.UÇAK BİLETİ İPTAL ETME                 |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|3.UÇAK BİLETİ BİLGİLERİ GÜNCELLEME       |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|4.UÇAK BİLETİ SORGULAMA(ARAMA)           |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|5.EK BAGAJ İŞLEMLERİ                     |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|6.EK HİZMETLER(YEMEK,BATTANİYE)          |"))
    print(suslu_metin2("-------------------------------------------"))
    print(suslu_metin2("|7.ÇIKIŞ                                  |"))
    print(suslu_metin2("-------------------------------------------"))
    while True:
        try:
            secim = input("\nLütfen yapmak istediğiniz işlemi seçiniz: ")
            print("-------------------------------")
            if secim == "7":
                print(suslu_metin3("Sistemden çıkışınız yapılıyor..."))
                exit()
            elif secim == "1":
                musteri_sayisi = int(input("Lütfen almak istediğiniz bilet sayısını giriniz: "))
                musteri_ekle(musteri_sayisi)
                break
            elif secim == "2":
                while True:
                    iptal_bilet_no = input("Lütfen iptal etmek istediğiniz bilet numarasını giriniz:")
                    if iptal_bilet_no.isdigit():
                        musteri_bilet_iptal(str(iptal_bilet_no))
                        break
                    else:
                        print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                        continue
                break
            elif secim == "3":
                while True:
                    guncel_bilet_no = input("Lütfen bilgilerini değiştirmek istediğiniz bilet numarasını giriniz:")
                    if guncel_bilet_no.isdigit():
                        bilgi_guncelleme(guncel_bilet_no)
                        break
                    else:
                        print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                        continue
                break
            elif secim == "4":
                while True:
                    aranacak_bilet_no = input("Lütfen aramak istediğiniz bilet numarasını giriniz:")
                    if aranacak_bilet_no.isdigit():
                        bilet_arama(aranacak_bilet_no)
                        break
                    else:
                        print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                        continue
                break
            elif secim == "5":
                while True:
                    bagaj_bilet_no = input("Lütfen bagaj işlerimleri yapmak istediğiniz bilet numarasını giriniz:")
                    if bagaj_bilet_no.isdigit():
                        bagaj_hesabi(bagaj_bilet_no)
                        break
                    else:
                        print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                        continue
                break
            elif secim == "6":
                while True:
                    ek_bilet_no = input("Lütfen ücret hesabını görmek istediğiniz bilet numarasını giriniz:")
                    if ek_bilet_no.isdigit():
                        ek_hizmet(ek_bilet_no)
                        break
                    else:
                        print(suslu_metin3("Lütfen geçerli bir giriş yapın!!"))
                        continue
                break
            else:
                print(suslu_metin3("Lütfen geçerli bir seçim yapınız!"))
                continue
        except ValueError:
            print(suslu_metin3("Lütfen bir sayı giriniz!!"))
        except Exception as e:
            print(suslu_metin3(f"Bilinmeyen bir hata oluştu!! --> {e}"))

def secim_kontrol():
    print("-------------------------------")
    while True:
        secim = input("Ana menüye dönmek için 1'e, Sistemden çıkış yapmak için 2'ye basınız:")
        print()
        if secim == "1":
            menu()
        elif secim == "2":
            print(suslu_metin3("Sistemden çıkışınız yapılıyor..."))
            exit()
        else:
            print(suslu_metin3("Yanlış seçim yaptınız!!"))
            continue

menu()