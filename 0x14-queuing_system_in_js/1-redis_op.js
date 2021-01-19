/*
In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

setNewSchool:
It accepts two arguments schoolName, and value.
It should set in Redis the value for the key schoolName
It should display a confirmation message using redis.print
displaySchoolValue:
It accepts one argument schoolName.
It should log to the console the value for the key passed as argument
At the end of the file, call:

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
Requirements:

Use callbacks for any of the operation, we will look at async operations later
*/

import redis from 'redis';
const client = redis.createClient();

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

function displaySchoolValue(schoolName){
    client.get(schoolName, function(err, res){
        console.log(res);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');