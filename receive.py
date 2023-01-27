import pika

HOST_NAME = "localhost"
QUEUE_NAME = "snowdeer_queue"


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST_NAME))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, arguments={'x-message-ttl' : int(1000)})

    def callback(ch, method, properties, body):
        print("Message is Arrived %r" % body)

    channel.basic_consume(queue=QUEUE_NAME,
                          on_message_callback=callback,
                          auto_ack=True)

    try:
        print("Waiting for messages.")
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Ctrl+C is Pressed.')


if __name__ == '__main__':
    main()