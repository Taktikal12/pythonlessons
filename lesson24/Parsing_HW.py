from bs4 import BeautifulSoup
import csv
import requests


def get_data_from_page(page_num):
    import requests
    from bs4 import BeautifulSoup

    url = f'https://lalafo.kg/kyrgyzstan/zhivotnye-2/?page={page_num}'
    print(f"Парсим страницу {page_num}...")
    items = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ads = soup.find_all('article', class_="lf-ad-tile")

    for ad in ads:
        try:
            # Ищем все p с классом LFSubHeading
            p_tags = ad.find_all('p', class_='LFSubHeading')

            # p_tags[0] — описание животного
            # p_tags[1] — цена (иногда наоборот, надо проверять)
            if len(p_tags) >= 2:
                description = p_tags[0].text.strip()
                price = p_tags[1].text.strip()
            elif len(p_tags) == 1:
                description = p_tags[0].text.strip()
                price = 'Цена не указана'
            else:
                description = 'Нет описания'
                price = 'Нет цены'

            # Название объявления (внутри <span class="LFCaption">)
            title_tag = ad.find('span', class_='LFCaption')
            title = title_tag.text.strip() if title_tag else 'Нет заголовка'

            print(f'Заголовок: {title}')
            print(f'Описание: {description}')
            print(f'Цена: {price}')
            print('-' * 40)

            items.append({
                'title': title,
                'description': description,
                'price': price
            })

        except Exception as e:
            print(f'Ошибка при парсинге объявления: {e}')
            continue

    return items



# Открытие CSV файла для записи
with open('animals_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'price', 'description'])
    writer.writeheader()  # Запись заголовка

    # Сбор данных с 50 страниц
    for page in range(1, 51):
        print(f"Парсим страницу {page}...")
        page_data = get_data_from_page(page)

        # Запись данных на текущей странице в файл
        for item in page_data:
            writer.writerow(item)

# Закрытие браузера
# driver.quit()

print("Парсинг завершен! Данные сохранены в файл 'animals_data.csv'.")
