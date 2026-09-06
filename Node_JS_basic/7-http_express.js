const express = require('express');

const app = express();
const PORT = 8080;
const DB_FILE = process.argv[2];
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, fileContent) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = fileContent
        .split('\n')
        .filter((line) => line.trim() !== '');

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

      const studentData = [];
      studentData.push(`Number of students: ${total}`);
      Object.keys(fields).forEach((field) => {
        studentData.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });
      resolve(studentData.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const body = ['This is the list of our students'];

  try {
    const data = await countStudents(DB_FILE);
    body.push(data);
    res.end(body.join('\n'));
  } catch (err) {
    res.end(`${body.join('\n')}\n${err.message}`);
  }
});

app.listen(PORT);

module.exports = app;
