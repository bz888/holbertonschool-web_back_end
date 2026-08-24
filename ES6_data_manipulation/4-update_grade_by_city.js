export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  return listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.find((newGrade) => newGrade.studentId === student.id);

      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
