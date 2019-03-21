# Tietokantakaavio

- Kiireellisyysluokka((pk) id:Integer, nimi:String, lääkäreitä:Integer, sairaanhoitajia:Integer, perushoitajia:Integer)
- Aukiolotunti((pk) id:Integer, (fk) kiireellisyysluokka_id -> Kiireellisyysluokka, päivämäärä:Date, alku:Integer)
- Työvuoro((pk) id:Integer, päivämäärä:Date)
- Työntekijäluokka((pk) id:Integer, nimi:String)
- Työntekijä((pk) id:Integer, (fk) työntekijäluokka_id -> Työntekijäluokka, nimi:String, henkilötunnus:String, päivätunnit:Integer, viikkotunnit:Integer)
- TyövuoroAukiolotunti((fk) työvuoro_id -> Työvuoro, (fk) aukiolotunti_id -> Aukiolotunti)
- TyöntekijäTyövuoro((fk) työntekijä_id -> Työntekijä, (fk) työvuoro_id -> Työvuoro)

