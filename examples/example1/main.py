import time
import threading
import threadactive

class BackWorker(threadactive.Agent):
    def tick(self):
        threadactive.Agent.tick(self)
        print("[%s][%d] front" % (threading.current_thread().getName(), time.clock()) )
        self.print_in_back()
        time.sleep(1)

    @threadactive.backend
    def print_in_back(self, *args, **kwargs):
        print("[%s][%d] back" % (threading.current_thread().getName(), time.clock()) )
        if time.clock() > 3:
            self.back_to_front()

    @threadactive.frontend
    def back_to_front(self, *args, **kwargs):
        print("[%s][%d] back to front" % (threading.current_thread().getName(), time.clock()) )


def main():
    bw = BackWorker()
    while True:
        bw.tick()


if __name__ == '__main__':
    main()