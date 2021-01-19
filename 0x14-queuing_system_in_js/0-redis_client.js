import redis from 'redis';
const client = redis.createClient();


client.on('error', function(error) {
  if (error)
    console.log(`Redis client not connected to the server: ${error}`);
});

client.on('ready', function(){
    console.log('Redis client connected to the server');
});


  
              
