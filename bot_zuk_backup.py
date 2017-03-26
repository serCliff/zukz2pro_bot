    #!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import logging
import sys
import os
import os.path
import subprocess
import mysql.connector
import MySQLdb



"""
-----------------------------------------------------------------------------------
    INTRODUCIR LOS SIGUIENTES VALORES PARA QUE EL BOT FUNCIONE CORRECTAMENTE
"""

pathof_scripts='/media/hdd/bot_zuk/old/'


#TOKEN vos
#TOKEN = "256162071:AAG6v8XkOk9877UXPX5AT6FvQU6iT-ym5fY"

##TOKEN descargas
#TOKEN = "242989022:AAERl3wLCOmkwr1mwmenSsvJ0iSbTMXW1D0"

##TOKEN zukz2pro
TOKEN = "329703840:AAEM1Bu9yXQAoPh9Yavs9x08SJDiN1bnjW4"


id_personal="12109646"
id_pruebas_grupo="-196861593"

id_gupo_zuk="-1001057339174"

"""
-----------------------------------------------------------------------------------
"""


path_of_users = pathof_scripts + "users.txt"
path_of_ids = pathof_scripts + "ids.txt"

path_of_help = pathof_scripts + "help.txt"



path_of_roms = pathof_scripts + "roms.txt"
path_of_pictures = pathof_scripts + "pictures.txt"
path_of_bootloader = pathof_scripts + "bootloader.txt"
path_of_beginers = pathof_scripts + "beginers.txt"
path_of_emmaus = pathof_scripts + "emmaus.txt"
path_of_faqs = pathof_scripts + "faqs.txt"
path_of_gadgets = pathof_scripts + "gadgets.txt"
path_of_link = pathof_scripts + "link.txt"
path_of_tools = pathof_scripts + "tools.txt"
path_of_bot = pathof_scripts + "recomendacion.txt"
path_of_twrp = pathof_scripts + "twrp.txt"
path_of_server = pathof_scripts + "server.txt"

path_of_suggestions = pathof_scripts + "suggestions.txt"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Reading file in start') 

    global path_of_help

    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:

        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     if id_personal != "12109646":
    #         bot.sendMessage(chat_id=id_personal, text=item)

    #     manageUsers(user_id, chat_id, item)

    ##MOSTRANDO TEXTO DE AYUDA
        if os.path.isfile(path_of_help):
            print('Fichero existente!')
            with open(path_of_help, 'r+') as file:
                if os.stat(path_of_help).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_help,'a')   # Create a file if
        file.closed

        
        

    except:
        bot.sendMessage(chat_id=id_personal, text='start function went wrong!')
        print('start function went wrong!')
        #sys.exit(0) # quit Python

    





def help(bot, update):
    print('Reading file in help') 

    global path_of_help
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")



    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)

    #     if id_personal != "12109646":
    #         bot.sendMessage(chat_id=id_personal, text=item)                
        
        if os.path.isfile(path_of_help):
            print('Fichero existente!')
            with open(path_of_help, 'r+') as file:
                if os.stat(path_of_help).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_help,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='help function went wrong!')
        print('help function went wrong!')
        #sys.exit(0) # quit Python
    

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    

def roms(bot, update):
    print('Reading file in roms') 

    global path_of_roms
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        
        item=""
        if os.path.isfile(path_of_roms):
            print('Fichero existente!')
            with open(path_of_roms, 'r+') as file:
                if os.stat(path_of_roms).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_roms,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='roms function went wrong!')
        print('roms function went wrong!')
        #sys.exit(0) # quit Python


def pictures(bot, update):
    print('Reading file in pictures') 

    global path_of_pictures
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")

        ## OPTION        
        item=""
        if os.path.isfile(path_of_pictures):
            print('Fichero existente!')
            with open(path_of_pictures, 'r+') as file:
                if os.stat(path_of_pictures).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_pictures,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='roms function went wrong!')
        print('roms function went wrong!')
        #sys.exit(0) # quit Python

