
from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

cf = CF_Base_Interpreter()

def enable_chain_function( cf_handle, chainObj, parameters, event ):
  print("enable chain Chain_2")
  cf_handle.enable_chain_base(["Chain_2"] )

def disable_chain_function( cf_handle, chainObj, parameters, event ):
   print("disable chain Chain_2 ")
   cf_handle.disable_chain_base(["Chain_2"])

def resume_chain_function( cf_handle, chainObj, parameters, event ):
  print("resume chain Chain_2")
  cf_handle.resume_chain_code(["Chain_2"] )

def suspend_chain_function( cf_handle, chainObj, parameters, event ):
   print("suspend chain Chain_2 ")
   cf_handle.suspend_chain_code(["Chain_2"])


def send_event_function( cf_handle, chainObj, parameters, event ):
   cf_handle.send_event("Test_Event",None )


cf.define_chain("Chain_1", True)   # this chain runs repediatively
cf.insert.one_step(enable_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(suspend_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(resume_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(disable_chain_function)
cf.insert.one_step(send_event_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.log("Chain_1 is terminating")
cf.insert.terminate( )

cf.define_chain("Chain_2", False)  
cf.insert.log("Chain_2 is active")
cf.insert.reset()


cf.define_chain("Chain_3",True )
cf.insert.wait_event_count( event="Test_Event", count = 1 )
cf.insert.log("Chain 3 received event")
cf.insert.terminate()

cf.execute()

