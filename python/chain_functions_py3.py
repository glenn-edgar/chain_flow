
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


def init_function( cf_handle, chainObj):
   print("*** chain init chain name is ",chainObj["name"] )

def term_function( cf_handle, chainObj):
   print("*** chain term chain name is ",chainObj["name"] )



cf.define_chain("Chain_1", True, init_function = init_function, term_function = term_function) 
cf.insert.one_step(enable_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(suspend_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(resume_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.one_step(disable_chain_function)
cf.insert.wait_event_count( count = 5 )
cf.insert.log("Chain_1 is terminating")
cf.insert.terminate( )

cf.define_chain("Chain_2", False, init_function = init_function, term_function = term_function)  
cf.insert.log("Chain_2 is active")
cf.insert.reset()


cf.execute()

