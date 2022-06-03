from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton

async def main_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text ='Заказать ДОСТАВКУ 🤖',callback_data='make_order')
    b2 = InlineKeyboardButton(text ='Заказать столик 🛎',callback_data='book_table')
    b3 = InlineKeyboardButton(text ='Личный кабинет🔑‍',callback_data='personal_info')
    b4 = InlineKeyboardButton(text ='☎Связь с нами☎',callback_data='contacts')
    b5 = InlineKeyboardButton(text='Отзывы📌', callback_data='reviews')
    b6 = InlineKeyboardButton(text='Соц. сети 🔔', callback_data='social_networks')
    b7 = InlineKeyboardButton(text='Корзина🗑', callback_data='basket')
    b8 = InlineKeyboardButton(text='Оплата⚠️', callback_data='payment')
    b9 = InlineKeyboardButton(text='💣Акции💣', callback_data='stock')
    menu.row(b1)
    menu.row(b2)
    menu.row(b3,b8)
    menu.row(b7,b5)
    menu.row(b9)
    menu.row(b4,b6)
    return menu

########################### ANSWER TO ALL REPLY_MARKUP ###############################


async def next_step_proccesing():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='🍕Пицца',callback_data="pizza")
    b2 = InlineKeyboardButton(text='Япония🀄️', callback_data="Japan_menu")
    #b2 = InlineKeyboardButton(text ='🍣Суши',switch_inline_query_current_chat="Суши")
    b3 = InlineKeyboardButton(text='🥤Напитки',switch_inline_query_current_chat="Напитки")
    b4 = InlineKeyboardButton(text='🍟Закуски',switch_inline_query_current_chat="Бургеры")
    b5 = InlineKeyboardButton(text='🥗Салаты',switch_inline_query_current_chat="Картошка")
    b6 = InlineKeyboardButton(text='🧁Десерты',switch_inline_query_current_chat="ЧикенРол")
    b7 = InlineKeyboardButton(text='Добавить в избранное⭐️', callback_data='Favorite')
    b8 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_bigtypes_menu')
    #b8 = InlineKeyboardButton(text='Модификатор', callback_data='modificator',switch_inline_query_current_chat="Пицца")
    #b9 = InlineKeyboardButton(text='Модификатор', callback_data='modificator',switch_inline_query_current_chat="Пицца")

    menu.add(b1,b2)
    #menu.add(b2)
    menu.add(b3)
    menu.add(b4)
    menu.add(b5,b6)
    menu.add(b7)
    menu.add(b8)
    return menu


async def book_a_table():
    menu = InlineKeyboardMarkup()
    return menu



async def personal_information():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text ='Кешбек и зароботок💸',callback_data='cashback')
    b3 = InlineKeyboardButton(text='Реферальная ссылка📣', callback_data='ref_url')
    b4 = InlineKeyboardButton(text='Сделаные заказ✔️', callback_data='finished_offer')
    b5 = InlineKeyboardButton(text='Повтор заказа🔂', callback_data='repeat_offer')
    b6 = InlineKeyboardButton(text='Профиль💼', callback_data='profile')
    b7 = InlineKeyboardButton(text='Финансы⚜', callback_data='finance')
    b8 = InlineKeyboardButton(text='Мои рефералы👀', callback_data='my_referals')
    b9 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_personal_menu')


    menu.add(b6)
    menu.add(b7)
    menu.add(b4,b5)
    menu.add(b8)
    menu.add(b1)
    menu.add(b3)

    return menu







async def finance():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text='Бонусный счет',callback_data='bonus_account')
    b2 = InlineKeyboardButton(text='Личный счет', callback_data='own_balance')
    b3 = InlineKeyboardButton(text='Доходы от рефералов', callback_data='profit_from_referals')
    b5 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_finance_menu')

    menu.add(b1)
    menu.add(b2)
    menu.add(b3)
    menu.add(b5)
    return menu


async def bonus_account():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text='История пополнения',callback_data='replenish_chek')
    b2 = InlineKeyboardButton(text='История списания', callback_data='censellation_chek')
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_bonus_menu')


    menu.add(b1)
    menu.add(b2)
    menu.add(b3)
    return menu


async def back_func():
    menu = InlineKeyboardMarkup()
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_func_data')

    menu.add(b3)
    return menu


async def own_balance_func():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text='Пополнить счет',callback_data='replenish_account')
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_my_balance_menu')

    menu.add(b1)
    menu.add(b2)
    return menu

