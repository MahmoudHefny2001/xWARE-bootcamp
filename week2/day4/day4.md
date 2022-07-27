test> show dbs
test> admin 40.00 KiB
config      108.00 KiB
local        72.00 KiB
myDataBase  524.00 KiB
system      144.00 KiB
test> use system
switched to db system
system> show collections

Messages
Notification

system> db.Messages.find()
[
  {
    _id: ObjectId("62e14eaf2cc5caae2107247b"),
    id: '1',
    name: 'Mahmoud',
    phone: '01065717371'
  },
  {
    _id: ObjectId("62e14efb2cc5caae2107247c"),
    id: '2',
    name: 'Mohammed',
    phone: '124578785421'
  },
  { _id: ObjectId("62e14f152cc5caae2107247d"), message: 'Hello' },
  {
    _id: ObjectId("62e151b22cc5caae21072481"),
    sender: 'Abdo',
    reciever: 'hamada',
    message: 'M'
  }
]
system> [
  {
    _id: ObjectId("62e14f692cc5caae2107247e"),
    id: '3',
    name: 'Aly',
    phone: '789654123'
  },
  {
    _id: ObjectId("62e14f782cc5caae2107247f"),
    id: '4',
    name: 'Ayman',
    phone: '852365417'
  },
  {
    _id: ObjectId("62e151522cc5caae21072480"),
    sender: 'Aya',
    reciever: 'Belal',
    Type: 'Message',
    content: 'Notification content',
    date: '1/1/2001'
  },
  {
    _id: ObjectId("62e153122cc5caae21072482"),
    sender: 'Aya',
    reciever: 'Belal',
    Type: 'Message',
    content: 'Notification content',
    date: '1/1/2001',
    created_at: '1/1/2001'
  }
]
system> 
