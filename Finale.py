from selenium import webdriver


driver = webdriver.Chrome()
# 1. Открыть страницу http://google.com/ncr
driver.get("http://google.com/ncr")

# 2. Выполнить поиск слова “selenide”
driver.find_element('xpath', './/input[contains(@class, "gLFyf")]').send_keys('selenide\n')

# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
assert 'selenide.org' in driver.find_element('tag name', 'cite').text

# 4. Перейти в раздел поиска изображений
driver.find_element('link text',"Images").click()

# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
assert "selenide.org" in driver.find_element('xpath', '//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text

# 6. Вернуться в раздел поиска Все
driver.find_element('link text', "Все").click()

# 7. Проверить, что первый результат такой же, как и на шаге 3.
assert 'selenide.org' in driver.find_element('tag name', 'cite').text

