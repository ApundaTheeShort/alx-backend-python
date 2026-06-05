from seed import connect_to_prodev


def stream_user_ages():
    """Stream user ages from a database."""
    # Simulate streaming ages from a database

    # for age in [25, 30, 35, 40, 45]:
    #     yield age
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT AGE FROM user_data WHERE AGE > 25 ORDER BY name ASC")

        while True:
            age = cursor.fetchone()
            if not age:
                break
            for age in age.values():
                yield age

        cursor.close()
        connection.close()


def calculate_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average_age = total_age / count if count > 0 else 0
    return average_age


a = stream_user_ages()
# for age in a:
# print(age)


print("Average Age:", calculate_average_age())
