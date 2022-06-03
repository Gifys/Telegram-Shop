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
    #await bot.send_message(message.chat.id,text='���� ����������� ������'+(URL))
    await bot.send_sticker(message.chat.id,'https://tlgrm.ru/_/stickers/061/2ac/0612acc2-f6fd-3470-83df-429ee8ba3d3b/192/25.webp')
    await message.answer("������!\n���� ����� ������-���!\n� ����� ����� ������ ������ � ����������.\n� ������ ����:\n- ������� ����� �� �������� ��� ���������\n- ������������� ������ � ����� ���������\n- ��������� � ����������\n- �������� ���� �����\n- ����������  ������ � ������ �������� �� ������", reply_markup = await key.main_menu())



################################## CALLBACK QUERY HANDLERS  #################################################

###################################
@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    # ��������� ������ ������������ � ������������ ����������� (None, ���� ������ ���)



    # ���� �����
    articles = [types.InlineQueryResultArticle(
        id=3333,
        #photo_url='https://klike.net/uploads/posts/2020-04/1587719791_1.jpg',
        thumb_url='https://klike.net/uploads/posts/2020-04/1587719791_1.jpg',
        title='�������-������',
        description="���-������",
        input_message_content = types.InputTextMessageContent(
            message_text="������� � �������",
            parse_mode="HTML"))]

    await query.answer(
        articles, cache_time=5, is_personal=True,
        switch_pm_parameter="add")



###################################


@dp.message_handler()
async def show_items(message:types.Message):
    if message.text == '������� � �������':
        f = open('patrick.jpg', 'rb')
        await bot.send_photo(message.chat.id, f, caption='�������� ������')
        await bot.send_message(message.chat.id,'� ����� ���������: \n ������� � ������� \n 189.00 * 1 = 189.00 ��� \n  ����� ������: 189 ��� \n��� ������ ���� ���� ������ � �� ����� ��� ����� ��������������� ����� -> (����,��,��������) ������')
        await message.answer(text=' �������� ���������� ������ ������,������� ��� ��������:',reply_markup=await key.defoult_menu())




