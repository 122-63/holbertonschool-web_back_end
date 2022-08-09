export default function getStudentIdsSum(students) {
  const value = students.map((ids) => ids.id);
  const sum = (idprev, idcurrent) => idprev + idcurrent;

  return value.reduce(sum);
}
