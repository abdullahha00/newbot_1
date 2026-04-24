
from itertools import product

import telebot
from telebot import types

TOKEN = "8786811766:AAFgfWxYYvnstR-d8KcdhEUJ_BYZFfpciIU"
bot = telebot.TeleBot(TOKEN)
ADMEN_ID = 5923258583
WORK_ACCOUNT = "@BellaBoxX"

selected_box = {}
user_name = {}
user_phone = {}
user_address = {}
cart = {}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_info = types.KeyboardButton("ما هي BellaBox؟ 🎀")
    btn_support = types.KeyboardButton("خدمة العملاء 💬")
    btn_choose = types.KeyboardButton("إختاري باقتك 💖")

    keyboard.add(btn_info, btn_support)
    keyboard.add(btn_choose)

    bot.send_message(
        message.chat.id,
        "أهلاً فيكي بعالم BellaBox\nحيث تبدأ لحظاتك الجميلة ✨",
        reply_markup=keyboard
    )
   

# ================================
#   واجهة اختيار الباقات
# ================================

@bot.message_handler(func=lambda m: m.text and m.text.strip() == "ما هي BellaBox؟ 🎀")
def what_is_bellabox(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "BellaBox هو بوكس مفاجآت جاهز، منسّق بإيدين مختصين، وبيوصلك فيه منتجات مختارة بعناية لتعيشي تجربة فريدة وممتعة كل مرة ❤️✨",
        reply_markup=keyboard
    )
#==================
#==================


@bot.message_handler(func=lambda m: m.text and m.text.strip() == "خدمة العملاء 💬")
def customer_service(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "إذا واجهتك أي مشكلة في الحجز أو التوصيل، يسعدنا استقبال شكواك على الحساب وسنقوم بالرد عليك في أقرب وقت 🤍✨\n\n@BellaBoxX",
        reply_markup=keyboard
    )
#==================
#==================
#باقة
@bot.message_handler(func=lambda m: m.text == "إختاري باقتك 💖")
def choose_package(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    basic = types.KeyboardButton("Basic Box 📦")
    glow = types.KeyboardButton("Glow Box 🎗")
    lux = types.KeyboardButton("Luxury Box 💎")
   
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")

    keyboard.add(basic, glow, lux)
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "يلا نعيش تجربة الخيال مع BellaBox.....🎀\nإختاري باقتك..!",
        reply_markup=keyboard
    )
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home),

# ================================
#private box
#=================================

#==============================
#   Glowry 
# ================================
@bot.message_handler(func=lambda m: m.text == "Glow Box 🎗")
def basic_box(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    content = types.KeyboardButton("محتوى البوكس ✨")
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(content)
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "اختيار موفق… Glow Box دايمًا لمسة جمال 🎀✨",
        reply_markup=keyboard
    )
