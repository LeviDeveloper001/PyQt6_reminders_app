PATH_TO_STYLES_FILE='C:\\Users\\Лев\\Desktop\\programs\\desktop_python\\reminders_app\\app\\static\\styles\\style.css'

def get_styles():
    with open(PATH_TO_STYLES_FILE, 'r', encoding='utf-8') as file:
        return file.read()