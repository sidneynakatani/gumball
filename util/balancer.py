from singleton import Singleton

@Singleton
class Balancer:
  host = None

  def host_selector(self):
    if self.host is None:
        self.host =  1
    return self.host

  def change_host(self):
	self.host = 2
