base = {
    'servers':[
              {'index':0,
               'name': 'server0', 
              'host': 'redis-0.redis',
              'port': 6379,
              'password': '',
              'databases':16
              },
              {'index':1,
               'name': 'server1', 
              'host': 'redis-1.redis',
              'port': 6379,
              'databases':16
              },
              {'index':2,
               'name': 'server1', 
              'host': 'redis-2.redis',
              'port': 6379,
              'databases':16
              },
          ],
    'seperator' : ':',
    'maxkeylen' : 100
}
media_prefix = "pyred_media"

host = '0.0.0.0'
port = 80
debug = False

scan_batch = 10000
show_key_self_count = False

lang = 'zh_CN'

admin_user = 'admin'
admin_pwd = 'admin'