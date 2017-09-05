
from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

cf = CF_Base_Interpreter()




cf = CF_Base_Interpreter()


cf.define_chain("Chain_1", True)   # this chain runs repediatively
cf.insert.log("Chain_1 is printed  many times ")
cf.insert.reset( )

cf.define_chain("Chain_2", True)  #this chain runs once
cf.insert.log("Chain_2 is printed once")
cf.insert.terminate()


cf.execute()

