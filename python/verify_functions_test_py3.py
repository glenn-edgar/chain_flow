
import datetime
import time



from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

def test_function_1(  cf_handle, chainObj, parameters, event ):
   print("test function 1 ",event)

def test_function_2( *args):
   time_stamp = datetime.datetime.today()
   print("Seconds ",time_stamp.second)

def verify_test_function( cf_handle, chainObj, parameters, event ):
   print("verify test function   event",event)
   return_value = True
   if event["name"] == "INIT":
       parameters.append(0)
       return_value = True
   if event["name"] == "TIME_TICK":
      parameters[-1] = parameters[-1] +1
      if parameters[-1] >= parameters[-2]:
          return_value = False
   return return_value

cf = CF_Base_Interpreter()

cf.define_chain("Chain_11",False) # verify_tod_reset  chain should reset unless time is 30 seconds
cf.insert.log("Chain 11 started")
cf.insert.verify_tod_reset(second = 30, reset_event = "Test_Event_1", reset_data = "Chain 11 reset" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 11 is ended ")

cf.define_chain("Chain_12",False) # verify_tod_terminate chain should terminate unless time is 30 seconds
cf.insert.log("Chain 12 started")
cf.insert.verify_tod_terminate( second = 30, reset_event = "Test_Event_1", reset_data = "Chain 12 terminated" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 12 is ended ")



cf.define_chain("Chain_21",True) # verify_tod_ge_reset  chain should reset unless time is greater than 30 seconds
cf.insert.log("Chain 21 started")
cf.insert.verify_tod_ge_reset(second = 30, reset_event = "Test_Event_1", reset_data = "Chain 21 reset" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 21 is ended ")

cf.define_chain("Chain_22",True) # verify_tod_ge_terminate  chain should terminate unless time is greater than 30 seconds
cf.insert.log("Chain 22 started")
cf.insert.verify_tod_ge_terminate( second = 30, reset_event = "Test_Event_1", reset_data = "Chain 22 terminated" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 22 is ended ")



cf.define_chain("Chain_31",False) # verify_tod_le_reset  chain should reset unless time is less than 30 seconds
cf.insert.log("Chain 31 started")
cf.insert.verify_tod_le_reset(second = 30, reset_event = "Test_Event_1", reset_data = "Chain 31 reset" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 31 is ended ")

cf.define_chain("Chain_32",False) # verify_tod_le_terminate  chain should terminate unless time is less than 30 seconds
cf.insert.log("Chain 32 started")
cf.insert.verify_tod_le_terminate( second = 30, reset_event = "Test_Event_1", reset_data = "Chain 32 terminated" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 32 is ended ")


 
cf.define_chain("Chain_41",False) # verify_not_event_count_reset  chain should reset in 10 seconds
cf.insert.log("Chain 41 started")
cf.insert.verify_not_event_count_reset( count = 5, reset_event = "Test_Event_1", reset_data = "Chain 41 reset" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 41 is ended ")

cf.define_chain("Chain_42",False) # verify_not_event_count_terminate  chain should reset in 10 seconds
cf.insert.log("Chain 42 started")
cf.insert.verify_not_event_count_terminate( count = 10, reset_event = "Test_Event_1", reset_data = "Chain 42 terminated" )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 42 is ended ")



cf.define_chain("Chain_51",False) # verify_test_function_reset  chain should reset in 10 seconds
cf.insert.log("Chain 51 started")
cf.insert.verify_function_reset( "Test_Event_1","Chain 51 reset",verify_test_function,  10 )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 51 is ended ")


cf.define_chain("Chain_52",False) # verify_test_function_terminate  chain should terminate in 10 seconds
cf.insert.log("Chain 52 started")
cf.insert.verify_function_terminate(  "Test_Event_1","Chain 52 terminating",verify_test_function, 10 )
cf.insert.wait_event_count(event = "Bogus_Blocking_event")  # will block chain
cf.insert.log("Chain 52 is ended ")
cf.insert.reset()





cf.define_chain("Chain_15",True) # display verify event verify event
cf.insert.check_event( test_function_1, event = "Test_Event_1")
cf.insert.check_event( test_function_2, event = "TIME_TICK")
cf.execute()

'''

   def verify_tod_terminate( self, dow="*",hour="*",minute="*",second="*", reset_event = None ):
       self.cf.insert_link("Verify_Tod",[dow,hour,minute,second,reset_event, False] )

   def verify_tod_ge_terminate( self, dow="*",hour="*",minute="*",second="*",reset_event = None ):
       self.cf.insert_link("Verify_Tod_GE",[dow,hour,minute,second,reset_event,False] )

   def verify_tod_le_terminate( self,dow="*",hour="*",minute="*",second="*",reset_event = None ):
       self.cf.insert_link("Verify_Tod_LE",[dow,hour,minute,second,reset_event,False] )
'''