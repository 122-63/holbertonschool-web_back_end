export default function updateStudentGradeByCity(students, city, newGrades) {
  const CityGrade = students
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.filter(
        (grdes) => student.id === grdes.studentId,
      );
      let grade = 'N/A';

      if (grades[0]) {
        grade = grades[0].grade;
      }

      return { ...student, grade };
    });

  return CityGrade;
}
