export default function createPushNotificationsJobs (jobs, queue)  {
    if (!(jobs instanceof Array))  throw Error('Jobs is not an array');
    jobs.forEach((j) => {
<<<<<<< HEAD
      const job = queue.create('push_notification_code_3', j);
        job.save((err) => {
          if (!err) console.log(`Notification job created: ${job.id}`);
        });
      job.on('complete', (result) => console.log(`Notification job ${job.id} completed`));
      job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
      job.on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
=======
      const job = queue.create('push_notification_code_3', j)
        .save((err) => {
          if (!err) console.log(`Notification job created: ${job.id}`);
        });
      job.on('complete', () => console.log(`Notification job ${job.id} completed`));
      job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
      job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
>>>>>>> 1a9fbec56324279c0a8f96240d916f50dff75154
    });
  };
  
  