# -*- coding: UTF-8 -*-
import logging

import DatabaseLogicMarket
import DatabaseLogicProduct
import DatabaseLogicBuyData
import telebot
import DatabaseLogicAdminPanel


log = logging.getLogger('KeyboardClass')


class NameSpace:
    # &#128138;
    ANSWER_STARTMARKET = "&#9940;  <b>ВНИМАНИЕ</b>  &#9940;\n\n&#128202;  У нас самые низкие цены  &#128202;\n\n&#128722;  Самые большие скидки  &#128722;\n\n&#9878; Адекватные операторы  &#9878;\n\n\n&#9989; Не переплачивай на площадках за переводы, бери разумно, оплачивай как тебе хочется\n\n&#127759;  Из списка ниже выберите ваш город  &#127759;"
    ANSWER_DELETEPRODUCT = "Введите"
    ANSWER_ADDPRODUCT = "&#128226; ВНИМАНИЕ &#128226;\n&#128218; Введите данные товара как показанно на примере:\n\nИмя\nЦена\nТип фасовки(грамм/штук)"
    ANSWER_REQESTJOBTEST = "&#128204;  Пример:\n\n1. Горячий клад\n2. Мефедрод кристаллы 1г\n3. Москва, центр\n4. Магнит\n5. Telegram @examplecontact"
    ANSWER_REQUESTJOB = "&#128203;  Форма заявки:\n\n1.  Предзаказ | Горячий клад\n2.  Товар и количество\n3.  Город, (Гео | Адрес | Остановка)\n4.  Тип клада (Магнит | Тайник | Прикоп)\n5. Контакты (<b>Telegram username</b>)\n\n" + ANSWER_REQESTJOBTEST
    ANSWER_SECTIONADMINCONTROL = "Вы в разделе ADMIN CONTROL"
    ANSWER_OKADD = "Вы успешно добавленны в администраторы"
    ANSWER_JOBMESSAGE = "&#128531; <b>Не нашли нужной позиции товара у вас на районе?</b>\n\n&#10024; Наш магазин предоставляет услугу предзаказа и горячего клада!\n\n&#128293; <b>Горячий клад</b> - это платная услуга. Вы вносите предоплату за товар и за услугу горячего клада и мы доставим его в радиусе 1-5км от указанной вами точки в течении 1-3ч с момента оплаты, но если мы не укладываемся в этот срок - в следующий раз доставка бесплатная!\n\n&#128142; Стоимость услуги - 1800 ₽\nЕсли заказ на сумму от 7500 ₽ - <b>БЕСПЛАТНО</b>\n\n&#9752; <b>Предзаказ</b> - это бесплатная услуга. Разница с горячим кладом в том, что доставка не срочная и и может занять 12-24ч\n\n&#9989; Нажмите ОФОРМИТЬ ЗАКАЗ чтобы заказать услугу предзаказа или горячего клада :)"
    ANSWER_ERRORCODE = "Нет такого кода.\nЛибо вы уже имеете данные права."
    ANSWER_WELCOM = "&#10052;  ДОБРО ПОЖАЛОВАТЬ В  НАШ МАРКЕТ  &#10052;\n\n&#127970;  ИЩИ СВОЙ ГОРОД В БОТЕ ИЛИ УТОЧНЯЙ У ОПЕРАТОРА\n\n\n&#127807;  В НАШЕМ МАГАЗИНЕ ТЫ НАЙДЕШЬ:\n\n&#9989;  РОВНЫЕ КЛАДЫ\n\n&#9989;  ВСЕГДА СВЕЖИЕ АДРЕСА\n\n&#9989;  ТОВАР ВЫСОКОГО КАЧЕСТВА\n\n&#9989;  СКИДКИ ПОСТОЯННЫМ КЛИЕНТАМ\n\n\n&#10071;  ПРИ ОФОРМЛЕНИИ ЗАКАЗА ВЫ АВТОМАТИЧЕСКИ СОГЛАШАЕТЕСЬ С ПРАВИЛАМИ НАШЕГО МАГАЗИНА&#10071;\nhttps://t.me/DLG_Official\n\n  &#8226; Гарантия на адрес составляет 12 часов с момента оплаты товара клиентом. По истечении этого срока претензии по товару не принимаются. Время считается от момента совершения покупки до момента получения письма о проблеме. Вам необходимо предоставить фото с места ваших поисков и сам заказ, в том виде, в котором вы его получили. Отсутствие фото/видео доказательств влечет за собой отказ в перезакладе. Чтобы доказать недовес необходимо сделать фото на весах в запакованном виде и в распакованном"
    ANSWER_ENTERREFCODE = "&#127873;  Введите реферальный код  &#127873;"
    ANSWER_SAVEDATABITCOIN = "Данные Bitcoin сохраненны."
    ANSWER_SAVEDATAQIWI = "Данные QIWI сохраненны."
    ANSWER_ERROR = "У вас нет прав на такие вещи :("
    ANSWER_ENTERNEWDATAQIWI = "Отправте ссылку на оплату по никнейму, либо введите сам никнейм"
    ANSWER_ENTERNEWFATABITCOIN = "Введите новые данные для Bitcoin"
    ANSWER_LEVELADMIN = "&#128220;  Какие права будут?\n\n&#128273;  0 - Полный доступ\n&#128273;  1 - Доступ на чтение/изменение реквезитов, админ пользователей(кроме админа 0 уровня)\n&#128273;  2 - Только просомтр информации без изменений."
    ANSWER_ADMIN_WELCOME = "&#128526 <b>{}</b>. Добро пожаловать в AdminPanel \n \n &#128172 Для быстрой навигации используйте кнопки над клавиатурой\n &#128172 По тех.вопросам пишите р@зрабy :)\n"
    ANSWER_ADMIN_STAT = "&#127919; Вот ваша статистика 	&#127919; \n\n&#128064 Администраторов: {}\n&#128064 Уникальных посетителей: {}\n&#128064 Кол-во активированных рефералок: {}\n\n&#128084; Кол-во поданных заявок: {}\n\n&#127942; Охват магазина:\n\n&#127970;  Городов: {}\n&#127973;  Районов: {}\n&#128138;  Товаров:  {}"
    ANSWER_EDITCONTACT ="&#128221;  Введите новые контакты оператора\n\n&#128204  Пример: @examplecontact"