@dp.callback_query_handler()
async def buying(call:CallbackQuery):
    #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #try:
    #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id-1)
    #except:
    #pass

    if call.data == "make_order":
        await call.message.answer(text='�������� �������� ��� ������',reply_markup=await key.next_step_proccesing())
    # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #await bot.delete_sticker(call.message.chat.id,'https://tlgrm.ru/_/stickers/061/2ac/0612acc2-f6fd-3470-83df-429ee8ba3d3b/192/25.webp')
    #elif call.data == "pizza":
    #await call.message.answer(text='H',
    #reply_markup= await key.test())


    elif call.data == "book_table":
        f = open('patrick.jpg', 'rb')
        await bot.send_photo(call.message.chat.id,f,caption='�����' )
        await call.message.answer("�������� ������!\n Prime - ���� �� ������� �������� 7-15 ������� \n VIP - ���� �� 6-7 �������, � ��������� ��������",reply_markup=await key.key_table())
        #tables = ['����1','����2', '����3', '����4','����5' ,'����6(Prime)','����7(Prime)', '����8' ,'����9', '����10','����11(VIP)','����12(VIP)','����13','����14']
        #bot.send_message(call.message.chat.id,text="�������� ������!\n Prime - ���� �� ������� �������� 7-15 ������� \n VIP - ���� �� 6-7 �������, � ��������� ��������")
        #for table in tables:
            #await call.message.answer(table, reply_markup=await key.key_table())
            #await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    if call.data == "back_from_key_table_menu":
        await call.message.answer(text='�����������',reply_markup=await key.main_menu())


    if call.data == "y":
        await call.message.answer(text='�������� ���� ������:',reply_markup=await key.days_week())

    if call.data == "back_from_days_menu":
        await call.message.answer(text='�����������',reply_markup=await key.key_table())


    elif call.data == "personal_info":
        await call.message.answer('���� ����������:', reply_markup=await key.personal_information())


    #elif call.data == "profit":
        #await call.message.answer('���� ��������:', reply_markup=await key.referals())



    elif call.data == "contacts":
        await call.message.answer('�� �������:', reply_markup=await key.contacts())



    elif call.data == "stock":
        await bot.send_message(call.message.chat.id,'������� �����:')


    elif call.data == "reviews":
        await call.message.answer('������ - ������ ��� � ��������', reply_markup=await key.reviews())



    elif call.data == "social_networks":
        await call.message.answer('�� � ���. �����:', reply_markup=await key.social_networks())


    #elif call.data == "basket":
    # await call.message.answer('�� �������:', reply_markup=await key.basket())


    elif call.data == "payment":
        await call.message.answer('������� ����, ������ �������� �� ��� �������. ��������� ��� �� ������ �������� ����� ����� ����� ��������� �������:', reply_markup=await key.payment())


    ### ^^^^ �� MAIN MARKUP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



    ##### ϲ�����:


    elif call.data == "modificator":
        await call.message.answer('MODIFICATOR')

    elif call.data == "favorites":
        await call.message.answer('� ��������� ���������:')



    elif call.data == "book_a_table_into":
        await call.message.answer(text='����� ������\n'
                                       '�������� ����')

    elif call.data == "cashback":
        await call.message.answer(text='��� ������:',reply_markup=await key.back_func())


    elif call.data == "back_func_data":
        await call.message.answer(text='�����������',reply_markup=await key.finance())



    elif call.data == "profit":
        await call.message.answer(text='��� ���������:')

    elif call.data == "ref_url":
        unique_code = call.message.chat.id
        URL = f'https://t.me/havchik123_bot?start={unique_code}'
        await call.message.answer(text='���� ����������� ������:' + URL,reply_markup=await key.back_func())

    elif call.data == "made_offer":
        await call.message.answer(text='�������� ������:')

    #elif call.data == "repeat_offer":
        #await call.message.answer(text='�� ���������� �����')

    elif call.data == "profile":
        await call.message.answer(text='��������� ���� ������ � �������� ����� � ������� 50���!\n \n������� :\n���:\n��������:\n���� ��������:\n����� ��������:\n�����:\nID:',reply_markup=await key.profile_button())

    elif call.data == "operators_number":
        await call.message.answer(text='������� ���������')

    elif call.data == "calling_me":
        await call.message.answer(text='����������� ���')

    elif call.data == "texting_in_chat":
        await call.message.answer(text='�������� � ���')

    elif call.data == "instagram":
        await call.message.answer(text='INSTAGRAM')

    elif call.data == "facebook":
        await call.message.answer(text='FACEBOOK')

    elif call.data == "basket":
        await call.message.answer(text='�� �������� � �������:')

    elif call.data == "payment":
        await call.message.answer(text='������')

    elif call.data == "finance":
        await call.message.answer(text='����� ����:',reply_markup=await key.finance())

    if call.data == "bonus_account":
        await call.message.answer(text='�� ����� ����� 0 ���. �� �������.', reply_markup=await key.bonus_account())


    elif call.data == "own_balance":
        await call.message.answer(text='������ ��������:\n ������� ����������:\n ������� ��������: ', reply_markup=await key.own_balance_func())

    elif call.data == "profit_from_referals":
        await call.message.answer(text='����� ����:0 \n������ �� ��������� 1 �������:0 \n������ �� ��������� 2 �������: 0\n������ �� ��������� 3 �������: 0\n������ �� ��������� 4 �������: 0\n������ �� ��������� 5 �������: 0',reply_markup=await key.back_func())


    elif call.data == "finished_offer":
        await call.message.answer(text='�c��� �� �������� �� 0 ���.',reply_markup=await key.back_func())

    elif call.data == "back_data_func":
        await call.message.answer(text='�����������', reply_markup=await key.personal_information())


    elif call.data == "my_referals":
        await call.message.answer(text='���-�� ��������� 1 �������:\n ���-�� ��������� 2 �������:\n���-�� ��������� 3 �������:\n���-�� ��������� 4 �������:\n���-�� ��������� 5 �������:',reply_markup=await key.back_func())

    elif call.data == "repeat_offer":
        await call.message.answer(text='� ��� ��� �� ���� �������.',reply_markup=await key.back_func())

    elif call.data == "back_to_menu":
        await call.message.answer(text='�� ��������� � ���� ������!',reply_markup = await key.next_step_proccesing())

    elif call.data == "bortics":
        await call.message.answer(text='������ ������',reply_markup = await key.bortics())

    elif call.data == "back_to_menu_quantity":
        await call.message.answer(text='�� ��������� � ���� ������!', reply_markup=await key.defoult_menu())




