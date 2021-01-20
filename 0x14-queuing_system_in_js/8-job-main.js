import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
<<<<<<< HEAD
        message: 'This is the code 1234 to verify your account'
=======
    message: 'This is the code 1234 to verify your account'
>>>>>>> 1a9fbec56324279c0a8f96240d916f50dff75154
    }
];
createPushNotificationsJobs(list, queue);