import time
# Объявляем адрес страницы
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 

# Запускаем тест
def test_add_to_cart_button_is_displayed(browser):
    # Открываем ссылку в драйвере
    browser.get(link)
    # Находим кнопку по имени класса
    button_basket = browser.find_element_by_class_name('btn-add-to-basket')
    # Ассерт на наличие кнопки
    assert button_basket is not None, 'ERROR: Button basket is NOT found'