####### Back Button ########

    elif call.data == "back_to_previous_menu":
        await call.message.answer(text='�����������', reply_markup=await key.deliver_place())

    elif call.data == "back_to_classic_roll":
        await call.message.answer(text='�����������', reply_markup=await key.types_Japan_food())

    elif call.data == "back_to_profile_menu":
        await call.message.answer(text='�����������', reply_markup=await key.personal_information())

    elif call.data == "back_to_menu_types":
        await call.message.answer(text='�����������', reply_markup=await key.next_step_proccesing())



    elif call.data == "back_from_payment_menu":
        await call.message.answer(text='�����������', reply_markup=await key.main_menu())


    elif call.data == "back_from_reviews_menu":
        await call.message.answer(text='�����������', reply_markup=await key.confirming())


    elif call.data == "back_from_social_menu":
        await call.message.answer(text='�����������', reply_markup=await key.main_menu())


    elif call.data == "back_from_contact_menu":
        await call.message.answer(text='�����������', reply_markup=await key.main_menu())



    elif call.data == "back_from_my_referals":
        await call.message.answer(text='�����������', reply_markup=await key.personal_information())


    elif call.data == "back_from_my_balance_menu":
        await call.message.answer(text='�����������', reply_markup=await key.finance())

    elif call.data == "back_from_bonus_menu":
        await call.message.answer(text='�����������', reply_markup=await key.finance())

    elif call.data == "back_from_finance_menu":
        await call.message.answer(text='�����������', reply_markup=await key.personal_information())

    elif call.data == "back_from_bigtypes_menu":
        await call.message.answer(text='�����������', reply_markup=await key.main_menu())


    elif call.data == "back_from_personal_menu":
        await call.message.answer(text='�����������', reply_markup=await key.main_menu())

    elif call.data == "back_from_deliver_menu":
        await call.message.answer(text='�����������', reply_markup=await key.choise())

    elif call.data == "back_from_deliver_place_menu":
        await call.message.answer(text='�����������', reply_markup=await key.delivering())














    elif call.data == "see_my_offer":
        await call.message.answer(text='��������������', reply_markup=await key.menu_after_see_my_offer())

    elif call.data == "back_to_main_menu":
        await call.message.answer(text='�� ��������� � ���� ������!', reply_markup=await key.next_step_proccesing())

    elif call.data == "pizza":
        await call.message.answer(text='�������� �������� ��� ������',reply_markup=await key.types_pizza())

    elif call.data == "Japan_menu":
        await call.message.answer(text='�������� ��� ������)', reply_markup=await key.types_Japan_food())

    elif call.data == "classic_roll":
        await call.message.answer(text='������(����� �����)', reply_markup=await key.types_Japan_food_next())

    elif call.data == "additional_supplment":
        await call.message.answer(text='�������!', reply_markup=await key.additional_supplment())
        # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id,'���������� : ��� ������� �� ��� �������,��� ����� ���������� � ���� �������(�� �������� ������ ��� ��)')
        await bot.send_message(call.message.chat.id,'����� : ������,� ��� �����,����� � ��� ����� �����-�� ���������?',reply_markup=await key.choise())


    elif call.data == "yessssss":
        await bot.send_message(call.message.chat.id, '��,�������� �� ����')
        await Last_procces.first_question.set()

    elif call.data == "nooooooo":
        await bot.send_message(call.message.chat.id, '������,��� �������,������� ��������� �����.�������� ���������� ���� ���:')
        await Last_procces.first_question.set()



    elif call.data == "order_a_table":
        await call.message.answer(text='�������� ���� �����!', reply_markup=await key.days_week())

    elif call.data == "n_day":
        await bot.send_message(call.message.chat.id,'���������� : ��� ����� ������ � ����� ������,��-������� �����,��� ������ ��������� ����')
        await call.message.answer(text='<b>�������� ����� ��� ������ ��������� ���!</b> <i>\n (��,��� � �������� ��������) </i> \n <i>(��,��� � ��������� ������)</i>', reply_markup=await key.day_time())


    elif call.data == "backkkk":
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


    elif call.data == "x_time":
        await bot.send_message(call.message.chat.id,'������,�� ��� ��� ����� ��� �����?')
        await Name.name.set()

    #elif call.data == "no_nice_time":
        #await call.message.answer(text='�������� ���� �����!', reply_markup=await key.days_week())
        #await persons_quantity.persons_quantity.set()

