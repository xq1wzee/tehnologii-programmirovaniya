from chain import ConcreteHandlerA, ConcreteHandlerB, Request, RequestType

def main():
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next_handler(handler_b)
    request_a = Request(RequestType.TYPE_A)
    request_b = Request(RequestType.TYPE_B)
    handler_a.handle_request(request_a)
    handler_a.handle_request(request_b)

if __name__ == "__main__":
    main()