    # Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
    # Specify your login credentials
username = "desshub"
apikey   = "b8a87060086b16297c5ebe5190964f09fd258ec51a969ad88cd8c131243ef8fc"

def get_phone_number():
    input_var = raw_input("Enter phone no ,including country code: ")
    return input_var

def sendMessage():
        # Specify the numbers that you want to send to in a comma-separated list
        # Please ensure you include the country code (+254 for Kenya)
    phone = get_phone_number()
    to    = phone
        # And of course we want our recipients to know what we really do
    message = "Hello andela"
        # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)
        # Any gateway errors will be captured by our custom Exception class below,
        # so wrap the call in a try-catch block
    try:
            # Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)

        for recipient in results:
                # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                    recipient['status'],
                                                                    recipient['messageId'],
                                                                    recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)



sendMessage()
