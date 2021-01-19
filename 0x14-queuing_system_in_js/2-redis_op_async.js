/*
Using promisify, modify the function displaySchoolValue to use ES6 async / await

Same result as 1-redis_op.js
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

function setNewSchool(schoolName, value){
    client.set(schoolName, value, function(err,res){
        redis.print(`Replay: ${res}`);
    });
}

const displaySchoolValue = async(schoolName) =>  {
    const reply = await getAsync(schoolName);
    console.log(reply);
}

(async() => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  })();
  