def beginers(bot, update):
    print('Reading file in primeros_pasos') 

    global path_of_beginers
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


        # ##GESTIÓN DE USUARIOS
        #     user_id = update.message.from_user.id
        #     chat_id = update.message.chat_id
        #     people = update.message.from_user
        #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

        #     manageUsers(user_id, chat_id, item)

        item=""
        if os.path.isfile(path_of_beginers):
            print('Fichero existente!')
            with open(path_of_beginers, 'r+') as file:
                if os.stat(path_of_beginers).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_beginers,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='primeros_pasos function went wrong!')
        print('primeros_pasos function went wrong!')
        #sys.exit(0) # quit Python

def bootloader(bot, update):
    print('Reading file in bootloader') 

    global path_of_bootloader
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")

        item=""
                        
        
        if os.path.isfile(path_of_bootloader):
            print('Fichero existente!')
            with open(path_of_bootloader, 'r+') as file:
                if os.stat(path_of_bootloader).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_bootloader,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='bootloader function went wrong!')
        print('bootloader function went wrong!')
        #sys.exit(0) # quit Python

def emmaus(bot, update):
    print('Reading file in emmaus') 

    global path_of_emmaus
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_emmaus):
            print('Fichero existente!')
            with open(path_of_emmaus, 'r+') as file:
                if os.stat(path_of_emmaus).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_emmaus,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='emmaus function went wrong!')
        print('emmaus function went wrong!')
        #sys.exit(0) # quit Python


def faqs(bot, update):
    print('Reading file in faqs') 

    global path_of_faqs
    global id_personal


    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                    
        
        if os.path.isfile(path_of_faqs):
            print('Fichero existente!')
            with open(path_of_faqs, 'r+') as file:
                if os.stat(path_of_faqs).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_faqs,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='faqs function went wrong!')
        print('faqs function went wrong!')
        #sys.exit(0) # quit Python


def gadgets(bot, update):
    print('Reading file in gadgets') 

    global path_of_gadgets
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_gadgets):
            print('Fichero existente!')
            with open(path_of_gadgets, 'r+') as file:
                if os.stat(path_of_gadgets).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_gadgets,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='gadgets function went wrong!')
        print('gadgets function went wrong!')
        #sys.exit(0) # quit Python




def link(bot, update):
    print('Reading file in links') 

    global path_of_link
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_link):
            print('Fichero existente!')
            with open(path_of_link, 'r+') as file:
                if os.stat(path_of_link).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_link,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='links function went wrong!')
        print('links function went wrong!')
        #sys.exit(0) # quit Python     


def tools(bot, update):
    print('Reading file in tools') 

    global path_of_tools
    global id_personal

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_tools):
            print('Fichero existente!')
            with open(path_of_tools, 'r+') as file:
                if os.stat(path_of_tools).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_tools,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='tools function went wrong!')
        print('tools function went wrong!')
        #sys.exit(0) # quit Python   


def twrp(bot, update):
    print('Reading file in twrp') 

    global path_of_twrp
    global id_personal


    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_twrp):
            print('Fichero existente!')
            with open(path_of_twrp, 'r+') as file:
                if os.stat(path_of_twrp).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_twrp,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='twrp function went wrong!')
        print('twrp function went wrong!')
        #sys.exit(0) # quit Python   


def bot(bot, update):
    print('Reading file in bot') 

    global path_of_bot
    global id_personal


    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_bot):
            print('Fichero existente!')
            with open(path_of_bot, 'r+') as file:
                if os.stat(path_of_bot).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_bot,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='bot function went wrong!')
        print('bot function went wrong!')
        #sys.exit(0) # quit Python   




def server(bot, update):
    print('Reading file in server') 

    global path_of_server
    global id_personal


    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
                        
        
        if os.path.isfile(path_of_server):
            print('Fichero existente!')
            with open(path_of_server, 'r+') as file:
                if os.stat(path_of_server).st_size != 0:
                    read_data = file.read()
                    update.message.reply_text(read_data, parse_mode='HTML')
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo vacío.')
        else:
            print('Creamos fichero!')
            update.message.reply_text('Archivo vacío.')  
            file = open(path_of_server,'a')   # Create a file if
        file.closed
        

    except:
        bot.sendMessage(chat_id=id_personal, text='server function went wrong!')
        print('server function went wrong!')
        #sys.exit(0) # quit Python   


