import { uploadPhoto, createUser } from './utils.js';

const handleProfileSignup = () => {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
};

export default handleProfileSignup;