async def referals():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text='Мои рефералы🧑‍💼',callback_data='my_referals')
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_my_referals')
    menu.insert(b1)
    menu.add(b2)
    return menu


async def contacts():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text ='Набрать оператора☎',callback_data='operators_number')
    b2 = InlineKeyboardButton(text ='Перезвонить мне📞',callback_data='calling_me')
    b3 = InlineKeyboardButton(text='Написать в чат📱', callback_data='texting_in_chat')
    b4 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_contact_menu')
    menu.add(b1)
    menu.add(b2)
    menu.add(b3)
    menu.add(b4)
    return menu



async def social_networks():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='--- Instagram ---',url='https://www.instagram.com/?hl=ru')
    b2 = InlineKeyboardButton(text ='--- Facebook ---',url='https://uk-ua.facebook.com/')
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_social_menu')
    menu.add(b1,b2)
    menu.add(b3)######### БАЗА ДАННИХ ##############
    return menu



async def reviews():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text ='Отзывы Дунька',callback_data='reviews')
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_reviews_menu')
    menu.insert(b1)
    menu.add(b2)
    return menu         ######### BAZA DANNIH ############

async def payment():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text ='YooMoney',callback_data='payment')
    b2 = InlineKeyboardButton(text='webmoney', callback_data='payment')
    b3 = InlineKeyboardButton(text='Payeer', callback_data='payment')
    b4 = InlineKeyboardButton(text='Qiwi', callback_data='payment')
    b5 = InlineKeyboardButton(text='Сбербанк России', callback_data='payment')
    b6 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_payment_menu')
    menu.add(b1)
    menu.insert(b2)
    menu.add(b3)
    menu.insert(b4)
    menu.add(b5)
    menu.add(b6)

    return menu


#################### TABLE ####################

async def key_table():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='1',callback_data='y')
    b2 = InlineKeyboardButton(text='2', callback_data='y')
    b3 = InlineKeyboardButton(text='3', callback_data='y')
    b4 = InlineKeyboardButton(text='4', callback_data='y')       #### y - База меняет
    b5 = InlineKeyboardButton(text='5(♨Prime♨)', callback_data='y')
    b6 = InlineKeyboardButton(text='6(♨Prime♨)', callback_data='y')
    b7 = InlineKeyboardButton(text='7', callback_data='y')
    b8 = InlineKeyboardButton(text='8', callback_data='y')
    b9 = InlineKeyboardButton(text='9', callback_data='y')
    b10 = InlineKeyboardButton(text='10', callback_data='y')
    b11 = InlineKeyboardButton(text='11(⚜vip⚜)', callback_data='y')
    b12 = InlineKeyboardButton(text='12(⚜vip⚜)', callback_data='y')
    b13 = InlineKeyboardButton(text='13', callback_data='y')
    b14 = InlineKeyboardButton(text='14', callback_data='y')
    b15 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_key_table_menu')



    menu.add(b1,b2)
    menu.add(b3,b4)
    menu.add(b5,b6)
    menu.add(b7,b8)
    menu.add(b9,b10)
    menu.add(b11,b12)
    menu.add(b13,b14)
    menu.add(b15)




    return menu

########################################
async def test():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="🔔Избранное🔔",callback_data='Favorite')
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_main_menu')
    menu.insert(b1)
    menu.add(b2)
    return menu
###################################






async def defoult_menu():
    menu = InlineKeyboardMarkup(row_width=3)
    #b1 = InlineKeyboardButton(text ='-',callback_data='-')
    b2 = InlineKeyboardButton(text='25 см(не работает без БД)', callback_data='25_см')
   # b3 = InlineKeyboardButton(text='+', callback_data='+')
    #b4 = InlineKeyboardButton(text='-', callback_data='-_')
    b5 = InlineKeyboardButton(text='30 cм(не работает без БД)', callback_data='30_cm')
    #b6 = InlineKeyboardButton(text='+', callback_data='+_')
    b7 = InlineKeyboardButton(text='🧀Бортики🌭', callback_data='bortics')
   # b8 = InlineKeyboardButton(text='🧐Вернутся в меню🍴', callback_data='back_to_menu')
   # b9 = InlineKeyboardButton(text='👀Посмотреть мой заказ📦', callback_data='see_my_offer')
    b3 = InlineKeyboardButton(text='Выбирете дополнительные добавки', callback_data="additional_supplment")
    b4 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_menu_types')
    menu.add(b2,b5)
    menu.add(b3)
    menu.add(b7)
    #menu.add(b4,b5,b6)
    menu.add(b4)
    #menu.add(b8)
    #menu.add(b9)
    return menu


