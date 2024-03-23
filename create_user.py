from db_cmnds import BotDB


BotDB = BotDB('./usr_list.db')


def create_usr(login, mail, password):
    if BotDB.user_exists(login):
        # print("username alredy taken!")
        return "usr_taken_error"

    elif BotDB.user_exists_mail(mail):
        # print("mail alredy taken!")
        return "mail_taken_error"

    else:
        BotDB.add_main_user(login, mail, password)
        # print("registered")
        return "success_reg"

def login_usr(login, mail, password):
    if BotDB.user_exists(login):
        if BotDB.is_mail_login(login) == mail:
            if BotDB.is_mail_pass(login) == password:
                # print("successifully logined!")
                return "success_login"
            else:
                # print("wrong password")
                return "error_password_login"

        else:
            # print("wrong mail")
            return "error_mail_login"

    # print("wrong login")
    return "error_usrname_login"
