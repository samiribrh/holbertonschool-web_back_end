const fs = require('fs');

function countStudents(path) {
  let fileData;

  try {
    fileData = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  console.log(`Number of students: ${fileData.split('\n').length - 2}`);

  const CS = fileData.split('\n').filter((line) => line.includes('CS')).length;
  const SWE = fileData.split('\n').filter((line) => line.includes('SWE')).length;
  let CSstudents = fileData.split('\n').filter((line) => line.includes('CS')).map((line) => line.split(',')[0]);
  let SWEstudents = fileData.split('\n').filter((line) => line.includes('SWE')).map((line) => line.split(',')[0]);

  CSstudents = CSstudents.join(', ');
  SWEstudents = SWEstudents.join(', ');

  console.log(`Number of students in CS: ${CS}. List: ${CSstudents}`);
  console.log(`Number of students in SWE: ${SWE}. List: ${SWEstudents}`);
}

module.exports = countStudents;