async def send_ref():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="📣Ссылка📣")
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_main_menu')
    menu.insert(b1)
    menu.add(b2)
    return menu

async def bortics():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="Бортик1",callback_data='bortick1')
    b2 = InlineKeyboardButton(text="Бортик2",callback_data='bortick2')
    b3 = InlineKeyboardButton(text="Бортик3",callback_data='bortick3')
    b4 = InlineKeyboardButton(text="Бортик4",callback_data='bortick4')
    b5 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_menu_quantity')

    menu.add(b1)
    menu.add(b2)
    menu.add(b3)
    menu.add(b4)
    menu.add(b5)
    return menu

async def menu_after_see_my_offer():
    menu = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="🧐Вернуться в меню🍴", callback_data='again_back_to_menu')
    b2 = InlineKeyboardButton(text="✏️Редактировать заказ📦", callback_data='edit_offer')
    b3 = InlineKeyboardButton(text="🚚Изменить тип доставки🏃", callback_data='type_delivering')
    b4 = InlineKeyboardButton(text="🥳Я именинник🎉", callback_data='birthday_day')
    b5 = InlineKeyboardButton(text="❌Очистить заказ❌", callback_data='clear_offer')
    b6 = InlineKeyboardButton(text="Продолжить➡️", callback_data='continue')



    menu.add(b2)
    menu.add(b3)
    menu.add(b4)
    menu.add(b5)
    menu.add(b6)
    menu.add(b1)
    return menu



async def types_pizza():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='🍕Все пиццы',switch_inline_query_current_chat="Все пиццы")
    b2 = InlineKeyboardButton(text ='🍕Без мяса',switch_inline_query_current_chat="Без мяса")
    b3 = InlineKeyboardButton(text='🍕Острые без лука',switch_inline_query_current_chat="Острые без лука")
    b4 = InlineKeyboardButton(text='🍕Сладкие',switch_inline_query_current_chat="Сладкие")
    b5 = InlineKeyboardButton(text='🍕Детские',switch_inline_query_current_chat="Детские")
    b6 = InlineKeyboardButton(text='🍕Хиты продаж',switch_inline_query_current_chat="Хиты продаж")
    b7 = InlineKeyboardButton(text='🍕Без лука', switch_inline_query_current_chat="Хиты продаж")
    b8 = InlineKeyboardButton(text='↩Назад', callback_data='back_to_menu_types')

    menu.add(b1)
    menu.add(b3,b4)
    menu.add(b5,b6)
    menu.add(b2,b7)
    menu.add(b8)
    return  menu


async def types_Japan_food():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='Класические роллы',callback_data="classic_roll")
    b2 = InlineKeyboardButton(text ='Запеченые роллы',switch_inline_query_current_chat="baked_roll")
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_main_menu')


    menu.add(b1,b2)
    menu.add(b3)
    #menu.add(b2)
    return  menu


async def profile_button():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text ='Заполнить данные',callback_data="user_data")
    b2 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_profile_menu')

    menu.add(b1)
    menu.add(b2)
    return  menu

async def types_Japan_food_next():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Роллы "Филадельфия', switch_inline_query_current_chat='philadelfia_roll')
    b2 = InlineKeyboardButton(text='Роллы "Калифорния"', switch_inline_query_current_chat='california_roll')
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_classic_roll')
    #b3 = InlineKeyboardButton(text='Выбирете дополнительные добавки',callback_data="additional_supplment")

    menu.add(b1,b2)
    menu.add(b3)
    #menu.add(b2)
    return menu

async def additional_supplment():
    menu = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='Добавка1',callback_data="additional_supplment1")
    b2 = InlineKeyboardButton(text='Добавка2', callback_data="additional_supplment2")
    b3 = InlineKeyboardButton(text='Добавка3',callback_data="additional_supplment3")
    b4 = InlineKeyboardButton(text='Добавка4', callback_data="additional_supplment4")
    b5 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_main_menu')

    menu.add(b1,b2)
    menu.add(b3)
    menu.add(b4)
    menu.add(b5)
    return menu


