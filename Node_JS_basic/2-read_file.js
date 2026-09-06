const fs = require('fs');

function countStudents(path) {
  try {
    const fileContent = fs.readFileSync(path, 'utf-8');

    const lines = fileContent.split('\n').filter((line) => line.trim() !== '');

    const students = lines.slice(1);
    const total = students.length;

    const fields = {};

    for (const student of students) {
      const studentData = student.split(',');
      const firstName = studentData[0];
      const field = studentData[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstName);
    }

    console.log(`Number of students: ${total}`);
    Object.keys(fields).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
