from aria.log_manager import LogManager
from aria.log_config import LogConfiguration
from aria.event_properties import EventProperties
from aria import configuration
from datetime import datetime
import time
import sys
import subprocess
import importlib
from . import data_modules
from .data_modules import *

#compatible with both py2.7 and py3
class EventSender(object):

    def send(self, tenant_token):
        '''
        logConfig = LogConfiguration()
        config1 = configuration.LogManagerConfiguration(log_configuration = logConfig)
        LogManager.initialize(tenant_token, config1)
        logger = LogManager.get_logger("", tenant_token)
        
        # modules should have a class with the same name
        # the class should have at least two functions: name(), returning the event name 
        # and collect_data(), returning collected data as a value

        #refresh
        #importlib.invalidate_caches()

        import os
        classarr = []
        modules_to_import = os.listdir('./richard/data_modules')
        for modulestr in modules_to_import:
            if (modulestr[-3:] == '.py') and (modulestr != '__init__.py'):
                module = importlib.import_module('.' + modulestr[:-3],'richard.data_modules')
                #class name should be same as module name
                classobj = getattr(module, modulestr[:-3])
                classarr.append(classobj)
        # should add implementation for directories later

        #should change range and time interval later
        for a in range (0, 1):
            # find a way to change this
            event_properties = EventProperties("Time")
            
            for classobj in classarr:
                print(classobj.collect_data())
                event_properties.set_property(classobj.name() + ":", classobj.collect_data())
            id = logger.log_event(event_properties)
            # wait time before checking again
            time.sleep(1)
        

        #should put this in another thread
        LogManager().flush_and_tear_down()
        '''
        data_modules.get_gpu.get_gpu.collect_data()
        return
        