@dp.message_handler(state=Name.name)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,text='�����,�������� �� ������� ������� �� ������ ������:')
    # ��������� ���
    await Name.count_people.set()  # ������� � �������



@dp.message_handler(state=Name.count_people)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������,����� ������ ��������:')
    await Name.number_phone.set()  # ������� � �������



@dp.message_handler(state=Name.number_phone)
async def get(message: types.Message, state: FSMContext):
     await bot.send_message(message.chat.id, text='������,��� �������!')
     #await bot.delete_message(message.chat.id,message_id = message.message_id)
     await bot.send_message(message.chat.id, text='������������� �����?: ������� \n ����� �7(Prime) \n ����: ������� \n �����: 13:00 - 14:30 !', reply_markup = await key.confirmation_order())
     await Name.next_class_step.set()  # ������� � �������

@dp.callback_query_handler(state=Name.next_class_step)
async def get(call:CallbackQuery, state: FSMContext):
    #await bot.send_message(message.chat.id, text='��� �����: bla blba',reply_markup=await key.confirmation_order())

    if call.data == "nooo":
        await call.message.answer(text='�� ��������� � ���� ����!', reply_markup=await key.days_week())

    if call.data == "yesss":
        await bot.send_message(call.message.chat.id,'�� ����� ����� ������� �������� ���(���� ������)\n ����� ������� ������������ �������� ����� �����-���� ��')









######################### MEEEEEEEESSSAAAAGGEEEEE #########################



@dp.message_handler()
async def message_get(message: types.Message):
    if message.text == '��':
        # print("fd")
        await bot.send_message(message.chat.id, '����������� ���� ������ ,������� ������������?')
        #await yes_menu.yes_state.set()

    elif message.text == '���':
        await bot.send_message(message.chat.id, '�����,����� ������� ������ ������ �����.������ �� ������ �������� ���')








