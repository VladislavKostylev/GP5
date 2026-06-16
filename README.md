# GP5 — Deep Learning

### О работе

**Заказчик** — селлер на маркетплейсе **Ozon** в категории «Мужская одежда»
У селлера две практические задачи на одних и тех же данных:

1. **Куда вкладывать бюджет** - какие товары ведут себя как лидеры по продажам.
2. **Проверка карточки товара** - соответствует ли превью заявленной нише.

### Данные

Источник = MPStats, категория «Мужская одежда»

Объем - 41,3 млн строк, 16 столбцов

<img width="482" height="497" alt="Данные в таблице" src="https://github.com/user-attachments/assets/380800c6-97a4-4bcb-9831-1ce991bda1a7" />

### EDA

Изучили пропуски по признакам

<img width="575" height="573" alt="Пропуски" src="https://github.com/user-attachments/assets/298fafb3-64a7-4099-9e4b-8c51cdfcd029" />

Посмотрели распредеделение продаж по количеству и по различным нишам

<img width="649" height="462" alt="Распределение продаж по количеству" src="https://github.com/user-attachments/assets/4a0f14d2-c2fa-4503-8760-e7579720c524" />

<img width="1058" height="356" alt="Распределение по нишам" src="https://github.com/user-attachments/assets/7f2a4e69-3126-47ca-969c-3de76d4b9c6f" />

Провери корреляцию по числовым признакам

<img width="798" height="592" alt="Корреляция" src="https://github.com/user-attachments/assets/780c43f9-7bc0-4d80-a176-494c50715417" />



Ввели целевую переменную high_sales

Смотрим только на товары с Sales > 0

high_sales = 1, если товар входит в топ 25 процентов по продажам, иначе high_sales = 0

Для товаров Sales = 0 считаем, что high_sales = 0

<img width="652" height="456" alt="Соотношение целевой переменной" src="https://github.com/user-attachments/assets/1528a0f5-7b01-45a4-a999-8b566c2e55e4" />


### Задача A

Сравни 3 конфигурации: 
| Модель | Суть |
|--------|------|
| `fc_shallow` | слои `[128, 64]`, Adam |
| `fc_deep` | слои `[256, 128, 64]`, Adam |
| `fc_deep_dropout_sgd` | `[256, 128, 64]` + Dropout 0.3, SGD |

Метрики

<img width="654" height="464" alt="Метрики моделей" src="https://github.com/user-attachments/assets/445e4922-e47d-4e29-bdbd-98fda44887a6" />


Логи обучения 
([`ozon_fc`](https://wandb.ai/mooninvader-hse/ozon_fc))

### Задача B

Мультиклассовая классификация **ниши по фото**

<img width="1044" height="402" alt="Превью по нишам" src="https://github.com/user-attachments/assets/d8ca0d17-8391-4cd6-aa33-b3b16d959c43" />

Сравнили **3 архитектуры** на картинках 64×64:

| Модель | Суть |
|--------|------|
| `img_fc_baseline` | FC без свёрток |
| `img_lenet` | LeNet-подобная CNN |
| `img_deepcnn` | глубокая CNN |

**Метрики**

<img width="630" height="459" alt="Метрики" src="https://github.com/user-attachments/assets/885be2ad-7f92-42f7-8607-e2a167b51cee" />

<img width="757" height="398" alt="По эпохам" src="https://github.com/user-attachments/assets/761a3ecb-5468-44ee-9bc0-c8dc394ec822" />

**Логи обучения** ([`ozon_cnn`](https://wandb.ai/mooninvader-hse/ozon_cnn))


### Вывод для заказчика

**Задача A** 

Табличная сеть хорошо отделяет лидеров по продажам от остальных. Результаты можно использовать для ранжирование своих товаров для рекламы и закупки

**Задача B** 

По превью карточки CNN определяет нишу с accuracy до **~94%**. Подходит для проверки соответвия картинки для ниши и может быть использована для определения ниши по фотографии

