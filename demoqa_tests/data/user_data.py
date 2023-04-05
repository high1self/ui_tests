from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    picture: str
    state: str
    city: str


kirill_k = User(first_name='Kirill',
                    last_name='Kozhevnikov',
                    email='test@gmail.com',
                    mobile='7945658756',
                    address='Russia',
                    gender='Male',
                    birth_year='1990',
                    birth_month='May',
                    birth_day=15,
                    subject='English',
                    hobby='Music',
                    picture='image.png',
                    state='NCR',
                    city='Delhi')
