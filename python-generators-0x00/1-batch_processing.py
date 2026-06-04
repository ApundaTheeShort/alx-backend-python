from seed import connect_to_prodev

# if __name__ == "__main__":


def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    if connection:
        # print("connection made")
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM user_data WHERE AGE > 25 ORDER BY name ASC")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                # print("breaking")
                break
            yield batch
            # print("batch yielded")

        cursor.close()
        connection.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            print(user)
