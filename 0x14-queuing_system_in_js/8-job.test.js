import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

    const list = [
        {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
        },
        {
            phoneNumber: '4153518782',
            message: 'This is the code 1232 to verify your account'
        }
    ];

describe('createPushNotificationsJobs function', function() {
    

    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());
    
    it('data cases', () => {
        createPushNotificationsJobs(list, queue);    
        
        /*for(let job in queue.testMode.jobs){
            console.log("hola",job);
            console.log("hola2",queue.testMode.jobs[job].data);
            console.log("hola3",queue.testMode.jobs[job].type);
            console.log("hola4",typeof(queue.testMode.jobs));
        }*/

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs.[0].data.phoneNumber).to.equal('4153518780');
        expect(queue.testMode.jobs.[1].data.phoneNumber).to.equal('4153518782');
    });

    it('type cases', () => {
        expect(()=>createPushNotificationsJobs({phoneNumber: '4', message: 'msg'}, queue))
        .to.throw('Jobs is not an array')
       });
});