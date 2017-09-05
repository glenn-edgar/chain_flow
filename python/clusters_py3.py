# File: clusters_py3.py
# 
# Examples on use of clusteers
#
#
#
from  py_cf_py3.chain_flow_py3       import CF_Base_Interpreter
from  py_cf_py3.cluster_control_py3  import Cluster_Control

cf = CF_Base_Interpreter()
cluster_control = Cluster_Control(cf)


cf.define_chain("System_Startup",True)
cf.insert.one_step(cluster_control.reset_cluster,"test_cluster")
cf.insert.enable_chains(["Control_Chain"])
cf.insert.terminate()

cf.define_chain("Control_Chain",False)
cf.insert.wait_event_count(count = 5) # 5 second delay
cf.insert.one_step(cluster_control.set_configuration_reset,"test_cluster","state_1")
cf.insert.wait_event_count(count=5 ) # 5 second delay
cf.insert.one_step(cluster_control.set_configuration_reset,"test_cluster","state_2")
cf.insert.wait_event_count(count=5 ) # 5 second delay
cf.insert.one_step(cluster_control.set_configuration_reset,"test_cluster","state_3")
cf.insert.wait_event_count(count=5 ) # 5 second delay
cf.insert.one_step(cluster_control.suspend_cluster,"test_cluster")
cf.insert.wait_event_count(count=5 ) # 5 second delay
cf.insert.one_step(cluster_control.resume_cluster,"test_cluster")
cf.insert.wait_event_count(count=5 ) # 5 second delay
cf.insert.one_step(cluster_control.disable_cluster,"test_cluster")

cf.insert.reset()



cf.define_chain("Initialize_Chain",False)
cf.insert.log("Initial Chain Starting")
cf.insert.log("Doing Setup Work")
cf.insert.log("Initialize_Chain is terminating")
cf.insert.terminate()

cf.define_chain("State_1", False)
cf.insert.log("State_1 is active")
cf.insert.reset()

cf.define_chain("State_2", False)
cf.insert.log("State_2 is active")
cf.insert.reset()

cf.define_chain("State_3_Setup", False)
cf.insert.log("State_3_Setup is active")
cf.insert.enable_chains(["State_3A","State_3B"])
cf.insert.wait_event_count( count = 5 ) # wait is to test the cluster no reset option
cf.insert.terminate()

cf.define_chain("State_3A", False)
cf.insert.log("State_3A is active")
cf.insert.reset()

cf.define_chain("State_3B", False)
cf.insert.log("State_3B is active")
cf.insert.reset()



test_list = ["Initialize_Chain","State_1","State_2","State_3_Setup","State_3A","State_3B"]
cluster_control.define_cluster(cluster_id = "test_cluster", 
                               list_of_chains = test_list,
                               initial_chain = "Initialize_Chain" )
   
cluster_control.define_state( "test_cluster", "state_1", ["State_1"])
cluster_control.define_state( "test_cluster", "state_2", ["State_2"])
cluster_control.define_state( "test_cluster", "state_3", ["State_3_Setup"])
cluster_control.validate_clusters_state(cf)

cf.execute()

