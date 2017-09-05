
from py_cf_py3.chain_flow_py3 import CF_Base_Interpreter

cf = CF_Base_Interpreter()




cf = CF_Base_Interpreter()


cf.define_chain("Chain_1", True)   # this chain controls the sequence
cf.insert.log("************** Enabling Chain 2 *************** ")
cf.insert.enable_chains(["Chain_2"] )
cf.insert.wait_event_count(count =10)
cf.insert.log("**************** Disabling Chain 2 ************* " )
cf.insert.disable_chains(["Chain_2"] )
cf.insert.wait_event_count(count= 3)
cf.insert.log("**************** Enabling Chain 3  *************")
cf.insert.enable_chains(["Chain_3"] )
cf.insert.wait_event_count( count = 3)
cf.insert.log("********************* Suspending Chain 3 ********")
cf.insert.suspend_chains(["Chain_3"] )
cf.insert.wait_event_count( count = 3 )
cf.insert.log("********************** Resuming Chain 3  ******* ")
cf.insert.resume_chains(["Chain_3"] )
cf.insert.wait_event_count( count = 9 )
cf.insert.log("\n\n\ntest is over")
cf.insert.log("***** starting the test over again\n\n\n\n")
cf.insert.reset( )

cf.define_chain("Chain_2", False)  #this chain runs once
cf.insert.log("Chain_2 is multiple times")
cf.insert.reset()

cf.define_chain("Chain_3", False)  #this chain runs once
cf.insert.log("Initial message should only occur once")
cf.insert.wait_event_count( count = 5 )
cf.insert.log("Message would not be printed without resuming the chain")
cf.insert.log("Enabling the chain caused the chain to be reset")
cf.insert.terminate()


cf.execute()

