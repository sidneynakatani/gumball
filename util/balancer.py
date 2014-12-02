from singleton import Singleton

@Singleton
class Balancer:
  host = None
  counter = 0
  hosts = ['http://sautenticador.appspot.com/', 'http://procuroprestador.appspot.com/', 'http://sidney-nakatani.appspot.com/']
  size = len(hosts)

  def host_selector(self):
    if self.host is None:
        self.host =  self.hosts[0]
    return self.host

  def change_host(self):
        self.counter += 1
        if(self.size == self.counter):
	    self.counter = 0 

	self.host = self.hosts[self.counter]