def sugg(bot, update, args):
    print('Reading file to add') 

    global path_of_suggestions
    global id_personal

    script=pathof_scripts+'sugg.sh'
    retorno = "\n"
    show=""
    item=""

    chat_id=""
    people=""
    item=""
    user_id=""
    add_id=0
    add_gr=0

    try:
        ## GESTIÓN DE USUARIOS ##
        
        tipo = str(update.message.chat.type)
        if tipo == "private":
            admin_of_users(update)
        else:
            try:
                admins = bot.getChatAdministrators(update.message.chat_id)
                # print("Admin management correct")
                admin_of_chats(update,admins)
            except:
                print("Not works admins management")


    # ##GESTIÓN DE USUARIOS
    #     user_id = update.message.from_user.id
    #     chat_id = update.message.chat_id
    #     people = update.message.from_user
    #     item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"

    #     manageUsers(user_id, chat_id, item)
        item=""
        

        arguments=len(args)
        
        if arguments == 0:
            
            update.message.reply_text('Escribe tu sugerencia tras escribir el comando /sugerencia.')
        else:
            for val in args:
                item+=val.encode('utf-8')+" "
            item+="\n"
            bot.sendMessage(chat_id=id_personal, text="Alguien ha añadido una sugerencia.")

            # subprocess.call([script])
            chat_id = update.message.chat_id
            people = update.message.from_user
        
            item="-----------------------------\nCHAT TITLE: \""+str(update.message.chat.title)+"\" chat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\nSugerencia: "+item

            with open(path_of_suggestions, "a") as file:                
                file.write(item)
                update.message.reply_text('Sugerencia añadida!')
                
            file.closed
        
    except:
        bot.sendMessage(chat_id=id_personal, text='sugg function went wrong!')
        print('sugg function went wrong!')
        #sys.exit(0) # quit Python

        

