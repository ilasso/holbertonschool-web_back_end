export default function getFullResponseFromAPI(success) {
  const myPromise = new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'success' });
    } else {
      reject(new Error('The fake API is not working'));
    }
  });
  return myPromise;
}
