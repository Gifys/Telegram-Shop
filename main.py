# -*- coding: cp1251 -*-

from aiogram import Bot, types
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from key import next_step_proccesing,book_a_table,personal_information,bortics
import config
import key
from key import key_table,test,referals
from aiogram.types.chosen_inline_result import ChosenInlineResult
from aiogram.dispatcher.dispatcher import Dispatcher



class Name(StatesGroup):
    name=State()
    count_people = State()
    number_phone = State()
    next_class_step = State()



class Last_procces(StatesGroup):
    first_question = State()
    first_question = State()
    second_question = State()
    third_question = State()
    fourth_question = State()
    fiveth_question = State()
    sixth_question = State()
    seventh_question = State()
    eight_question = State()
    nineth_question = State()




bot = Bot(token=config.BOT_TOKEN,parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

#### start ##

class yes_menu(StatesGroup):
    yes_state = State()


class no_menu(StatesGroup):
    no_state = State()


@dp.message_handler(Command('start'))
async def show_items(message:types.Message):
    unique_code = message.chat.id
    #URL = f'https://t.me/havchik123_bot?start={unique_code}'
    #await bot.send_message(message.chat.id,text='Ваша реферальная ссылка'+(URL))
    await bot.send_sticker(message.chat.id,'https://tlgrm.ru/_/stickers/061/2ac/0612acc2-f6fd-3470-83df-429ee8ba3d3b/192/25.webp')
    await message.answer("Привет!\nМеня зовут Дунька-Бот!\nЯ стану твоим лучшим другом и помощником.\nЯ помогу тебе:\n- сделать заказ на доставку или самовывоз\n- забронировать столик в нашем заведении\n- связаться с оператором\n- оставить свой отзыв\n- заработать  вместе с КЕШБЕК системой от ДУНЬКИ", reply_markup = await key.main_menu())



################################## CALLBACK QUERY HANDLERS  #################################################

###################################
@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    # Получение ссылок пользователя с опциональной фильтрацией (None, если текста нет)



    # БАЗА ДАНИХ
    articles = [types.InlineQueryResultArticle(
        id=3333,
        #photo_url='https://klike.net/uploads/posts/2020-04/1587719791_1.jpg',
        thumb_url='https://klike.net/uploads/posts/2020-04/1587719791_1.jpg',
        title='Салатик-Пример',
        description="Что-нибудь",
        input_message_content = types.InputTextMessageContent(
            message_text="Салатик с патрика",
            parse_mode="HTML"))]

    await query.answer(
        articles, cache_time=5, is_personal=True,
        switch_pm_parameter="add")



###################################


@dp.message_handler()
async def show_items(message:types.Message):
    if message.text == 'Салатик с патрика':
        f = open('patrick.jpg', 'rb')
        await bot.send_photo(message.chat.id, f, caption='Описание заказа')
        await bot.send_message(message.chat.id,'В заказ добавлено: \n Салатик с патрика \n 189.00 * 1 = 189.00 грн \n  Сумма заказа: 189 грн \nТУТ ДОЛЖНА БЫТЬ БАЗА ДАННЫХ И ОТ ЭТОГО УЖЕ БУДЕТ РЕДОКТИРОВАТЬСЯ ЗАКАЗ -> (цена,см,название) Пример')
        await message.answer(text=' Выберите пожалуйста размер товара,который вам подойдет:',reply_markup=await key.defoult_menu())




@dp.callback_query_handler()
async def buying(call:CallbackQuery):
    #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #try:
    #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id-1)
    #except:
    #pass

    if call.data == "make_order":
        await call.message.answer(text='Выберете тонибудь для заказа',reply_markup=await key.next_step_proccesing())
    # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #await bot.delete_sticker(call.message.chat.id,'https://tlgrm.ru/_/stickers/061/2ac/0612acc2-f6fd-3470-83df-429ee8ba3d3b/192/25.webp')
    #elif call.data == "pizza":
    #await call.message.answer(text='H',
    #reply_markup= await key.test())


    elif call.data == "book_table":
        f = open('patrick.jpg', 'rb')
        await bot.send_photo(call.message.chat.id,f,caption='Текст' )
        await call.message.answer("Выберите столик!\n Prime - стол на большую кампанию 7-15 человек \n VIP - стол на 6-7 человек, в отдельных комнатах",reply_markup=await key.key_table())
        #tables = ['Стол1','Стол2', 'Стол3', 'Стол4','Стол5' ,'Стол6(Prime)','Стол7(Prime)', 'Стол8' ,'Стол9', 'Стол10','Стол11(VIP)','Стол12(VIP)','Стол13','Стол14']
        #bot.send_message(call.message.chat.id,text="Выберите столик!\n Prime - стол на большую кампанию 7-15 человек \n VIP - стол на 6-7 человек, в отдельных комнатах")
        #for table in tables:
            #await call.message.answer(table, reply_markup=await key.key_table())
            #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    if call.data == "back_from_key_table_menu":
        await call.message.answer(text='Возвращение',reply_markup=await key.main_menu())


    if call.data == "y":
        await call.message.answer(text='Выбирите день заказа:',reply_markup=await key.days_week())

    if call.data == "back_from_days_menu":
        await call.message.answer(text='Возвращение',reply_markup=await key.key_table())


    elif call.data == "personal_info":
        await call.message.answer('Ваша информация:', reply_markup=await key.personal_information())


    #elif call.data == "profit":
        #await call.message.answer('Ваши рефералы:', reply_markup=await key.referals())



    elif call.data == "contacts":
        await call.message.answer('Вы выбрали:', reply_markup=await key.contacts())



    elif call.data == "stock":
        await bot.send_message(call.message.chat.id,'Текущие акции:')


    elif call.data == "reviews":
        await call.message.answer('Кнопка - Ссылка чат с отзывами', reply_markup=await key.reviews())



    elif call.data == "social_networks":
        await call.message.answer('Мы в соц. сетях:', reply_markup=await key.social_networks())


    #elif call.data == "basket":
    # await call.message.answer('Вы выбрали:', reply_markup=await key.basket())


    elif call.data == "payment":
        await call.message.answer('Дорогой друг, обрати внимание на эту функцию. Благодаря мне ты можешь оплатить заказ через такие платежные системы:', reply_markup=await key.payment())


    ### ^^^^ ДО MAIN MARKUP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



    ##### ПІДМЕНЮ:


    elif call.data == "modificator":
        await call.message.answer('MODIFICATOR')

    elif call.data == "favorites":
        await call.message.answer('В избранном находится:')



    elif call.data == "book_a_table_into":
        await call.message.answer(text='Планы столов\n'
                                       'Заказать стол')

    elif call.data == "cashback":
        await call.message.answer(text='Ваш кешбек:',reply_markup=await key.back_func())


    elif call.data == "back_func_data":
        await call.message.answer(text='Возвращение',reply_markup=await key.finance())



    elif call.data == "profit":
        await call.message.answer(text='Ваш заработок:')

    elif call.data == "ref_url":
        unique_code = call.message.chat.id
        URL = f'https://t.me/havchik123_bot?start={unique_code}'
        await call.message.answer(text='Ваша реферальная ссылка:' + URL,reply_markup=await key.back_func())

    elif call.data == "made_offer":
        await call.message.answer(text='Сделаные заказы:')

    #elif call.data == "repeat_offer":
        #await call.message.answer(text='Вы повторяете заказ')

    elif call.data == "profile":
        await call.message.answer(text='Заполните ваши данные и получите бонус в размере 50руб!\n \nФамилия :\nИмя:\nОтчество:\nДата рождения:\nНомер телефона:\nАдрес:\nID:',reply_markup=await key.profile_button())

    elif call.data == "operators_number":
        await call.message.answer(text='Набрать оператора')

    elif call.data == "calling_me":
        await call.message.answer(text='Перезвонить мне')

    elif call.data == "texting_in_chat":
        await call.message.answer(text='Написать в чат')

    elif call.data == "instagram":
        await call.message.answer(text='INSTAGRAM')

    elif call.data == "facebook":
        await call.message.answer(text='FACEBOOK')

    elif call.data == "basket":
        await call.message.answer(text='Вы добавили в корзину:')

    elif call.data == "payment":
        await call.message.answer(text='Оплата')

    elif call.data == "finance":
        await call.message.answer(text='Общий счет:',reply_markup=await key.finance())

    if call.data == "bonus_account":
        await call.message.answer(text='На вашем счету 0 руб. от Кешбека.', reply_markup=await key.bonus_account())


    elif call.data == "own_balance":
        await call.message.answer(text='Личные средства:\n История пополнения:\n История списания: ', reply_markup=await key.own_balance_func())

    elif call.data == "profit_from_referals":
        await call.message.answer(text='Общий счет:0 \nДоходы от рефералов 1 ступени:0 \nДоходы от рефералов 2 ступени: 0\nДоходы от рефералов 3 ступени: 0\nДоходы от рефералов 4 ступени: 0\nДоходы от рефералов 5 ступени: 0',reply_markup=await key.back_func())


    elif call.data == "finished_offer":
        await call.message.answer(text='Вcего вы заказали на 0 руб.',reply_markup=await key.back_func())

    elif call.data == "back_data_func":
        await call.message.answer(text='Возвращение', reply_markup=await key.personal_information())


    elif call.data == "my_referals":
        await call.message.answer(text='Кол-во рефералов 1 ступени:\n Кол-во рефералов 2 ступени:\nКол-во рефералов 3 ступени:\nКол-во рефералов 4 ступени:\nКол-во рефералов 5 ступени:',reply_markup=await key.back_func())

    elif call.data == "repeat_offer":
        await call.message.answer(text='У вас еще не было заказов.',reply_markup=await key.back_func())

    elif call.data == "back_to_menu":
        await call.message.answer(text='Вы вернулись в меню заказа!',reply_markup = await key.next_step_proccesing())

    elif call.data == "bortics":
        await call.message.answer(text='Выбери Бортик',reply_markup = await key.bortics())

    elif call.data == "back_to_menu_quantity":
        await call.message.answer(text='Вы вернулись в меню заказа!', reply_markup=await key.defoult_menu())




####### Back Button ########

    elif call.data == "back_to_previous_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.deliver_place())

    elif call.data == "back_to_classic_roll":
        await call.message.answer(text='Возвращение', reply_markup=await key.types_Japan_food())

    elif call.data == "back_to_profile_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.personal_information())

    elif call.data == "back_to_menu_types":
        await call.message.answer(text='Возвращение', reply_markup=await key.next_step_proccesing())



    elif call.data == "back_from_payment_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.main_menu())


    elif call.data == "back_from_reviews_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.confirming())


    elif call.data == "back_from_social_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.main_menu())


    elif call.data == "back_from_contact_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.main_menu())



    elif call.data == "back_from_my_referals":
        await call.message.answer(text='Возвращение', reply_markup=await key.personal_information())


    elif call.data == "back_from_my_balance_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.finance())

    elif call.data == "back_from_bonus_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.finance())

    elif call.data == "back_from_finance_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.personal_information())

    elif call.data == "back_from_bigtypes_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.main_menu())


    elif call.data == "back_from_personal_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.main_menu())

    elif call.data == "back_from_deliver_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.choise())

    elif call.data == "back_from_deliver_place_menu":
        await call.message.answer(text='Возвращение', reply_markup=await key.delivering())














    elif call.data == "see_my_offer":
        await call.message.answer(text='ТЕЕЕЕЕЕККССТТТ', reply_markup=await key.menu_after_see_my_offer())

    elif call.data == "back_to_main_menu":
        await call.message.answer(text='Вы вернулись в меню заказа!', reply_markup=await key.next_step_proccesing())

    elif call.data == "pizza":
        await call.message.answer(text='Выберете тонибудь для заказа',reply_markup=await key.types_pizza())

    elif call.data == "Japan_menu":
        await call.message.answer(text='Выберете вид роллов)', reply_markup=await key.types_Japan_food())

    elif call.data == "classic_roll":
        await call.message.answer(text='Дальше(любой текст)', reply_markup=await key.types_Japan_food_next())

    elif call.data == "additional_supplment":
        await call.message.answer(text='Выбирай!', reply_markup=await key.additional_supplment())
        # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id,'Коментарий : При нажатии на эти добавки,они будут добавлятся в меню расчета(не работает сейчас без БД)')
        await bot.send_message(call.message.chat.id,'ПОТОМ : Хорошо,я все понял,может у вас будут какие-то пожелания?',reply_markup=await key.choise())


    elif call.data == "yessssss":
        await bot.send_message(call.message.chat.id, 'Хм,напишите их сюда')
        await Last_procces.first_question.set()

    elif call.data == "nooooooo":
        await bot.send_message(call.message.chat.id, 'Хорошо,все записал,давайте оформлять заказ.Напишите пожалуйста свое имя:')
        await Last_procces.first_question.set()



    elif call.data == "order_a_table":
        await call.message.answer(text='Выберете день брони!', reply_markup=await key.days_week())

    elif call.data == "n_day":
        await bot.send_message(call.message.chat.id,'Коментарий : ТУТ НУЖНА СВЯЗКА С БАЗОЙ ДАННЫХ,ПО-ДРУГОМУ НИКАК,ЕТО ПРОСТО РАНДОМНЫЕ ДАТЫ')
        await call.message.answer(text='<b>Выберете время для заказа выбраного дня!</b> <i>\n (То,что с галочкой свободно) </i> \n <i>(То,что с крестиком занято)</i>', reply_markup=await key.day_time())


    elif call.data == "backkkk":
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


    elif call.data == "x_time":
        await bot.send_message(call.message.chat.id,'Хорошо,на чье имя будет ваш заказ?')
        await Name.name.set()

    #elif call.data == "no_nice_time":
        #await call.message.answer(text='Выберете день брони!', reply_markup=await key.days_week())
        #await persons_quantity.persons_quantity.set()

@dp.message_handler(state=Name.name)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,text='Понял,напишите на сколько человек вы хотите столик:')
    # відправляє смс
    await Name.count_people.set()  # перенос в хендлер



