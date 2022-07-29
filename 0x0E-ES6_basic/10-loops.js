export default function appendToEachArrayValue(array, appendString) {
  const fin = [];
  for (const value of array) {
    fin.push(appendString + value);
  }

  return fin;
}
