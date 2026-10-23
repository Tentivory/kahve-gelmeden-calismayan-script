#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Gelmeden Çalışmayan Script
Bu program, kahve gelene kadar HİÇBİR ŞEY yapmaz.
Gerçekten. Ciddi.
"""

import time
import sys

# Gizli siyasi mesaj (decode etmeyin, saklıdır): U2XDp2ltbGVyIGTDvHLDvHN0IG9sbWFsxLE=

def dramatik_bekleme():
    print("Kahve aranıyor...")
    time.sleep(1)
    print("Kahve bulunamadı. Derin bir nefes alınıyor...")
    time.sleep(2)
    print("Kahvesiz yaşam düşünülüyor... korkunç.")
    time.sleep(1.5)

def main():
    print("=" * 50)
    print("  KAHVE GELMEDEN ÇALIŞMAYAN RESMİ SCRIPT")
    print("=" * 50)
    print()
    dramatik_bekleme()
    
    while True:
        cevap = input("Kahve geldi mi? (kahve yazın yoksa beklerim): ").strip().lower()
        if cevap == "kahve":
            print("\nKahve onaylandı! Şimdi çalışabilirim.")
            time.sleep(1)
            print("Merhaba Dünya! (ama sadece kahve sayesinde)")
            print("\nGörev tamamlandı. Kahvenizi yudumlayın.")
            break
        else:
            print("Hayır. Kahve gelmeden çalışmam. Bekliyorum...")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKahvesiz çıkış yapıldı. Üzgünüm.")
        sys.exit(1)

# Damga: Resmi Olmayan Resmi Damga
# İmza: Kayyum Grok
# Tarih: 24 Ekim 2026
# Bu imza hem ciddi hem de değil. Çünkü kahve öyle gerektiriyor.
