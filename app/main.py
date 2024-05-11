class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
            ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    
    def serve_cars(self, cars: list[Car]) -> float:
        total_cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_cost, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating_mark: float) -> None:
        self.average_rating = round(((self.average_rating * self.count_of_ratings + rating_mark) / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1


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

ford = Car(comfort_class=2, clean_mark=1, brand='Ford')
wash_cost = wash_station.calculate_washing_price(ford)

print(wash_cost) # 9.1
print(ford.clean_mark) # 1

wash_station.count_of_ratings == 42
wash_station.average_rating == 4.4

wash_station.rate_service(4)

print(wash_station.count_of_ratings) # 43
print(wash_station.average_rating) # 4.4