class ListKeyBoard:
    kb_setting_back = telebot.types.InlineKeyboardButton(text='⏮ Назад', callback_data='setting_data')
    kb_world_back = telebot.types.InlineKeyboardButton(text='⏮ Назад',callback_data='world_data')
    button_menu_admin = telebot.types.InlineKeyboardButton(text="⏮ Меню", callback_data="admin_menu")
    button_back_admin_control = telebot.types.InlineKeyboardButton(text='⏮ Назад',callback_data='control_admin')

    KB_SALE_JOIN = telebot.types.InlineKeyboardMarkup()
    KB_SALE_JOIN.add(telebot.types.InlineKeyboardButton(text='🕒 Открыть',callback_data='join_market'))

    KB_WORL_JOIN = telebot.types.InlineKeyboardMarkup()
    kb_yes = telebot.types.InlineKeyboardButton(text='✍️',callback_data='job_join')
    kb_not = telebot.types.InlineKeyboardButton(text='👎',callback_data='cancel_pay')
    KB_WORL_JOIN.row(kb_yes,kb_not)

    kb_all_cancel = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_all_cancel.add("❌ Отмена")
    KB_DEFAULT = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_DEFAULT.add('⏮ Главное Меню')
    KB_DEFAULT.add('🏪 Магазин')
    KB_DEFAULT.add('☘️ Предзаказ | Горячий клад 🔥')
    KB_DEFAULT.row('👥 Пригласить друга', '📝 Ввести код')



    KB_DEFAULTANDADRMIN = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_DEFAULTANDADRMIN.add('👽 Меню Админки')
    KB_DEFAULTANDADRMIN.add('🏪 Магазин')
    KB_DEFAULTANDADRMIN.add('☘️ Предзаказ | Горячий клад 🔥')
    KB_DEFAULTANDADRMIN.row('👥 Пригласить друга', '📝 Ввести код')

    KB_JOBMENU = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_JOBMENU.row('✉️ Оформить заказ', '⏮ Главное Меню')
    KB_JOBCANCEL = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_JOBCANCEL.add("ОТМЕНА")


    KB_ADMINCONTROL = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_ADMINCONTROL.row('Добавить Админа', 'Удалить Админа')
    KB_ADMINCONTROL.add('Какие у меня права?')
    KB_ADMINCONTROL.add('👽 Меню Админки')

    KB_ADMIN = telebot.types.InlineKeyboardMarkup()
    kb_main_menu = telebot.types.InlineKeyboardButton(text='⏮ Главное Меню',callback_data='main_menu')
    kb_stat = telebot.types.InlineKeyboardButton(text='📊 Статистика',callback_data='stat_data')
    kb_order = telebot.types.InlineKeyboardButton(text='✅ Заказы',callback_data='order_data')
    kb_buy = telebot.types.InlineKeyboardButton(text='💰 Реквизиты',callback_data='buy_data')
    kb_setting = telebot.types.InlineKeyboardButton(text='🔧 Настройки', callback_data='setting_data')
    kb_control_admin = telebot.types.InlineKeyboardButton(text=' 🔑 Уч.Записи',callback_data='control_admin')
    kb_world = telebot.types.InlineKeyboardButton(text='🌏 Территории',callback_data='world_data')
    kb_sale = telebot.types.InlineKeyboardButton(text='🔔 Рассылка 🔔',callback_data='sale_data')
    KB_ADMIN.add(kb_main_menu)
    KB_ADMIN.row(kb_stat, kb_order)
    KB_ADMIN.row(kb_buy, kb_setting)
    KB_ADMIN.row(kb_control_admin, kb_world)
    KB_ADMIN.add(kb_sale)

    KB_SALE = telebot.types.InlineKeyboardMarkup()
    button_sale_precent_10 = telebot.types.InlineKeyboardButton(text='🛍 Скидка 10%',callback_data='sale_10')
    button_sale_precent_20 = telebot.types.InlineKeyboardButton(text='🛍 Скидка 20%',callback_data='sale_20')
    button_new_product = telebot.types.InlineKeyboardButton(text='🔥  Новый товар на районе  🔥',callback_data='push_product')
    button_job_need = telebot.types.InlineKeyboardButton(text='😓  Не нашли?  😓',callback_data='push_work')
    KB_SALE.add(button_menu_admin)
    KB_SALE.row(button_sale_precent_10,button_sale_precent_20)
    KB_SALE.add(button_new_product)
    KB_SALE.add(button_job_need)

    KB_CONTROL_ADMIN = telebot.types.InlineKeyboardMarkup()
    kb_all_admin = telebot.types.InlineKeyboardButton(text='👮‍♂️ ‍Все Администраторы',callback_data='all_admin')
    kb_my_right = telebot.types.InlineKeyboardButton(text='📜 Мои данные',callback_data='admin_info_data')
    kb_delete_admin = telebot.types.InlineKeyboardButton(text='➖ Удалить Админа.',callback_data='admin_delete_data')
    kb_add_admin = telebot.types.InlineKeyboardButton(text='➕ Добавить Админа.',callback_data='admin_add_admin')
    KB_CONTROL_ADMIN.add(kb_all_admin)
    KB_CONTROL_ADMIN.add(kb_my_right)
    KB_CONTROL_ADMIN.row(kb_add_admin, kb_delete_admin)
    KB_CONTROL_ADMIN.add(button_menu_admin)

    kb_button_order_all = telebot.types.InlineKeyboardButton(text='📋 Все Заказы',callback_data='order_all')
    kb_button_order_last = telebot.types.InlineKeyboardButton(text='📜 Последний',callback_data='order_last')
    kb_button_order_delete = telebot.types.InlineKeyboardButton(text='🗑 Удалить все',callback_data='order_delete')

    KB_BUY = telebot.types.InlineKeyboardMarkup()
    button_edit_qiwi = telebot.types.InlineKeyboardButton(text='💵 Изменить Qiwi',callback_data='edit_qiwi')
    button_edit_bitcoin = telebot.types.InlineKeyboardButton(text='💵 Изменить BitCoin',callback_data='edit_bitcoin')
    KB_BUY.add(button_edit_qiwi)
    KB_BUY.add(button_edit_bitcoin)
    KB_STAT = telebot.types.InlineKeyboardMarkup()
    button_stat_all = telebot.types.InlineKeyboardButton(text='Далее ⏩', callback_data='stat_all')
    button_stat_default = telebot.types.InlineKeyboardButton(text='⏪ Назад', callback_data='stat_data')
    KB_CANCEL_S = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    KB_CANCEL_S.add('❌ Отмена')

    KB_CITYCONTROL = telebot.types.InlineKeyboardMarkup()
    button_all = telebot.types.InlineKeyboardButton(text='📂 Все Территории',callback_data='allworld')
    button_addcity = telebot.types.InlineKeyboardButton(text='➕ Добавить Город',callback_data='addcity')
    button_addarea = telebot.types.InlineKeyboardButton(text='➕ Добавить Район',callback_data='addarea')
    button_deletecity = telebot.types.InlineKeyboardButton(text='✖️ Удалить Город',callback_data='deletecity')
    button_deletearea = telebot.types.InlineKeyboardButton(text='✖️ Удалить Район',callback_data='deletearea')
    KB_CITYCONTROL.add(button_all)
    KB_CITYCONTROL.row(button_addcity,button_addarea)
    KB_CITYCONTROL.row(button_deletecity,button_deletearea)
    KB_CITYCONTROL.add(button_menu_admin)


    button_close = telebot.types.InlineKeyboardButton(text='⏮ Назад',callback_data='close_world')
    KB_CLOSE = telebot.types.InlineKeyboardMarkup()
    KB_CLOSE.add(button_close)

    KB_CATEGORY_ADD = telebot.types.InlineKeyboardMarkup()
    KB_CATEGORY_ADD.add(telebot.types.InlineKeyboardButton(text='💰 Низкая цена',callback_data='cost_c0'))
    KB_CATEGORY_ADD.add(telebot.types.InlineKeyboardButton(text='💰 Средняя цена',callback_data='cost_c1'))
    KB_CATEGORY_ADD.add(telebot.types.InlineKeyboardButton(text='💰 Высокая цена',callback_data='cost_c2'))
    KB_CATEGORY_ADD.add(kb_setting_back)

    KB_SETTING = telebot.types.InlineKeyboardMarkup()
    button_showProduct = telebot.types.InlineKeyboardButton(text='📖  Список Товаров  📖', callback_data='list_product')
    button_addProduct = telebot.types.InlineKeyboardButton(text='📝 ️Добавить Товары', callback_data='add_product')
    button_random_product = telebot.types.InlineKeyboardButton(text='📌 Закрепить Товары',callback_data='random_product')
    button_deleteProduct = telebot.types.InlineKeyboardButton(text='🗑 Удалить Товар', callback_data='delete_product_data')
    button_contact = telebot.types.InlineKeyboardButton(text='✉️ Контакты Оператора', callback_data='contact')
    button_Export = telebot.types.InlineKeyboardButton(text="☁️Экспорт БД", callback_data='export')
    KB_SETTING.add(button_showProduct,button_random_product)
    KB_SETTING.row(button_addProduct, button_deleteProduct)
    KB_SETTING.add(button_contact)
    KB_SETTING.add(button_Export)
    KB_SETTING.add(button_menu_admin)

    KB_LAST_RANDOM = telebot.types.InlineKeyboardMarkup()
    kb_close = telebot.types.InlineKeyboardButton(text='🔨',callback_data='close')
    kb_random_last = telebot.types.InlineKeyboardButton(text='📌 Закрепить Товары',callback_data='random_product_last')
    KB_LAST_RANDOM.row(kb_close,kb_random_last)

    button_edit_contact = telebot.types.InlineKeyboardButton(text='✏ ️Изменить Контакты', callback_data='edit_contact')
    KB_EXPORT = telebot.types.InlineKeyboardMarkup()
    button_ExportYes = telebot.types.InlineKeyboardButton(text='Начать экспорт', callback_data='yesexport')
    button_ExportNot = telebot.types.InlineKeyboardButton(text='Отмена', callback_data='notexport')
    KB_EXPORT.row(button_ExportYes,button_ExportNot)


    KB_DELETE = telebot.types.ReplyKeyboardRemove()



    def createAddAdmin(self,rights):
        KB = telebot.types.InlineKeyboardMarkup()
        if rights == 2:
            return
        elif rights == 1:
            KB.add(telebot.types.InlineKeyboardButton(text='🔑 2 Уровень',callback_data='addadmin{}'.format(2)))
        elif rights == 0:
            KB.add(telebot.types.InlineKeyboardButton(text='🔑 2 Уровень',callback_data='addadmin{}'.format(2)))
            KB.add(telebot.types.InlineKeyboardButton(text='🔑 1 Уровень',callback_data='addadmin{}'.format(1)))
            KB.add(telebot.types.InlineKeyboardButton(text='🔑 0 Уровень',callback_data='addadmin{}'.format(0)))
        KB.add(self.button_back_admin_control)
        return KB

    def createAdminDelete(self, rights):
        log.info(f'Called with arg: {rights}')
        KB = telebot.types.InlineKeyboardMarkup()
        listAdmin = DatabaseLogicAdminPanel.DBAdminPanelClass().listAdmins()
        if not len(listAdmin) > 0:
            log.warning('Not found any ADMINs!')
            KB.add(self.button_back_admin_control)
            return KB
        if rights == 2:
            log.warning('Not enough rights!')
            KB.add(self.button_back_admin_control)
            return KB
        for admin in listAdmin:
            log.debug(f'admin: {admin}')
            if rights == 1 and admin[2] != 2:
                log.debug('ADMIN can\'t delete superadmin.')
                continue
            KB.add(telebot.types.InlineKeyboardButton(text='👮‍♂️ {} - {} уровень '.format(admin[1], admin[2]),
                                                      callback_data="deladmin{}".format(admin[0])))
        KB.add(self.button_back_admin_control)
        return KB

    def createBuy(self, areaId, productId):
        KB_PAY = telebot.types.InlineKeyboardMarkup()
        qiwi = telebot.types.InlineKeyboardButton(text='💳 Банковская карта +10%', callback_data="/qiwi{}|{}".format(areaId,productId))
        bitcoin = telebot.types.InlineKeyboardButton(text='₿ Bitcoin (БЕЗ КОМИССИИ) ', callback_data="/bitcoin{}|{}".format(areaId,productId))
        KB_PAY.add(qiwi)
        KB_PAY.add(bitcoin)
        KB_PAY.add(telebot.types.InlineKeyboardButton(text='❌ Отменить',callback_data='cancel_pay'))
        return KB_PAY

    def createBuyBtc(self, productInfo, idProduct):
        callbackCheck = "/c{}|{}|{}|{}".format(productInfo[0], productInfo[1], productInfo[2], idProduct)
        KB = telebot.types.InlineKeyboardMarkup()
        button_checkbuy = telebot.types.InlineKeyboardButton(text='🛍 Статус Заказа',callback_data=callbackCheck)
        button_back = self.button_back
        KB.add(button_checkbuy)
        KB.add(button_back)
        return KB
    def create(self, list):
        KB_CREATE = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        print(list)
        for item in list:
            KB_CREATE.add(item)
        return KB_CREATE

    def createBuyBitcoin(self, idArea, idProduct, order):
        KB = telebot.types.InlineKeyboardMarkup()
        button_send_btcpay = telebot.types.InlineKeyboardButton(text='✉️ Я оплатил',callback_data='sendbtcpay{}|{}'.format(idArea,idProduct))
        button_info = telebot.types.InlineKeyboardButton(text='🛍 Информация', callback_data="/infobitcoin{}|{}|{}".format(idArea, idProduct, order))
        button_geo = telebot.types.InlineKeyboardButton(text='🗺 Координаты Клада', callback_data="/geobitcoin{}|{}|{}".format(idArea, idProduct, order))
        button_cancel = telebot.types.InlineKeyboardButton(text='🗑 Отменить заказ', callback_data='cancel_pay')
        KB.add(button_send_btcpay)
        KB.row(button_info, button_geo)
        KB.add(button_cancel)
        return KB
    def createBuyQiwi(self, idArea, idProduct, order):
        dbBuy = DatabaseLogicBuyData.DBBuyDataClass()
        KB = telebot.types.InlineKeyboardMarkup()
        button_send_pay = telebot.types.InlineKeyboardButton(text='✉️ Я оплатил',callback_data='sendpay{}|{}'.format(idArea,idProduct))
        print("/info{}|{}|{}".format(idArea, idProduct, order))
        print("/geo{}|{}|{}".format(idArea, idProduct, order))
        button_info = telebot.types.InlineKeyboardButton(text='🛍 Информация',callback_data="/info{}|{}|{}".format(idArea, idProduct, order))
        button_geo = telebot.types.InlineKeyboardButton(text='🗺 Координаты Клада', callback_data="/geo{}|{}|{}".format(idArea, idProduct, order))
        button_cancel = telebot.types.InlineKeyboardButton(text='🗑 Отменить заказ', callback_data='cancel_pay')
        KB.add(button_send_pay)
        KB.row(button_info,button_geo)
        KB.add(button_cancel)
        return KB
    def createCityForDeleteArea(self):
        dbCity = DatabaseLogicMarket.DBMarketClass()
        listCity = dbCity.listCity()
        KB_CITY = telebot.types.InlineKeyboardMarkup()
        print(len(listCity))
        if len(listCity) == 0:
            KB_CITY.add(self.kb_world_back)
            return KB_CITY
        i = 0
        while i != len(listCity):
            try:
                cb_o = "/cda{}".format(listCity[i])
                cb_t = "/cda{}".format(listCity[i+1])
                KB_CITY.row(telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i]), callback_data=cb_o),
                            telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i+1]), callback_data=cb_t))
                i+=2
            except:
                KB_CITY.add(telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i]), callback_data=cb_o))
                break
        KB_CITY.add(self.kb_world_back)
        return KB_CITY
    def createCityDelete(self):
        dbCity = DatabaseLogicMarket.DBMarketClass()
        listCity = dbCity.listCity()
        KB_CITY = telebot.types.InlineKeyboardMarkup()
        if not len(listCity) > 0:
            KB_CITY.add(self.kb_world_back)
            return KB_CITY
        for city in listCity:
            cb = "/dc{}".format(city)
            KB_CITY.add(telebot.types.InlineKeyboardButton(text="🗑  {}".format(city), callback_data=cb))
        KB_CITY.add(self.kb_world_back)
        return KB_CITY
    def createCityEdit(self):
        dbCity = DatabaseLogicMarket.DBMarketClass()
        listCity = dbCity.listCity()
        KB_CITY = telebot.types.InlineKeyboardMarkup()
        if len(listCity) == 0:
            KB_CITY.add(self.kb_world_back)
            return KB_CITY
        i=0
        while i != len(listCity):
            try:
                cb_o = "/ac{}".format(listCity[i])
                cb_t = "/ac{}".format(listCity[i+1])
                KB_CITY.row(telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i]), callback_data=cb_o),
                            telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i+1]), callback_data=cb_t))
                i+=2
            except:
                KB_CITY.add(telebot.types.InlineKeyboardButton(text="🏙  {}".format(listCity[i]), callback_data=cb_o))
                break
        KB_CITY.add(self.kb_world_back)
        return KB_CITY
    def createCity(self,aceptCity):
        dbCity = DatabaseLogicMarket.DBMarketClass()
        listCity = dbCity.listCity()
        KB_CITY = telebot.types.InlineKeyboardMarkup()
        if listCity == False:
            return False
        if aceptCity == True:
            i = 5
            while len(listCity)-1 >= i:
                KB_CITY.add(telebot.types.InlineKeyboardButton(text="🌇  {}".format(listCity[i]),
                                                               callback_data="/city{}".format(listCity[i])))
                i += 1
            KB_CITY.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад',callback_data='/nexttwo'))
            return KB_CITY
        if len(listCity) >= 6:
            i = 0
            while 4 >= i:
                KB_CITY.add(telebot.types.InlineKeyboardButton(text="🌇  {}".format(listCity[i]),
                                                               callback_data="/city{}".format(listCity[i])))
                i += 1
            KB_CITY.add(telebot.types.InlineKeyboardButton(text='Еще города ➡️',callback_data='/nextone'))
            return KB_CITY
        else:
            for city in listCity:
                KB_CITY.add(telebot.types.InlineKeyboardButton(text="🌇  {}".format(city),
                                                               callback_data="/city{}".format(city)))
            return KB_CITY
    def createAreaDelete(self, city):
        dbArea = DatabaseLogicMarket.DBMarketClass()
        listArea = dbArea.listAreaForCity(city)
        idCity = dbArea.getIdCity(city)
        KB_AREA = telebot.types.InlineKeyboardMarkup()
        if listArea == False:
            KB = telebot.types.InlineKeyboardMarkup()
            KB.add(self.kb_world_back)
            return KB
        for item in listArea:
            callbackdata = "/da{}|{}".format(item, idCity)
            button = telebot.types.InlineKeyboardButton(text="🗑  {}".format(item), callback_data=callbackdata)
            KB_AREA.add(button)
        KB_AREA.add(self.kb_world_back)
        return KB_AREA
    def createArea(self, city):
        dbArea = DatabaseLogicMarket.DBMarketClass()
        listArea = dbArea.listAreaForCity(city)
        KB_AREA = telebot.types.InlineKeyboardMarkup()
        if listArea == False:
            KB_AREA.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад', callback_data='/nexttwo'))
            return KB_AREA
        if len(listArea) == 1:
            c_o = dbArea.getIdArea(city, listArea[0])
            KB_AREA.add(telebot.types.InlineKeyboardButton(text='🏣 {}'.format(listArea[0]),callback_data='/area{}'.format(c_o)))
            KB_AREA.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад', callback_data='/nexttwo'))
            return KB_AREA
        i = 0
        while len(listArea)-1 > i:
            i += 1
            c_o = dbArea.getIdArea(city,listArea[i])
            c_t = dbArea.getIdArea(city,listArea[i-1])
            KB_AREA.row(telebot.types.InlineKeyboardButton(text='🏣 {}'.format(listArea[i]),callback_data='/area{}'.format(c_o)),
                        telebot.types.InlineKeyboardButton(text='🏣 {}'.format(listArea[i-1]),callback_data='/area{}'.format(c_t)))
            i += 1
            if len(listArea)-1 == i:
                c_o = dbArea.getIdArea(city, listArea[i])
                KB_AREA.add(telebot.types.InlineKeyboardButton(text='🏣 {}'.format(listArea[i]),callback_data='/area{}'.format(c_o)))
                break
        KB_AREA.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад', callback_data='/nexttwo'))
        return KB_AREA
    def createProductDelete(self):
        dbProduct = DatabaseLogicProduct.DBProductClass()
        count = dbProduct.countProduct()
        if count == 0:
            return False
        list = dbProduct.listDelete()
        KB = telebot.types.InlineKeyboardMarkup()
        for p in list:
            KB.add(telebot.types.InlineKeyboardButton(text='🛍 {} {} - {}₽'.format(
                p[1], p[2], p[3]
            ), callback_data="/delete_product{}".format(p[0])))
        KB.add(self.kb_setting_back)
        return KB
    def createProduct(self, areaID):
        dbProduct = DatabaseLogicProduct.DBProductClass()
        dbMarket = DatabaseLogicMarket.DBMarketClass()
        KB_PRODUCT = telebot.types.InlineKeyboardMarkup()
        cityName = dbMarket.getInfoArea(areaID)[0]
        productID = dbMarket.productIDsByArea(areaID)
        count = len(productID)
        if not count > 0:
            KB_PRODUCT.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад', callback_data='/product_back{}'.format(
                cityName
            )))
            return KB_PRODUCT
        for product in productID:
            cb = "/sell{}|{}".format(areaID,product)
            print("cb = {}".format(cb))
            p_i = "🛍 {}".format(dbProduct.productInfo(product))
            KB_PRODUCT.add(telebot.types.InlineKeyboardButton(text=p_i, callback_data=cb))

        KB_PRODUCT.add(telebot.types.InlineKeyboardButton(text='⬅️ Назад', callback_data='/product_back{}'.format(
            cityName
        )))
        return KB_PRODUCT