@dp.message_handler(state=Name.count_people)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо,номер вашего телефона:')
    await Name.number_phone.set()  # перенос в хендлер



@dp.message_handler(state=Name.number_phone)
async def get(message: types.Message, state: FSMContext):
     await bot.send_message(message.chat.id, text='Хорошо,Все записал!')
     #await bot.delete_message(message.chat.id,message_id = message.message_id)
     await bot.send_message(message.chat.id, text='Подтверждаете заказ?: ТЕЕККСТ \n Столл №7(Prime) \n День: Четверг \n Время: 13:00 - 14:30 !', reply_markup = await key.confirmation_order())
     await Name.next_class_step.set()  # перенос в хендлер

@dp.callback_query_handler(state=Name.next_class_step)
async def get(call:CallbackQuery, state: FSMContext):
    #await bot.send_message(message.chat.id, text='Ваш заказ: bla blba',reply_markup=await key.confirmation_order())

    if call.data == "nooo":
        await call.message.answer(text='Вы вернулись в меню дней!', reply_markup=await key.days_week())

    if call.data == "yesss":
        await bot.send_message(call.message.chat.id,'На даном етапе поворам приходит смс(База данных)\n Чтобы столики показывались занятыми нужно снова-таки БД')









######################### MEEEEEEEESSSAAAAGGEEEEE #########################



