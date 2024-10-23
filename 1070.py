def convert_to_minutes(time_str):
    hours, minutes = map(int, time_str.split('.'))
    return hours * 60 + minutes


def calculate_flight_duration(departure, arrival):
    # Учитываем переход через полночь
    if arrival < departure:
        arrival += 24 * 60
    return arrival - departure


def time_difference(t1, t2, t3, t4):
    # Преобразуем время в минуты
    t1_minutes = convert_to_minutes(t1)
    t2_minutes = convert_to_minutes(t2)
    t3_minutes = convert_to_minutes(t3)
    t4_minutes = convert_to_minutes(t4)

    # Рассчитываем продолжительность полётов
    duration1 = calculate_flight_duration(t1_minutes, t2_minutes)
    duration2 = calculate_flight_duration(t3_minutes, t4_minutes)

    # Рассчитываем среднее время полёта
    average_duration = (duration1 + duration2) / 2

    # Рассчитываем разницу между часовыми поясами
    time_diff = abs(duration1 - duration2) / 2

    # Преобразуем минуты в часы и округляем
    time_diff_hours = round(time_diff / 60)
    if time_diff_hours > 5:
        return 5
    return time_diff_hours

t1, t2 = input().split()
t3, t4 = input().split()
print(time_difference(t1, t2, t3, t4))

