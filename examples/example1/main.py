import time
import threading
import threadactive

class BackWorker(threadactive.Agent):
    def tick(self):
        threadactive.Agent.tick(self)
        print("[%s][%d] front" % (threading.current_thread().getName(), time.clock()) )
        self.print_in_front2()
        self.print_in_back()
        time.sleep(1)

    @threadactive.backend
    def print_in_back(self, *args, **kwargs):
        print("[%s][%d] back" % (threading.current_thread().getName(), time.clock()) )
        self.print_in_back2()
        if time.clock() > 3:
            self.back_to_front()

    @threadactive.frontend
    def back_to_front(self, *args, **kwargs):
        print("[%s][%d] back to front" % (threading.current_thread().getName(), time.clock()) )

    @threadactive.frontend
    def print_in_front2(self, *args, **kwargs):
        print("[%s][%d] front2" % (threading.current_thread().getName(), time.clock()) )

    @threadactive.backend
    def print_in_back2(self, *args, **kwargs):
        print("[%s][%d] back2" % (threading.current_thread().getName(), time.clock()) )


def main():
    i = 0
    bw = BackWorker()
    while True:
        bw.tick()

        # restart backend thread
        i += 1
        if i > 5:
            bw.stop_backend()
            bw.start_backend()
            i = 0


if __name__ == '__main__':
    main()