/*
In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value

Create Hash:
Using hset, let’s store the following:

The key of the hash should be HolbertonSchools
It should have a value for:
Portland=50
Seattle=80
New York=20
Bogota=20
Cali=40
Paris=2
Make sure you use redis.print for each hset
Display Hash:
Using hgetall, display the object stored in Redis. It should return the following:

Requirements:

Use callbacks for any of the operation, we will look at async operations later
*/

import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', function(error) {
  if (error)
    console.log(`Redis client not connected to the server: ${error}`);
});

client.on('ready', function(){
    console.log('Redis client connected to the server');
});

let values = {'Portland':50,'Seattle': 80,'New York': 20,'Bogota': 20,
              'Cali': 40,'Paris':2 };

for ( let val in values){
    client.hset('HolbertonSchools', val, values[val], function(err, res){
        redis.print(`Replay: ${res}`);
    });
}
      


/*client.hset('HolbertonSchools', 'Portland',50,
                                'Seattle', 80,
                                'New York', 20,
                                'Bogota', 20,
                                'Cali', 40,
                                'Paris',2,
            function(err, res){
                    console.log(res);
                }
            );*/
client.hgetall('HolbertonSchools', (error, object) => console.log(object));            