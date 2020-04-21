def second_func(name:str, surname:str, year:str, city:str, email:str, mfon:str) -> str:
    """
    Выводит данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.

    """
    print(f"Имя - {name} "
          f"Фамилия - {surname} "
          f"Год рождения - {year} "
          f"Город проживания - {city} "
          f"Email- {email} "
          f"Телефон - {mfon}")


print(second_func(name = 'Михаил', surname = 'Бородин', year = 1991, city = 'Новосибирск', email = 'bam_nsk@mail.ru', mfon = 9059590285))