async def choise():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='Да',callback_data="yessssss")
    b2 = InlineKeyboardButton(text='Нет',callback_data="nooooooo")

    menu.row(b1,b2)
    return menu


async def days_week():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='Понедельник(Дата: 1.08)',callback_data="n_day")
    b2 = InlineKeyboardButton(text='Вторник(Дата: 2.08)',callback_data="n_day")
    b3 = InlineKeyboardButton(text='Среда(Дата: 3.08)', callback_data="n_day")
    b4 = InlineKeyboardButton(text='Четверг(Дата: 4.08)', callback_data="n_day")
    b5 = InlineKeyboardButton(text='Пятница(Дата: 5.08)',callback_data="n_day")
    b6 = InlineKeyboardButton(text='Субота(Дата: 6.08)',callback_data="n_day")
    b7 = InlineKeyboardButton(text='Воскресенье(Дата: 7.08)', callback_data="n_day")
    b8 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_days_menu')





    menu.row(b1)
    menu.row(b2)
    menu.row(b3)
    menu.row(b4)
    menu.row(b5)
    menu.row(b6)
    menu.row(b7)
    menu.add(b8)

    return menu


async def day_time():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=2)
    b1 = InlineKeyboardButton(text='12:00 - 13:30✅',callback_data="x_time")
    b2 = InlineKeyboardButton(text='13:00 - 14:30✅',callback_data="x_time")
    b3 = InlineKeyboardButton(text='14:00 - 15:30✅', callback_data="x_time")
    b4 = InlineKeyboardButton(text='15:00 - 16:00❌', callback_data="x_time")
    b5 = InlineKeyboardButton(text='16:00 - 17:30✅', callback_data="x_time")
    b6 = InlineKeyboardButton(text='17:00 - 18:30✅', callback_data="x_time")
    b7 = InlineKeyboardButton(text='18:00 - 19:30✅', callback_data="x_time")
    b8 = InlineKeyboardButton(text='19:00 - 20:30✅', callback_data="x_time")
    b9 = InlineKeyboardButton(text='20:00 - 21:30❌', callback_data="x_time")
    b10 = InlineKeyboardButton(text='21:00 - 22:30✅', callback_data="x_time")
    b11 = InlineKeyboardButton(text='22:00 - 23:30❌', callback_data="x_time")
    b12 = InlineKeyboardButton(text='Назад⬅', callback_data="backkkk")


    menu.row(b1,b2)
    menu.row(b3,b4)
    menu.row(b5,b6)
    menu.row(b7,b8)
    menu.row(b9,b10)
    menu.row(b11)
    menu.row(b12)

    return menu



async def confirmation_order():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='ДА',callback_data="yesss")
    b2 = InlineKeyboardButton(text='НЕТ',callback_data="nooo")


    menu.row(b1,b2)
    return menu


async def delivering():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='Cамовывоз',callback_data="pickup")
    b2 = InlineKeyboardButton(text='Доставка',callback_data="delivver")
    b3 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_deliver_menu')

    menu.row(b1,b2)
    menu.add(b3)
    return menu


async def deliver_place():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='Район1',callback_data="place1")
    b2 = InlineKeyboardButton(text='Район2',callback_data="place1")         ###### Меняется в зависимости от БД
    b3 = InlineKeyboardButton(text='Район3', callback_data="place1")
    b4 = InlineKeyboardButton(text='Район4', callback_data="place1")
    b5 = InlineKeyboardButton(text='Район5', callback_data="place1")
    b6 = InlineKeyboardButton(text="Назад↩️", callback_data='back_from_deliver_place_menu')




    menu.row(b1)
    menu.row(b2)
    menu.row(b3)
    menu.row(b4)
    menu.row(b5)
    menu.add(b6)
    return menu



async def confirming():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='ДА',callback_data="yesssssssssssss")


    menu.row(b1)
    return menu




async def payment_variant():
    menu = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    b1 = InlineKeyboardButton(text='Картой',callback_data="card")                   ### разные коллбеки
    b2 = InlineKeyboardButton(text='Наличкой', callback_data="cash")
    b3 = InlineKeyboardButton(text='Електронный кошелек', callback_data = "internet_balance")
    b4 = InlineKeyboardButton(text="Назад↩️", callback_data='back_to_previous_menu')
    menu.row(b1)
    menu.row(b2)
    menu.row(b3)
    menu.add(b4)
    return menu