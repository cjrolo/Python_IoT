from gattlib import GATTRequester, GATTResponse

termo_peaners = [GATTRequester("00:A0:50:01:11:2B"),
                 GATTRequester("00:A0:50:0C:0F:24"),
                 GATTRequester("00:A0:50:06:27:14")]
response = GATTResponse()

for req in termo_peaners:
    #req.read_by_handle_async(0x15, response)
    print(req.read_by_handle(0x15))
    
    #while not response.received():
    #    time.sleep(0.1)
    #print(response)
