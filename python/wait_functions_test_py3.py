
from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

def test_function_1(  cf_handle, chainObj, parameters, event ):
   print("test function 1 ",event)

def wait_test_function( cf_handle, chainObj, parameters, event ):
   print("event",event)
   return_value = False
   if event["name"] == "INIT":
       parameters.append(0)
   if event["name"] == "TIME_TICK":
      parameters[-1] = parameters[-1] +1
      if parameters[-1] >= parameters[1]:
          return_value = True
   return return_value

cf = CF_Base_Interpreter()

 
cf.define_chain("Chain_1", False)   # wait_tod
cf.insert.log("Chain 1 started")
cf.insert.wait_tod( "*","*","*",15 )  # wait for 15 seconds
cf.insert.one_step( test_function_1)
cf.insert.log("Chain 1 is reset")
cf.insert.reset( )


cf.define_chain("Chain_2",False)   # wait_tod_ge wait_tod_le
cf.insert.log("Chain 2 started")
cf.insert.wait_tod_ge( "*","*","*",45 )  # wait for 15 seconds
cf.insert.check_event( test_function_1, "TIME_TICK" )
cf.insert.wait_tod_le( "*","*","*",15)  # wait for 15 seconds
cf.insert.reset( )


cf.define_chain("Chain_3",False)  #wait_event_count
cf.insert.log("Chain 3 started")
cf.insert.wait_event_count(count = 10)
cf.insert.one_step( test_function_1)
cf.insert.reset()

cf.define_chain("Chain_4",True) # wait_function
cf.insert.log("Chain 4 has started")
cf.insert.wait_function(wait_test_function, 10 )
cf.insert.log("Chain 4 is ended ")
cf.insert.reset()


cf.execute()

