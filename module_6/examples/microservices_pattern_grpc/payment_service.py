from concurrent.futures import ThreadPoolExecutor
import grpc
import payment_pb2
import payment_pb2_grpc


class PaymentServiceImpl(payment_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        return payment_pb2.PaymentResponse(payment_id="12345", status="SUCCESS")


def main():
    print("Payment Processing Service ready!")
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentServiceImpl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()

#Наш файл payment.proto - це "закон" по якому ісе діє
#буває що мікросервіси пишуться різними мовами, але для усіх proto спільний
#Він не дає зроюити будь який запит окрім щапиту на оплату (замовлення і число)
#PaymentService - це наш виконавець і в ньому max_workers = 10, тобто він може обробляти 10 платежів одночасно
#Це потрібно, бо мікросервіси мають бути масштабовані
#Client - це просто клієнт нашого мікросервісу