#====================
#====================
@bot.message_handler(func=lambda m: m.text == "محتوى البوكس ✨")
def box_content(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    book = types.KeyboardButton("للحجز و الطلب 💗")
    back_basic = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(book)
    keyboard.add(back_basic)

    bot.send_message(
        message.chat.id,
          "✨🌸 يلا نشوف محتوى الـ Glow Box\n\n"
    "محتوى البوكس:\n"
    "- Glow Lip Tint 💋\n"
    "- Highlighter Mini ✨\n"
    "- Creamy Blush 🌷\n"
    "- Skin Care Serum 🌸\n"
    "- Eye Patches 👀💧\n"
    "- Surprise Gift 🎁",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "رجوع لـ Glow Box ↩️")
def back_to_basic(message):
    basic_box(message)


#==============
@bot.message_handler(func=lambda m: m.text == "للحجز و الطلب 💗")
def booking(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    confirm = types.KeyboardButton("تثبيت الحجز 🧸✨")
    back_content = types.KeyboardButton("رجوع لـ محتوى البوكس ↩️")

    keyboard.add(confirm)
    keyboard.add(back_content)

    bot.send_message(
        message.chat.id,
        "سعر الـ Glow Box هو:\n"
        "99,000 / 990 ل.س 🧸💗\n"
        "متضمنة التوصيل داخل دمشق 🚚✨",
        reply_markup=keyboard
    )

# ================================
#   Luxury غير متوفر
# ================================
@bot.message_handler(func=lambda m: m.text == "Luxury Box 💎")
def basic_box(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    content = types.KeyboardButton("محتوى البوكس 🧸")
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(content)
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "اختيار موفق… Luxury Box دايمًا لمسة جمال 🎀✨",
        reply_markup=keyboard
    )
#====================
#====================
@bot.message_handler(func=lambda m: m.text == "محتوى البوكس 🧸")
def box_content(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    book = types.KeyboardButton("للحجز و الطلب 🧸")
    back_basic = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(book)
    keyboard.add(back_basic)

    bot.send_message(
        message.chat.id,
        "✨🧸 يلا نشوف محتوى الـ Luxury Box\n\n"
        "محتوى البوكس:\n"
       " بوكس فخم يجمع بين Any Klaen وسكين كير عالي الجودة… خمس خطوات جمال بتفاصيل مدروسة",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "رجوع لـ Luxury Box ↩️")
def back_to_basic(message):
    basic_box(message)


#==============
@bot.message_handler(func=lambda m: m.text == "للحجز و الطلب 🧸")
def booking(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    confirm = types.KeyboardButton("تثبيت الحجز 🧸✨")
    back_content = types.KeyboardButton("رجوع لـ محتوى البوكس ↩️")

    keyboard.add(confirm)
    keyboard.add(back_content)

    bot.send_message(
        message.chat.id,
        "سعر الـ Luxury Box هو:\n"
        "149,000 / 1490 ل.س 🧸💗\n"
        "متضمنة التوصيل داخل دمشق 🚚✨",
        reply_markup=keyboard
    )
#   Basic Box (جاهز للتعديل)
# ================================
@bot.message_handler(func=lambda m: m.text == "Basic Box 📦")
def basic_box(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    content = types.KeyboardButton("محتوى البوكس 🧸✨")
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(content)
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "اختيار موفق… Basic Box دايمًا لمسة جمال 🎀✨",
        reply_markup=keyboard
    )
#====================
#====================
@bot.message_handler(func=lambda m: m.text == "محتوى البوكس 🧸✨")
def box_content(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    book = types.KeyboardButton("للحجز و الطلب 🧸💗")
    back_basic = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(book)
    keyboard.add(back_basic)

    bot.send_message(
        message.chat.id,
        "✨🧸 يلا نشوف محتوى الـ Basic Box\n\n"
        "محتوى البوكس:\n"
        "Mini lip oil 💄\n"
        "Skin care 🌸\n"
        " manicure 💐\n"
        "Mini perfume 🌷\n"
        "Body Lotion 💐\n"
        "Eyeliner💖\n"
        "Surprise 🎁",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "رجوع لـ Basic Box ↩️")
def back_to_basic(message):
    basic_box(message)


#==============
@bot.message_handler(func=lambda m: m.text == "للحجز و الطلب 🧸💗")
def booking(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    confirm = types.KeyboardButton("تثبيت الحجز 🧸✨")
    back_content = types.KeyboardButton("رجوع لـ محتوى البوكس ↩️")

    keyboard.add(confirm)
    keyboard.add(back_content)

    bot.send_message(
        message.chat.id,
        "سعر الـ Basic Box هو:\n"
        "59,000 / 590 ل.س 🧸💗\n"
        "متضمنة التوصيل داخل دمشق 🚚✨",
        reply_markup=keyboard
    )
#===============================

@bot.message_handler(func=lambda m: m.text == "تثبيت الحجز 🧸✨")
def start_collecting(message):
    bot.send_message(message.chat.id, "تمام 💖\nيلا نبلّش… اكتبي اسمك:")
    bot.register_next_step_handler(message, get_name)
    
# ================================
#   تثبيت الحجز – الخطوة الأولى
# ================================
from telebot import types

# تخزين الباقة المختارة لكل مستخدم

# زر الرجوع
back_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn.add("رجوع")

# القائمة الرئيسية للباقة
def show_box_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Basic Box 📦", "Glow Box 🎗", "Luxury Box 💎")
    bot.send_message(chat_id, "اختاري الباقة اللي بدك ياها ✨", reply_markup=keyboard)

# عند الضغط على زر الحجز والطلب
@bot.message_handler(func=lambda m: m.text == "تثبيت الحجز 🧸✨")
def start_order(message):
    show_box_menu(message.chat.id)

# اختيار الباقة
@bot.message_handler(func=lambda m: m.text in ["Basic Box 📦", "Glow Box 🎗", "Luxury Box 💎"])
def choose_box(message):
    selected_box[message.chat.id] = message.text

    bot.send_message(
        message.chat.id,
        f"اخترتي: {message.text} ✨\nاكتبي اسمك:",
        reply_markup=back_btn
    )

    bot.register_next_step_handler(message, get_name)

# دالة الرجوع الذكي
def go_back(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    box = selected_box.get(message.chat.id)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if box == "Basic Box 📦":
        keyboard.add("Basic Box 📦")
    elif box == "Glow Box 🎗":
        keyboard.add("Glow Box 🎗")
    elif box == "Luxury Box 💎":
        keyboard.add("Luxury Box 💎")
    else:
        keyboard.add("Basic Box 📦", "Glow Box 🎗", "Luxury Box 💎")

    bot.send_message(
        message.chat.id,
        "تم الرجوع للباقة السابقة ✨",
        reply_markup=keyboard
    )

# دالة الاسم


    bot.send_message(
        message.chat.id,
        f"اخترتي: {message.text} ✨\nاكتبي اسمك:",
        reply_markup=back_btn
    )
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    if "رجوع" in message.text:
        return go_back(message)

    name = message.text
    bot.send_message(message.chat.id, "اكتبي رقم الموبايل:", reply_markup=back_btn)
    bot.register_next_step_handler(message, get_phone, name)

# دالة الرقم
def get_phone(message, name):
    if "رجوع" in message.text:
        return go_back(message)

    phone = message.text
    bot.send_message(message.chat.id, "اكتبي عنوان التوصيل:", reply_markup=back_btn)
    bot.register_next_step_handler(message, get_address, name, phone)

# دالة العنوان
def get_address(message, name, phone):
    if "رجوع" in message.text:
        return go_back(message)

    address = message.text
    box = selected_box.get(message.chat.id, "غير محدد")

    bot.send_message(
        message.chat.id,
        f"تم استلام طلبك بنجاح 💗🧸\n"
        f"الباقة: {box}\n"
        f"الاسم: {name}\n"
        f"الرقم: {phone}\n"
        f"العنوان: {address}\n"
        "رح يتم التواصل معك لتأكيد الطلب ✨🎀"
    )

    # مسح البيانات
    selected_box.pop(message.chat.id, None)

    # إرسال الطلب للإدمن
    ADMIN_ID = 5923258583
    bot.send_message(
        ADMIN_ID,
        f"طلب جديد من BellaBox 🧸✨\n\n"
        f"الاسم: {name}\n"
        f"الرقم: {phone}\n"
        f"العنوان: {address}\n"
        f"نوع البوكس: {box}"
    )

    # زر الرجوع للصفحة الرئيسية
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "اضغطي رجوع للعودة للقائمة الرئيسية 🌸",
        reply_markup=keyboard
    )
# ================================
@bot.message_handler(func=lambda m: m.text == "رجوع لـ محتوى البوكس ↩️")
def back_to_content(message):
    box_content(message)
#   زر الرجوع
# ================================
@bot.message_handler(func=lambda m: m.text == "رجوع للصفحة الرئيسية ⬅️")
def back_home(message):
    start(message)

@bot.message_handler(func=lambda m: m.text == "رجوع للباقات 🔄")
def back_to_packages(message):
    choose_package(message)

# ================================
bot.polling(none_stop=True)