def admin(bot, update, args):
    print('Reading file to admin') 

    global id_personal

    global path_of_help

    global path_of_roms
    global path_of_gadgets
    global path_of_bootloader
    global path_of_tools
    global path_of_twrp
    global path_of_emmaus
    global path_of_faqs
    global path_of_link

    global path_of_suggestions 

    retorno = "\n"
    show=""
    item=""
    chat_id=""
    temporal=""
    avoiding=0
    try:


        if id_personal == str(update.message.from_user.id):
            arguments=len(args)
    
            if arguments == 0:
                update.message.reply_text('Comandos:\n'
                                          '/admin roms => Añadir rom.\n'
                                          '/admin gadgets => Añadir gadget.\n'
                                          '/admin bootloader => Añadir Instrucciones para desbloquear bootloader.\n'
                                          '/admin tools => Añadir tool.\n'
                                          '/admin twrp => Cambiar recovery.\n'
                                          '/admin emmaus => Añadir Material de emmaus.\n'
                                          '/admin faqs => Añadir faqs.\n'
                                          '/admin link => Cambiar Link del grupo.\n'
                                          '/admin sugg => Leer sugerencias..\n'
                                          '/admin delsugg => Borrar sugerencias.')
            else:
                
                for val in args:
                    if avoiding != 0:
                        item+=val.encode('utf-8')+" "
                    avoiding = 1    
                item+="\n"


            if args[0] == 'roms':
                with open(path_of_roms, "a") as file:                
                    file.write("\n"+item)
                    update.message.reply_text('roms añadida /roms para visualizar!')
                file.closed
            elif args[0] == 'gadgets':
                with open(path_of_gadgets, "a") as file:                
                    file.write("\n"+item)
                    update.message.reply_text('gadgets añadida /gadgets para visualizar!')
                file.closed
            elif args[0] == 'bootloader':
                with open(path_of_bootloader, "a") as file:                
                    file.write("\n"+item)
                    update.message.reply_text('bootloader añadida /bootloader para visualizar!')
                file.closed
            elif args[0] == 'tools':
                with open(path_of_tools, "a") as file:                
                    file.write("\n"+item)
                    update.message.reply_text('tools añadida /tools para visualizar!')
                file.closed
            elif args[0] == 'twrp':
                temporal="/help => Para ver todos los comandos.\n\n"+item
                with open(path_of_twrp, "w") as file:                
                    file.write(temporal)
                    update.message.reply_text('twrp añadida /twrp para visualizar!')
                file.closed
            elif args[0] == 'emmaus':
                with open(path_of_emmaus, "a") as file:                
                    file.write("\n"+item)
                    update.message.reply_text('emmaus añadida /emmaus para visualizar!')
                file.closed
            elif args[0] == 'faqs':
                with open(path_of_faqs, "a") as file: 
                    file.write("\n"+item)
                    update.message.reply_text('faqs añadida /faqs para visualizar!')
                file.closed
            elif args[0] == 'link':
                temporal="/help => Para ver todos los comandos.\n\n"+item
                with open(path_of_link, "w") as file:                
                    file.write(temporal)
                    update.message.reply_text('link añadida /link para visualizar!')
                file.closed
            elif args[0] == 'sugg':
                try:                
                    if os.path.isfile(path_of_suggestions):
                        print('Fichero existente!')
                        with open(path_of_suggestions, 'r+') as file:
                            if os.stat(path_of_suggestions).st_size != 0:
                                read_data = file.read()
                                update.message.reply_text(read_data, parse_mode='HTML')
                            else:
                                print('Fichero vacío.')
                                update.message.reply_text('Archivo vacío.')
                    else:
                        print('Creamos fichero!')
                        update.message.reply_text('Archivo vacío.')  
                        file = open(path_of_suggestions,'a')   # Create a file if
                    file.closed
                    

                except:
                    update.message.reply_text('read function went wrong!')
                    print('read function went wrong!')
            elif args[0] == 'delsugg':
                with open(path_of_suggestions, "w") as file:                
                    file.write("")
                    update.message.reply_text('Sugerencias borradas!')
                file.closed
        
        else:
            update.message.reply_text('Solo el admin puede ejecutar este comando!')
            chat_id = update.message.chat_id
            people = update.message.from_user
            
            item="El siguiente usuario ejecutó el codigo ADMIN.\nChat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"
            bot.sendMessage(chat_id=id_personal, text=item)
  
    except:
        # bot.sendMessage(chat_id=id_personal, text='admin function went wrong!')
        print('admin function always wrong!')
        #sys.exit(0) # quit Python

def echo(bot, update, args):

    global id_gupo_zuk
    global id_personal

    item=""

    try:
        if id_personal == str(update.message.chat_id):
            arguments=len(args)
        
            if arguments == 0:
                update.message.reply_text('Escribe tu publicacion tras escribir el comando /publicar.')
            else:
                for val in args:
                    item+=val+" "
                item+="\n"
                
                bot.sendMessage(chat_id=id_gupo_zuk, text=item)
        else:
            update.message.reply_text('Solo el admin puede ejecutar este comando!')
            chat_id = update.message.chat_id
            people = update.message.from_user
            
            item="El siguiente usuario ejecutó el codigo PUBLICACIÓN.\nChat_id: "+str(chat_id)+"\nFrom User:"+str(people)+"\n\n"
            bot.sendMessage(chat_id=id_personal, text=item)

        

    except:
        bot.sendMessage(chat_id=id_personal, text='publicacion function went wrong!')
        print('publicacion function went wrong!')
        #sys.exit(0) # quit Python
      

