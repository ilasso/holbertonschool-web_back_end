/*
In a file named 6-job_creator.js:

Create a queue with Kue
Create an object containing the Job data with the following format:
{
  phoneNumber: string,
  message: string,
}
Create a queue named push_notification_code, and create a job with the object created before
When the job is created without error, log to the console Notification job created: JOB ID
When the job is completed, log to the console Notification job completed
When the job is failing, log to the console Notification job failed

bob@dylan:~$ npm run dev 6-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1

Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the JOB ID increasing - it means you are storing new job to process…
*/

import kue from 'kue';

const queue = kue.createQueue();

const data = {'phoneNumber': '4153518780', 'message': 'string'};

const job = queue.create('push_notification_code', data).save( function(err){
        if(!err ) console.log(`Notification job created: ${job.id}`);
    });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