@dp.message_handler(state=Last_procces.first_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������,��� �������,������� ��������� �����.�������� ���������� ���� ���:')
    await Last_procces.second_question.set()


@dp.message_handler(state=Last_procces.second_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������,�������� ��� ��������:',reply_markup= await key.delivering())
    await Last_procces.third_question.set()


@dp.callback_query_handler(state=Last_procces.third_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_from_deliver_menu':
        await call.message.answer('������� ����', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "pickup":
        await bot.send_message(call.message.chat.id, '������,�������� �� ����� ����� ����� ��� �����?')
        await Last_procces.third_question.set()


    if call.data == "delivver":
        await bot.send_message(call.message.chat.id, '�������� ���������� ����� �������� (�����, ����� ����, ����� ��������)')
        await Last_procces.fourth_question.set()




@dp.message_handler(state=Last_procces.third_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������,�������� ���������� �������',reply_markup=await key.payment_variant())
    #await bot.send_message(message.chat.id, text='��� �� ����������,� ������ ��� ��� �� �������� ���')
    await Last_procces.eight_question.set()






@dp.message_handler(state=Last_procces.fourth_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������! �������� ����� �� ������ � ������� ����� ��������� ������:',reply_markup=await key.deliver_place())
    await Last_procces.fiveth_question.set()


@dp.callback_query_handler(state=Last_procces.fiveth_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_from_deliver_place_menu':
        await call.message.answer('������� ����', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "place1":
        await bot.send_message(call.message.chat.id, '�������� � ��� ����� ����� ����������: 380�.\n  ������� "��" ��� �������������',reply_markup=await key.confirming())


    if call.data == "yesssssssssssss":
        await bot.send_message(call.message.chat.id, '�������� ����� ������� ��� �������')
        await Last_procces.sixth_question.set()


@dp.message_handler(state=Last_procces.sixth_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������! �������� ��� ����� ��������:')
    await Last_procces.seventh_question.set()


@dp.message_handler(state=Last_procces.seventh_question)
async def get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text='������! ��� ������ ����������?',reply_markup=await key.payment_variant())
    await Last_procces.eight_question.set()




@dp.callback_query_handler(state=Last_procces.eight_question)
async def get(call:CallbackQuery, state: FSMContext):
    if call.data == 'back_to_previous_menu':
        await call.message.answer('������� ����', reply_markup=await key.main_menu())
        await state.finish()
    if call.data == "card":
        await bot.send_message(call.message.chat.id, '��� �������������� ������,�� �������� �� ������,����� ����� � ����������')
        await bot.send_message(call.message.chat.id,'����� ��������')

    if call.data == "cash":
        await bot.send_message(call.message.chat.id, '��� �������������� ������,�� �������� �� ������,��� ���������� �������� �����')

    if call.data == "internet_balance":
        await bot.send_message(call.message.chat.id, '��� �������������� ������,�� �������� �� ������,� ��� ���������� �� �������')
        await bot.send_message(call.message.chat.id, '����� ��������')
    await bot.send_message(call.message.chat.id,'�� ����� ����� � ������ ��� ������������ ���(������� ������)', reply_markup=await key.main_menu())





























######################################### STATE ###################################


@dp.message_handler(state=yes_menu.yes_state)
async def message_get(message: types.Message,state:FSMContext):
    await bot.send_message(message.chat.id,'FUCK')
    #await bot.send_message(message.chat.id, '�����,����� ������� ������ �����.������ �� ������ �������� �����')

@dp.message_handler(state=no_menu.no_state)
async def message_get(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,'COOL')

###################################################################################

    #elif call.data == "yesss":
    #await bot.send_message(call.message.chat.id, '����������� ���� ������ ,������� ������������?')
    #await yes_menu.yes_state.set()
    #await bot.send_message(call.message.chat.id,'���������� : ��� ��� �������������� � �������������')

    #elif call.data == "nooo":
    #await bot.send_message(call.message.chat.id, '����������� ���� ������ ,������� ������������?')
    # await yes_menu.yes_state.set()
    #await bot.send_message(call.message.chat.id, '���������� : ��� ��� �������������� � �������������')



#@dp.callback_query_handler(state=yes_menu.yes_state)
#async def buying(call:CallbackQuery):
#await bot.send_message(call.message.chat.id, text="Hello bitch")

#############################################################################################



if __name__ == '__main__':
    executor.start_polling(dp)