def manageUsers(userId, chatID, itemToPrint):

    global path_of_users
    global path_of_ids
    global id_personal

    chat_id= chatID
    item= itemToPrint
    user_id= userId
    add_id=0
    add_gr=0

    try:
    ##GESTIÓN DE USUARIOS

        if os.path.isfile(path_of_ids):
            print('Fichero existente!')

            with open(path_of_ids, 'r+') as file:
                if os.stat(path_of_ids).st_size != 0:
                    read_data = file.readlines()
                    for line in read_data:
                        # print("*"+line+"* - *"+str(user_id)+"* - *"+str(chat_id)+"*")
                        if line == str(user_id)+"\n":
                            add_id=1
                        if line == str(chat_id)+"\n":
                            add_gr=1
                else:
                    print('Fichero vacío.')
                    update.message.reply_text('Archivo de usuarios vacío.')

        if add_id == 0:
            print("Nuevo user id")
            with open(path_of_ids, "a") as file:                
                file.write(str(user_id)+"\n")
            file.closed
        else:
            print("User id ya existente.")

        if add_gr == 0:
            print("Nuevo chat id")
            with open(path_of_ids, "a") as file:                
                file.write(str(chat_id)+"\n")
            file.closed
        else:
            print("Chat id ya existente")

        if add_id == 0:
            print("user id add")
            with open(path_of_users, "a") as file:                
                file.write(item)
            file.closed 
        elif add_gr == 0:
            print("chat id add")
            with open(path_of_users, "a") as file:                
                file.write(item)
            file.closed



    except:
        bot.sendMessage(chat_id=id_personal, text='MANAGE USERS function went wrong!')
        print('MANAGE USERS function went wrong!')
    
    return




def admin_of_users(update):
    print('\nCOME ON WITH admin_of_users') 

    global path_of_help
    global id_personal

    query_user = ("""INSERT INTO USUARIOS VALUES (%s,%s,%s,%s,%s,%s)""")
    query_chat = ("""INSERT INTO CHATS VALUES (%s,%s,%s)""")
    query_chat_users = ("""INSERT INTO CHAT_USERS VALUES (%s,%s,%s)""")
    query_chat_admins = ("""INSERT INTO CHAT_ADMINS VALUES (%s,%s,%s)""")

    try:

        db = MySQLdb.connect("localhost","films_manager","films_pass","telegram_users" )
        cursor = db.cursor()


        ##  USUARIOS  ##

        user_id = update.message.from_user.id
        username = str(update.message.from_user.username)
        firstname = str(update.message.from_user.first_name).encode('utf-8')
        lastname = str(update.message.from_user.last_name).encode('utf-8')
        tipo = str(update.message.from_user.type)

        try:
            if id_personal == str(user_id):
                cursor.execute(query_user, (user_id, username, firstname, lastname, tipo, 2))
            else:
                cursor.execute(query_user, (user_id, username, firstname, lastname, tipo, 0)) # USUARIOS(id, username, firstname, lastname, type, superuser)
            db.commit()
        except:
            print(" - existing USER")
            db.rollback()


        print("FINALIZED admin_of_users\n")
        db.close()
    except:
        bot.sendMessage(chat_id=id_personal, text='admin_of_users function went wrong!')
        print('admin_of_users function went wrong!')