@dp.message_handler()
async def message_get(message: types.Message):
    if message.text == 'Да':
        # print("fd")
        await bot.send_message(message.chat.id, 'Внимательно тебя слушаю ,дорогой пользователь?')
        #await yes_menu.yes_state.set()

    elif message.text == 'Нет':
        await bot.send_message(message.chat.id, 'Супер,тогда погнали дальше делать заказ.Сейчас вы должны оформить его')








@dp.message_handler(state=Last_procces.first_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо,все записал,давайте оформлять заказ.Напишите пожалуйста свое имя:')
    await Last_procces.second_question.set()


@dp.message_handler(state=Last_procces.second_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо,выбирите тип доставки:',reply_markup= await key.delivering())
    await Last_procces.third_question.set()


@dp.callback_query_handler(state=Last_procces.third_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_from_deliver_menu':
        await call.message.answer('Главное меню', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "pickup":
        await bot.send_message(call.message.chat.id, 'Хорошо,напишите на какое время будет ваш заказ?')
        await Last_procces.third_question.set()


    if call.data == "delivver":
        await bot.send_message(call.message.chat.id, 'Напишите пожалуйста адрес доставки (улица, номер дома, номер подъезда)')
        await Last_procces.fourth_question.set()




@dp.message_handler(state=Last_procces.third_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо,оплатите пожалуйста покупку',reply_markup=await key.payment_variant())
    #await bot.send_message(message.chat.id, text='Тут он оплачивает,в другой чат так же кидается смс')
    await Last_procces.eight_question.set()






@dp.message_handler(state=Last_procces.fourth_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо! Выберите район из списка в который будет отправлен курьер:',reply_markup=await key.deliver_place())
    await Last_procces.fiveth_question.set()


@dp.callback_query_handler(state=Last_procces.fiveth_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_from_deliver_place_menu':
        await call.message.answer('Главное меню', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "place1":
        await bot.send_message(call.message.chat.id, 'Доставка в ето место будет состовлять: 380р.\n  Нажмите "ДА" для подтверждения',reply_markup=await key.confirming())


    if call.data == "yesssssssssssss":
        await bot.send_message(call.message.chat.id, 'Уточните время приезда для курьера')
        await Last_procces.sixth_question.set()


@dp.message_handler(state=Last_procces.sixth_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо! Напишите ваш номер телефона:')
    await Last_procces.seventh_question.set()


@dp.message_handler(state=Last_procces.seventh_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='Хорошо! Как будете оплачивать?',reply_markup=await key.payment_variant())
    await Last_procces.eight_question.set()




@dp.callback_query_handler(state=Last_procces.eight_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_to_previous_menu':
        await call.message.answer('Главное меню', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "card":
        await bot.send_message(call.message.chat.id, 'Тут расчитвыаються бонусы,он нажимает на кнопку,пишет карту и оплачивает')
        await bot.send_message(call.message.chat.id,'ЗАКАЗ ОФОРМЛЕН')

    if call.data == "cash":
        await bot.send_message(call.message.chat.id, 'Тут расчитвыаються бонусы,он нажимает на кнопку,ему показывает конечную сумму')

    if call.data == "internet_balance":
        await bot.send_message(call.message.chat.id, 'Тут расчитвыаються бонусы,он нажимает на кнопку,и его закидывает на кошелек')
        await bot.send_message(call.message.chat.id, 'ЗАКАЗ ОФОРМЛЕН')
    await bot.send_message(call.message.chat.id,'На даном етапе в другой чат отправляется смс(готовый зааказ)', reply_markup=await key.main_menu())





























######################################### STATE ###################################


@dp.message_handler(state=yes_menu.yes_state)
async def message_get(message: types.Message,state:FSMContext):
    await bot.send_message(message.chat.id,'FUCK')
    #await bot.send_message(message.chat.id, 'Супер,тогда погнали дальше заказ.Сейчас вы должны оформить заказ')

@dp.message_handler(state=no_menu.no_state)
async def message_get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,'COOL')

###################################################################################

    #elif call.data == "yesss":
    #await bot.send_message(call.message.chat.id, 'Внимательно тебя слушаю ,дорогой пользователь?')
    #await yes_menu.yes_state.set()
    #await bot.send_message(call.message.chat.id,'Коментарий : ето смс обробатывается и отправляеться')

    #elif call.data == "nooo":
    #await bot.send_message(call.message.chat.id, 'Внимательно тебя слушаю ,дорогой пользователь?')
    # await yes_menu.yes_state.set()
    #await bot.send_message(call.message.chat.id, 'Коментарий : ето смс обробатывается и отправляеться')



#@dp.callback_query_handler(state=yes_menu.yes_state)
#async def buying(call:CallbackQuery):
#await bot.send_message(call.message.chat.id, text="Hello bitch")

#############################################################################################



if __name__ == '__main__':
    executor.start_polling(dp)


