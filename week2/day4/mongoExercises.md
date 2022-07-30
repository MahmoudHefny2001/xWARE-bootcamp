# Exercise 1 (MongoDB)

* Design Messaging and Notification System in MongoDB
* Messages Collection Will Documents, Every Document Will Have
* sender Sender info Like (id, name, etc..) and The Sender May Be Student Or Professor
* reciever Reciever info Like (id, name, etc..) and The Sender May Be Student Or Professor
* message Message
* Notification Collection Will Documents, Every Document Will Have
* sender Sender info Like (id, name, etc..) and The Sender May Be Student Or Professor
* reciever Reciever info Like (id, name, etc..) and The Sender May Be Student Or Professor
* type Notification Type (Message For Now)
* content Notification Content
* is_read is Notification Read
* created_at Notification Creation Date

```

- db.Messages.insert({
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
    })
    
- db.Messages.insert({
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
    })

```
 ## Retrieve  documents in the Messages collection.

 ### db.messages.find()
 

 
 ```
 [
  {
    _id: ObjectId("62e243096b762d79ea87f4dc"),
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
  },
  {
    _id: ObjectId("62e243326b762d79ea87f4dd"),
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
  }
]
 
 ```
 
 
```
db.Notification.insert({
  sender: {id: 1, name:'Ahmed'},
reciever: {id: 1, name:'Emad'}, 
type: {type:'text'}, 
content:"Hello World",
is_read:true, 
created_at:"july"} 
)
 
```
