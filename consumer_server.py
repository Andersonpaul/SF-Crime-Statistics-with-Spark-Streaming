from kafka import KafkaConsumer
import json


def consumer_start():
     consumer = KafkaConsumer(
    'SF_Crime_Statistics',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True
     #value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                              )
    
     #print ("testing testing")
    
     for message in consumer:
        message = (message.value).decode('utf-8')
        print(message)

if __name__ == "__main__":
    consumer_start()