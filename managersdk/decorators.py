import os
import multiprocessing
import psutil
import inspect
from time import sleep

def monitored(common_name = None, monitor_delay = 0.5):
    def decorator(fn):
        def wrapper(*args, **kwargs):

            soft_kill_marker = "soft_kill"
            event = None
            if 'event' in inspect.signature(fn).parameters.keys():
                if 'event' not in kwargs.keys():
                    kwargs['event'] = multiprocessing.Event()
                event = kwargs['event']


            process = multiprocessing.Process(target=fn, args=args, kwargs=kwargs)
            process.start()
            
            current_process = psutil.Process(os.getpid())
            child_process = psutil.Process(process.pid)
            process_name = common_name if common_name else fn.__name__
            while (child_process.is_running()):
                mem = current_process.memory_info().rss + child_process.memory_info().rss
                print("[ "+ process_name +" ] HeartBeat: " + str(mem))
                if(os.path.exists(soft_kill_marker)):
                    if event:
                        # set the event
                        event.set()
                        # wait until the process is finished
                        process.join()
                    else:
                        # kill the process
                        process.terminate()
                    break
                sleep(monitor_delay)
        return wrapper

    return decorator