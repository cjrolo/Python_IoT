from gattlib import GATTRequester, GATTResponse

termo_peaners = GATTRequester("00:A0:50:01:11:2B")
#response = GATTResponse()

    #req.read_by_handle_async(0x15, response)
steps = termo_peaners.read_by_handle(0x15)[0]
print(steps)
    #while not response.received():
    #    time.sleep(0.1)
    #print(response)