def admin_of_chats(update,administrators):
    print('\nCOME ON WITH admin_of_users') 

    global path_of_help
    global id_personal

    query_user = ("""INSERT INTO USUARIOS VALUES (%s,%s,%s,%s,%s,%s)""")
    query_chat = ("""INSERT INTO CHATS VALUES (%s,%s,%s)""")
    query_chat_users = ("""INSERT INTO CHAT_USERS VALUES (%s,%s,%s)""")
    query_chat_admins = ("""INSERT INTO CHAT_ADMINS VALUES (%s,%s,%s)""")

    try:

        db = MySQLdb.connect("localhost","films_manager","films_pass","telegram_users" )
        cursor = db.cursor()


        ##  USUARIOS  ##

        user_id = update.message.from_user.id
        username = str(update.message.from_user.username)
        firstname = str(update.message.from_user.first_name).encode('utf-8')
        lastname = str(update.message.from_user.last_name).encode('utf-8')
        tipo = str(update.message.from_user.type)

        try:
            if id_personal == str(user_id):
                cursor.execute(query_user, (user_id, username, firstname, lastname, tipo, 2))
            else:
                cursor.execute(query_user, (user_id, username, firstname, lastname, tipo, 0)) # USUARIOS(id, username, firstname, lastname, type, superuser)
            db.commit()
        except:
            print(" - existing USER")
            db.rollback()


        # print(update.message.chat)
        # print(update.message.chat.id)
        # print(update.message.chat.title)
        # print(update.message.chat.type)

        ##  CHATS  ##

        id_of_chat=update.message.chat.id
        chat_title=str(update.message.chat.title)

        for i in administrators:
            if str(i.status) == "creator":
                admin_chat = i.user.id
                # print("ADMINISTRATORS")
                # print(admin_chat)
        try:
            cursor.execute(query_chat, (id_of_chat, chat_title, admin_chat)) # CHATS(id, title, creator)
            db.commit()
        except:
            print(" - existing CHAT")
            db.rollback()


        
       ##  CHAT_USERS  ##
        
        try:
            try:
                cursor.execute(""" SELECT count(*) FROM CHAT_USERS """)
            except:
                print("not working")

            for (num,) in cursor:
                user_num=int(num)+1
                # print(user_num)
            cursor.execute(""" SELECT count(*) FROM CHAT_USERS where group_id = %s and user_id = %s """, (update.message.chat.id, user_id))
            for (number_of,) in cursor:
                # print(number_of)
                if int(number_of) == 0:
                    try:
                        cursor.execute(query_chat_users, (user_num, update.message.chat.id, user_id)) # chat_USERS(Numero, group_id, user_id)
                        db.commit()
                        print(" - ADDED chat_USER")
                    except:
                        print(" - existing chat_USER")
                        db.rollback()
                else:
                    print(" - existing chat_USER")
            
            db.commit()
        except:
            print(" - existing chat_USER")
            db.rollback()


        ##  CHAT_ADMINS  ##
        try:

            try:
                cursor.execute(""" SELECT count(*) FROM CHAT_ADMINS """)
            except:
                print("not working")

            for (num,) in cursor:
                admin_num=int(num)+1
                # print(admin_num)

            # print("\nShow admins")
            for i in administrators:
                # print(i.status)
                # print(i.user.id)

                try:
                    cursor.execute(""" SELECT count(*) FROM CHAT_ADMINS where group_id = %s and user_id = %s """, (update.message.chat.id,i.user.id))
                    for (number_of,) in cursor:
                        # print(number_of)
                        if int(number_of) == 0:
                            try:
                                cursor.execute(query_chat_admins, (admin_num, update.message.chat.id, i.user.id)) # CHAT_ADMINS(Numero, group_id, user_id)
                                db.commit()
                                admin_num=admin_num+1
                                print(" - ADDED chat_ADMINS")
                            except:
                                db.rollback()
                                print(" - existing chat")
                        else:
                            print(" - existing chat")
                    db.commit()
                except:
                    print("Not works admins number")
                    db.rollback()
        except:
            print(" - existing chat")
            



        print("FINALIZED admin_of_users\n")
        db.close()
    except:
        bot.sendMessage(chat_id=id_personal, text='admin_of_users function went wrong!')
        print('admin_of_users function went wrong!')




def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ese comando no existe pulse /help")

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
    
    global TOKEN
    
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    #unknown commands handler
    unknown_handler = MessageHandler(Filters.command, unknown)

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("roms", roms))
    dp.add_handler(CommandHandler("fotos", pictures))
    dp.add_handler(CommandHandler("inicio", beginers))

    dp.add_handler(CommandHandler("bootloader", bootloader))
    dp.add_handler(CommandHandler("emmaus", emmaus))
    dp.add_handler(CommandHandler("faqs", faqs))
    dp.add_handler(CommandHandler("gadgets", gadgets))
    dp.add_handler(CommandHandler("link", link))
    dp.add_handler(CommandHandler("tools", tools))
    dp.add_handler(CommandHandler("twrp", twrp))
    dp.add_handler(CommandHandler("bot", bot))
    dp.add_handler(CommandHandler("servidor", server))
    dp.add_handler(CommandHandler("admin", admin, pass_args=True))
    dp.add_handler(CommandHandler("sugerencia", sugg, pass_args=True))
    
    dp.add_handler(CommandHandler("publicar", echo, pass_args=True))


    dp.add_handler(unknown_handler)



    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
