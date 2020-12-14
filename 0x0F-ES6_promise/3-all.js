import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      let body;
      let firstname;
      let lastname;
      for (const response of results) {
        if (Object.prototype.hasOwnProperty.call(response, 'body')) {
          body = response.body;
        }
        if (Object.prototype.hasOwnProperty.call(response, 'firstName')) {
          firstname = response.firstName;
          lastname = response.lastName;
        }
      }
      console.log(body, firstname, lastname);
    })
    .catch(() => console.log('Signup system offline'));
}
