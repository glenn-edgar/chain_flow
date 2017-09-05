
from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

def test_function_1(  cf_handle, chainObj, parameters, event ):
   print("one step test function ")
   print("parameters",parameters)
   print("event",event)

def test_function_2(  cf_handle, chainObj, parameters, event ):
   return_value = "HALT"
   print("code function acting like a one step function ")
   if event["name"] == "INIT":
      print("executing init function")
   else:
      return_value = "DISABLE"
   return return_value

def test_function_3(  cf_handle, chainObj, parameters, event ):
    if event["name"] == "TIME_TICK":
        print("test_function_3  ",event)
    return "CONTINUE"
 

def test_function_4(  cf_handle, chainObj, parameters, event ):
    return_value = "HALT"
    if event["name"] == "TIME_TICK":
       if event["data"] == 59:
          return_value = "DISABLE"
 
    return return_value
     
def test_function_5(  cf_handle, chainObj, parameters, event ):
   print(event)
cf = CF_Base_Interpreter()


cf.define_chain("Chain_1", False)   # this function demonstrates the One Set function
cf.insert.one_step( test_function_1, "parm1","parm2",[1,2,3,4,5] )
cf.insert.wait_event_count( count = 10)
cf.insert.reset( )


cf.define_chain("Chain_2", False)   # this shows example of code function
cf.insert.code( test_function_2, "parm1","parm2",[1,2,3,4,5] )
cf.insert.code( test_function_3, "parm1","parm2",[1,2,3,4,5] )
cf.insert.code( test_function_4, "parm1","parm2",[1,2,3,4,5] )
cf.insert.log("Resetting Chain_2")
cf.insert.reset( )


cf.define_chain("Chain_3", True)  #demonstration of sending and event
cf.insert.send_event("Test_Event_1",1)
cf.insert.send_event("Test_Event_2",2)
cf.insert.wait_event_count( count = 5)
cf.insert.reset()

cf.define_chain("Chain_4",False) # catching an event with wait_event_count
cf.insert.wait_event_count(event = "Test_Event_2", count = 1 )
cf.insert.log("Test_Event_2 occurred ")
cf.insert.wait_event_count(event = "Test_Event_1",count = 3 )
cf.insert.log("Test_Event_1 has occurred" )
cf.insert.log("Chain 4 is reset")
cf.insert.reset()

cf.define_chain("Chain_5",True) # example of check event
cf.insert.check_event(test_function_5,"Test_Event_1" )
cf.insert.check_event(test_function_5,"Test_Event_2" )
cf.insert.reset()






cf.execute()

