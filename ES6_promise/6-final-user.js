import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = (firstName, lastName, fileName) => {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((result) => ({
      status: result.status,
      value:
        result.status === 'fulfilled' ? result.value : result.reason.toString(),
    })),
  );
};

export default handleProfileSignup;
