import threading, os, time



def proxy():
    try:
        f = int(input("Specify the port for the proxy: "))
        os.system(f'python -m pproxy -l http://0.0.0.0:{f}')
    except:
        print('Port must be a number!')
        time.sleep(5)
        exit()


		
threading.Thread(target=proxy).start()
