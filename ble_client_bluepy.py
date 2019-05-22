from bluepy.btle import *

#init ble client
server_mac = '30:ae:a4:40:f1:ea'
server_service_uuid = 'd47e7069-ca9a-47e2-8c94-b85a87190927'
server_characteristic_uuid = '47de1cee-d731-4fea-a7ba-b8742d734992'

serv = UUID(server_service_uuid)
chara = UUID(server_characteristic_uuid)

p = Peripheral()
charac_notif = ""

#callback
class NotifyDelegate(DefaultDelegate) :
	def __init__ (self) :
		DefaultDelegate.__init__(self)

	def handleNotification(self, cHandle, data) :
		print 'Data : %s' % data

#scan selama 5 detik
scanner = Scanner(0)
devices = scanner.scan(5)

for d in devices : 
	print 'Device address : % s ..'  % d.addr

	if (d.addr == server_mac) :
		p = Peripheral(d,"random")
		p.withDelegate(NotifyDelegate())
		
		#bingung
		if (p.getServiceByUUID(serv)) : 
			service_notif = p.getServiceByUUID(serv)
			charac_notif = service_notif.getCharacteristics(chara)[0]
			if(charac_notif.supportsRead()):
				#print 'Data : %s' % charac_notif.read()
				#setup_data = "\x02\x00"
				#notify_handle = charac_notif.getHandle() + 1
				#p.writeCharacteristic(notify_handle, setup_data, withResponse=True)
				#charac_notif.write(setup_data)
				print 'sampai kene gak'

while True :
	print 'Data : % s' % charac_notif.read()
	