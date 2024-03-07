import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes, Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import pytz
import datetime
import aiohttp
import json

import config as cfg
import markups as nav
from states import register

logging.basicConfig(level=logging.INFO)

PROXY_URL = 'http://proxy.server:3128'
storage = MemoryStorage()
bot = Bot(token=cfg.TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot, storage=storage)

with open("info.json", "r") as json_file:
  uni_bot_data= json.load(json_file)

with open("members.json", "r") as json_file:
  members_data = json.load(json_file)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  if message.chat.type == 'private':
    await message.reply(uni_bot_data["general_info"]["greeting"], reply_markup=nav.BotMenu)

@dp.callback_query_handler(text="info")
async def info(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["contacts"], reply_markup=nav.BackMenu)

@dp.callback_query_handler(text="back")
async def back(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["back"], reply_markup=nav.BotMenu)

#кнопки назад для всех разделов
@dp.callback_query_handler(text="bentr")
async def bentr(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Программы", reply_markup=nav.EntrMenu)

@dp.callback_query_handler(text="balum")
async def balum(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Alumni club", reply_markup=nav.AlumMenu)


@dp.callback_query_handler(text="bbac")
async def bbac(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Бакалавриат", reply_markup=nav.BacMenu)

@dp.callback_query_handler(text="bmag")
async def bmag(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Магистратура", reply_markup=nav.MagMenu)

@dp.callback_query_handler(text="bdoc")
async def bdoc(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Докторантура", reply_markup=nav.DocMenu)

@dp.callback_query_handler(text="bcoll")
async def bcoll(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Колледж", reply_markup=nav.CollMenu)

@dp.callback_query_handler(text="bUNT")
async def bUNT(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Курсы ЕНТ", reply_markup=nav.UNTMenu)

#основное меню
@dp.callback_query_handler(text="entr")
async def entr(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Программы", reply_markup=nav.EntrMenu)

@dp.callback_query_handler(text="alum")
async def alum(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Ассоциация выпускников - подразделение, организующее взаимодействие выпускников с вузом.", reply_markup=nav.AlumMenu)

@dp.callback_query_handler(text="stud")
async def stud(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["tech_works"], reply_markup=nav.BackMenu)

@dp.callback_query_handler(text="empl")
async def empl(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["tech_works"], reply_markup=nav.BackMenu)

@dp.callback_query_handler(text="appl")
async def appl(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["tech_works"], reply_markup=nav.BackMenu)

@dp.callback_query_handler(text="qans")
async def qans(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["general_info"]["tech_works"], reply_markup=nav.BackMenu)

#кнопки поступающим
@dp.callback_query_handler(text="bac")
async def bac(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Бакалавриат", reply_markup=nav.BacMenu)

@dp.callback_query_handler(text="mag")
async def mag(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Магистратура", reply_markup=nav.MagMenu)

@dp.callback_query_handler(text="doc")
async def doc(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Докторантура", reply_markup=nav.DocMenu)

@dp.callback_query_handler(text="coll")
async def coll(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Колледж", reply_markup=nav.CollMenu)

@dp.callback_query_handler(text="UNT")
async def unt(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Курсы ЕНТ", reply_markup=nav.UNTMenu)

#кнопки выпускникам
@dp.callback_query_handler(text="faq")
async def faq(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["alumni_club"]["FAQ"], parse_mode="Markdown", reply_markup=nav.BalumMenu)

@dp.callback_query_handler(text="club")
async def club(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Вы выпускник?", reply_markup=nav.YNAlumMenu)

@dp.callback_query_handler(text="yalum")
async def yalum(callback: types.CallbackQuery):
  global is_alumni
  is_alumni = True
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Вы начали заполнение формы в клуб,\nВведите своe ФИО. Чтобы отменить заполнение формы, просто нажмите /stop в любое время.")
  await register.test1.set()

@dp.callback_query_handler(text="nalum")
async def nalum(callback: types.CallbackQuery):
  global is_alumni
  is_alumni = False
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, "Вы начали заполнение формы в клуб,\nВведите своe ФИО. Чтобы отменить заполнение формы, просто нажмите /stop в любое время.")
  await register.test1.set()
  
@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text
  if answer == "/stop":
    await message.answer("Вы остановили заполнение формы!", reply_markup=nav.BalumMenu)
    await state.finish()
  else:
    await state.update_data(test1=answer)
    await message.answer("Введите свой год окончания. Чтобы отменить заполнение формы, просто нажмите /stop в любое время.")
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text
  if answer == "/stop":
    await message.answer("Вы остановили заполнение формы!", reply_markup=nav.BalumMenu)
    await state.finish()
  else:
    await state.update_data(test2=answer)
    await message.answer("Введите свой факультет-направление. Чтобы отменить заполнение формы, просто нажмите /stop в любое время.")
    await register.test3.set()

@dp.message_handler(state=register.test3)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text
  if answer == "/stop":
    await message.answer("Вы остановили заполнение формы!", reply_markup=nav.BalumMenu)
    await state.finish()
  else:
    await state.update_data(test3=answer)
    await message.answer("Введите свою почту. Чтобы отменить заполнение формы, просто нажмите /stop в любое время.")
    await register.test4.set()

@dp.message_handler(state=register.test4)
async def state1(message: types.Message, state: FSMContext):
  answer = message.text
  if answer == "/stop":
    await message.answer("Вы остановили заполнение формы!", reply_markup=nav.BalumMenu)
    await state.finish()
  else:
    await state.update_data(test4=answer)
    almaty_timezone = pytz.timezone('Asia/Almaty')
    data = await state.get_data()
    name = data.get('test1')
    year = data.get('test2')
    fac = data.get('test3')
    mail = data.get('test4')
    link = uni_bot_data["alumni_club"]["join_the_club"]["telegram_channel_link"]
    new_member = {
        "exec_time": datetime.datetime.now(almaty_timezone).strftime("%Y-%m-%d %H:%M"),
        "is_alumni": is_alumni,
        "name": name,
        "year": year,
        "faculty": fac,
        "email": mail
    }
    members_data["members"].append(new_member)
    with open("members.json", "w", encoding='utf-8') as json_file:
      json.dump(members_data, json_file, indent = 2, ensure_ascii=False)
    await message.answer(f"Форма успешно заполнена!\nФИО: {name}\nГод окончания: {year}\nФакультет-направление: {fac}\nПочта: {mail}\n\n{link}", reply_markup=nav.BalumMenu)
    await state.finish()

#кнопки для бакалавриата
@dp.callback_query_handler(text="bac1")
async def bac1(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["educational_programs"], reply_markup=nav.BbacMenu)

@dp.callback_query_handler(text="bac2")
async def bac2(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["admission_rules"], parse_mode="Markdown", reply_markup=nav.BbacMenu)

@dp.callback_query_handler(text="bac3")
async def bac3(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["grants_and_scholarships"], parse_mode="Markdown", reply_markup=nav.BbacMenu)

@dp.callback_query_handler(text="bac4")
async def bac4(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["document_submission"], reply_markup=nav.BbacMenu)

@dp.callback_query_handler(text="bac5")
async def bac5(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["info_for_nonlocal_and_foreign_applicants"], reply_markup=nav.BbacMenu)

@dp.callback_query_handler(text="bac6")
async def bac6(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["bachelor"]["tuition_fees"], parse_mode="Markdown", reply_markup=nav.BbacMenu)

#кнопки для магистратуры
@dp.callback_query_handler(text="mag1")
async def mag1(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["registration_for_CT"], reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag2")
async def mag2(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["educational_programs"], parse_mode="Markdown", reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag3")
async def mag3(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["CT_for_admission"], parse_mode="Markdown", reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag4")
async def mag4(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["tuition_fees"], reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag5")
async def mag5(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["document_submission"], reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag6")
async def mag6(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["international_certificates"], parse_mode="Markdown", reply_markup=nav.BmagMenu)

@dp.callback_query_handler(text="mag7")
async def mag7(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["master"]["catalog_of_elective_courses"], parse_mode="Markdown", reply_markup=nav.BmagMenu)

#кнопки для докторантуры
@dp.callback_query_handler(text="doc1")
async def doc1(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["doctoral"]["educational_programs"], reply_markup=nav.BdocMenu)

@dp.callback_query_handler(text="doc2")
async def doc2(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["doctoral"]["what_you_need_to_know"], reply_markup=nav.BdocMenu)

@dp.callback_query_handler(text="doc3")
async def doc3(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["doctoral"]["document_submission"], reply_markup=nav.BdocMenu)

@dp.callback_query_handler(text="doc4")
async def doc4(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["doctoral"]["questions_from_previous_years"], reply_markup=nav.BdocMenu)

#кнопки для колледжа
@dp.callback_query_handler(text="coll1")
async def coll1(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["college"]["contacts_and_website"], reply_markup=nav.BcollMenu)

@dp.callback_query_handler(text="coll2")
async def coll2(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["college"]["admission_rules"], reply_markup=nav.BcollMenu)

#кнопки для ЕНТ
@dp.callback_query_handler(text="unt1")
async def unt1(callback: types.CallbackQuery):
  await bot.delete_message(callback.from_user.id, callback.message.message_id)
  await bot.send_message(callback.from_user.id, uni_bot_data["entrants"]["UNT_courses"]["information_and_contacts"], reply_markup=nav.BUNTMenu)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates = True)