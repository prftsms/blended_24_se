# blended-practice

---

## Автомийка

Ви маєте автомийку і прагнете автоматизувати розрахунок вартості мийки. Вартість визначається залежно від класу комфорту автомобіля, його чистоти, рейтингу мийки та її відстані від центру міста.

### Класи та методи

1. `Car` - представляє автомобіль:

   - `comfort_class` - клас комфорту автомобіля (1-7),
   - `clean_mark` - ступінь чистоти автомобіля (1-10),
   - `brand` - марка автомобіля.

2. `CarWashStation` - представляє мийку:
   - `distance_from_city_center` - відстань до центру міста (1.0-10.0),
   - `clean_power` - максимальний рівень чистоти, який може забезпечити мийка (1-10)
   - `average_rating` - середній рейтинг мийки (1.0-5.0), округлений до одного десяткового,
   - `count_of_ratings` - кількість оцінок мийки.

Методи класу `CarWashStation`:

- `serve_cars(cars: List[Car]) -> float` - приймає список автомобілів `Car` і миє лише ті, чия чистота менша за `clean_power`. Повертає дохід від обслуговування цих автомобілів (округлений до одного десяткового).

- `calculate_washing_price(car: Car) -> float` - розраховує вартість мийки одного автомобіля.
- _Вартість мийки, округлена до одного десяткового_.
- Вартість обраховується за формулою:

```
cost = comfort_class * (clean_power - clean_mark) * average_rating / distance_from_city_center
```

- `wash_single_car(car: Car) -> None` - миє один автомобіль, так що його чистота стає рівною `clean_power` мийки, якщо `clean_power` мийки більше, ніж `clean_mark` автомобіля.

- `rate_service(rating: float) -> None` - додає одну оцінку до мийки, і на основі цієї оцінки змінюються `average_rating` та `count_of_ratings`.

````python

-

### Приклад використання

```python
bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')
mercedes = Car(comfort_class=7, clean_mark=1, brand='Mercedes')

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

income = wash_station.serve_cars([bmw, audi, mercedes])

print(income) # 41.7

print(bmw.clean_mark)  # 8
print(audi.clean_mark) # 9
print(mercedes.clean_mark) # 8

# audi не помито, тому що ступінь чистоти (clean_mark) більша за максимальний рівень очищення (clean_power) мийки

````

---

```python
ford = Car(comfort_class=2, clean_mark=1, brand='Ford')
wash_cost = wash_station.calculate_washing_price(ford)

print(wash_cost) # 9.1
print(ford.clean_mark) # 1

# вартість розрахована, але автомобіль не митий
```

```python
# оцінка мийки

wash_station.count_of_ratings == 42
wash_station.average_rating == 4.4

wash_station.rate_service(4)

print(wash_station.count_of_ratings) # 43
print(wash_station.average_rating) # 4.4


```
